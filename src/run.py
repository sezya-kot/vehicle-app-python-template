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
from typing import Any
from set_position_request_processor import SetPositionRequestProcessor
from bfb_adapter import BfbAdapter
from vehicle_sdk.talent import Talent, subscribeDataPoints, subscribeTopic
from vehicle_sdk.client import VehicleClient
from vehicle_sdk.databroker_pb2 import Notification

class SeatAdjusterTalent(Talent):
    def __init__(self):
        super().__init__()

    @subscribeTopic("seatadjuster/setPosition/request/gui-app")
    def onSetPositionRequestGuiAppReceived(self, data: any) -> None:
        data = json.loads(data)
        print(f'Set Position Request received: data={data}', flush=True)  # noqa: E501
        self.onSetPositionRequestReceived(data, "seatadjuster/setPosition/response/gui-app")

    @subscribeTopic("seatadjuster/setSeatPosition")
    def onSetPositionRequestBfbAppReceived(self, data: any) -> None:
        bfb_data = json.loads(data)
        print(f'Set Position Request received: data={bfb_data}', flush=True)  # noqa: E501
        bfbAdapter = BfbAdapter()
        data = bfbAdapter.process(bfb_data)
        self.onSetPositionRequestReceived(data, "seatadjuster/setPosition/response")

    def onSetPositionRequestReceived(self, data: any, resp_topic: str) -> None:
        vehicleClient = VehicleClient()
        vehicleSpeed = vehicleClient.get_vehicle_speed()
        if vehicleSpeed == 0: 
            setPositionRequestProcessor = SetPositionRequestProcessor()
            setPositionRequestProcessor.process(data, resp_topic, vehicleClient, self)
        else:
            print('Not allowed to move seat because vehicle speed is {vehicleSpeed} and not 0')
    
    @subscribeDataPoints(["Vehicle.Speed"])
    def onDataPointUpdates(self, notification: Notification):
        self.vehicle_speed = notification.datapoints[0].int32_value
        print(notification, flush=True)

if __name__ == '__main__':
    logging.basicConfig()
    print(f'Starting seat adjuster app...', flush=True)
    seatAdjusterTalent = SeatAdjusterTalent()
    seatAdjusterTalent.run()
