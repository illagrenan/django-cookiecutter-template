# Deploy `{{ cookiecutter.project_name }}`

## Source code and requirements

```bash
$ cd /var/www
$ git clone git@{{ cookiecutter.git_provider }}.org:{{ cookiecutter.author_username }}/{{ cookiecutter.repo_name }}.git
$ cd {{ cookiecutter.repo_name }}

$ mkvirtualenv {{ cookiecutter.repo_name }}
$ easy_install -U pip; pip install ipython setuptools wheel --upgrade
$ pip install -r requirements/production.txt --upgrade --use-wheel
$ bower install
```

## Configure Django

```bash
$ cp /var/www/{{ cookiecutter.repo_name }}/{{ cookiecutter.src_dir }}/{{ cookiecutter.main_app }}/settings/dist/production.py /var/www/{{ cookiecutter.repo_name }}/{{ cookiecutter.src_dir }}/{{ cookiecutter.main_app }}/settings/local.py
```

## User&group

```bash
$ sudo groupadd --system webapps
$ sudo useradd --system --gid webapps --home /var/www/{{ cookiecutter.repo_name }} {{ cookiecutter.repo_name }}
$ sudo chown -R {{ cookiecutter.repo_name }}:users /var/www/{{ cookiecutter.repo_name }}
$ # sudo chmod -R g+w /var/www/{{ cookiecutter.repo_name }}
$ sudo chmod u+x /var/www/{{ cookiecutter.repo_name }}/bin/gunicorn_start.sh
```


## Supervisor

```bash
$ sudo cp /var/www/{{ cookiecutter.repo_name }}/conf/supervisor.conf /etc/supervisor/conf.d/{{ cookiecutter.repo_name }}.conf
$ sudo supervisorctl reread
$ # {{ cookiecutter.repo_name }}: available
```

```bash
$ sudo supervisorctl update
# {{ cookiecutter.repo_name }}: added process group
$ sudo supervisorctl status {{ cookiecutter.repo_name }}
```

OK if:
```bash
{{ cookiecutter.repo_name }}                  RUNNING    pid 1204, uptime 1:44:32
```

Not OK if:
```bash
{{ cookiecutter.repo_name }}                    FATAL      Exited too quickly (process log may have details)
```

## Nginx

```bash
$ cp /var/www/{{ cookiecutter.repo_name }}/conf/nginx.conf /etc/supervisor/conf.d/{{ cookiecutter.repo_name }}.conf
$ sudo ln -s /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf /etc/nginx/sites-enabled/{{ cookiecutter.repo_name }}.conf
$ sudo service nginx restart 
```

[How to uninstall project?](UNINSTALL.md)

## Misc

### Protect web with hpasswd

```bash
$ sudo apt-get install -y apache2-utils
$ sudo htpasswd -c /var/www/{{ cookiecutter.repo_name }}/.htpasswd admin
```