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

from sdv.client import VehicleClient
from sdv.proto.databroker_pb2 import Notification
from sdv.talent import Talent, subscribeDataPoints, subscribeTopic

from set_position_request_processor import SetPositionRequestProcessor


class SeatAdjusterTalent(Talent):
    def __init__(self):
        super().__init__()

    @subscribeTopic("seatadjuster/setPosition/request/gui-app")
    def onSetPositionRequestGuiAppReceived(self, data: str) -> None:
        data = json.loads(data)
        print(f"Set Position Request received: data={data}", flush=True)  # noqa: E501
        self.onSetPositionRequestReceived(
            data, "seatadjuster/setPosition/response/gui-app"
        )

    def onSetPositionRequestReceived(self, data: str, resp_topic: str) -> None:
        vehicleClient = VehicleClient()
        vehicleSpeed = vehicleClient.get_vehicle_speed()
        if vehicleSpeed == 0:
            setPositionRequestProcessor = SetPositionRequestProcessor()
            setPositionRequestProcessor.process(data, resp_topic, vehicleClient, self)
        else:
            print(
                "Not allowed to move seat because vehicle speed is {vehicleSpeed} and not 0"
            )

    @subscribeDataPoints(["Vehicle.Speed"])
    def onDataPointUpdates(self, notification: Notification):  # type: ignore
        self.vehicle_speed = notification.datapoints[0].int32_value  # type: ignore
        print(notification, flush=True)


if __name__ == "__main__":
    logging.basicConfig()
    print("Starting seat adjuster app...", flush=True)
    seatAdjusterTalent = SeatAdjusterTalent()
    seatAdjusterTalent.run()
