# -*- encoding: utf-8 -*-
# ! python3

default_app_config = 'main.apps.MainAppsConfig'

# This will make sure the app is always imported when Django starts so that shared_task will use this app.
# noinspection PyUnresolvedReferences
from .celery import app as celery_app  # noqa

__all__ = ['celery_app']
