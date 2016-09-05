# -*- encoding: utf-8 -*-
# ! python3

import logging

from invoke import run, task

logger = logging.getLogger(__name__)


@task
def worker():
    """ Run Celery Worker """
    run("celery worker --workdir=src/ --app=main --concurrency=2 --loglevel=INFO")


@task
def beat():
    """ Run Celery Beat """
    run("celery beat --workdir=src/ --app=main --loglevel=INFO")


@task
def test():
    """ Test project """
    run("pytest src/ --verbose --color=yes --showlocals")


@task
def coverage():
    """ Create coverage report """
    run("coverage run pytest")
    run("coverage report -m")
    run("coverage html")
