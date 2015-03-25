# Django project template #

[![Travis CI Badge](https://api.travis-ci.org/illagrenan/django-cookiecutter-template.png)](https://travis-ci.org/illagrenan/django-cookiecutter-template)&nbsp;[![Requirements Status](https://requires.io/github/illagrenan/django-cookiecutter-template/requirements.svg?branch=master)](https://requires.io/github/illagrenan/django-cookiecutter-template/requirements/?branch=master)

## How to start ##

Install cookiecutter:
```bash
$ pip install cookiecutter --upgrade
```

Download and run template:
```bash
$ cookiecutter https://github.com/illagrenan/django-cookiecutter-template.git
```

## Setup Django project ##

Setup virtualenv:
```bash
$ cd ...
$ mkvirtualevn project_name
$ pip install setuptools ipython wheel --upgrade
$ easy_install -U mysql-python
$ pip install -r requirements/local.txt --upgrade
$ python manage.py migrate
$ python manage.py runserver
```

Migrate and run:
```bash
$ python manage.py migrate
$ python manage.py runserver
```