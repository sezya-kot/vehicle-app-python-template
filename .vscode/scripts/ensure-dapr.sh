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
echo "### Installing dapr                                 ###"
echo "#######################################################"

version=$(dapr --version | grep "Runtime version: " | sed 's/^.*: //')

if ! [[ $version =~ ^([0-9]{1,2})\.([0-9]{1,2})\.([0-9]{1,2}) ]]; then
      daprReleaseUrl="https://api.github.com/repos/dapr/cli/releases"
      latest_release=$(curl -s $daprReleaseUrl | grep \"tag_name\" | grep -v rc | awk 'NR==1{print $2}' |  sed -n 's/\"\(.*\)\",/\1/p')
      if [ -z "$latest_release" ]
      then
            echo "Installing dapr pre-defined version: 1.6.0"
            wget -q https://raw.githubusercontent.com/dapr/cli/master/install/install.sh -O - | /bin/bash -s 1.6.0
      else
            echo "Installing dapr latest version: $latest_release"
            wget -q https://raw.githubusercontent.com/dapr/cli/master/install/install.sh -O - | /bin/bash
      fi

      dapr uninstall
      dapr init
else
      echo "Dapr is already installed and initialized, skipping setup."
fi

dapr --version