#!/bin/bash

echo "Preparing project {{ cookiecutter.project_name }}."

if [ "$UID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

cd /var/www/{{ cookiecutter.repo_name }}

sudo groupadd --system webapps
sudo useradd --system --gid webapps --home /var/www/{{ cookiecutter.repo_name }} {{ cookiecutter.repo_name }}

sudo chown -R {{ cookiecutter.repo_name }}:users /var/www/{{ cookiecutter.repo_name }}
sudo chmod -R g+w /var/www/{{ cookiecutter.repo_name }}
sudo chmod u+x /var/www/{{ cookiecutter.repo_name }}/bin/gunicorn_start.sh

sudo usermod -a -G webapps vasek
cd /var/www/{{ cookiecutter.repo_name }}/log
chmod g+w django_logging.log

# TODO next steps...

echo "Done."
