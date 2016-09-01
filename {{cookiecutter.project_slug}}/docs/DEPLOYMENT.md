# Deploy `{{ cookiecutter.project_slug }}`

- **Project already deployed? Check [Update guide](UPDATES.md)**.
- **New server? First install all required software, check [Server setup](SERVER_SETUP.md)**

## 1) Create new user and setup SSH

```bash
sudo groupadd --system {{ cookiecutter.group }}

mkdir -p {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
sudo useradd --system --gid {{ cookiecutter.group }} --groups supervisor --home {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }} {{ cookiecutter.repo_name }}
sudo chown -R {{ cookiecutter.repo_name }}:{{ cookiecutter.group }} {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
```

Copy bashrc profile:

```bash
cp /etc/skel/.bashrc ~/.bashrc
touch ~/.profile && nano ~/.profile
```

Content of `.profile`:

```
# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin directories
PATH="$HOME/bin:$HOME/.local/bin:$PATH"
```

Add {{ cookiecutter.git_provider }} to `authorized_keys`:

```bash
mkdir -p ~/.ssh
touch ~/.ssh/known_hosts
ssh-keyscan -t rsa,dsa {{ cookiecutter.git_provider }} 2>&1 | sort -u - ~/.ssh/known_hosts > ~/.ssh/tmp_hosts
mv ~/.ssh/tmp_hosts ~/.ssh/known_hosts
```


And create new ssh-keypair:

```bash
ssh-keygen -t rsa -C "your_email@example.com"
# Or simply:
ssh-keygen -t rsa
touch ~/.ssh/authorized_keys

# Copy your public key
nano ~/.ssh/authorized_keys
```


Fix `~/.ssh` and home directory permissions:

```bash
chmod go-w ~/
chmod 700 ~/.ssh
chmod 600 -R  ~/.ssh/*
```


## 2) Deployment keys for git

```bash
# Copy your public key and register it on {{ cookiecutter.git_provider }}.
cat ~/.ssh/id_rsa.pub
```

## 3) Source code and requirements

```bash
cd {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
git clone git@{{ cookiecutter.git_provider }}:{{ cookiecutter.author_username }}/{{ cookiecutter.repo_name }}.git app/
cd app/

# On Python2:
virtualenv data/.venv; source activate.sh

# On Python3 using deadsnakes:
virtualenv -p /usr/bin/python3.5 data/.venv


pip install --upgrade pip ipython setuptools wheel
pip install -r requirements/production.txt --upgrade --use-wheel
```

**Optional step**
```bash
bower install
npm install
```

## 4) Configure Django

To automatically export ENV_VARS, create this file:

```bash
touch {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/app/.env
```

Example of minimal configuration:

```config
DATABASE_URL=mysql://USER:PASSWORD@127.0.0.1:3306/DATABASE_NAME
SECRET_KEY=SOME_SECRET_KEY
ALLOWED_HOSTS=www.{{ cookiecutter.domain_name }},{{ cookiecutter.domain_name }},127.0.0.1,localhost,0.0.0.0
```

## 5) Supervisor

**1) Check if Gunicorn is working**


```bash
cd {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/app/src/
gunicorn main.wsgi:application --bind 0.0.0.0:8001 --access-logfile -
```

**2) Setup Supervisor to start Gunicorn**

```bash
sudo cp {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/app/conf/supervisor.conf /etc/supervisor/conf.d/{{ cookiecutter.repo_name }}.conf
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
cp {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/app/conf/site.conf /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf
sudo ln -sf /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf /etc/nginx/sites-enabled/{{ cookiecutter.repo_name }}.conf
sudo service nginx configtest
nginx -t
sudo service nginx restart
```

**OR** use sh script:

```bash
sudo bash bin/update_nginx.sh
```

* [How to uninstall project?](UNINSTALL_PROJECT.md)
* [Tips&tricks](MISC.md)
