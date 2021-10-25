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
            print("Request setting seat position to ", pos, flush=True)
            response = self.Sdk.SetPosition(pos, port)
            print(f'New seat position returned from vehicle api is "{pos}"', flush=True)
            return response
        except (Exception) as e:
            template = "Failed to connect to vehicleapi. An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            print (message)

    def processing_loop(self):
        self.is_running = True
        pos = 0

        # Wait a second for the the dapr sidecar to start
        sleep(1)
        while self.is_running:
            pos = pos + 1
            response = self.setSeatPosition(pos)
            sleep(5)
