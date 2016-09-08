# DOCKER

Source: [https://docs.docker.com/engine/installation/linux/ubuntulinux/](https://docs.docker.com/engine/installation/linux/ubuntulinux/)

## Installation

**Login as root!**

```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates

sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
nano /etc/apt/sources.list.d/docker.list
```

Remove everything and add:

```
deb https://apt.dockerproject.org/repo ubuntu-xenial main
```


```bash
sudo apt update
sudo apt-get purge lxc-docker

# Verify installation source:
apt-cache policy docker-engine

sudo apt install linux-image-extra-$(uname -r) linux-image-extra-virtual
sudo apt install docker-engine
sudo service docker start
sudo docker run --rm hello-world
```

Configure Docker to start on boot:

```bash
sudo systemctl enable docker
```

## Permissions

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Modify UFW forward policy:

```bash
sudo nano /etc/default/ufw
```

Add:

```ini
DEFAULT_FORWARD_POLICY="ACCEPT"
```

```bash
sudo ufw reload
```
