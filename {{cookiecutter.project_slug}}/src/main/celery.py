# -*- encoding: utf-8 -*-
# ! python3

import os
from datetime import timedelta

import celery
from django.conf import settings
from kombu import Exchange, Queue

if not settings.configured:
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
    task_serializer='json',
    task_ignore_result=True,
    result_serializer='json',
    accept_content=['json'],
    enable_utc=True,
    timezone=settings.TIME_ZONE,
    broker_url=settings.REDIS_URL,
    task_always_eager=settings.CELERY_TASK_ALWAYS_EAGER,
    broker_transport_options={
        'fanout_prefix': True,
        'fanout_patterns': True
    },
    task_default_queue='{prefix}_default'.format(prefix=settings.REDIS_PREFIX),
    task_default_exchange='{prefix}_exchange'.format(prefix=settings.REDIS_PREFIX),
    task_default_routing_key='{prefix}_routing_key'.format(prefix=settings.REDIS_PREFIX),
    task_queues=(
        Queue(name='{prefix}_default'.format(prefix=settings.REDIS_PREFIX),
              exchange=Exchange('{prefix}_exchange'.format(prefix=settings.REDIS_PREFIX)),
              routing_key='{prefix}_routing_key'.format(prefix=settings.REDIS_PREFIX)),
    ),
    beat_schedule={
        'web:import_queries': {
            'task': 'web:import_queries',
            'schedule': timedelta(hours=5),
            'args': (),
            'kwargs': {'create_async_subtasks': True}
        },
        'web:import_products': {
            'task': 'web:import_products',
            'schedule': timedelta(hours=5),
            'args': (),
            'kwargs': {}
        }
    }
)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
