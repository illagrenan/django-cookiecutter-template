# Welcome to {{ cookiecutter.project_name }}

## Start with this repository ##

**Existing repository?**

```bash
git remote add origin git@{{ cookiecutter.git_provider }}:{{ cookiecutter.author_username }}/{{ cookiecutter.repo_name }}.git
git push -u origin --all
git push -u origin --tags
```

**New repository?**

```bash
git clone git@{{ cookiecutter.git_provider }}:{{ cookiecutter.author_username }}/{{ cookiecutter.repo_name }}.git
```

## What's next ##

* [Deploy project to Ubuntu](docs/DEPLOYMENT.md)
* [Uninstall project from Ubuntu](docs/UNINSTALL.md)
