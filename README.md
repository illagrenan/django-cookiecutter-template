# Django project template #

[![Travis CI Badge](https://api.travis-ci.org/illagrenan/django-cookiecutter-template.png)](https://travis-ci.org/illagrenan/django-cookiecutter-template)&nbsp;[![Updates](https://pyup.io/repos/github/illagrenan/django-cookiecutter-template/shield.svg)](https://pyup.io/repos/github/illagrenan/django-cookiecutter-template/)&nbsp;[![Python 3](https://pyup.io/repos/github/illagrenan/django-cookiecutter-template/python-3-shield.svg)](https://pyup.io/repos/github/illagrenan/django-cookiecutter-template/)

## Use this template ##

Install cookiecutter:
```bash
pip install cookiecutter --upgrade
```

Download and run template:
```bash
cookiecutter https://github.com/illagrenan/django-cookiecutter-template.git
```

## Setup Django project ##

1) Setup virtualenv:
```bash
cd ...
virtualenv data/.venv
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

# Other #

## Credits ##

- Cookiecutter project: [https://github.com/audreyr/cookiecutter](https://github.com/audreyr/cookiecutter)
- This template is based on [https://github.com/pydanny/cookiecutter-django](https://github.com/pydanny/cookiecutter-django) and [https://github.com/twoscoops/django-twoscoops-project](https://github.com/twoscoops/django-twoscoops-project)
- Error pages templates made in Bootstrap: https://github.com/alexphelps/Server-Error-Pages

## License ##

The MIT License (MIT)

Copyright (c) 2015&ndash;2016 illagrenan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


