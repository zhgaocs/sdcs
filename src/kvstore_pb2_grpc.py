# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import kvstore_pb2 as kvstore__pb2


class KVStoreStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Set = channel.unary_unary(
                '/KVStore/Set',
                request_serializer=kvstore__pb2.SetRequest.SerializeToString,
                response_deserializer=kvstore__pb2.SetResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/KVStore/Get',
                request_serializer=kvstore__pb2.GetRequest.SerializeToString,
                response_deserializer=kvstore__pb2.GetResponse.FromString,
                )
        self.Remove = channel.unary_unary(
                '/KVStore/Remove',
                request_serializer=kvstore__pb2.RemoveRequest.SerializeToString,
                response_deserializer=kvstore__pb2.RemoveResponse.FromString,
                )


class KVStoreServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Set(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KVStoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Set': grpc.unary_unary_rpc_method_handler(
                    servicer.Set,
                    request_deserializer=kvstore__pb2.SetRequest.FromString,
                    response_serializer=kvstore__pb2.SetResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=kvstore__pb2.GetRequest.FromString,
                    response_serializer=kvstore__pb2.GetResponse.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=kvstore__pb2.RemoveRequest.FromString,
                    response_serializer=kvstore__pb2.RemoveResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'KVStore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KVStore(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Set(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/KVStore/Set',
            kvstore__pb2.SetRequest.SerializeToString,
            kvstore__pb2.SetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/KVStore/Get',
            kvstore__pb2.GetRequest.SerializeToString,
            kvstore__pb2.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/KVStore/Remove',
            kvstore__pb2.RemoveRequest.SerializeToString,
            kvstore__pb2.RemoveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)