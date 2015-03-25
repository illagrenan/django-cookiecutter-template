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
$ mkvirtualenv project_name
$ pip install setuptools ipython wheel --upgrade
```
Install all requirements:
```bash
$ pip install setuptools ipython wheel --upgrade
$ easy_install -U mysql-python
$ easy_install -U pip
$ pip install -r requirements/local.txt --upgrade
```

Migrate and run:
```bash
$ cd src
$ python manage.py check
$ python manage.py migrate
$ python manage.py runserver
```