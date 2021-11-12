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

import swdc_comfort_seats_pb2
import swdc_comfort_seats_pb2_grpc

class VehicleSdk:
    def Move(seat: swdc_comfort_seats_pb2.Seat, port: int):
        with grpc.insecure_channel(f'localhost:{port}') as channel:
            stub = swdc_comfort_seats_pb2_grpc.SeatsStub(channel)
            response = stub.Move.with_call(swdc_comfort_seats_pb2.MoveRequest(seat = seat), 
            metadata=(('dapr-app-id', 'vehicleapi'),))

        channel.close()
        return response

    def MoveComponent(self, seatLocation: swdc_comfort_seats_pb2.SeatLocation, component: swdc_comfort_seats_pb2.SeatComponent, position: int, port: int):
        with grpc.insecure_channel(f'localhost:{port}') as channel:
            stub = swdc_comfort_seats_pb2_grpc.SeatsStub(channel)
            response = stub.MoveComponent.with_call(swdc_comfort_seats_pb2.MoveComponentRequest(seat = seatLocation, component = component, position = position), 
            metadata=(('dapr-app-id', 'vehicleapi'),))

        channel.close()
        return response

    def CurrentPosition(row: int, index: int, port: int):
        with grpc.insecure_channel(f'localhost:{port}') as channel:
            stub = swdc_comfort_seats_pb2_grpc.SeatsStub(channel)
            response = stub.CurrentPosition.with_call(swdc_comfort_seats_pb2.CurrentPositionRequest(row = row, index = index), 
            metadata=(('dapr-app-id', 'vehicleapi'),))

        channel.close()
        return response