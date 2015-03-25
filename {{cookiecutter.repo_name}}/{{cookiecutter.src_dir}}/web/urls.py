# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^$', 'web.views.default_page', name='default_page'),
)