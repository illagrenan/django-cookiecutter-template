# PostgreSQL

Source: [https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)

**Login as root!**

Enter psql shell:

```bash
sudo su - postgres
psql
```

Create database:

```bash
CREATE DATABASE {{ cookiecutter.repo_name }};
CREATE USER {{ cookiecutter.db_user }} WITH PASSWORD '******';
```


Change connection parameters:

```bash
ALTER ROLE {{ cookiecutter.db_user }} SET client_encoding TO 'utf8';
ALTER ROLE {{ cookiecutter.db_user }} SET default_transaction_isolation TO 'read committed';
ALTER ROLE {{ cookiecutter.db_user }} SET timezone TO 'UTC';
```


And give access to create user:

```bash
GRANT ALL PRIVILEGES ON DATABASE {{ cookiecutter.repo_name }} TO {{ cookiecutter.db_user }};
```

Finally exit shell:

```bash
\q
```

And exit session:

```bash
exit
```
