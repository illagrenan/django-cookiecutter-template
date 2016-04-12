# Server setup

This guide is based on:


- [Michał Karzyński: Setting up Django with Nginx, Gunicorn, virtualenv, supervisor and PostgreSQL](http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/),
- [DigitalOcean.com: How To Install and Configure Django with Postgres, Nginx, and Gunicorn](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn).

## 0) Prerequisites ##

Create new Ubuntu LTS (current LTS version is `14.04 x64` (**`trusty`**)) server. For more information check Official Server Guide: [https://help.ubuntu.com/lts/serverguide/index.html](https://help.ubuntu.com/lts/serverguide/index.html).


## 1) Swap ##


Check already configured swap:

```bash
sudo swapon -s
# OR
free -m
```

Check available space:

```bash
df -h
```


Create 4GB swapfile:

```bash
sudo fallocate -l 4G /swapfile
ls -lh /swapfile
```

Enable swapfile:

```bash
sudo chmod 600 /swapfile
ls -lh /swapfile
-rw------- 1 root root 4.0G Apr 22 07:39 /swapfile

sudo mkswap /swapfile
Setting up swapspace version 1, size = 4194300 KiB
no label, UUID=9a23f475-2d54-4589-a03e-e499b5142986

sudo swapon /swapfile
sudo swapon -s
free -m
```

Make the swap file permanent:

```bash
sudo nano /etc/fstab
```

Add to last line:

```
/swapfile   none    swap    sw    0   0
```

**Swappiness (optional)**

```bash
sudo sysctl vm.swappiness=10
sudo sysctl vm.vfs_cache_pressure=50
```

Open:

```bash
sudo nano /etc/sysctl.conf
```

And add at the bottom:

```
vm.swappiness=10
vm.vfs_cache_pressure = 50
```

More info:

- [https://www.digitalocean.com/community/tutorials/how-to-add-swap-on-ubuntu-14-04](https://www.digitalocean.com/community/tutorials/how-to-add-swap-on-ubuntu-14-04)


## 2) Update packages ##

```bash
sudo apt-get update
sudo apt-get upgrade
```

It is recomended to reboot computer after first upgrade:

```bash
reboot
```

Install required libraries:

```bash
sudo apt-get install libxml2-dev libxslt1-dev libffi-dev python-lxml
```

## 3) Python tools ##

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


## 4) Database ##

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


## 5) nginx ##

```bash
sudo apt-get install nginx
```

To get latest releases append these lines to `/etc/apt/sources.list`:

```bash
echo "deb http://nginx.org/packages/mainline/ubuntu/ $(lsb_release -cs) nginx" | tee -a /etc/apt/sources.list
echo "deb-src http://nginx.org/packages/mainline/ubuntu/ $(lsb_release -cs) nginx" | tee -a /etc/apt/sources.list
```

And install signing key:

```bash
wget -O - http://nginx.org/keys/nginx_signing.key | apt-key add -
```

And run:

```bash
apt-get update
apt-get install nginx
```

Check if nginx is installed:

```bash
nginx -v
nginx version: nginx/1.8.0
```

**Note:**

If you previously installed nginx from Ubuntu sources, uninstall package by:

```bash
sudo apt-get purge nginx
sudo apt-get autoremove
```

- Homepage: [http://nginx.org/](http://nginx.org/)

## 6) Supervisor ##

> Supervisor is a client/server system that allows its users to monitor and control a number of processes on UNIX-like operating systems. In this dev-stack will Supervisor monitor Gunicorn process.

Follow these instructions: https://github.com/illagrenan/ubuntu-supervisor-configuration.

- Homepage: [http://supervisord.org/](http://supervisord.org/)
- Tutorial: [DigitalOcean.com: How To Install and Manage Supervisor on Ubuntu and Debian VPS](https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-supervisor-on-ubuntu-and-debian-vps)

## 7) Git ##

Install Git:

```
sudo apt-get install git-core
```

- Homepage: [https://git-scm.herokuapp.com/](https://git-scm.herokuapp.com/)

## 8) node.js: node&npm&bower (optional) ##

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

Update node and npm:

```
sudo npm cache clean -f
sudo npm install -g n
sudo n stable

sudo ln -sf /usr/local/n/versions/node/<VERSION>/bin/node /usr/bin/node
```

And now install Bower globally:

```bash
npm -g install bower
```

- Tutorial: [DigitalOcean.com: How To Install Node.js on an Ubuntu 14.04 server](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-an-ubuntu-14-04-server)

## 9) Useful software (optional) ##

**Gettext**

```bash
apt-get install -y gettext
```

**Glances**

> Glances an Eye on your system, see: [https://nicolargo.github.io/glances/](https://nicolargo.github.io/glances/)

*Optional dependencies (only if you want more features e.g. sensors):*
```bash
sudo apt-get install lm-sensors
pip install bottle batinfo https://bitbucket.org/gleb_zhulik/py3sensors/get/tip.tar.gz zeroconf netifaces pymdstat influxdb statsd pystache
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
/etc/init.d/postfix reload
```

**GoAccess**

> GoAccess is an open source real-time web log analyzer and interactive viewer that runs in a terminal in \*nix systems. It provides fast and valuable HTTP statistics for system administrators that require a visual server report on the fly. See: [http://goaccess.io/](http://goaccess.io/).

```bash
# See: http://goaccess.io/download#official-repo
echo "deb http://deb.goaccess.io $(lsb_release -cs) main" | tee -a /etc/apt/sources.list
wget -O - http://deb.goaccess.io/gnugpg.key | apt-key add -
apt-get update
apt-get install goaccess
```

**Links2**

> Links is a graphics and text mode WWW browser, similar to Lynx.

```bash
apt-get install links2
```



## 10) Pillow (optional) ##

Install external libraries (see: [pillow.readthedocs.org/en/latest/installation.html#external-libraries](https://pillow.readthedocs.org/en/latest/installation.html#external-libraries)):

```bash
sudo apt-get install libjpeg-dev libtiff-dev libfreetype6 libfreetype6-dev zlib1g-dev
```

and then:

```bash
pip install Pillow
```

## 11) Caching ##

A) Redis (optional, preferred)

```bash
sudo apt-get -y install python-software-properties
sudo add-apt-repository -y ppa:chris-lea/redis-server
sudo apt-get -y update
sudo apt-get -y install redis-server
```

See: https://github.com/niwinz/django-redis and http://michal.karzynski.pl/blog/2013/07/14/using-redis-as-django-session-store-and-cache-backend/

B) Memcached (optional)

```bash
sudo apt-get install -y memcached libmemcached-dev libmemcached-tools
```

Check if Memcache is running by:

```bash
echo stats | nc 127.0.0.1 11211
```

To use Memcached from Python/Django, install:

```bash
pip install --upgrade python-memcached
```

For more information check:

- [https://docs.djangoproject.com/en/1.8/topics/cache/#memcached](https://docs.djangoproject.com/en/1.8/topics/cache/#memcached)
- [https://github.com/lericson/pylibmc](https://github.com/lericson/pylibmc)

## 12) Webmin (optional) ##

Update and upgrade packages:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Download Webmin:

```bash
wget http://prdownloads.sourceforge.net/webadmin/webmin_1.791_all.deb
dpkg --install webmin_1.791_all.deb
```

To install missing dependencies, install them with:

```bash
apt-get -f install
```

Now open `https://IP_ADDRESS:10000`.

Finally remove downloaded package:

```bash
rm webmin_1.791_all.deb
```

For more information check:

- [http://www.webmin.com/deb.html](http://www.webmin.com/deb.html)

## 13) Users and groups ##

Create new non-sudo user:

```bash
adduser <username>
mkdir -p /var/www/
sudo chown -R <username>:root /var/www
```

Switch to newly created user:

```bash
su <username>
```

And create new ssh-keypair:

```bash
ssh-keygen -t rsa -C "your_email@example.com"
# Or simply:
ssh-keygen -t rsa
touch ~/.ssh/authorized_keys

# Copy your public key
nano ~/.ssh/authorized_keys
```

Create new group:

```bash
sudo groupadd --system webapps
# Add newly created user:
usermod -a -G {{ cookiecutter.group }} <username>
usermod -a -G supervisor <username>
```

If you're logged-in as non-sudo user, reload profile:

```bash
. ~/.profile
```

Fix `~/.ssh` permissions:

```bash
chmod go-w ~/
chmod 700 ~/.ssh
chmod 600 -R  ~/.ssh/*
```

## 14) Celery ##


```bash
echo "deb http://www.rabbitmq.com/debian/ testing main" | tee -a /etc/apt/sources.list
wget -O - https://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add -

apt-get update
sudo apt-get install rabbitmq-server
```

Add new rabbitmq user and vhost:

```bash
rabbitmqctl add_user <USERNAME> <PASSWORD>
rabbitmqctl add_vhost <VHOST_NAME>
rabbitmqctl set_permissions -p <VHOST_NAME> <USERNAME> ".*" ".*" ".*"
```

## 15) Install global npm packages ##


```bash
npm install -g gulp less jshint imagemin-pngquant node-gyp
```

## 16) Install fail2ban ##


```bash
sudo apt-get install fail2ban
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
```

----------

**You have now all required software installed!** Continue to [Deployment guide](DEPLOYMENT.md).
