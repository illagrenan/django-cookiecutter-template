# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from django.conf.urls import url
from web import views


urlpatterns = [
    url(r'^$', views.default_page, name='default_page'),
    url(r'^index-cbv$', views.IndexView.as_view(), name='default_page_cbv'),
]