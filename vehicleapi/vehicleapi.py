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


import grpc
import vehicleapi_pb2
import vehicleapi_pb2_grpc

from dapr.clients import DaprClient


class VehicleApi(vehicleapi_pb2_grpc.SeatControllerServicer):

    def SetPosition(self, request, context):
        print("New position is ", request.position, flush=True)

        req_data = {
            'id': request.position,
            'SeatPosition': request.position
        }

        with DaprClient() as d:
            # Create a typed message with content type and body
            resp = d.publish_event(
                pubsub_name='mqtt-pubsub',
                topic_name='SEATPOSITION',
                data=json.dumps(req_data),
                data_content_type='application/json',
            )

        return vehicleapi_pb2.SetPositionResponse()


def serve():
    port = '127.0.0.1:50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vehicleapi_pb2_grpc.add_SeatControllerServicer_to_server(VehicleApi(), server)
    server.add_insecure_port(port)
    server.start()
    print("Listening on port ", port, flush=True)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
