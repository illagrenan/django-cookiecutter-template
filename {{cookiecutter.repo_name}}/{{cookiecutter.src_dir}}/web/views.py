# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from django.shortcuts import render
from django.views.generic import TemplateView



def default_page(request):
    return render(request, 'web/index.html', {
    })

class IndexView(TemplateView):
    template_name = "web/index.html"

