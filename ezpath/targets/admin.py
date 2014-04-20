from django.contrib import admin
from .models import (University, Specialty, School, Area, SchoolNameErrorLog, WithURLLog)


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'address', 'rank')

admin.site.register(University, UniversityAdmin)


class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_specialty')

    def parent_specialty(self, instance):
        return instance.parent

admin.site.register(Specialty, SpecialtyAdmin)


class AreaAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Area, AreaAdmin)

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'url', 'address', 'university', 'specialties_list')
    list_per_page = 25
    search_fields = ('name', 'nickname', 'university__name')

    # using iteraltor ()
    def specialties_list(self, instance):
        return ','.join((spec['name'] for spec in instance.specialties.values('name')))


admin.site.register(School, SchoolAdmin)


admin.site.register(SchoolNameErrorLog)
admin.site.register(WithURLLog)