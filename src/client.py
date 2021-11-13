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
from set_position_request_processor import SetPositionRequestProcessor
from vehicle_movement_detail import VehicleMovementDetail
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
    vehicleMovingSpeed = VehicleMovementDetail().getMovingSpeed()
    setPositionRequestProcessor = SetPositionRequestProcessor()
    setPositionRequestProcessor.process(data, topic, vehicleClient, vehicleMovingSpeed)

if __name__ == '__main__':
    logging.basicConfig()
    app.run(50008)
