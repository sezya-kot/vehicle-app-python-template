from vehicleapi.vehicleapi_pb2 import SetPositionRequest, SetPositionResponse
from vehicleapi.vehicleapi_pb2_grpc import SeatControllerServicer

class Servicer(SeatControllerServicer):
    def handler(self, request: SetPositionRequest, context) -> SetPositionResponse:
        return SetPositionResponse(name=f'test-{request.name}')

    def error_handler(self, request:SetPositionRequest, context) -> SetPositionResponse:
        raise RuntimeError('some error')