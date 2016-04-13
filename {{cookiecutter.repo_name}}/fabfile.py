# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

from color_printer import colors
from django_fab_deployer.fabfile import get_tasks
from fabric.decorators import task
from fabric.operations import local

for target, task_func in get_tasks():
    globals()[target] = task_func


@task()
def migrate(*args, **kwargs):
    colors.blue("Migrating")

    local("python manage.py makemigrations")
    local("python manage.py migrate")
    local("python manage.py migrate --database=local")

    colors.green("Done.")


@task(alias="mm")
def makemessages(*args, **kwargs):
    local("python manage.py makemessages --all --symlink --no-wrap --ignore=templates/account/* --ignore=templates/socialaccount/*")

    colors.green("Done.")


@task()
def worker(*args, **kwargs):
    colors.blue("Starting Celery worker.")

    local("celery worker --workdir=src/ --app=main --concurrency=2 --loglevel=INFO")

    colors.green("Done.")


@task()
def beat(*args, **kwargs):
    colors.blue("Starting Celery beat.")

    local("celery beat --workdir=src/ --app=main --loglevel=INFO")

    colors.green("Done.")
