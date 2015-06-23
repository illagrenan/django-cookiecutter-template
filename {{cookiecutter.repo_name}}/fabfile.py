# coding=utf-8

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from fabric.decorators import task
from fabric.operations import local
from color_printer import colors


@task
def check(*args, **kwargs):
    local("python src/manage.py check")
    local("python src/manage.py validate_templates")

    colors.green("Done.")


@task
def migrate(*args, **kwargs):
    local("python src/manage.py makemigrations")
    local("python src/manage.py migrate")

    colors.green("Done.")
