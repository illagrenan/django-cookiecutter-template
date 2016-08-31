# Welcome to {{ cookiecutter.project_slug }}

> Description of this project: {{ cookiecutter.description }}


## Start with this repository ##

1) Setup virtualenv:
```bash
py -3 -m venv C:\Users\YourName\.virtualenvs\{{ cookiecutter.project_slug }}
.\activate.ps1
python -m pip install -U pip
pip install setuptools ipython pyreadline wheel --upgrade
```

2) Install all requirements:
```bash
npm install -g bower
pip install -r requirements/local.txt --upgrade --use-wheel
bower install
```

3) Create database

4) Migrate and run:
```bash
cd src
python manage.py check
# System check identified no issues (0 silenced).
python manage.py migrate
python manage.py runserver
```

## What's next ##

* [Deploy project on Ubuntu](docs/DEPLOYMENT.md)
* [Uninstall project from Ubuntu](docs/UNINSTALL.md)


----------

Copyright (c) {% now 'utc', '%Y' %} {{ cookiecutter.author_name }} <`{{ cookiecutter.email }}`>
