#!/bin/bash

echo "Updating project {{ cookiecutter.repo_name }}."

source data/.venv/bin/activate

git pull --no-edit
bower install

pip install -r requirements/production.txt --use-wheel
python src/manage.py collectstatic --noinput
python src/manage.py migrate
python src/manage.py compress

supervisorctl restart {{ cookiecutter.repo_name }}:*
sudo supervisorctl status | grep "{{ cookiecutter.repo_name }}"


echo "Done."
