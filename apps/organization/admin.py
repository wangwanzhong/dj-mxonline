import xadmin
from .models import CityDict, CourseOrg


class CityDictAdmin:
    list_display = ('name', 'desc', 'add_time')
    search_fields = ('name', 'desc')
    list_filter = ('name', 'desc', 'add_time')


class CourseOrgAdmin:
    list_display = ('name', 'desc', 'click_nums', 'fav_nums', 'image', 'address',
                    'city', 'add_time')
    search_fields = ('name', 'desc', 'click_nums', 'fav_nums', 'image', 'address',
                     'city', 'add_time')
    list_filter = ('name', 'desc', 'click_nums', 'fav_nums', 'image', 'address',
                   'city', 'add_time')


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
