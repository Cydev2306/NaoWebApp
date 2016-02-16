# NaoWebApp.md
### A simple web application to control the Nao Robot


## Installation

This application only require **Vagrant**, you can install it by **[this way](https://www.vagrantup.com)**.
The application detect automatically if nao is on Wifi or Ethernet network.

First, you have to deploy Vagrant Machine and let the script running.

```
cd NaoWebApp
vagrant up --provision
```

if you want to find the application easilly, edit your **/etc/hosts** and add this row :
```
172.28.128.3 nao.local
```
## Logs
```
user: admin@gmail.com
pwd: admin

```
## Details

The VagrantFile will install this packages into a Debian VM with a shared folder into **/www/Nao-App**

```
apache2 php5  php5-mysql php5-sqlite sqlite3 mysql-server python
libpython2.7 build-essential python-dev python-PIL
```

Moreover, the provision script will configure NaoQi 1.14 and add the library to your PYTHONPATH

The web application is running on ZF1



## Motivation

I would simulate the application into a VM to get out of MAMP ( I am working on Mac OSX).

Further, if i have to change my environment (Win,OSX,linux), the installation of my work will not take several times. Just modify the
*public_network* into VagrantFile

---
## Technologies uses
- Python , Python Image Library
- PHP, mySql, ZF1
- Vagrant / VirtualBox
- NaoQi 1.14
