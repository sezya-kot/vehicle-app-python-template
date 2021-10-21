#********************************************************************************
#* Copyright (c) 2021 Contributors to the Eclipse Foundation
#*
#* See the NOTICE file(s) distributed with this work for additional
#* information regarding copyright ownership.
#*
#* This program and the accompanying materials are made available under the
#* terms of the Eclipse Public License 2.0 which is available at
#* http://www.eclipse.org/legal/epl-2.0
#*
#* SPDX-License-Identifier: EPL-2.0
#********************************************************************************/

echo "#######################################################"
echo "### Checking proxy configuration                    ###"
echo "#######################################################"
sudo .devcontainer/proxy-script/configure-proxies.sh

echo "#######################################################"
echo "### Initializing mosquitto broker                   ###" 
echo "#######################################################"
docker run -d -p 1883:1883 -p 9001:9001 eclipse-mosquitto:1.6.9
