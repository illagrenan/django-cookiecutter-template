# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

from django.shortcuts import render
from django.views.generic import TemplateView


def default_page(request):
    return render(request, 'web/index.html', {
    })


class IndexView(TemplateView):
    template_name = "web/index.html"
