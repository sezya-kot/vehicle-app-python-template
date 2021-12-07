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


from concurrent import futures
import logging

import json
import time
import grpc
import swdc_comfort_seats_pb2 as swdc_comfort_seats_pb2
import swdc_comfort_seats_pb2_grpc as swdc_comfort_seats_pb2_grpc
import databroker_pb2 as databroker_pb2
import databroker_pb2_grpc as databroker_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp

from typing import Iterable

from dapr.clients import DaprClient

DATA_STORE = {}
DATA_POINTS = {}
class VehicleApi(swdc_comfort_seats_pb2_grpc.SeatsServicer,databroker_pb2_grpc.VehicleDataServicer):

    def Move(self, request, context):
        print("New position is ", request.seat.position, flush=True)

        req_data = {
            'id': request.seat.position.base,
            'SeatPosition': request.seat.position.base
        }

        with DaprClient() as d:
            # Create a typed message with content type and body
            resp = d.publish_event(
                pubsub_name='mqtt-pubsub',
                topic_name='SEATPOSITION',
                data=json.dumps(req_data),
                data_content_type='application/json',
            )

        return swdc_comfort_seats_pb2.MoveReply()

    def MoveComponent(self, request, context):
        print("New component position is ", request.position, flush=True)

        req_data = {
            'location-index': request.seat.index,
            'location-row': request.seat.row,
            'component': request.component,
            'position': request.position
        }

        with DaprClient() as d:
            # Create a typed message with content type and body
            resp = d.publish_event(
                pubsub_name='mqtt-pubsub',
                topic_name='SEATCOMPONENTPOSITION',
                data=json.dumps(req_data),
                data_content_type='application/json',
            )

        return swdc_comfort_seats_pb2.MoveComponentReply()

    def CurrentPosition(self, request, context):
        print("Received CurrentPosition request for seat in row ", request.row, ", index ", request.index, flush=True)

        return swdc_comfort_seats_pb2.CurrentPositionReply()

    def GetDatapoints(self, request, context):
        datapoints = []
        print("Id request received are ", request.ids , flush=True)

        for id in request.ids:
            if not DATA_POINTS.get(id):
                datapoint = databroker_pb2.Datapoint()
                datapoint.id = id
                datapoint.failure_value = databroker_pb2.Datapoint.NOT_AVAILABLE
                DATA_POINTS[datapoint.id] = datapoint

            datapoints.append(DATA_POINTS.get(id))

        response = databroker_pb2.GetDatapointsReply(datapoints=datapoints)

        return response
    
    def Subscribe(self, request, context) -> Iterable[databroker_pb2.Notification]:
        while True:
            time.sleep(5)
            datapoints = []
            for id in request.ids:
                datapoints.append(DATA_POINTS.get(id))
            if datapoints == []:
                response = databroker_pb2.Notification(datapoints=DATA_POINTS.values())
            else:
                response = databroker_pb2.Notification(datapoints=datapoints)
            print("Response from server: ", response)
            yield response

            print("Received a request for ", request.ids)

    def GetMetadata(self, request, context):
        metadatas = []
        print("Name request received are ", request.names , flush=True)
        for name in request.names:
            metadatas.append(DATA_STORE.get(name))

        print("Listing all metadata")
        if metadatas == []:
            response = databroker_pb2.GetMetadataReply(list=DATA_STORE.values())
        else:
            response = databroker_pb2.GetMetadataReply(list=metadatas)
        print("Response from server: ", response)
        return response

def createMetadata():
    print("createMetadata method started")

    metadata = databroker_pb2.Metadata()
    metadata.id = 1
    metadata.value_type = databroker_pb2.ValueType.UNKNOWN
    metadata.name = "Vehicle.Speed"

    DATA_STORE[metadata.name] = metadata

    metadata = databroker_pb2.Metadata()
    metadata.id = 2
    metadata.value_type = databroker_pb2.ValueType.UNKNOWN
    metadata.name = "Vehicle.Position"

    DATA_STORE[metadata.name] = metadata

    datapoint = databroker_pb2.Datapoint()
    datapoint.id = 1
    datapoint.int32_value = 0
    timestamp = Timestamp()
    timestamp.GetCurrentTime()

    datapoint.timestamp.seconds = timestamp.seconds
    datapoint.timestamp.nanos = timestamp.nanos

    DATA_POINTS[datapoint.id] = datapoint

    # datapoint = databroker_pb2.Datapoint()
    # datapoint.id = 2
    # timestamp = Timestamp()
    # timestamp.GetCurrentTime()
    # datapoint.timestamp.seconds = timestamp.seconds
    # datapoint.timestamp.nanos = timestamp.nanos

    # DATA_POINTS[datapoint.id] = datapoint
    print("createMetadata method completed")

def serve():
    createMetadata()
    port = '127.0.0.1:50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    swdc_comfort_seats_pb2_grpc.add_SeatsServicer_to_server(VehicleApi(), server)
    databroker_pb2_grpc.add_VehicleDataServicer_to_server(VehicleApi(), server)
    server.add_insecure_port(port)
    server.start()
    print("Listening on port ", port, flush=True)
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
