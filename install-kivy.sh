#!/usr/bin/env bash

#raspberry pi icin kivy kurulum scripti
#Yararlanilan Adres http://mattrichardson.com/kivy-gpio-raspberry-pi-touch/index.html

cd ~

sudo su root -c "echo 'Acquire::http::Proxy \"http://10.1.1.51:3128\";' >> /etc/apt/apt.conf"

sudo apt-get update && sudo apt-get -y upgrade
sudo su root -c "echo 'deb http://vontaene.de/raspbian-updates/ . main' >> /etc/apt/sources.list"
gpg --keyserver pgp.mit.edu --recv-keys 0C667A3E
gpg -a --export 0C667A3E | sudo apt-key add -

sudo apt-get update
sudo apt-get -y install pkg-config libgl1-mesa-dev libgles2-mesa-dev python-pygame python-setuptools libgstreamer1.0-dev git-core gstreamer1.0-plugins-{bad,base,good,ugly} gstreamer1.0-{omx,alsa} python-dev

wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo pip install cython pygments docutils
git clone https://github.com/kivy/kivy
cd kivy
python setup.py build
sudo python setup.py install
cd ~/uretim

