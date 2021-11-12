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
from seat_adjuster import SeatAdjuster
import json
from VehicleSdk import VehicleSdk
import swdc_comfort_seats_pb2

from dapr.clients import DaprClient

app = App()


@app.subscribe(pubsub_name='mqtt-pubsub', topic='SEATPOSITION')
def onSeatPositionUpdate(event: v1.Event) -> None:
    data = json.loads(event.Data())
    print(f'Subscriber received: id={data["id"]}, SeatPosition="{data["SeatPosition"]}", content_type="{event.content_type}"', flush=True)  # noqa: E501


@app.subscribe(pubsub_name='mqtt-pubsub-raw', topic='seatadjuster/setPosition/request/gui-app', metadata={'rawPayload': 'true'}, )
def onSetPositionRequestGuiAppReceived(event: v1.Event) -> None:
    data = json.loads(event.Data())
    onSetPositionRequestReceived(data, "gui-app")


@app.subscribe(pubsub_name='mqtt-pubsub-raw', topic='seatadjuster/setPosition/request/bfb-app', metadata={'rawPayload': 'true'}, )
def onSetPositionRequestBfbAppReceived(event: v1.Event) -> None:
    data = json.loads(event.Data())
    onSetPositionRequestReceived(data, "bfb-app")


def onSetPositionRequestReceived(data: any, topic: str) -> None:

    print(f'Set Position Request received: Position={data["position"]}, RequestId="{data["requestId"]} Topic={topic}', flush=True)  # noqa: E501
    port = os.getenv('DAPR_GRPC_PORT')
    sdk = VehicleSdk()

    location = swdc_comfort_seats_pb2.SeatLocation(row=1, index=1)
    component = swdc_comfort_seats_pb2.BASE

    # try catch
    sdk.MoveComponent(location, component, data["position"], port)

    resp_data = {
        'requestId': data["requestId"],
        'result': {
            'status': 0
        }
    }
# catch
##

    # Publish event to MQTT Response
    with DaprClient() as d:
        # Create a typed message with content type and body
        d.publish_event(
            pubsub_name='mqtt-pubsub-raw',
            topic_name='seatadjuster/setPosition/response/' + topic,
            data=json.dumps(resp_data),
            data_content_type='application/json'
            # metadata= ( "rawPayload",  "true" ) TODO: send metadata
        )


if __name__ == '__main__':
    logging.basicConfig()
    seatAdjuster = SeatAdjuster(VehicleSdk)
    seatAdjuster.start()
    app.run(50008)
