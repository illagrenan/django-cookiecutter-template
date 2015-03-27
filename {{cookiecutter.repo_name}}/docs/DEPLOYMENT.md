# Deploy `{{ cookiecutter.project_name }}`

## Permissions

```bash
$ git update-index --chmod=+x .\bin\gunicorn_start.sh
```

## Source code and requirements

```bash
$ cd {{ cookiecutter.deploy_path }}
$ git clone git@{{ cookiecutter.git_provider }}:{{ cookiecutter.author_username }}/{{ cookiecutter.repo_name }}.git
$ cd {{ cookiecutter.repo_name }}

$ cd {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
$ virtualenv data/.venv; source activate.sh
$ easy_install -U pip; pip install ipython setuptools wheel --upgrade
$ pip install -r requirements/production.txt --upgrade --use-wheel
$ bower install
```

## Configure Django

```bash
$ cp {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.src_dir }}/{{ cookiecutter.main_app }}/settings/dist/production.py {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.src_dir }}/{{ cookiecutter.main_app }}/settings/local.py
```

## User&amp;group

```bash
$ sudo groupadd --system {{ cookiecutter.group }}
$ sudo useradd --system --gid {{ cookiecutter.group }} --home {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }} {{ cookiecutter.repo_name }}
$ sudo chown -R {{ cookiecutter.repo_name }}:{{ cookiecutter.group }} {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
$ sudo chmod g+w -R {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/log/*log
$ sudo chmod u+x {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/bin/gunicorn_start.sh
```


## Supervisor

```bash
$ sudo cp {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/conf/supervisor.conf /etc/supervisor/conf.d/{{ cookiecutter.repo_name }}.conf
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

```bash
$ cd {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.src_dir }}
$ gunicorn main.wsgi:application --bind 0.0.0.0:8001
$ # When fixed:
$ sudo supervisorctl restart {{ cookiecutter.repo_name }}
```

## Nginx

```bash
$ cp {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/conf/nginx.conf /etc/supervisor/conf.d/{{ cookiecutter.repo_name }}.conf
$ sudo ln -s /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf /etc/nginx/sites-enabled/{{ cookiecutter.repo_name }}.conf
$ sudo service nginx restart 
```

[How to uninstall project?](UNINSTALL.md)

## Misc

### Protect web with hpasswd

```bash
$ sudo apt-get install -y apache2-utils
$ sudo htpasswd -c {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/.htpasswd admin
```

### Fix permissions

```bash
$ cd {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
$ find . -not -path '*/\.*' -type d -exec chmod 775 {} +
$ find . -not -path '*/\.*' -type f -exec chmod 664 {} +
$ chmod g+w log/*log
$ chmod u+x bin/gunicorn_start.sh   
```