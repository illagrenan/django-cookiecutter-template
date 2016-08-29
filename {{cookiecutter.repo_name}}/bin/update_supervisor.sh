#!/bin/bash

set -e

# +---------------------------------+
# | Update Supervisor configuration |
# +---------------------------------+

echo "Updating supervisor for project {{ cookiecutter.project_name }}."

if [ "$UID" -ne 0 ]
  then echo "Please run as root"
  exit
fi


cp {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/app/conf/supervisor.conf /etc/supervisor/conf.d/{{ cookiecutter.repo_name }}.conf
sudo supervisorctl reread
sudo supervisorctl update

sudo supervisorctl restart {{ cookiecutter.repo_name }}:*
sudo supervisorctl status | grep "{{ cookiecutter.repo_name }}"

echo "Done."
