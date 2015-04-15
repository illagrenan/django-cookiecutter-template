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

Install required libraries:

```bash
sudo apt-get install libxml2-dev libxslt1-dev libffi-dev
```

## 2) Python tools ##

**Install Python header files:**

```bash
sudo apt-get install python-dev
```

**Install pip:**

```bash
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
rm get-pip.py

# Upgrade after installation
pip install --upgrade pip setuptools
```

**Install virtualenvs:**

```bash
[sudo] pip install virtualenv
```

- More information about virtualenv: [The Hitchhiker’s Guide to Python: Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
- Official installation instruction: [https://virtualenv.pypa.io/en/latest/installation.html](https://virtualenv.pypa.io/en/latest/installation.html)


## 3) Database ##

A) Install MySQL:

```bash
sudo apt-get install mysql-server
sudo apt-get install python-mysqldb libmysqlclient-dev
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

# ########################################  
# Try run "node"
# if /usr/bin/env: node: No such file or directory
#  
# Fix this by:
sudo ln -s /usr/bin/nodejs /usr/bin/node
# ########################################  
```

And now install Bower globally:

```bash
npm -g install bower
```

- Tutorial: [DigitalOcean.com: How To Install Node.js on an Ubuntu 14.04 server](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-an-ubuntu-14-04-server)

## 8) Useful software (optional) ##

**Glances**

> Glances an Eye on your system, see: [https://nicolargo.github.io/glances/](https://nicolargo.github.io/glances/)

*Optional dependencies (more features):*
```bash
sudo apt-get install lm-sensors
pip install bottle batinfo https://bitbucket.org/gleb_zhulik/py3sensors/get/tip.tar.gz zeroconf netifaces pymdstat influxdb statsd pystache
pip install --upgrade Glances
```

*Required:*
```bash
pip install --upgrade Glances
```


**Midnight Commander**

> GNU Midnight Commander is a visual file manager, see: [https://www.midnight-commander.org/](https://www.midnight-commander.org/)

```bash
sudo apt-get install mc
```

**Mutt**

> The Mutt E-Mail Client, see: [http://www.mutt.org/](http://www.mutt.org/)

```bash
sudo apt-get install mutt
```

----------

**You have now all required software installed!** Continue to [Deployment guide](DEPLOYMENT.md).
