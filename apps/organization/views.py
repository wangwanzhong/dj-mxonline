from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import CityDict, CourseOrg


class OrgView(View):
    def get(self, request):
        org_list = CourseOrg.objects.all()
        city_list = CityDict.objects.all()
        org_count = org_list.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(org_list, 2, request=request)

        org_list = p.page(page)

        context = {
            'org_list': org_list,
            'city_list': city_list,
            'org_count': org_count
        }
        return render(request, 'org-list.html', context)
