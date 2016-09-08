# SECURITY

## UFW

Source: 

* [https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server](https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server)
* [https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)

**Login as root!**

Enable UFW and check status:

```bash
ufw enable
ufw status verbose
```

Add some rules:

```bash
ufw default deny incoming
ufw default allow outgoing

ufw allow ssh
ufw allow https
ufw allow www
ufw allow from YOUR_IP to any port 10000 proto tcp
```

Delete single rule:

```bash
ufw status numbered
ufw delete <RULE_NUMBER>
```


Reset all:

```bash
ufw reset
```


## Fail2Ban

Source: [https://www.thefanclub.co.za/how-to/how-secure-ubuntu-1604-lts-server-part-1-basics](https://www.thefanclub.co.za/how-to/how-secure-ubuntu-1604-lts-server-part-1-basics)

```bash
sudo nano /etc/fail2ban/jail.conf
```

Add:

```ini
[sshd]

enabled  = true
port     = ssh
filter   = sshd
logpath  = /var/log/auth.log
maxretry = 3
sudo nano /etc/fail2ban/jail.conf
```


```bash
sudo service fail2ban restart
sudo fail2ban-client status
```
