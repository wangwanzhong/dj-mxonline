# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import OrgView, AddUserAskView, OrgHomeView

app_name = 'org'
urlpatterns = [
    url(r'$', OrgView.as_view(), name='org_list'),
    url(r'add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
]
