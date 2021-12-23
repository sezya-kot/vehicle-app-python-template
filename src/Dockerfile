# syntax=docker/dockerfile:1.2
FROM python:3.9-slim-bullseye

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y git

ADD ./* $HOME/src/
WORKDIR /src
RUN --mount=type=secret,id=github_token credential=$(cat /run/secrets/github_token); pip3 install git+https://${credential}@github.com/SoftwareDefinedVehicle/sdv-vehicle-app-python-sdk.git@v0.1.2
RUN pip3 install -r requirements.txt

RUN apt-get update
RUN apt-get upgrade -y

LABEL org.opencontainers.image.source="https://github.com/softwaredefinedvehicle/vehicle-app-python-template"

ENTRYPOINT ["python"]
CMD ["run.py"]
