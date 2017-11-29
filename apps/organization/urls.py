# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import OrgView, AddUserAskView, OrgHomeView


urlpatterns = [
    url(r'list/$', OrgView.as_view(), name='org_list'),
    url(r'add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>[0-9]+)/$', OrgHomeView, name='org-home'),
]