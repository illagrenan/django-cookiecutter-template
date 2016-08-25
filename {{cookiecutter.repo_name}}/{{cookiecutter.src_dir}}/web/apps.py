# -*- encoding: utf-8 -*-
# ! python3

from django.apps import AppConfig


class WebAppConfig(AppConfig):
    """
    Django app config, this will set human readable name in Django admin.
    """

    name = 'web'
    verbose_name = "Web"

    def ready(self):
        # noinspection PyUnresolvedReferences
        import web.receivers
