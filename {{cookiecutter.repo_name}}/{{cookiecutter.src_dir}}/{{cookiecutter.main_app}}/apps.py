# -*- encoding: utf-8 -*-
# ! python3

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
