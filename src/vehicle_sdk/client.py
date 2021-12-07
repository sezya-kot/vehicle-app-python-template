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

import vehicle_sdk.swdc_comfort_seats_pb2 as swdc_comfort_seats_pb2
import vehicle_sdk.swdc_comfort_seats_pb2_grpc as swdc_comfort_seats_pb2_grpc
import vehicle_sdk.databroker_pb2 as databroker_pb2
import vehicle_sdk.databroker_pb2_grpc as databroker_pb2_grpc
from typing import Optional

class VehicleClient:
    def __init__(self, port: Optional[int] = None):
        if not port:
            port = int(os.getenv('DAPR_GRPC_PORT'))
        self._address = f'localhost:{port}'
        self._channel = grpc.insecure_channel(self._address)   # type: ignore
        self._metadata = (('dapr-app-id', 'vehicleapi'),)
        self.Seats = self._Seats(self._channel, self._metadata)
        self.vehicleDataBroker = self._vehicleDataBroker(self._channel, self._metadata)

    def close(self):
        """Closes runtime gRPC channel."""
        if self._channel:
            self._channel.close()

    def __del__(self):
        self.close()

    def __enter__(self) -> 'VehicleClient':
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()

    # Telemetry section
    def get_vehicle_speed(self) -> int:
        metadataReply: databroker_pb2.GetMetadataReply = self.vehicleDataBroker.GetMetadata(["Vehicle.Speed"])   
        getDatapointsReply: databroker_pb2.GetDatapointsReply = self.vehicleDataBroker.GetDatapoints([metadataReply.list[0].id])
        return getDatapointsReply[0].datapoints[0].int32_value
            
    class _Seats:
        def __init__(self, channel, metadata):
            self._stub = swdc_comfort_seats_pb2_grpc.SeatsStub(channel)   # type: ignore
            self._metadata = metadata

        def Move(self, seat: swdc_comfort_seats_pb2.Seat):
            response = self._stub.Move.with_call(swdc_comfort_seats_pb2.MoveRequest(seat = seat), 
                metadata=self._metadata)
            return response

        def MoveComponent(self, seatLocation: swdc_comfort_seats_pb2.SeatLocation, component: swdc_comfort_seats_pb2.SeatComponent, position: int):
            response = self._stub.MoveComponent.with_call(swdc_comfort_seats_pb2.MoveComponentRequest(seat = seatLocation, component = component, position = position), 
                metadata=self._metadata)
            return response

        def CurrentPosition(self, row: int, index: int):
            response = self._stub.CurrentPosition.with_call(swdc_comfort_seats_pb2.CurrentPositionRequest(row = row, index = index), 
                metadata=self._metadata)
            return response

    class _vehicleDataBroker:
        def __init__(self, channel, metadata):  
            self._stub = databroker_pb2_grpc.VehicleDataStub(channel) # type: ignore
            self._metadata = metadata

        def GetDatapoints(self, ids: list):
            response = self._stub.GetDatapoints.with_call(databroker_pb2.GetDatapointsRequest(ids = ids),
                metadata=self._metadata)
            return response

        def Subscribe(self, ids: list, rule: str):
            response = self._stub.Subscribe(databroker_pb2.SubscribeRequest(ids = ids, rule = rule),
                metadata=self._metadata)
            return response
            
        def GetMetadata(self, names: list):
            response = self._stub.GetMetadata(databroker_pb2.GetMetadataRequest(names = names),
                metadata=self._metadata)
            return response