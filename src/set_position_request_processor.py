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

"""This module contains the SetPositionRequestProcessor class."""

import json

from sdv.client import VehicleClient
from sdv.proto.swdc_comfort_seats_pb2 import BASE, SeatLocation
from sdv.talent import Talent


class SetPositionRequestProcessor:
    """A class to process position requests."""

    def process(
        self, data: str, resp_topic: str, vehicleClient: VehicleClient, talent: Talent
    ):
        """Process the position request."""
        resp_data = self.__getProcessedResponse(data, vehicleClient)
        self.__publishDataToTopic(resp_data, resp_topic, talent)

    def __getProcessedResponse(self, data, vehicleClient):
        try:
            location = SeatLocation(row=1, index=1)
            vehicleClient.Seats.MoveComponent(location, BASE, data["position"])
            resp_data = {"requestId": data["requestId"], "result": {"status": 0}}
        except Exception as ex:
            resp_data = {
                "requestId": data["requestId"],
                "result": {"status": 1, "message": self.__getErrorMessageFrom(ex)},
            }
        return resp_data

    def __publishDataToTopic(self, resp_data: dict, resp_topic: str, talent: Talent):
        status = 0
        try:
            talent.publish_event(resp_topic, json.dumps(resp_data))
        except Exception:
            status = -1
        return status

    def __getErrorMessageFrom(self, ex: Exception):
        return "Exception details: " + ex.args[0].debug_error_string
