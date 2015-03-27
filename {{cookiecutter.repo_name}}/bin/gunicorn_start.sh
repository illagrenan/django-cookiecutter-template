#!/bin/bash

# +-----------------------+
# | Gunicorn start script |
# +-----------------------+

# Name of the application
NAME="{{ cookiecutter.repo_name }}"
# Django project directory
DJANGODIR={{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.src_dir }}
# we will communicte using this unix socket
SOCKFILE={{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/gunicorn.sock
# the user to run as
USER={{ cookiecutter.repo_name }}
# the group to run as
GROUP=webapps
# how many worker processes should Gunicorn spawn
NUM_WORKERS=3
# which settings file should Django use
DJANGO_SETTINGS_MODULE={{ cookiecutter.main_app }}.settings.base
# WSGI module name
DJANGO_WSGI_MODULE={{ cookiecutter.main_app }}.wsgi

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd ${DJANGODIR}
source ../data/.venv/bin/activate
export DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}
export PYTHONPATH=${DJANGODIR}:${PYTHONPATH}

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name ${NAME} \
  --workers ${NUM_WORKERS} \
  --user=$USER --group=${GROUP} \
  --log-level=debug \
  --log-file=${DJANGODIR}/../log/gunicorn.log \
  --bind=unix:${SOCKFILE}