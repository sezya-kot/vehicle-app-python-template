#!/bin/sh

echo "Script executed from: ${PWD}"
temp=$OTA_SYSTEM_CREDENTIALS

# CONTAINER_REGISTRY=$(echo $temp | jq '.CONTAINER_REGISTRY')
CONTAINER_REGISTRY_ENDPOINT="swdceuwedevgsopscr.azurecr.io"
REGISTRY_USER=$(echo $temp | jq '.REGISTRY_USER')
REGISTRY_PASSWORD=$(echo $temp | jq '.REGISTRY_PASSWORD')
echo "::add-mask::$REGISTRY_PASSWORD"

echo "CONTAINER_REGISTRY_ENDPOINT=$CONTAINER_REGISTRY_ENDPOINT" >> $GITHUB_ENV
echo "REGISTRY_USER=$REGISTRY_USER" >> $GITHUB_ENV
echo "REGISTRY_PASSWORD=$REGISTRY_PASSWORD" >> $GITHUB_ENV

printenv
