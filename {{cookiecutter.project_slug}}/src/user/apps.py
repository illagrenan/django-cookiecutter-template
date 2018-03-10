# -*- encoding: utf-8 -*-
# ! python3

from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = 'user'
    verbose_name = "Users"

    def ready(self):
        pass
