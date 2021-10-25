from vehicleapi.vehicleapi_pb2 import SetPositionRequest


def test_some(grpc_stub):
    request = SetPositionRequest()
    response = grpc_stub.handler(request)

    # assert response.name == f'test-{request.name}'
    pass

def test_example(grpc_stub):
    request = SetPositionRequest()
    response = grpc_stub.error_handler(request)

    # assert response.name == f'test-{request.name}'
    pass