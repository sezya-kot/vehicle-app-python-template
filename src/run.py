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

import asyncio
import json
import logging
import signal

from sdv.proto.databroker_pb2 import Notification
from sdv.util.log import get_default_date_format, get_default_log_format
from sdv.vehicle_app import VehicleApp, subscribe_data_points, subscribe_topic

from set_position_request_processor import SetPositionRequestProcessor
from vdm.Vehicle import Vehicle

logging.basicConfig(format=get_default_log_format(), datefmt=get_default_date_format())
logging.getLogger().setLevel("INFO")
logger = logging.getLogger(__name__)


class SeatAdjusterApp(VehicleApp):
    """
    A sample SeatAdjusterTalent.

    The SeatAdjusterTalent subcribes at the VehicleDataBroker for updates for the
    Vehicle.Speed signal.It also subscribes at a MQTT topic to listen for incoming
    requests to change the seat position and calls the SeatService to move the seat
    upon such a request, but only if Vehicle.Speed equals 0.
    """

    def __init__(self, vehicle_client: Vehicle):
        super().__init__()
        self.vehicle_client = vehicle_client

    @subscribe_topic("seatadjuster/setPosition/request/gui-app")
    async def on_set_position_request_received(self, data: str) -> None:
        """Handle set position request from GUI app from MQTT topic"""
        data = json.loads(data)
        logger.info("Set Position Request received: data=%s", data)  # noqa: E501
        await self._on_set_position_request_received(
            data, "seatadjuster/setPosition/response/gui-app"
        )

    async def _on_set_position_request_received(
        self, data: str, resp_topic: str
    ) -> None:
        vehicle_speed = await self.vehicle_client.Speed.get()

        if vehicle_speed == 0:
            processor = SetPositionRequestProcessor(self.vehicle_client)
            await processor.process(data, resp_topic, self)
        else:
            logger.warning(
                "Not allowed to move seat because vehicle speed is %s and not 0",
                vehicle_speed,
            )

    @subscribe_data_points(["Vehicle.Speed"])
    def on_vehicle_speed_change(self, notification: Notification):  # type: ignore
        """Handle vehicle speed change"""
        logger.info(notification)


async def main():
    """Main function"""
    logger.info("Starting seat adjuster app...")
    seat_adjuster_talent = SeatAdjusterApp(Vehicle())
    await seat_adjuster_talent.run()


LOOP = asyncio.get_event_loop()
LOOP.add_signal_handler(signal.SIGTERM, LOOP.stop)
LOOP.run_until_complete(main())
LOOP.close()
