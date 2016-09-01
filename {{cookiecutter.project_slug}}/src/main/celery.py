# -*- encoding: utf-8 -*-
# ! python3

import os

import celery
from django.conf import settings
from kombu import Exchange, Queue

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings.base')


class Celery(celery.Celery):
    def on_configure(self):
        if hasattr(settings, 'RAVEN_CONFIG') and settings.RAVEN_CONFIG['dsn']:
            import raven
            from raven.contrib.celery import register_signal, register_logger_signal

            client = raven.Client(dsn=settings.RAVEN_CONFIG['dsn'])
            register_logger_signal(client)
            register_signal(client)


app = Celery('{prefix}_celery_app'.format(prefix=settings.REDIS_PREFIX))
app.config_from_object('django.conf:settings')
app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_IGNORE_RESULT=True,
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_ENABLE_UTC=True,
    CELERY_TIMEZONE=settings.TIME_ZONE,
    BROKER_URL='redis://',
    ROKER_TRANSPORT_OPTIONS={
        'fanout_prefix': True,
        'fanout_patterns': True
    },
    CELERY_DEFAULT_QUEUE='{prefix}_default'.format(prefix=settings.REDIS_PREFIX),
    CELERY_QUEUES=(
        Queue(name='{prefix}_default'.format(prefix=settings.REDIS_PREFIX), exchange=Exchange('default'), routing_key='default'),
    )
)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
