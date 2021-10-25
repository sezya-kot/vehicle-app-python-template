import pytest

from vehicleapi import vehicleapi_pb2

@pytest.fixture(scope='module')
def grpc_add_to_server():
    from vehicleapi.vehicleapi_pb2_grpc import add_SeatControllerServicer_to_server

    return add_SeatControllerServicer_to_server

@pytest.fixture(scope='module')
def grpc_servicer():
    from seat_controler_servicer import Servicer

    return Servicer()

@pytest.fixture(scope='module')
def grpc_stub_cls(grpc_channel):
    from vehicleapi.vehicleapi_pb2_grpc import SeatControllerStub

    return SeatControllerStub