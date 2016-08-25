# -*- encoding: utf-8 -*-
# ! python3

import os

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ cookiecutter.main_app }}.settings.base')

import celery
from django.conf import settings


class Celery(celery.Celery):
    def on_configure(self):
        if hasattr(settings, 'RAVEN_CONFIG') and settings.RAVEN_CONFIG['dsn']:
            import raven
            from raven.contrib.celery import (register_signal,
                                              register_logger_signal)

            client = raven.Client(settings.RAVEN_CONFIG['dsn'])
            register_logger_signal(client)
            register_signal(client)


app = Celery('{{ cookiecutter.main_app }}')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
