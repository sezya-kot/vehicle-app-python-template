# Copyright (c) 2022 Robert Bosch GmbH and Microsoft Corporation
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0

chmod +x .devcontainer/scripts/*.sh
sudo chown -R $(whoami) $HOME

echo "#######################################################"
echo "### Checking proxies                                ###"
echo "#######################################################"
sudo .devcontainer/scripts/configure-proxies.sh | tee -a $HOME/configure-proxies.log

echo "#######################################################"
echo "### Install Jq                                      ###"
echo "#######################################################"
apt-get install -y jq

echo "#######################################################"
echo "### Executing container-set.sh                      ###"
echo "#######################################################"
.devcontainer/scripts/container-set.sh 2>&1 | tee -a $HOME/container-set.log

echo "#######################################################"
echo "### Executing add-python.sh                         ###"
echo "#######################################################"
.devcontainer/scripts/add-python.sh 2>&1 | tee -a $HOME/add-python.log

echo "#######################################################"
echo "### Install python requirements                     ###"
echo "#######################################################"
REQUIREMENTS="./requirements-dev.txt"
if [ -f $REQUIREMENTS ]; then
    pip3 install -r $REQUIREMENTS
fi
REQUIREMENTS="./src/requirements-sdv.txt"
if [ -f $REQUIREMENTS ]; then
    pip3 install -r $REQUIREMENTS
fi
REQUIREMENTS="./src/requirements.txt"
if [ -f $REQUIREMENTS ]; then
    pip3 install -r $REQUIREMENTS
fi
