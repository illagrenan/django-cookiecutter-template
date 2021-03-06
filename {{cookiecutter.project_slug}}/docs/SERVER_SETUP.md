# Server setup

This guide is based on:


- [Michał Karzyński: Setting up Django with Nginx, Gunicorn, virtualenv, supervisor and PostgreSQL](http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/),
- [DigitalOcean.com: How To Install and Configure Django with Postgres, Nginx, and Gunicorn](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn).

## 0) Prerequisites ##

Create new Ubuntu LTS (current LTS version is `16.04 x64` (**`xenial`**)) server. For more information check Official Server Guide: [https://help.ubuntu.com/lts/serverguide/index.html](https://help.ubuntu.com/lts/serverguide/index.html).

## 01) Password ##

Change root's password:

```bash
sudo passwd
```


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
sudo apt update
sudo apt upgrade
```

It is recomended to reboot computer after first upgrade:

```bash
reboot
```

Install required libraries:

```bash
sudo apt install libffi-dev         # bridge between interpreted and natively compiled code
sudo apt install ntpdate            # for Time server sync (`ntp.ubuntu.com`)

# ???:
# sudo apt install libxml2-dev libxslt1-dev python-lxml
```

## 3) Python ##

**Install Python 3.5 [from deadsnakes](https://launchpad.net/~fkrull/+archive/ubuntu/deadsnakes):**

```bash
sudo apt -y install software-properties-common
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get -y install python3.5 python3.5-dev
```

Python is now installed at `/usr/bin/python3.5`. Or use [pyenv](https://github.com/yyuu/pyenv).

**Install pip:**

```bash
wget https://bootstrap.pypa.io/get-pip.py -O - | python

# Upgrade after installation
pip install --upgrade pip setuptools
```

**Install virtualenvs:**

```bash
[sudo] pip install virtualenv
```

- More information about virtualenv: [The Hitchhiker’s Guide to Python: Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
- Official installation instruction: [https://virtualenv.pypa.io/en/latest/installation.html](https://virtualenv.pypa.io/en/latest/installation.html)


## 4) PostgreSQL ##

```bash
# Check version that will be installed (should be 9.6+)
apt-cache policy postgresql

sudo apt install postgresql postgresql-contrib

# Needed by psycopg:
sudo apt install libpq-dev
```

- Check official documentation: [http://www.postgresql.org/docs/9.4/static/index.html](http://www.postgresql.org/docs/9.4/static/index.html)


## 5) nginx ##

```bash
sudo apt install nginx
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
apt update
apt install nginx
```

Check if nginx is installed:

```bash
nginx -v
nginx version: nginx/1.11.3
```

**Note:**

If you previously installed nginx from Ubuntu sources, uninstall package by:

```bash
sudo apt-get purge nginx
sudo apt-get autoremove
```

Continue to page [NGINX CONFIGURATION](NGINX.md)

## 6) Supervisor ##

**Follow these instructions:** [https://github.com/illagrenan/ubuntu-supervisor-configuration](https://github.com/illagrenan/ubuntu-supervisor-configuration).

## 7) Git ##

Install Git:

```bash
sudo apt install git-core
```

- Homepage: [https://git-scm.herokuapp.com/](https://git-scm.herokuapp.com/)

## 8) node.js: node&(npm or yarn)&bower (optional) ##

> Web sites are made of lots of things — frameworks, libraries, assets, utilities, and rainbows. Bower manages all these things for you.

Install `node.js` only if you use Bower package manager for managing assets. See: [http://bower.io/](http://bower.io/).

```bash
sudo apt install nodejs
sudo apt install npm

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

Yarn:

```bash
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get install yarn
```

See: [https://yarnpkg.com/en/docs/install](https://yarnpkg.com/en/docs/install#linux-tab).

## 9) Useful software (optional) ##

**Gettext**

```bash
apt install -y gettext
```

**Glances**

> Glances an Eye on your system, see: [https://nicolargo.github.io/glances/](https://nicolargo.github.io/glances/)

*Optional dependencies (only if you want more features e.g. sensors):*
```bash
sudo apt install lm-sensors
pip install bottle batinfo https://bitbucket.org/gleb_zhulik/py3sensors/get/tip.tar.gz zeroconf netifaces pymdstat influxdb statsd pystache
```

*Required:*
```bash
pip install --upgrade Glances
```


**Midnight Commander**

> GNU Midnight Commander is a visual file manager, see: [https://www.midnight-commander.org/](https://www.midnight-commander.org/)

```bash
sudo apt install mc
```

**Mutt**

> The Mutt E-Mail Client, see: [http://www.mutt.org/](http://www.mutt.org/)

```bash
sudo apt install mutt
/etc/init.d/postfix reload
```

**GoAccess**

> GoAccess is an open source real-time web log analyzer and interactive viewer that runs in a terminal in \*nix systems. It provides fast and valuable HTTP statistics for system administrators that require a visual server report on the fly. See: [http://goaccess.io/](http://goaccess.io/).

```bash
# See: http://goaccess.io/download#official-repo
echo "deb http://deb.goaccess.io $(lsb_release -cs) main" | tee -a /etc/apt/sources.list
wget -O - http://deb.goaccess.io/gnugpg.key | apt-key add -
apt update
apt install goaccess
```

**Links2**

> Links is a graphics and text mode WWW browser, similar to Lynx.

```bash
apt install links2
```



## 10) Pillow (optional) ##

Install external libraries (see: [pillow.readthedocs.org/en/latest/installation.html#external-libraries](https://pillow.readthedocs.org/en/latest/installation.html#external-libraries)):

```bash
# ???
# sudo apt install libjpeg-dev libtiff-dev libfreetype6 libfreetype6-dev zlib1g-dev
```

and then:

```bash
pip install Pillow
```

## 11) Caching ##

A) Redis (optional, preferred)

```bash
# ???
# sudo apt -y install python-software-properties


sudo add-apt-repository -y ppa:chris-lea/redis-server
sudo apt -y update
sudo apt -y install redis-server
```

See: https://github.com/niwinz/django-redis and http://michal.karzynski.pl/blog/2013/07/14/using-redis-as-django-session-store-and-cache-backend/

## 12) Webmin (optional) ##

Update and upgrade packages:

```bash
sudo apt update
sudo apt upgrade
```

Download Webmin:

```bash
wget https://prdownloads.sourceforge.net/webadmin/webmin_1.810_all.deb
dpkg --install webmin_1.810_all.deb
```

To install missing dependencies, install them with:

```bash
apt-get -f install
```

Now open `https://IP_ADDRESS:10000`.

Finally remove downloaded package:

```bash
rm webmin_1.810_all.deb
```

For more information check:

- [http://www.webmin.com/deb.html](http://www.webmin.com/deb.html)

If isn't Webmin running, reboot it:

```bash
/etc/init.d/webmin restart
```


## 13) RabbitMQ for Celery (deprecated, use Redis) ##


```bash
echo "deb http://www.rabbitmq.com/debian/ testing main" | tee -a /etc/apt/sources.list
wget -O - https://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add -

apt update
sudo apt install rabbitmq-server
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
sudo apt install fail2ban
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
```

## 17) Let's Encrypt ##


```bash
sudo apt -y install letsencrypt 
```

----------

**You have now all required software installed!** Continue to [Deployment guide](DEPLOYMENT.md).
