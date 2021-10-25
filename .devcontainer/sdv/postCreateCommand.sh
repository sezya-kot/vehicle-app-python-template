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
echo "### Re-installing dapr if not available - fallback  ###"
echo "#######################################################"
if ! command -v dapr &> /dev/null
then
    #Re-installing dapr 
    sh .devcontainer/sdv/add-dapr.sh
fi

echo "#######################################################"
echo "### Initializing dapr                               ###"
echo "#######################################################"
dapr uninstall --all 
dapr init 

echo "#######################################################"
echo "### Initializing vehicleApp project                 ###"
echo "#######################################################"
pwsh -Command "Import-Module ./.sdv/Sdv.psm1; Find-SdvVehicleApp -Recurse | Get-SdvComponent | Initialize-SdvComponent -Verbose"
