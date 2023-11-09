import os
import hashlib

import grpc
import kvstore_pb2, kvstore_pb2_grpc

from concurrent import futures

class MyKVStoreServicer(kvstore_pb2_grpc.KVStoreServicer):
    def __init__(self):
        self.__current_id = int(os.environ['CURRENT_ID'])
        self.__kv_data = {}

    def __get_target_id(self, key):
        md5_hash = hashlib.md5(key.encode())
        hex_hash = md5_hash.hexdigest()
        int_hash = int(hex_hash, 16)
        total_servers = int(os.environ['TOTAL_SERVERS'])
        target_id = int_hash % total_servers + 1
        return target_id

    def __create_stub(self, target_id):
        channel = grpc.insecure_channel('server' + str(target_id) + ':50051')
        stub = kvstore_pb2_grpc.KVStoreStub(channel)
        return stub

    def Set(self, request, context):
        target_id = self.__get_target_id(request.key)
        if self.__current_id == target_id:
            self.__kv_data[request.key] = request.value
        else:
            stub = self.__create_stub(target_id)
            stub.Set(kvstore_pb2.SetRequest(key=request.key, value=request.value))

        return kvstore_pb2.SetResponse()

    def Get(self, request, context):
        target_id = self.__get_target_id(request.key)
        if self.__current_id == target_id:
            if request.key in self.__kv_data:
                return kvstore_pb2.GetResponse(value=self.__kv_data[request.key])
            else:
                return kvstore_pb2.GetResponse(value = None)
        else:
            stub = self.__create_stub(target_id)
            response = stub.Get(kvstore_pb2.GetRequest(key=request.key))
            return response

    def Remove(self, request, context):
        target_id = self.__get_target_id(request.key)
        if self.__current_id == target_id:
            if request.key in self.__kv_data:
                self.__kv_data.pop(request.key)
                return kvstore_pb2.RemoveResponse(success=True)
            else:
                return kvstore_pb2.RemoveResponse(success=False)
        else:
            stub = self.__create_stub(target_id)
            response = stub.Remove(kvstore_pb2.RemoveRequest(key=request.key))
            return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    kvstore_pb2_grpc.add_KVStoreServicer_to_server(MyKVStoreServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()