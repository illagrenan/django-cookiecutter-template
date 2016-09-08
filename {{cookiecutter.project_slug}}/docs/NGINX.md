# NGINX

**Login as root!**

```bash
service nginx stop


mkdir -p /etc/nginx/sites-enabled
mkdir -p /etc/nginx/sites-available

sudo curl https://raw.githubusercontent.com/illagrenan/django-cookiecutter-template/master/%7B%7Bcookiecutter.project_slug%7D%7D/conf/etc-nginx/nginx.conf > /etc/nginx/nginx.conf
sudo curl https://raw.githubusercontent.com/illagrenan/django-cookiecutter-template/master/%7B%7Bcookiecutter.project_slug%7D%7D/conf/etc-nginx/mime.types > /etc/nginx/mime.types
sudo curl https://raw.githubusercontent.com/illagrenan/django-cookiecutter-template/master/%7B%7Bcookiecutter.project_slug%7D%7D/conf/etc-nginx/conf.d/no-default.conf > /etc/nginx/conf.d/no-default.conf

sudo service nginx configtest
service nginx start
```
