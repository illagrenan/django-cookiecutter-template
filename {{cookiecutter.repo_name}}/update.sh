#!/bin/bash

echo "Updating project {{ cookiecutter.repo_name }}."

source data/venv/bin/activate

git pull --no-edit
bower install

cp -fr {{ cookiecutter.src_dir }}/{{ cookiecutter.main_app }}/settings/dist/production.py src/main/settings/local.py

pip install -r requirements/production.txt --use-wheel
python src/manage.py collectstatic --noinput
python src/manage.py migrate
python src/manage.py compress

supervisorctl reload {{ cookiecutter.repo_name }}


echo "Done."