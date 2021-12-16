FROM python:3.9-slim-bullseye

RUN apt-get update 
RUN apt-get upgrade -y

ADD ./* $HOME/src/
WORKDIR /src
RUN pip3 install -r requirements.txt

RUN apt-get update 
RUN apt-get upgrade -y

LABEL org.opencontainers.image.source="https://github.com/softwaredefinedvehicle/vehicle-app-python-template"

ENTRYPOINT ["python"]
CMD ["run.py"]