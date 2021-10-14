echo
echo "#######################################################"
echo "### Installing OS updates"
echo "#######################################################"
sudo apt-get update
sudo apt-get upgrade -y

sudo apt-get install -y wget ca-certificates

echo
echo "#######################################################"
echo "### Installing node js (version 14.x) and npm"
echo "#######################################################"
curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs

echo
echo "#######################################################"
echo "### Installing yarn"
echo "#######################################################"
curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/yarnkey.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/yarnkey.gpg] https://dl.yarnpkg.com/debian stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get install -y yarn
sudo apt upgrade -y
sudo yarn config set network-timeout 600000 -g
