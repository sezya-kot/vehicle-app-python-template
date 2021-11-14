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

import os
import flask
from flask import request, jsonify
# from __future__ import print_function

from cloudevents.sdk.event import v1
from dapr.ext.grpc import App
import logging
import json
from VehicleSdk import VehicleClient
import swdc_comfort_seats_pb2


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
    location = swdc_comfort_seats_pb2.SeatLocation(row=1, index=1)
    component = swdc_comfort_seats_pb2.BASE

    # Check if speed = 0, if yes, call MoveComponent, otherwise return MQTT Response Error

    # try catch
    vehicleClient.MoveComponent(location, component, data["position"])

    resp_data = {
        'requestId': data["requestId"],
        'result': {
            'status': 0
        }
    }
# catch
##
    vehicleClient.PublishEvent(
        'seatadjuster/setPosition/response/' + topic,
        json.dumps(resp_data)
    )


if __name__ == '__main__':
    logging.basicConfig()
    app.run(50008)
