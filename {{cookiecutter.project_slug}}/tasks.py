# -*- encoding: utf-8 -*-
# ! python3

import glob
import logging
import os
import shutil
import sys

from invoke import run, task

logger = logging.getLogger(__name__)


@task
def worker(ctx):
    """ Run Celery Worker """
    ctx.run("celery worker --pidfile=../data/celery/celery-worker.pid --workdir=src/ --app=main --concurrency=2 --loglevel=INFO")


@task
def beat(ctx):
    """ Run Celery Beat """
    ctx.run("celery beat --pidfile=../data/celery/celery-beat.pid --schedule=../data/celery/celerybeat-schedule --workdir=src/ --app=main --loglevel=INFO")


@task
def make_doc(ctx):
    """ Make Sphinx Doc """
    sys.path.insert(0, os.path.abspath('src/'))
    from main.settings.base import LOCAL_APPS
    os.chdir("sphinx")

    for a in LOCAL_APPS:
        ctx.run("sphinx-apidoc --force -o source/{app}/ ../src/{app}/".format(app=a))

    ctx.run("make html")


@task
def test(ctx):
    """ Test project """
    ctx.run("pytest src/ --verbose --color=yes --showlocals")


@task
def clean(ctx):
    """ Clean project """
    for f in glob.glob("./**/**.py[c|o]", recursive=True):
        print("Removing {}".format(f))
        os.remove(f)

    for ff in glob.glob("./**/**/__pycache__", recursive=True):
        print("Removing {}".format(ff))
        shutil.rmtree(ff)

    shutil.rmtree("htmlcov/", ignore_errors=True)


@task
def coverage(ctx):
    """ Create coverage report """
    ctx.run("coverage run --branch -m pytest --verbose --color=yes --showlocals src/")
    ctx.run("coverage report -m")
    ctx.run("coverage html")

    print("Open htmlcov/index.html in your browser.")
