#!/bin/bash

set -e

# +--------------------------+
# | Update nginx virtualhost |
# +--------------------------+

echo "Preparing project {{ cookiecutter.project_name }}."

if [ "$UID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

cp {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.app_subdirectory_in_deploy_path }}conf/site.conf /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf
sudo ln -sf /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf /etc/nginx/sites-enabled/{{ cookiecutter.repo_name }}.conf

nginx -t -v
sudo service nginx restart

echo "Done."
