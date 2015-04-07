# Uninstall `{{ cookiecutter.project_name }}`

```bash
# 1) Remove Gunicorn configuration:
sudo supervisorctl stop {{ cookiecutter.repo_name }}
sudo rm /etc/supervisor/conf.d/{{ cookiecutter.repo_name }}.conf

# 2) Remove Nginx configuration:
sudo rm /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf
sudo rm /etc/nginx/sites-enabled/{{ cookiecutter.repo_name }}.conf
sudo rm -rf /tmp/ngx_pagespeed_cache/{{ cookiecutter.repo_name }}

sudo service nginx restart

# 3) Remove source code:
rm -r {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}

# 4) Remove user:
sudo userdel {{ cookiecutter.repo_name }}

# 5) Remove database
```