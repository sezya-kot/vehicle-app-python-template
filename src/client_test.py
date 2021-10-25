import json
import os
import sys
import unittest

from cloudevents.sdk.event import v1
from dapr.ext.grpc.app import App
from client import onSeatPositionUpdate, sayHello

# sys.path.insert(1, os.path.join(os.path.dirname(__file__), '../../','src'))


class ClientTest(unittest.TestCase):

    def test_client(self):
        # eventTopicData = {"type": "com.dapr.event.sent","id": "9740ae6d-4a4b-49a9-af0a-a3ae51fd65f8","specversion": "1.0","datacontenttype": "application/json","traceid": "00-6db85710be668d081cce97e0b8266938-bea4cd91de14e805-01","data": {"id": 556,"SeatPosition": 556},"source": "vehicleapi","topic": "SEATPOSITION","pubsubname": "mqtt-pubsub"}
        event = v1.Event()
        event.type = "com.dapr.event.sent"
        event.id = "9740ae6d-4a4b-49a9-af0a-a3ae51fd65f8"
        # event.specversion='1.0'
        event.datacontenttype = "application/json"
        event.traceid = "00-6db85710be668d081cce97e0b8266938-bea4cd91de14e805-01"
        event.data = '{"id": 1, "SeatPosition": 556}'
        event.source = "vehicleapi"
        event.topic = "SEATPOSITION"
        event.pubsubname = "mqtt-pubsub"
        # print(json.loads(eventTopicData.Data()))
        # data = json.loads(eventTopicData)
        # print(type(eventTopicData))
        print(type(event))
        
        # app = App()
        onSeatPositionUpdate(event)
        # sayHello()
        # self.assertEqual()