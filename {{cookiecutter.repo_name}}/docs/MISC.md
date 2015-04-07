# Tips&tricks for `{{ cookiecutter.project_name }}`

## Protect web with hpasswd

```bash
$ sudo apt-get install -y apache2-utils
$ sudo htpasswd -c {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/.htpasswd admin
```

## Fix permissions

```bash
cd {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
sudo chown -R {{ cookiecutter.repo_name }}:{{ cookiecutter.group }} {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
find . -not -path '*/\.*' -type d -exec chmod 775 {} +
find . -not -path '*/\.*' -type f -exec chmod 664 {} +
chmod g+w log/*log
chmod u+x bin/gunicorn_start.sh
```

## Flush ngx_pagespeed cache

```bash
touch /tmp/ngx_pagespeed_cache/{{ cookiecutter.repo_name }}/cache.flush
```

## Generate CSR request

```bash
cd {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/data/certs
openssl req -new -newkey rsa:4096 -days 365 -nodes -keyout {{ cookiecutter.repo_name }}.key -out {{ cookiecutter.repo_name }}.csr
```

## Supervisor without sudo

Create new group and add ourselves:

```bash
groupadd supervisor
usermod -a -G supervisor <myusername>
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