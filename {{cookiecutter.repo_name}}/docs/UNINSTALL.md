# Uninstall `{{ cookiecutter.project_name }}`

```bash
$ sudo rm /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf
$ sudo service nginx restart
$ 
$ sudo supervisorctl stop {{ cookiecutter.repo_name }}
$ sudo rm /etc/supervisor/conf.d/{{ cookiecutter.repo_name }}.conf
$ 
$ rmvirtualenv {{ cookiecutter.repo_name }}
$ rm -r /var/www/{{ cookiecutter.repo_name }}
```