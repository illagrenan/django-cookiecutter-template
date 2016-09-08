# -*- encoding: utf-8 -*-
# ! python3

from debug_toolbar.middleware import DebugToolbarMiddleware
from django.utils.deprecation import MiddlewareMixin

# Credits: https://github.com/jazzband/django-debug-toolbar/issues/853
class AtopdedTo110DebugMiddleware(MiddlewareMixin, DebugToolbarMiddleware):
    pass
