# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

from colorama import init, Fore
from django_fab_deployer.fabfile import get_tasks
from fabric.decorators import task
from fabric.operations import local

for target, task_func in get_tasks():
    globals()[target] = task_func

init(autoreset=True)


@task()
def migrate(*args, **kwargs):
    print(Fore.BLUE + 'Migrating.')

    local("python manage.py makemigrations")
    local("python manage.py migrate")

    print(Fore.GREEN + 'Done.')


@task(alias="mm")
def makemessages(*args, **kwargs):
    local("python manage.py makemessages --all --symlink --no-wrap --ignore=templates/account/* --ignore=templates/socialaccount/*")

    print(Fore.GREEN + 'Done.')


@task()
def worker(*args, **kwargs):
    print(Fore.BLUE + 'Starting Celery worker.')

    local("celery worker --workdir=src/ --app=main --concurrency=2 --loglevel=INFO")

    print(Fore.GREEN + 'Done.')


@task()
def beat(*args, **kwargs):
    print(Fore.BLUE + 'Starting Celery beat.')

    local("celery beat --workdir=src/ --app=main --loglevel=INFO")

    print(Fore.GREEN + 'Done.')
