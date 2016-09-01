# -*- encoding: utf-8 -*-
# ! python3

from django.apps import AppConfig


class MainAppsConfig(AppConfig):
    name = 'main'
    verbose_name = "Main app"

    def ready(self):
        # noinspection PyUnresolvedReferences
        try:
            import main.receivers
        except ImportError:
            pass
