# -*- encoding: utf-8 -*-
# ! python3

import glob
import logging
import os
import shutil

from invoke import run, task

logger = logging.getLogger(__name__)


@task
def worker():
    """ Run Celery Worker """
    run("celery worker --pidfile=../data/celery/celery-worker.pid --workdir=src/ --app=main --concurrency=2 --loglevel=INFO")


@task
def beat():
    """ Run Celery Beat """
    run("celery beat --pidfile=../data/celery/celery-beat.pid --schedule=../data/celery/celerybeat-schedule --workdir=src/ --app=main --loglevel=INFO")


@task
def test():
    """ Test project """
    run("pytest src/ --verbose --color=yes --showlocals")


@task
def clean():
    """ Clean project """
    for f in glob.glob("./**/**.py[c|o]", recursive=True):
        print("Removing {}".format(f))
        os.remove(f)

    for ff in glob.glob("./**/**/__pycache__", recursive=True):
        print("Removing {}".format(ff))
        shutil.rmtree(ff)

    shutil.rmtree("htmlcov/", ignore_errors=True)


@task
def coverage():
    """ Create coverage report """
    run("coverage run -m pytest --verbose --color=yes --showlocals src/")
    run("coverage report -m")
    run("coverage html")

    print("Open htmlcov/index.html in your browser.")
