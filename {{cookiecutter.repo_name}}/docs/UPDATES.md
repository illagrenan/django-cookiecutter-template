# Update `{{ cookiecutter.project_name }}`

You can update your project from localhost or on remote server.

## A) Update directly on the server ##

```bash
# Install updates:
cd {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}{{ cookiecutter.app_subdirectory_in_deploy_path }}
bash update.sh
```

This will:

1. Activate virtualenv
2. Pull repository
3. Install bower components
4. Copy `production.py` over `local.py`
5. Install Python requirements
6. Run `manage.py` commands: `collectstatic`, `migrate`, `compress`
7. Restart supervisor process


## B) Update from localhost ##

```bash
# Go to project root
djdeploy {TARGET} deploy
```
