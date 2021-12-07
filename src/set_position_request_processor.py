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
from typing import Any

from flask import jsonify, request
from grpc import local_channel_credentials

import vehicle_sdk.swdc_comfort_seats_pb2 as swdc_comfort_seats_pb2
from vehicle_sdk.client import VehicleClient
from vehicle_sdk.talent import Talent

class SetPositionRequestProcessor:
    
    def process(self, data: any, resp_topic: str, vehicleClient: VehicleClient, talent: Talent):
        resp_data = self.getProcessedResponse(data, vehicleClient)
        self.publishDataToTopic(resp_data, resp_topic, talent)

    def getProcessedResponse(self, data, vehicleClient):
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
                'requestId': data["requestId"],
                'result': {
                    'status': 1,
                    'message': self.getErrorMessageFrom(ex)
                }
            }
        return resp_data

    
    def publishDataToTopic(self, resp_data: dict, resp_topic: str, talent: Talent):
        status = 0
        try:
            talent.publish_event(
                resp_topic,
                json.dumps(resp_data)
            )
        except Exception as ex:
            status = -1
        return status
    

    def getErrorMessageFrom(self, ex: Exception):
        return 'Exception details: ' + ex.args[0].debug_error_string