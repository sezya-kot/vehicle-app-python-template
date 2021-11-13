# /********************************************************************************
# * Copyright (c) 2021 Contributors to the Eclipse Foundation
# *
# * See the NOTICE file(s) distributed with this work for additional
# * information regarding copyright ownership.
# *
# * This program and the accompanying materials are made available under the
# * terms of the Eclipse Public License 2.0 which is available at
# * http://www.eclipse.org/legal/epl-2.0
# *
# * SPDX-License-Identifier: EPL-2.0
# ********************************************************************************/

import json
import logging
import os
from typing import Any

# from __future__ import print_function
from cloudevents.sdk.event import v1
from dapr.ext.grpc import App
from flask import jsonify, request
from grpc import local_channel_credentials

import swdc_comfort_seats_pb2
from VehicleSdk import VehicleClient

app = App()


@app.subscribe(pubsub_name='mqtt-pubsub', topic='seatadjuster/setPosition/request/gui-app', metadata={'rawPayload': 'true'}, )
def onSetPositionRequestGuiAppReceived(event: v1.Event) -> None:
    data = json.loads(event.Data())
    onSetPositionRequestReceived(data, "gui-app")


@app.subscribe(pubsub_name='mqtt-pubsub', topic='seatadjuster/setPosition/request/bfb-app', metadata={'rawPayload': 'true'}, )
def onSetPositionRequestBfbAppReceived(event: v1.Event) -> None:
    data = json.loads(event.Data())
    onSetPositionRequestReceived(data, "bfb-app")


def onSetPositionRequestReceived(data: any, topic: str) -> None:
    print(f'Set Position Request received: Position={data["position"]}, RequestId="{data["requestId"]} Topic={topic}', flush=True)  # noqa: E501
    vehicleClient = VehicleClient()
    vehicleMovingSpeed = getVehicleMovingSpeed()

    if vehicleMovingSpeed == 0:
        try:
            location = swdc_comfort_seats_pb2.SeatLocation(row=1, index=1)
            component = swdc_comfort_seats_pb2.BASE
            vehicleClient.Seats.MoveComponent(location, component, data["position"])

            resp_data = {
                'requestId': data["requestId"],
                'result': {
                    'status': 0
                }
            }
        except Exception as ex:
            resp_data = {
                'status': data["requestId"],
                'message': getErrorMessageFrom(ex)
            }
    else:
        resp_data = {
            'requestId': data["requestId"],
            'result': {
                'status': 1
            }
        }
    publishDataToTopic(resp_data, topic, vehicleClient)

def getErrorMessageFrom(ex: Exception):
    errorMessage = str()
    if hasattr(ex, 'message'):
        errorMessage = ex.message
    else:
        errorMessage = ex[0]
    return errorMessage

def publishDataToTopic(resp_data: dict, topic: str, vehicleClient: VehicleClient):
    vehicleClient.PublishEvent(
        'seatadjuster/setPosition/response/' + topic,
        json.dumps(resp_data)
    )

def getVehicleMovingSpeed():
    return int(0)

if __name__ == '__main__':
    logging.basicConfig()
    app.run(50008)
