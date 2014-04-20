from django.db import models
from lib.models import CommonBaseModel

# # sync data
# class OldUniversityList(models.Model):
#     name = models.CharField(max_length=1000)
#     url = models.CharField(max_length=1000)
#     address = models.CharField(max_length=1000)
#     priority = models.IntegerField()
#     rank = models.IntegerField()

#     class Meta:
#         db_table = 'universitylist'
#         managed = False

class SchoolBase(CommonBaseModel):
    name = models.CharField(max_length=200, db_index=True)
    abbreviate = models.CharField(max_length=50, db_index=True)
    url = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        abstract = True

# EX, business, marking etc.
class Specialty(CommonBaseModel):
    name = models.CharField(max_length=200, db_index=True)
    # parent specialty, reverse using children_set
    parent = models.ForeignKey('self',related_name='children_set', null=True, blank=True)

    def __str__(self):
        return self.name


class Area(CommonBaseModel):
    name = models.CharField(max_length=200, db_index=True)


class University(SchoolBase):
    priority = models.IntegerField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class School(SchoolBase):
    university = models.ForeignKey(University)
    area = models.ForeignKey(Area)
    specialties = models.ManyToManyField(Specialty)
    nickname = models.CharField(max_length=50, db_index=True)

class SchoolNameErrorLog(CommonBaseModel):
    university_name = models.CharField(max_length=50, db_index=True)
    content = models.TextField()
    program = models.CharField(max_length=50)
    url = models.URLField(null=True, blank=True)

class WithURLLog(CommonBaseModel):
    university_name = models.CharField(max_length=50, db_index=True)
    content = models.TextField()
    program = models.CharField(max_length=50)
    url = models.URLField(null=True, blank=True)


