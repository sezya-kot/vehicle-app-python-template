# syntax=docker/dockerfile:1.2

FROM python:3.9-slim-bullseye as base

# Build stage, to create a Virtual Environent
FROM base as builder

RUN apt-get update && apt-get upgrade -y

ADD ./* /

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN --mount=type=secret,id=github_token credential=$(cat /run/secrets/github_token); apt-get install -y git \
    && /opt/venv/bin/python3 -m pip install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt \
    && pip3 install --no-cache-dir git+https://${credential}@github.com/SoftwareDefinedVehicle/sdv-vehicle-app-python-sdk.git@v0.1.10

# Runner stage, to copy in the virtual environment and the app
FROM base

COPY --from=builder ./opt/venv /opt/venv

ADD ./* $HOME/src/

WORKDIR /src

ENV PYTHONPATH=/src:/opt/venv
ENV PATH=/opt/venv/bin/:$PATH

LABEL org.opencontainers.image.source="https://github.com/softwaredefinedvehicle/vehicle-app-python-template"

ENTRYPOINT ["python"]
CMD ["run.py"]
