#!/bin/bash

echo "Updating project {{ cookiecutter.repo_name }}."

workon {{ cookiecutter.repo_name }}

git pull
bower install

cp -fr src/main/settings/dist/production.py src/main/settings/local.py

pip install -r requirements/production.txt --use-wheel
python src/manage.py collectstatic --noinput
python src/manage.py migrate
python src/manage.py compress

supervisorctl reload {{ cookiecutter.repo_name }}


echo "Done."
