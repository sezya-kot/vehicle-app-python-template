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
    [Parameter(Mandatory=$true, Position=0)]
    [string]$Name,
    [switch]$InPipeline,
    [switch]$UseDockerCompose
)

Import-Module $PSScriptRoot/Sdv.psm1 -Force

$Configuration = Find-SdvVehicleApp -Name $Name

$Configuration | Get-SdvComponent | Start-SdvComponent

Start-Sleep 10

$Configuration | Get-SdvComponent | Stop-SdvComponent 
