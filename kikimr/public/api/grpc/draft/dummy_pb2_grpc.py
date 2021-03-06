# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kikimr.public.api.grpc.draft import dummy_pb2 as kikimr_dot_public_dot_api_dot_grpc_dot_draft_dot_dummy__pb2


class DummyServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Ping = channel.unary_unary(
        '/Draft.Dummy.DummyService/Ping',
        request_serializer=kikimr_dot_public_dot_api_dot_grpc_dot_draft_dot_dummy__pb2.PingRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_grpc_dot_draft_dot_dummy__pb2.PingResponse.FromString,
        )
    self.Infinite = channel.unary_unary(
        '/Draft.Dummy.DummyService/Infinite',
        request_serializer=kikimr_dot_public_dot_api_dot_grpc_dot_draft_dot_dummy__pb2.InfiniteRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_grpc_dot_draft_dot_dummy__pb2.InfiniteResponse.FromString,
        )
    self.BiStreamPing = channel.stream_stream(
        '/Draft.Dummy.DummyService/BiStreamPing',
        request_serializer=kikimr_dot_public_dot_api_dot_grpc_dot_draft_dot_dummy__pb2.PingRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_grpc_dot_draft_dot_dummy__pb2.PingResponse.FromString,
        )


class DummyServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Ping(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Infinite(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BiStreamPing(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DummyServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=kikimr_dot_public_dot_api_dot_grpc_dot_draft_dot_dummy__pb2.PingRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_grpc_dot_draft_dot_dummy__pb2.PingResponse.SerializeToString,
      ),
      'Infinite': grpc.unary_unary_rpc_method_handler(
          servicer.Infinite,
          request_deserializer=kikimr_dot_public_dot_api_dot_grpc_dot_draft_dot_dummy__pb2.InfiniteRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_grpc_dot_draft_dot_dummy__pb2.InfiniteResponse.SerializeToString,
      ),
      'BiStreamPing': grpc.stream_stream_rpc_method_handler(
          servicer.BiStreamPing,
          request_deserializer=kikimr_dot_public_dot_api_dot_grpc_dot_draft_dot_dummy__pb2.PingRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_grpc_dot_draft_dot_dummy__pb2.PingResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Draft.Dummy.DummyService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
