# -*- encoding: utf-8 -*-
# ! python2

"""
Django application configuration introduced in `1.7`.
For more info see: https://docs.djangoproject.com/en/1.7/ref/applications/#application-configuration.
"""

from __future__ import (absolute_import, division, print_function, unicode_literals)

from django.apps import AppConfig


class MainAppsConfig(AppConfig):
    """
    Django app config, this will set human readable name in Django admin.
    """

    name = '{{cookiecutter.main_app}}'
    verbose_name = "Main app"

    def ready(self):
        # noinspection PyUnresolvedReferences
        try:
            import {{cookiecutter.main_app}}.receivers
        except ImportError:
            pass
