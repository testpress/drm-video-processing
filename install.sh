#!/bin/bash

REQUIRED_PKG="ffmpeg"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG | grep "installed")

echo "Checking for $REQUIRED_PKG: $PKG_OK"

if [ "" = "$PKG_OK" ]; then
  echo "No $REQUIRED_PKG. Setting up $REQUIRED_PKG."
  sudo apt-get --yes install $REQUIRED_PKG 
  echo "Installed $REQUIRED_PKG"
fi

if ! which packager > /dev/null 2>&1; then
  echo "Installing Shaka packager"
  wget https://github.com/shaka-project/shaka-packager/releases/download/v2.6.1/packager-linux-x64
  sudo mv packager-linux-x64 /usr/local/bin/packager
  sudo chmod +rx /usr/local/bin/packager
  echo "Shaka packager installation completed successfully"
else
  echo "Shaka packager: already installed"
fi

if ! type python3 > /dev/null 2>&1; then
  echo "Installing Python 3"
  sudo apt-get --yes install python3
  echo "Installed Python 3"
else
  echo "Python 3: already installed"
fi

# Install pycryptodomex
echo "Installing pycryptodomex"
sudo apt-get --yes install python3-pip
python3 -m pip install pycryptodomex
echo "Installed pycryptodomex"
