# Django project template #

[![Travis CI Badge](https://api.travis-ci.org/illagrenan/django-cookiecutter-template.png)](https://travis-ci.org/illagrenan/django-cookiecutter-template)

## How to start ##

```bash
$ cookiecutter https://github.com/illagrenan/django-cookiecutter-template.git
$ mkvirtualevn project_name
$ pip install setuptools ipython wheel --upgrade
$ easy_install -U mysql-python
$ pip install -r requirements/local.txt
$ python manage.py migrate
$ python manage.py runserver
```
