# SSL Connection

## Generate CSR request

```bash
cd {{ cookiecutter.deploy_path }}{{ cookiecutter.repo_name }}/{{ cookiecutter.app_subdirectory_in_deploy_path }}data/certs
openssl req -new -newkey rsa:4096 -days 365 -nodes -keyout {{ cookiecutter.repo_name }}.key -out {{ cookiecutter.repo_name }}.csr
```

```conf
ssl                         on;
ssl_certificate             {{ cookiecutter.repo_name }}.crt+class1.sha2.crt;
ssl_certificate_key         {{ cookiecutter.repo_name }}.key;
ssl_trusted_certificate     BUNDLE+ROOT.crt;
ssl_dhparam                 dhparam2048.pem;
```

https://www.startssl.com/certs/class1/sha2/pem/sub.class1.server.sha2.ca.pem

```bash
openssl dhparam -outform pem -out dhparam2048.pem 2048
```


# Generate self-signed certificate

```
openssl genrsa -des3 -out server.key 2048
openssl rsa -in server.key -out server.key
openssl req -sha256 -new -key server.key -out server.csr -subj '/CN=TODO_ADD_IP_OR_DOMAIN'
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```
