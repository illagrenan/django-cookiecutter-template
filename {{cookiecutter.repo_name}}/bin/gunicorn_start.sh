#!/bin/bash

# +-----------------------+
# | Gunicorn start script |
# +-----------------------+

NAME="{{ cookiecutter.repo_name }}"					                        # Name of the application
DJANGODIR={{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.src_dir }}			    		# Django project directory
SOCKFILE={{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/gunicorn.sock			# we will communicte using this unix socket
USER={{ cookiecutter.repo_name }}                                   		# the user to run as
VENV_USER=vasek														        # Python virtualenv user
GROUP=webapps                                     			                # the group to run as
NUM_WORKERS=3                                     			                # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE={{ cookiecutter.main_app }}.settings.base           			                    # which settings file should Django use
DJANGO_WSGI_MODULE={{ cookiecutter.main_app }}.wsgi			                     	            # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd ${DJANGODIR}
source /home/${VENV_USER}/.virtualenvs/${NAME}/bin/activate
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
