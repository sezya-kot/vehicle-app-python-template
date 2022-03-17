# Local kubernetes cluster
Devcontainer does not come with all the prerequisites installation required to run local kubernetes cluster.
Therefore for the user who has these needs to run demo-app within the local kubernetes cluster, we prepared the solution for that.

## Prerequisites
In order to build Vehicle-App image locally, you have to be authenticated into github.com registry. To do that follow the steps:

- Generate Bearer token in Github.com, [Account -> Settings -> Developer settings -> Personal Access Token -> Generate new token]
    - Use the scopes: Repository & Workflow
    - Write down the token for later access, you won't be able to display it again! If you miss to write it down, you have to re-generate the token
- Authorize the generated token [Configure SSO -> SoftwareDefinedVehicle -> Authorize ]
- In PowerShell [docker login ghcr.io -> Provide Username / Personal Access token]
- Login Succeeded message needs to be given

Troubleshooting:
- If the console returns you "Error response from daemon: unauthorized", please Authorize the granted token in Github (step 2).

## Installation and run:
- cd .sdv/k3d/
    - It is important for the scripts to be started from this directory
- 01_install-k3d.sh
    - Script will install k3d; helm; kubectl; k9s
- 02_configure-k3d.sh
    - Script will create a k3d cluster; local registry;
    - It will initialize environment with: Dapr, Mosquitto; Redis
- 03_deployprerequisites.sh
  - Prior to run a script, login to ghcr.io with your github token: ```docker login ghcr.io```
  - It will pull and install vehicle-data-broker and seatservice applications into k3d cluster
- 04_deploy-k3d.sh
  - It will build seatadjuster application and deploy it to the cluster. Personal token is required to be configured.
  - Ensure that the github_token.txt file is in its place with the correct content (Refer to the main README.md file for more details on how to create a github_token.txt)
- 99_installtooling.sh
  - It will install: k8s dashboard with printing out credentials
- Execute K9S and check that all containers are running

## Connecting to MQTT broker within the k3d cluster
- Seatadjuster app communicates over the mqtt broker outside of k8s cluster
- MQTT Broker is exposed over the port: 31883
- MQTT Broker can be found in vscode panel of extensions: symbol-cloud

## Connecting to Vehicle-data-broker within the k3d cluster
- Make sure that extension ```httpYac - Rest Client``` is installed
- Open script ```/test/vdb_collector.http```
- Change port to ```@port=30555```
- After pressing connect button, results with ```Vehicle.Speed``` should be returned
## Using k3d
k9s and kubectl tool are installed to operate local k3d cluster.
