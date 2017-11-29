import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin:
    list_display = ('name', 'desc', 'add_time')
    search_fields = ('name', 'desc')
    list_filter = ('name', 'desc', 'add_time')
    model_icon = 'fa fa-university'


class CourseOrgAdmin:
    list_display = ('name', 'desc', 'click_nums', 'fav_nums', 'image', 'address',
                    'city', 'add_time')
    search_fields = ('name', 'desc', 'click_nums', 'fav_nums', 'image', 'address',
                     'city', 'add_time')
    list_filter = ('name', 'desc', 'click_nums', 'fav_nums', 'image', 'address',
                   'city', 'add_time')
    model_icon = 'fa fa-university'


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org', 'name', 'work_years', 'work_company']
    model_icon = 'fa fa-user-md'


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
