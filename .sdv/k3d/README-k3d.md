# Local kubernetes cluster
Devcontainer does not come with the all the prerequisites installation required to run local kubernetes cluster. 
Therefore for the user who has these needs to run demo-app within the local kubernetes cluster, we prepared the solution for that. 

## Prerequisites 
In order to build Vehicle-App image locally, you have to be authenticated into github.com registry. To do that follow the steps: 

- Generate Bearer token in Github.com [Account -> Settings -> Personal Access Token -> Generate token with correct scope]
- Authorize the generated token [Configure SSO -> SoftwareDefinedVehicle -> Authorize ]
- In PowerShell [docker login ghcr.io -> Provide Username / Personal Access token]
- Login Succeeded message needs to be given

Troubleshooting: 
- If the console returns you "Error response from daemon: unauthorized", please Authorize the granted token in Github (step 2). 

## Installation and run:
- 01_install-k3d.sh
    - Script will install k3d; helm; kubectl; brew; k9s
- 02_configure-k3d.sh
    - Script will create a k3d cluster; local registry; 
    - It will initialize environment with: Dapr, Mosquitto; Redis
    - It will install k8s dashboard and show token
    - > **PROXY:** When running devcontainer behind corporate proxy, execute script as following: ```./02_configure-k3d.sh proxy```
- 03_deploy-k3d.sh
    - It will build seat-adjuster application and deploy it to the cluster
    - > **PROXY:** When running devcontainer behind corporate proxy, execute script as following: ```./03_deploy-k3d.sh proxy```

## Connecting to MQTT broker within the k8s cluster
- Seatadjuster app communicates over the mqtt broker outside of k8s cluster
- MQTT Broker is exposed over the port: 31883
- MQTT Broker can be found in vscode panel of extensions: symbol-cloud

## Using k8s
k9s and kubectl tool are installed to operate local k3d cluster. 

## Opening local k8s dashboard:
- FETCH BEARER TOKEN: ```kubectl -n kubernetes-dashboard describe secret admin-user-token | grep ^token```
- RUN K8S PROXY: ```kubectl proxy```
- OPEN DASHBOARD IN BROWSER: [k8s Dashboard](http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/workloads?namespace=default)
