echo
echo "#######################################################"
echo "### Initializing dapr"
echo "#######################################################"
dapr uninstall --all 
dapr init 

echo
echo "#######################################################"
echo "### Initializing sender (python) project"
echo "#######################################################"
pip3 install -r ./sender/requirements.txt 

echo
echo "#######################################################"
echo "### Initializing receiver (node) project"
echo "#######################################################"
cd receiver 
sudo npm install