# Deploy `{{ cookiecutter.project_name }}`

## Already deployed?

```bash
# Install updates:
cd {{ cookiecutter.deploy_path }}
source update.sh
```

This will:

1. Activate virtualenv
2. Pull repository
3. Install bower components
4. Copy `production.py` over `local.py` 
5. Install Python requirements
6. Run `manage.py` commands: `collectstatic`, `migrate`, `compress`
7. Reload supervisor


----------

## Permissions

```bash
# Run this on localhost
git update-index --chmod=+x bin/gunicorn_start.sh
git commit -am "Added `x` flag to sh script."
git push
```

## Deployment keys


cat ~/.ssh/id_rsa.pub

## Source code and requirements

```bash
# Connect to remote server
cd {{ cookiecutter.deploy_path }}
git clone git@{{ cookiecutter.git_provider }}:{{ cookiecutter.author_username }}/{{ cookiecutter.repo_name }}.git
cd {{ cookiecutter.repo_name }}

virtualenv data/.venv; source activate.sh
easy_install -U pip; pip install ipython setuptools wheel --upgrade
pip install -r requirements/production.txt --upgrade --use-wheel
bower install
```

## Configure Django

```bash
cp {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.src_dir }}/{{ cookiecutter.main_app }}/settings/dist/production.py {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.src_dir }}/{{ cookiecutter.main_app }}/settings/local.py
```

## User&group

```bash
sudo groupadd --system {{ cookiecutter.group }}
sudo useradd --system --gid {{ cookiecutter.group }} --home {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }} {{ cookiecutter.repo_name }}
sudo chown -R {{ cookiecutter.repo_name }}:{{ cookiecutter.group }} {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
sudo chmod g+w -R {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/log/
sudo chmod u+x {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/bin/gunicorn_start.sh
```


## Supervisor

**1) Check if Gunicorn is working**


```bash
cd {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.src_dir }}
gunicorn main.wsgi:application --bind 0.0.0.0:8001
```

**2) Setup Supervisor to start Gunicorn**

```bash
sudo cp {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/conf/supervisor.conf /etc/supervisor/conf.d/{{ cookiecutter.repo_name }}.conf
sudo supervisorctl reread
# {{ cookiecutter.repo_name }}: available

sudo supervisorctl update
# {{ cookiecutter.repo_name }}: added process group

sudo supervisorctl status {{ cookiecutter.repo_name }}
```

**OR** use sh script:

```bash
sudo source bin/update_supervisor.sh
```

OK if:
```bash
{{ cookiecutter.repo_name }}    RUNNING     pid 1204, uptime 1:44:32
```

Not OK if:
```bash
{{ cookiecutter.repo_name }}    FATAL       Exited too quickly (process log may have details)

# When fixed:
sudo supervisorctl restart {{ cookiecutter.repo_name }}
```

## Nginx

```bash
cp {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/conf/nginx.conf /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf
sudo ln -sf /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf /etc/nginx/sites-enabled/{{ cookiecutter.repo_name }}.conf
sudo service nginx configtest 
sudo service nginx restart 
```

**OR** use sh script:

```bash
sudo source bin/update_nginx.sh
```

* [How to uninstall project?](UNINSTALL.md)
* [Tips&tricks](MISC.md)