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
from typing import Optional

from cloudevents.sdk.event import v1
from dapr.ext.grpc import App
from flask import jsonify, request
from grpc import local_channel_credentials

import swdc_comfort_seats_pb2
from VehicleSdk import VehicleClient

class SetPositionRequestProcessor:
    def process(self, data: any, vehicleClient: VehicleClient,  resp_topic: Optional[str] = None):
        resp_data = self.getProcessedResponse(data, vehicleClient)
        self.publishDataToTopic(resp_data, vehicleClient, resp_topic)

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
            logging.error(self.getErrorMessageFrom(ex))
            resp_data = {
                'requestId': data["requestId"],
                'result': {
                    'status': 1,
                    'message': self.getErrorMessageFrom(ex)
                }
            }
        
        return resp_data

    
    def publishDataToTopic(self, resp_data: dict, vehicleClient: VehicleClient, resp_topic: Optional[str] = None):
        status = 0
        if resp_topic:
            try:
                vehicleClient.PublishEvent(
                    resp_topic,
                    json.dumps(resp_data)
                )
            except Exception as ex:
                status = -1
        
        return status
    
    def getErrorMessageFrom(self, ex: Exception):
        errorMessage = 'Exception details: '
        if hasattr(ex, 'message'):
            errorMessage = errorMessage + ex.message
        else:
            errorMessage = errorMessage + ex.args[0].debug_error_string
        return errorMessage
