#!/bin/bash

set -e

# +--------------------------+
# | Update nginx virtualhost |
# +--------------------------+

echo "Updating nginx configuration for project {{ cookiecutter.project_slug }}."

if [ "$UID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

cp {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/app/conf/site.conf /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf
sudo ln -sf /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf /etc/nginx/sites-enabled/{{ cookiecutter.repo_name }}.conf

nginx -t -v
sudo service nginx restart

echo "Done."
