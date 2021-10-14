# Install pre-requisite packages.
sudo apt-get update
sudo apt-get install -y wget apt-transport-https software-properties-common

# Download the Microsoft repository GPG keys
wget -q https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O .sdv/tmp/packages-microsoft-prod.deb
sudo dpkg -i .sdv/tmp/packages-microsoft-prod.deb

# Update the list of packages after we added packages.microsoft.com
sudo apt-get update
sudo apt-get install -y powershell

rm -f .sdv/tmp/packages-microsoft-prod.deb
