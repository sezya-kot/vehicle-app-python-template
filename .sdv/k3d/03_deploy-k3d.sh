#!/bin/bash

if [ -n "$1" ]; then
    echo "Building image with proxy configuration"
    # Build, push vehicleapi image
    cd /workspaces/vehicle-app-python-template/src/vehicle_sdk/vehicle_api_mock
    docker build \
    -f Dockerfile \
    -t localhost:12345/vehicleapi:local \
    --build-arg HTTP_PROXY="http://host.docker.internal:3128" \
    --build-arg HTTPS_PROXY="http://host.docker.internal:3128" \
    --build-arg FTP_PROXY="http://host.docker.internal:3128" \
    --build-arg ALL_PROXY="http://host.docker.internal:3128" \
    --build-arg NO_PROXY="localhost,127.0.0.1" .

    docker push localhost:12345/vehicleapi:local

    cd /workspaces/vehicle-app-python-template/src
    docker build \
    -f Dockerfile \
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
    cd /workspaces/vehicle-app-python-template/src/vehicle_sdk/vehicle_api_mock
    docker build -f Dockerfile -t localhost:12345/vehicleapi:local .
    docker push localhost:12345/vehicleapi:local

    cd /workspaces/vehicle-app-python-template/src
    docker build -f Dockerfile -t localhost:12345/seatadjuster:local .
    docker push localhost:12345/seatadjuster:local

    cd /workspaces/vehicle-app-python-template/.sdv/k3d
fi

# Deploy in Kubernetes
kubectl apply -f ./Deployment.vehicleapi.yml
kubectl apply -f ./Deployment.seatadjuster.yml