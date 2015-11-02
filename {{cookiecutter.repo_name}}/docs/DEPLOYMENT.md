# Deploy `{{ cookiecutter.project_name }}`

- **Project already deployed? Check [Update guide](UPDATES.md)**.
- **New server? First install all required software, check [Server setup](SERVER_SETUP.md)**

## 1) Deployment keys

```bash
# Copy your public key and register it on {{ cookiecutter.git_provider }}.
cat ~/.ssh/id_rsa.pub
```

## 2) Source code and requirements

```bash
# #######################################
# Connect to *REMOTE* server
# #######################################
mkdir -p {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
cd {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
git clone git@{{ cookiecutter.git_provider }}:{{ cookiecutter.author_username }}/{{ cookiecutter.repo_name }}.git {{ cookiecutter.app_subdirectory_in_deploy_path }}
cd {{ cookiecutter.app_subdirectory_in_deploy_path }}

virtualenv data/.venv; source activate.sh
pip install --upgrade pip ipython setuptools wheel
pip install -r requirements/production.txt --upgrade --use-wheel
```

# Optional step
```bash
bower install
npm install
```

## 3) Configure Django

To automatically export ENV_VARS, create this file:

```bash
touch {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.app_subdirectory_in_deploy_path }}.env
```

Example of minimal configuration:

```config
DATABASE_URL=mysql://USER:PASSWORD@127.0.0.1:3306/DATABASE_NAME
SECRET_KEY=SOME_SECRET_KEY
ALLOWED_HOSTS=www.{{ cookiecutter.domain_name }},{{ cookiecutter.domain_name }},127.0.0.1,localhost,0.0.0.0
```

## 4) User&group

```bash
sudo groupadd --system {{ cookiecutter.group }}
sudo useradd --system --gid {{ cookiecutter.group }} --home {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }} {{ cookiecutter.repo_name }}
sudo chown -R {{ cookiecutter.repo_name }}:{{ cookiecutter.group }} {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
```

Add GIT server to `authorized_keys`:

```bash
mkdir -p ~/.ssh
touch ~/.ssh/known_hosts
ssh-keyscan -t rsa,dsa bitbucket.org 2>&1 | sort -u - ~/.ssh/known_hosts > ~/.ssh/tmp_hosts
mv ~/.ssh/tmp_hosts ~/.ssh/known_hosts
```


## 5) Supervisor

**1) Check if Gunicorn is working**


```bash
cd {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.app_subdirectory_in_deploy_path }}{{ cookiecutter.src_dir }}
gunicorn main.wsgi:application --bind 0.0.0.0:8001 --access-logfile -
```

**2) Setup Supervisor to start Gunicorn**

```bash
sudo cp {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.app_subdirectory_in_deploy_path }}conf/supervisor.conf /etc/supervisor/conf.d/{{ cookiecutter.repo_name }}.conf
sudo supervisorctl reread
# {{ cookiecutter.repo_name }}_gunicorn: available
# {{ cookiecutter.repo_name }}_celerybeat: available
# {{ cookiecutter.repo_name }}_celeryd: available

sudo supervisorctl update
# {{ cookiecutter.repo_name }}: added process group
# ...

sudo supervisorctl status | grep "{{ cookiecutter.repo_name }}"
```

**OR** use sh script:

```bash
sudo bash bin/update_supervisor.sh
```

OK if:
```bash
{{ cookiecutter.repo_name }}    RUNNING     pid 1204, uptime 1:44:32
```

Not OK if:
```bash
{{ cookiecutter.repo_name }}    FATAL       Exited too quickly (process log may have details)

# When fixed:
sudo supervisorctl restart {{ cookiecutter.repo_name }}:*
```

## 6) Nginx

```bash
cp {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.app_subdirectory_in_deploy_path }}conf/site.conf /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf
sudo ln -sf /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf /etc/nginx/sites-enabled/{{ cookiecutter.repo_name }}.conf
sudo service nginx configtest
nginx -t
sudo service nginx restart
```

**OR** use sh script:

```bash
sudo bash bin/update_nginx.sh
```

* [How to uninstall project?](UNINSTALL.md)
* [Tips&tricks](MISC.md)
