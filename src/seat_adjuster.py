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

import os
from threading import Thread
from time import sleep
from typing import NewType
from VehicleSdk import VehicleSdk


class SeatAdjuster:
    Sdk: VehicleSdk

    def __init__(self, vehicleSdk) -> None:
        self.Sdk  = vehicleSdk

    def start(self):
        self.is_running = False
        self.worker_thread = Thread(
            target=self.processing_loop
        )
        self.worker_thread.start()

    def stop(self):
        self.is_running = False
        self.worker_thread.join()

    def setSeatPosition(self, pos: int):
        port = os.getenv('DAPR_GRPC_PORT')
        try:
            self.Sdk.SetPosition(pos, port)
        except:
            print('Failed to connect to vehicleapi')  

    def processing_loop(self):
        self.is_running = True
        pos = 0

        # Wait a second for the the dapr sidecar to start
        sleep(1)
        while self.is_running:
            pos = pos + 1
            print("Request setting seat position to ", pos, flush=True)
            self.setSeatPosition(pos)
            # port = os.getenv('DAPR_GRPC_PORT')
            # try:
            #     with grpc.insecure_channel(f'localhost:{port}') as channel:
            #         stub = vehicleapi_pb2_grpc.SeatControllerStub(channel)
            #         response = stub.SetPosition.with_call(vehicleapi_pb2.SetPositionRequest(position=pos),
            #                                             metadata=(('dapr-app-id', 'vehicleapi'),))
            # except:
            #     print('Failed to connect to vehicleapi')  
            # channel.close()
            sleep(5)
