# Let's Encrypt

**Login as root!**

```bash
cd /opt/letsencrypt
service nginx stop

# 1) Renew only selected domains:
./letsencrypt-auto certonly -d {{ cookiecutter.domain_name }} -d www.{{ cookiecutter.domain_name }} --standalone --agree-tos --non-interactive

# 2) Or renew all:
./letsencrypt-auto renew --standalone --agree-tos

service nginx start
```
