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
"""A sample talent for adjusting seat positions."""

import json
import logging
from typing import Optional

from sdv.client import VehicleClient
from sdv.proto.databroker_pb2 import Notification
from sdv.talent import Talent, subscribeDataPoints, subscribeTopic

from set_position_request_processor import SetPositionRequestProcessor


class SeatAdjusterTalent(Talent):
    """
    A sample SeatAdjusterTalent.

    The SeatAdjusterTalent subcribes at the VehicleDataBroker for updates for the
    Vehicle.Speed signal.It also subscribes at a MQTT topic to listen for incoming
    requests to change the seat position and calls the SeatService to move the seat
    upon such a request, but only if Vehicle.Speed equals 0.
    """

    def __init__(self):
        """Always call the super class __init__."""
        self.current_vehicle_speed: Optional[int] = None
        super().__init__()

    @subscribeTopic("seatadjuster/setPosition/request/gui-app")
    def on_set_position_request_received(self, data: str) -> None:
        """Handle incoming MQTT seat change request event."""
        data = json.loads(data)
        print(f"Set Position Request received: data={data}", flush=True)
        self._on_set_position_request_received(
            data, "seatadjuster/setPosition/response/gui-app"
        )

    def _on_set_position_request_received(self, data: str, resp_topic: str) -> None:
        vehicle_client = VehicleClient()
        self.current_vehicle_speed = vehicle_client.get_vehicle_speed()
        if self.current_vehicle_speed == 0:
            request_processor = SetPositionRequestProcessor()
            request_processor.process(data, resp_topic, vehicle_client, self)
        else:
            print(
                "Not allowed to move seat because vehicle speed is {vehicleSpeed} and not 0"
            )

    @subscribeDataPoints(["Vehicle.Speed"])
    def on_data_point_updates(self, notification: Notification):  # type: ignore
        """Handle incoming updates of the Vehicle.Speed signal from the VehicleDataBroker."""
        self.current_vehicle_speed = notification.datapoints[0].int32_value  # type: ignore
        print(notification, flush=True)


if __name__ == "__main__":
    logging.basicConfig()
    print("Starting seat adjuster app...", flush=True)
    seatAdjusterTalent = SeatAdjusterTalent()
    seatAdjusterTalent.run()
