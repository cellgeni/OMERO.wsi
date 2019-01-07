#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from django.views.generic.base import TemplateView

from . import views


urlpatterns = patterns(
    'django.views.generic.simple',

    url(r'^login/$', views.CustomWebclientLoginView.as_view(), name="wsi_weblogin"),

)
