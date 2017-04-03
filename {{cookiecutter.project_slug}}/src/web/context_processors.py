# -*- encoding: utf-8 -*-
# ! python3

from django.conf import settings
from django.http import HttpRequest


def debug(request: HttpRequest):
    return {
        'DEBUG': settings.DEBUG
    }
