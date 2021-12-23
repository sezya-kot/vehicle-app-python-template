#!/bin/bash

if [ -n "$1" ]; then
    echo "Building image with proxy configuration"
    # Build, push vehicleapi image
    pip install git+https://github.com/SoftwareDefinedVehicle/sdv-vehicle-app-python-sdk.git@v0.1.0
    cd /home/vscode/.local/lib/python3.8/site-packages/sdv/
    docker build \
    -f vehicle_api_mock/Dockerfile \
    -t localhost:12345/vehicleapi:local \
    --build-arg HTTP_PROXY="http://host.docker.internal:3128" \
    --build-arg HTTPS_PROXY="http://host.docker.internal:3128" \
    --build-arg FTP_PROXY="http://host.docker.internal:3128" \
    --build-arg ALL_PROXY="http://host.docker.internal:3128" \
    --build-arg NO_PROXY="localhost,127.0.0.1" .

    docker push localhost:12345/vehicleapi:local

    cd /workspaces/vehicle-app-python-template/src
    DOCKER_BUILDKIT=1 docker build \
    -f Dockerfile \
    --progress=plain --secret id=github_token,src=github_token.txt \
    -t localhost:12345/seatadjuster:local \
    --build-arg HTTP_PROXY="http://host.docker.internal:3128" \
    --build-arg HTTPS_PROXY="http://host.docker.internal:3128" \
    --build-arg FTP_PROXY="http://host.docker.internal:3128" \
    --build-arg ALL_PROXY="http://host.docker.internal:3128" \
    --build-arg NO_PROXY="localhost,127.0.0.1" .
    docker push localhost:12345/seatadjuster:local

    cd /workspaces/vehicle-app-python-template/.sdv/k3d
else
    echo "Building image without proxy configuration"
    # Build, push vehicleapi image - NO PROXY
    pip install git+https://github.com/SoftwareDefinedVehicle/sdv-vehicle-app-python-sdk.git@v0.1.0
    cd /home/vscode/.local/lib/python3.8/site-packages/sdv/
    docker build -f vehicle_api_mock/Dockerfile -t localhost:12345/vehicleapi:local .
    docker push localhost:12345/vehicleapi:local

    cd /workspaces/vehicle-app-python-template/src
    DOCKER_BUILDKIT=1 docker build -f Dockerfile --progress=plain --secret id=github_token,src=github_token.txt -t localhost:12345/seatadjuster:local .
    docker push localhost:12345/seatadjuster:local

    cd /workspaces/vehicle-app-python-template/.sdv/k3d
fi

# Deploy in Kubernetes
kubectl apply -f ./Deployment.vehicleapi.yml
kubectl apply -f ./Deployment.seatadjuster.yml
