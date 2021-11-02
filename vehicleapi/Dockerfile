FROM ghcr.io/softwaredefinedvehicle/vehicle-app-python-template/vehicleapi_base

RUN apt-get update 
RUN apt-get upgrade
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10 

WORKDIR /vehicleapi
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 50051

ENTRYPOINT ["python"]
CMD ["vehicleapi.py"]