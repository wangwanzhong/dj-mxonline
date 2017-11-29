import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import CityDict, CourseOrg
from .forms import UserAskForm


class OrgView(View):
    def get(self, request):
        org_list = CourseOrg.objects.all()
        city_list = CityDict.objects.all()
        hot_orgs = org_list.order_by('-click_nums')[:3]

        # filter city
        city_id = request.GET.get('city', '')
        if city_id:
            org_list = org_list.filter(city_id=int(city_id))

        # query city
        categroy = request.GET.get('ct', '')
        if categroy:
            org_list = org_list.filter(categroy=categroy)

        org_count = org_list.count()

        # sort org_list
        sort = request.GET.get('sort', '')
        if sort == 'students':
            org_list = org_list.order_by('-students')
        elif sort == 'courses':
            org_list = org_list.order_by('-courses')
        else:
            sort = ''

        # pagination for org list
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(org_list, 3, request=request)
        org_list = p.page(page)

        context = {
            'org_list': org_list,
            'city_list': city_list,
            'org_count': org_count,
            'city_id': city_id,
            'categroy': categroy,
            'hot_orgs': hot_orgs,
            'sort': sort
        }
        return render(request, 'org-list.html', context)


class AddUserAskView(View):
    """User add feedback"""

    def post(self, request):
        user_ask_form = UserAskForm(request.POST)

        if user_ask_form.is_valid():
            user_ask_form.save(commit=True)
            res_content = {"status": "success"}
        else:
            # error_list = [v for k, v in user_ask_form.errors.items()]
            res_content = {"status": "fail", "msg": user_ask_form.errors}

        return HttpResponse(json.dumps(res_content), content_type='application/json')
