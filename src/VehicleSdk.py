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

import sys
import os
import grpc

sys.path.insert(1, os.path.join(os.path.dirname(__file__), '..', 'vehicleapi'))
from vehicleapi import vehicleapi_pb2
from vehicleapi import vehicleapi_pb2_grpc

class VehicleSdk:
    def SetPosition(pos: int, port: int):
        with grpc.insecure_channel(f'localhost:{port}') as channel:
            stub = vehicleapi_pb2_grpc.SeatControllerStub(channel)
            response = stub.SetPosition.with_call(vehicleapi_pb2.SetPositionRequest(position=pos),
                                                    metadata=(('dapr-app-id', 'vehicleapi'),))
        channel.close()
        return response