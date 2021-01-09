#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.decorators.cache import cache_page
from base import views
from django_distill import distill_re_path

urlpatterns = [
    url(r'^contact/$', views.ContactUs.as_view(), name='contact'),

    distill_re_path(r'^$', views.HomeView.as_view(), name='index', distill_func=lambda: None)
]
