# Uninstall `{{ cookiecutter.project_name }}`

```bash
$ # 1) Remove Gunicorn:
$ sudo supervisorctl stop {{ cookiecutter.repo_name }}
$ sudo rm /etc/supervisor/conf.d/{{ cookiecutter.repo_name }}.conf
$
$ # 2) Remove Nginx:
$ sudo rm /etc/nginx/sites-available/{{ cookiecutter.repo_name }}.conf
$ sudo service nginx restart
$
$ # 3) Remove virtualenv:
$ cd {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
$ rm -r  data/.venv
$
$ # 4) Remove source code:
$ rm -r {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}
```