# docker login ghcr.io 

docker build -t ghcr.io/softwaredefinedvehicle/vehicle-app-python-template/client_base_amd64 -f src/Dockerfile.base .
docker push ghcr.io/softwaredefinedvehicle/vehicle-app-python-template/client_base_amd64


docker build -t ghcr.io/softwaredefinedvehicle/vehicle-app-python-template/vehicleapi_base_amd64 -f vehicleapi/Dockerfile.base ./vehicleapi
docker push ghcr.io/softwaredefinedvehicle/vehicle-app-python-template/vehicleapi_base_amd64

# docker build -t vehicleapi -f vehicleapi/Dockerfile .