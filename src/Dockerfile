FROM ghcr.io/softwaredefinedvehicle/vehicle-app-python-template/client_base

RUN apt-get update 
RUN apt-get upgrade -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10 

COPY ./src /src
COPY ./vehicleapi /vehicleapi
WORKDIR /src
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["client.py"]