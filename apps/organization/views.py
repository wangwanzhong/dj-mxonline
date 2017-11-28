from django.shortcuts import render

from django.views.generic.base import View

from .models import CityDict, CourseOrg


class OrgView(View):
    def get(self, request):
        org_list = CourseOrg.objects.all()
        city_list = CityDict.objects.all()
        context = {'org_list': org_list, 'city_list': city_list}
        return render(request, 'org-list.html', context)
