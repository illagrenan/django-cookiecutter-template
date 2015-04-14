# Server setup

This guide is based on:


- [Michał Karzyński: Setting up Django with Nginx, Gunicorn, virtualenv, supervisor and PostgreSQL](http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/),
- [DigitalOcean.com: How To Install and Configure Django with Postgres, Nginx, and Gunicorn](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn).

## 0) Prerequisites ##

Create new Ubuntu LTS (current version is `14.04 x64`) server. For more information check Official Server Guide: [https://help.ubuntu.com/lts/serverguide/index.html](https://help.ubuntu.com/lts/serverguide/index.html).


## 1) Update packages ##

```bash
sudo apt-get update
sudo apt-get upgrade
```

## 2) Python tools ##

Install virtualenvs:

```bash
sudo apt-get install python-virtualenv
```

- More information about virtualenv: [The Hitchhiker’s Guide to Python: Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

Install Python header files:

```bash
sudo apt-get install python-dev
```


## 3) Database ##

A) Install MySQL:

```bash
sudo apt-get install mysql-server
```

- Check official documentation:[ https://dev.mysql.com/doc/refman/5.6/en/index.html]( https://dev.mysql.com/doc/refman/5.6/en/index.html)

B) Install PostgreSQL:

```bash
sudo apt-get install postgresql postgresql-contrib
sudo apt-get install libpq-dev
```

- Check official documentation: [http://www.postgresql.org/docs/9.4/static/index.html](http://www.postgresql.org/docs/9.4/static/index.html)


## 4) nginx ##

```bash
sudo apt-get install nginx
```

- Homepage: [http://nginx.org/](http://nginx.org/)

## 5) Supervisor ##

> Supervisor is a client/server system that allows its users to monitor and control a number of processes on UNIX-like operating systems. In this dev-stack will Supervisor monitor Gunicorn process.

Install Supervisor:

```bash
sudo apt-get install supervisor
```

- Homepage: [http://supervisord.org/](http://supervisord.org/)
- Tutorial: [DigitalOcean.com: How To Install and Manage Supervisor on Ubuntu and Debian VPS](https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-supervisor-on-ubuntu-and-debian-vps)

## 6) Git ##

Install Git:

```
sudo apt-get install git-core
```

- Homepage: [https://git-scm.herokuapp.com/](https://git-scm.herokuapp.com/)

## 7) node.js: node&npm&bower (optional) ##

> Web sites are made of lots of things — frameworks, libraries, assets, utilities, and rainbows. Bower manages all these things for you.

Install `node.js` only if you use Bower package manager for managing assets. See: [http://bower.io/](http://bower.io/).

```bash
sudo apt-get install nodejs
sudo apt-get install npm
```

And now install Bower globally:

```bash
npm -g install bower
``` 

- Tutorial: [DigitalOcean.com: How To Install Node.js on an Ubuntu 14.04 server](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-an-ubuntu-14-04-server)

----------

**You have now all required software installed!** Continue to [Deployment guide](DEPLOYMENT.md).