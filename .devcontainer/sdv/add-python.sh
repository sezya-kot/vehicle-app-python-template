echo
echo "#######################################################"
echo "### Installing OS updates                           ###"
echo "#######################################################"
sudo apt-get update
sudo apt-get upgrade -y

sudo apt-get install -y wget ca-certificates

echo
echo "#######################################################"
echo "### Installing python version 3                     ###"
echo "#######################################################"
sudo apt-get install -y python3
sudo apt-get install -y python3-pip
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10 
pip3 install pytest
pip3 install -U flake8 