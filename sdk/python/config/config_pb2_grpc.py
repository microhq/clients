# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from config import config_pb2 as config_dot_config__pb2


class ConfigStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/config.Config/Create',
                request_serializer=config_dot_config__pb2.CreateRequest.SerializeToString,
                response_deserializer=config_dot_config__pb2.CreateResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/config.Config/Update',
                request_serializer=config_dot_config__pb2.UpdateRequest.SerializeToString,
                response_deserializer=config_dot_config__pb2.UpdateResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/config.Config/Delete',
                request_serializer=config_dot_config__pb2.DeleteRequest.SerializeToString,
                response_deserializer=config_dot_config__pb2.DeleteResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/config.Config/List',
                request_serializer=config_dot_config__pb2.ListRequest.SerializeToString,
                response_deserializer=config_dot_config__pb2.ListResponse.FromString,
                )
        self.Read = channel.unary_unary(
                '/config.Config/Read',
                request_serializer=config_dot_config__pb2.ReadRequest.SerializeToString,
                response_deserializer=config_dot_config__pb2.ReadResponse.FromString,
                )
        self.Watch = channel.unary_stream(
                '/config.Config/Watch',
                request_serializer=config_dot_config__pb2.WatchRequest.SerializeToString,
                response_deserializer=config_dot_config__pb2.WatchResponse.FromString,
                )


class ConfigServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Watch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConfigServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=config_dot_config__pb2.CreateRequest.FromString,
                    response_serializer=config_dot_config__pb2.CreateResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=config_dot_config__pb2.UpdateRequest.FromString,
                    response_serializer=config_dot_config__pb2.UpdateResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=config_dot_config__pb2.DeleteRequest.FromString,
                    response_serializer=config_dot_config__pb2.DeleteResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=config_dot_config__pb2.ListRequest.FromString,
                    response_serializer=config_dot_config__pb2.ListResponse.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=config_dot_config__pb2.ReadRequest.FromString,
                    response_serializer=config_dot_config__pb2.ReadResponse.SerializeToString,
            ),
            'Watch': grpc.unary_stream_rpc_method_handler(
                    servicer.Watch,
                    request_deserializer=config_dot_config__pb2.WatchRequest.FromString,
                    response_serializer=config_dot_config__pb2.WatchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'config.Config', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Config(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Config/Create',
            config_dot_config__pb2.CreateRequest.SerializeToString,
            config_dot_config__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Config/Update',
            config_dot_config__pb2.UpdateRequest.SerializeToString,
            config_dot_config__pb2.UpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Config/Delete',
            config_dot_config__pb2.DeleteRequest.SerializeToString,
            config_dot_config__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Config/List',
            config_dot_config__pb2.ListRequest.SerializeToString,
            config_dot_config__pb2.ListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Config/Read',
            config_dot_config__pb2.ReadRequest.SerializeToString,
            config_dot_config__pb2.ReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Watch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/config.Config/Watch',
            config_dot_config__pb2.WatchRequest.SerializeToString,
            config_dot_config__pb2.WatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
