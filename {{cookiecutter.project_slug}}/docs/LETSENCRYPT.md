# Let's Encrypt

**Login as root!**

```bash
cd /opt/letsencrypt
service nginx stop
./letsencrypt-auto certonly -d {{ cookiecutter.domain_name }} -d www.{{ cookiecutter.domain_name }} --standalone --agree-tos --non-interactive
service nginx start
```
