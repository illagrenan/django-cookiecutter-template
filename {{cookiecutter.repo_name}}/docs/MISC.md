# Tips&tricks for `{{ cookiecutter.project_name }}`

## Protect web with Basic auth

```bash
$ sudo apt-get install -y apache2-utils
$ sudo htpasswd -c {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.app_subdirectory_in_deploy_path }}.htpasswd admin
```

## Fix permissions in project directory

```bash
cd {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
sudo chown -R {{ cookiecutter.repo_name }}:{{ cookiecutter.group }} {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
find . -not -path '*/\.*' -type d -exec chmod 775 {} + # Better: 755
find . -not -path '*/\.*' -type f -exec chmod 664 {} + # Better: 644
chmod g+w log/*log
```

## Flush ngx_pagespeed cache

```bash
touch /tmp/ngx_pagespeed_cache/{{ cookiecutter.repo_name }}/cache.flush
```

## Supervisor without sudo

Create new group and add user that can control supervisorctl:

```bash
groupadd supervisor
usermod -a -G supervisor {SOME_USERNAME}
```

Edit supervisor config file:

```bash
nano /etc/supervisor/supervisord.conf
```

```ini
[unix_http_server]
file=/var/run/supervisor.sock   ; (the path to the socket file)
chmod=0770                      ; socket file mode (default 0700)
chown=root:supervisor
```

```bash
service supervisor restart
```

More info here: [https://github.com/illagrenan/ubuntu-supervisor-configuration](https://github.com/illagrenan/ubuntu-supervisor-configuration).

## Load database dump

```bash
psql -U postgres -d {{ cookiecutter.repo_name }} -f .\{{ cookiecutter.repo_name }}_2016-xxx.sql
```
