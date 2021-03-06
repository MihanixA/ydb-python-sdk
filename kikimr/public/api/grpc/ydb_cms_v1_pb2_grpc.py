# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kikimr.public.api.protos import ydb_cms_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2


class CmsServiceStub(object):
  """CMS stands for Cluster Management System. CmsService provides some
  functionality for managing cluster, i.e. managing YDB Database
  instances for example.

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateDatabase = channel.unary_unary(
        '/Ydb.Cms.V1.CmsService/CreateDatabase',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.CreateDatabaseRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.CreateDatabaseResponse.FromString,
        )
    self.GetDatabaseStatus = channel.unary_unary(
        '/Ydb.Cms.V1.CmsService/GetDatabaseStatus',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.GetDatabaseStatusRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.GetDatabaseStatusResponse.FromString,
        )
    self.AlterDatabase = channel.unary_unary(
        '/Ydb.Cms.V1.CmsService/AlterDatabase',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.AlterDatabaseRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.AlterDatabaseResponse.FromString,
        )
    self.ListDatabases = channel.unary_unary(
        '/Ydb.Cms.V1.CmsService/ListDatabases',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.ListDatabasesRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.ListDatabasesResponse.FromString,
        )
    self.RemoveDatabase = channel.unary_unary(
        '/Ydb.Cms.V1.CmsService/RemoveDatabase',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.RemoveDatabaseRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.RemoveDatabaseResponse.FromString,
        )
    self.DescribeDatabaseOptions = channel.unary_unary(
        '/Ydb.Cms.V1.CmsService/DescribeDatabaseOptions',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.DescribeDatabaseOptionsRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.DescribeDatabaseOptionsResponse.FromString,
        )


class CmsServiceServicer(object):
  """CMS stands for Cluster Management System. CmsService provides some
  functionality for managing cluster, i.e. managing YDB Database
  instances for example.

  """

  def CreateDatabase(self, request, context):
    """Create a new database.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDatabaseStatus(self, request, context):
    """Get current database's status.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AlterDatabase(self, request, context):
    """Alter database resources.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListDatabases(self, request, context):
    """List all databases.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveDatabase(self, request, context):
    """Remove database.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DescribeDatabaseOptions(self, request, context):
    """Describe supported database options.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CmsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateDatabase': grpc.unary_unary_rpc_method_handler(
          servicer.CreateDatabase,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.CreateDatabaseRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.CreateDatabaseResponse.SerializeToString,
      ),
      'GetDatabaseStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetDatabaseStatus,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.GetDatabaseStatusRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.GetDatabaseStatusResponse.SerializeToString,
      ),
      'AlterDatabase': grpc.unary_unary_rpc_method_handler(
          servicer.AlterDatabase,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.AlterDatabaseRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.AlterDatabaseResponse.SerializeToString,
      ),
      'ListDatabases': grpc.unary_unary_rpc_method_handler(
          servicer.ListDatabases,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.ListDatabasesRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.ListDatabasesResponse.SerializeToString,
      ),
      'RemoveDatabase': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveDatabase,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.RemoveDatabaseRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.RemoveDatabaseResponse.SerializeToString,
      ),
      'DescribeDatabaseOptions': grpc.unary_unary_rpc_method_handler(
          servicer.DescribeDatabaseOptions,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.DescribeDatabaseOptionsRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.DescribeDatabaseOptionsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Ydb.Cms.V1.CmsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
