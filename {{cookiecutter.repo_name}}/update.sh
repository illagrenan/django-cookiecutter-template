#!/bin/bash

set -e

echo "Updating project {{ cookiecutter.repo_name }}."

source data/.venv/bin/activate

git reset --hard
git pull --no-edit origin master

bower install
pip install --no-input --exists-action=i -r requirements/production.txt --use-wheel

python src/manage.py collectstatic --noinput
python src/manage.py migrate
python src/manage.py compress
python src/manage.py compilemessages

supervisorctl restart {{ cookiecutter.repo_name }}:*
sudo supervisorctl status | grep "{{ cookiecutter.repo_name }}"

echo "Done."
