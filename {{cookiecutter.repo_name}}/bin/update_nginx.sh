#!/bin/bash

# +--------------------------+
# | Update nginx virtualhost |
# +--------------------------+

echo "Preparing project {{ cookiecutter.project_name }}."

if [ "$UID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

cp {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/conf/nginx.conf /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf
sudo ln -s /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf /etc/nginx/sites-enabled/{{ cookiecutter.repo_name }}.conf

sudo service nginx configtest
sudo service nginx restart

echo "Done."
