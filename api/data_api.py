from concurrent import futures
import logging

import grpc
import loctaion_pb2 as loctaion_pb2
import loctaion_pb2_grpc as loctaion_pb2_grpc

class Locataion(loctaion_pb2_grpc.LocationServicer):

    def GetLocationByTimestamp(self, request, context):
        return loctaion_pb2.LocationReply(lat=524890500, long=133699979)
    
    def GetLocationsByTimeRange(self, request, context):
        return super().GetLocationByTimestamp(request, content) 


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    loctaion_pb2_grpc.add_LocationServicer_to_server(Locataion(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()