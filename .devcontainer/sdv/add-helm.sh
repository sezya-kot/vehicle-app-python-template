export HTTP_PROXY=${HTTP_PROXY}
export HTTPS_PROXY=${HTTPS_PROXY}
export NO_PROXY=${NO_PROXY}

echo "#######################################################"
echo "### Installing OS updates                           ###"
echo "#######################################################"
sudo apt-get update
sudo apt-get upgrade -y

echo "#######################################################"
echo "### Installing helm                                 ###"
echo "#######################################################"

echo "## Download the latest version of Helm"
sudo wget https://get.helm.sh/helm-v3.4.1-linux-amd64.tar.gz

echo "## Unpack the Helm file using tar command. The output displays four unpacked files"
sudo tar xvf helm-v3.4.1-linux-amd64.tar.gz

echo "## Move the linux-amd64/helm file to the /usr/local/bin directory. There will be no output if the command was executed correctly"
sudo mv linux-amd64/helm /usr/local/bin

echo "## Removing the downloaded file"
sudo rm helm-v3.4.1-linux-amd64.tar.gz

echo "## Removing the linux-amd64 directory to clean up space. There is no output if the process completes successfully"
sudo rm -rf linux-amd64

echo "## The installed Helm version of the software"
sudo helm version