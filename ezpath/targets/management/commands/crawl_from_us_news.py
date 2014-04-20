from optparse import make_option
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
import urlparse
import re
from targets.models import Specialty, University, School, Area, SchoolNameErrorLog, WithURLLog
import time

def is_absolute(url):
    return bool(urlparse.urlparse(url).netloc)

def get_absolute(url, domain):
    if is_absolute(url):
        return url
    else:
        return urlparse.urljoin(domain, url)



class Command(BaseCommand):
    def handle(self, *args, **options):

        for page_num in range(1, 16):
            start = time.clock()
            url = "http://grad-schools.usnews.rankingsandreviews.com/best-graduate-schools/top-business-schools/mba-rankings/page+%s" % (str(page_num))

            #url = "http://grad-schools.usnews.rankingsandreviews.com/best-graduate-schools/top-engineering-schools/eng-rankings?int=9a1f08"


            #url = "http://grad-schools.usnews.rankingsandreviews.com/best-graduate-schools/top-education-schools/edu-rankings/page+1"

            url = "http://grad-schools.usnews.rankingsandreviews.com/best-graduate-schools/top-education-schools/edu-rankings/page+2"

            domain = "{0.scheme}://{0.netloc}/".format(urlparse.urlparse(url))

            res = requests.get(url)
            if res .status_code != requests.codes.OK:
                pass

            content = res.content
            page_dom = BeautifulSoup(content)
            children_elms= page_dom.find_all('a', {'class':'school-name'})
            program_elm = page_dom.find('h1', {'class':'intro-heading'})
            program = re.search('Best (.*) Schools', program_elm.text).group(1).strip().lower()

            area = Area.objects.get_or_create(name=program)[0]

            for child_elm in children_elms:
                school_save = {'area': area}

                #school_raw_name = ''.join([char if ord(char) < 128 else '-' for char in child_elm.text])

                child_url = get_absolute(child_elm['href'], domain)
                child_page = requests.get(child_url)
                school_soup = BeautifulSoup(child_page.content)
                address_elm = school_soup.find('p',{'class':'address'})

                school_raw_name = school_soup.find('h1').text
                university_name = school_raw_name.split('(')[0].strip()

                school_save['university'] = University.objects.get_or_create(name=university_name)[0]

                match = re.search(r"\(([A-Za-z0-9_]+)\)", school_raw_name)
                if match:
                    school_save['nickname'] = match.group(1)

                school_save['address'] = ' '.join(re.sub('[^A-Za-z0-9 ]+', '', address_elm.text).split())

                overview_elm = school_soup.find('h3',{'class':'free_overview'})
                para_elm = overview_elm.findNext('p')
                #para_elm_text = ''.join([char if ord(char) < 128 else '-' for char in para_elm.text])
                # need to modify this(patten not correctly enough)
                try:
                    school_save['name'] = 'The %s at %s' % (
                        re.search('The (.*) at %s' % university_name, para_elm.text).group(1).strip(), university_name)
                except Exception, e:
                    try:
                        school_save['name'] = 'The %s at %s' % (
                            re.search('The (.*) at %s' % university_name.split('-')[0], para_elm.text).group(1).strip(), university_name)
                    except Exception, e:
                        try:
                            school_save['name'] = 'The %s %s at %s' % ( school_save['nickname'], re.search('The %s (.*) at' % school_save['nickname'], para_elm.text).group(1).strip(), university_name)
                        except Exception, e:
                            try:
                                school_save['name'] = 'The %s of %s at %s' % (re.search('The (.*) of %s' % program.capitalize(), para_elm.text).group(1).strip(), program.capitalize(), university_name)
                            except Exception, e:
                                school_save['name'] = 'The School of %s at %s' % (program.capitalize(), university_name)
                                SchoolNameErrorLog.objects.create(
                                    university_name=university_name,
                                    content=para_elm.text,
                                    program=program,
                                    url=child_url
                                )

                more_info_elm = school_soup.find('a',{'id':'moreinfo_link'})
                if more_info_elm:
                    school_save['url'] = more_info_elm['href']
                else:
                    WithURLLog.objects.create(
                        university_name=university_name,
                        content=para_elm.text,
                        program=program,
                        url=child_url
                    )

                school = School.objects.get_or_create(**school_save)[0]
                #school.specialties.add(specialty)
            elapsed = (time.clock() - start)
            print "run time %s at %s" % (str(elapsed), str(page_num))
