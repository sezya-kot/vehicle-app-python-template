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

param(
    [Parameter(ParameterSetName="ByName", Mandatory=$false, Position=0)]
    [string]$Name,
    [switch]$UseDockerCompose
)

Import-Module $PSScriptRoot/Sdv.psm1 -Force
if ($PsCmdlet.ParameterSetName -eq "ByName") {
    $Configuration = Find-SdvVehicleApp -Name $Name
} else {
    $Configuration = Find-SdvVehicleApp
}

Enter-LoggingGroup ("Starting application {0}" -f $Component.Name)
try {
    $Configuration | Get-SdvComponent | Start-SdvComponent
    Exit-LoggingGroup

    Write-SdvLogging "Waiting 10 seconds"
    Start-Sleep 10

    Enter-LoggingGroup ("Stopping application {0}" -f $Component.Name)
    $Configuration | Get-SdvComponent | Stop-SdvComponent 
    Exit-LoggingGroup
} catch {
    Write-SdvError ("Failed to run integration tests: {0}" -f $_)
}