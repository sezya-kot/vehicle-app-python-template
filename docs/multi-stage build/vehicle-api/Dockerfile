FROM ghcr.io/softwaredefinedvehicle/vehicle-app-python-template/client_base

RUN apt-get update 
RUN apt-get upgrade -y

ADD ./* $HOME/src/
WORKDIR /src
RUN pip3 install -r requirements.txt

EXPOSE 50051

ENTRYPOINT ["python"]
CMD ["run.py"]
