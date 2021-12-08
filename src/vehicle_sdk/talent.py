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
import threading
import os
from typing import Optional
from vehicle_sdk._servicier import _CallbackServicer
from dapr.proto import appcallback_service_v1
import grpc
from concurrent import futures
import inspect
from vehicle_sdk import databroker_pb2
import time
from dapr.proto import api_service_v1, api_v1

from vehicle_sdk.client import VehicleClient

_DAPR_PUB_SUB_NAME = "mqtt-pubsub"
_TALENT_PORT = 50008

_servicer = _CallbackServicer()

def subscribeTopic(topic):
    def wrap(func):
        func.subscribeTopic = topic
        return func
    return wrap

def subscribeDataPoints(dataPointNames):
    def wrap(func):
        func.subscribeDataPoints = dataPointNames
        return func
    return wrap

class Talent:
    def __init__(self):
        self._port = _TALENT_PORT
        self.vehicleClient = VehicleClient()
        self._executor = futures.ThreadPoolExecutor(max_workers=100)
        self._server = grpc.server(self._executor)   # type: ignore
        appcallback_service_v1.add_AppCallbackServicer_to_server(_servicer, self._server)
        self._dataPointSubscriptionThreads = []
        methods = inspect.getmembers(self)
        for m in methods:
            if hasattr(m[1], 'subscribeTopic'):
                _servicer.register_topic(_DAPR_PUB_SUB_NAME, m[1].subscribeTopic, m[1], metadata={'rawPayload': 'true'})
            if hasattr(m[1], 'subscribeDataPoints'):
                # Temporary (highly inefficient) workaround since dapr is crashing if using asyncio 
                # https://github.com/dapr/dapr/issues/3982
                worker_thread = threading.Thread(target=self._subscribe_to_data_points, args=[m[1].subscribeDataPoints, m[1]])
                worker_thread.start()
                self._dataPointSubscriptionThreads.append(worker_thread)

    def __del__(self):
        self.stop()

    def stop(self) -> None:
        self._server.stop(0)
        for t in self._dataPointSubscriptionThreads:
            t.join()
    
    def run(self):
        self._server.add_insecure_port(f'[::]:{self._port}')
        self._server.start()
        self._server.wait_for_termination()

    def publish_event(self, topic: str, data: any):
        port = int(os.getenv('DAPR_GRPC_PORT'))
        address = f'localhost:{port}'
        channel = grpc.insecure_channel(address) 
        daprStub =  api_service_v1.DaprStub(channel)
        req = api_v1.PublishEventRequest(
            pubsub_name=_DAPR_PUB_SUB_NAME,
            topic=topic,
            data=bytes(data, 'utf-8'),
            metadata={'rawPayload': 'true'},)
        daprStub.PublishEvent(req)

    def _subscribe_to_data_points(self, dataPointNames, cb) -> None:
        try:
            # wait for dapr sidecar to start
            time.sleep(1)
            port = int(os.getenv('DAPR_GRPC_PORT'))
            client = VehicleClient(port)
            metadataReply: databroker_pb2.GetMetadataReply = client.vehicleDataBroker.GetMetadata(dataPointNames)   
            ids = []
            for metadata in metadataReply.list:
                ids.append(metadata.id) 
            
            notifications: databroker_pb2.Notification = client.vehicleDataBroker.Subscribe(ids, rule="")
            for notification in notifications:
                cb(notification)
        except Exception as e:
            # TODO: error handling
            raise
    
 