#!/bin/bash

# +---------------------------------+
# | Update Supervisor configuration |
# +---------------------------------+

echo "Updating supervisor for project {{ cookiecutter.project_name }}."

if [ "$UID" -ne 0 ]
  then echo "Please run as root"
  exit
fi


cp /var/www/robert_riedl_cz/conf/supervisor.conf /etc/supervisor/conf.d/robert_riedl_cz.conf
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl status robert_riedl_cz

echo "Done."