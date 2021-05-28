# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ..registry import StageService_pb2 as registry_dot_StageService__pb2


class StageServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateTransition = channel.unary_unary(
        '/ai.verta.registry.StageService/CreateTransition',
        request_serializer=registry_dot_StageService__pb2.CreateTransitionRequest.SerializeToString,
        response_deserializer=registry_dot_StageService__pb2.Activity.FromString,
        )
    self.ApproveTransition = channel.unary_unary(
        '/ai.verta.registry.StageService/ApproveTransition',
        request_serializer=registry_dot_StageService__pb2.ApproveTransitionRequest.SerializeToString,
        response_deserializer=registry_dot_StageService__pb2.Activity.FromString,
        )
    self.RejectTransition = channel.unary_unary(
        '/ai.verta.registry.StageService/RejectTransition',
        request_serializer=registry_dot_StageService__pb2.RejectTransitionRequest.SerializeToString,
        response_deserializer=registry_dot_StageService__pb2.Activity.FromString,
        )
    self.CloseTransition = channel.unary_unary(
        '/ai.verta.registry.StageService/CloseTransition',
        request_serializer=registry_dot_StageService__pb2.CloseTransitionRequest.SerializeToString,
        response_deserializer=registry_dot_StageService__pb2.Activity.FromString,
        )
    self.CreateComment = channel.unary_unary(
        '/ai.verta.registry.StageService/CreateComment',
        request_serializer=registry_dot_StageService__pb2.CreateCommentRequest.SerializeToString,
        response_deserializer=registry_dot_StageService__pb2.Activity.FromString,
        )
    self.CommitTransition = channel.unary_unary(
        '/ai.verta.registry.StageService/CommitTransition',
        request_serializer=registry_dot_StageService__pb2.CommitTransitionRequest.SerializeToString,
        response_deserializer=registry_dot_StageService__pb2.Activity.FromString,
        )
    self.UpdateStage = channel.unary_unary(
        '/ai.verta.registry.StageService/UpdateStage',
        request_serializer=registry_dot_StageService__pb2.UpdateStageRequest.SerializeToString,
        response_deserializer=registry_dot_StageService__pb2.Activity.FromString,
        )
    self.FindActivities = channel.unary_unary(
        '/ai.verta.registry.StageService/FindActivities',
        request_serializer=registry_dot_StageService__pb2.FindActivitiesRequest.SerializeToString,
        response_deserializer=registry_dot_StageService__pb2.FindActivitiesRequest.Response.FromString,
        )
    self.FindTransitions = channel.unary_unary(
        '/ai.verta.registry.StageService/FindTransitions',
        request_serializer=registry_dot_StageService__pb2.FindTransitionsRequest.SerializeToString,
        response_deserializer=registry_dot_StageService__pb2.FindTransitionsRequest.Response.FromString,
        )


class StageServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateTransition(self, request, context):
    """Anyone with RW permission on the model version can do any of these
    Note that the author of the transition cannot approve or reject it themselves (like in github)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ApproveTransition(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RejectTransition(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CloseTransition(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateComment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CommitTransition(self, request, context):
    """Only a transition that has been approved can be commited. The user must have RW permission
    Similar to merging a PR
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateStage(self, request, context):
    """Directly update the stage without going through approval. The user must have RW permission
    Similar to merging to master directly
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindActivities(self, request, context):
    """List objects from the db. Similar to the PR history
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindTransitions(self, request, context):
    """Similar to listing PRs by state
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StageServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateTransition': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTransition,
          request_deserializer=registry_dot_StageService__pb2.CreateTransitionRequest.FromString,
          response_serializer=registry_dot_StageService__pb2.Activity.SerializeToString,
      ),
      'ApproveTransition': grpc.unary_unary_rpc_method_handler(
          servicer.ApproveTransition,
          request_deserializer=registry_dot_StageService__pb2.ApproveTransitionRequest.FromString,
          response_serializer=registry_dot_StageService__pb2.Activity.SerializeToString,
      ),
      'RejectTransition': grpc.unary_unary_rpc_method_handler(
          servicer.RejectTransition,
          request_deserializer=registry_dot_StageService__pb2.RejectTransitionRequest.FromString,
          response_serializer=registry_dot_StageService__pb2.Activity.SerializeToString,
      ),
      'CloseTransition': grpc.unary_unary_rpc_method_handler(
          servicer.CloseTransition,
          request_deserializer=registry_dot_StageService__pb2.CloseTransitionRequest.FromString,
          response_serializer=registry_dot_StageService__pb2.Activity.SerializeToString,
      ),
      'CreateComment': grpc.unary_unary_rpc_method_handler(
          servicer.CreateComment,
          request_deserializer=registry_dot_StageService__pb2.CreateCommentRequest.FromString,
          response_serializer=registry_dot_StageService__pb2.Activity.SerializeToString,
      ),
      'CommitTransition': grpc.unary_unary_rpc_method_handler(
          servicer.CommitTransition,
          request_deserializer=registry_dot_StageService__pb2.CommitTransitionRequest.FromString,
          response_serializer=registry_dot_StageService__pb2.Activity.SerializeToString,
      ),
      'UpdateStage': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateStage,
          request_deserializer=registry_dot_StageService__pb2.UpdateStageRequest.FromString,
          response_serializer=registry_dot_StageService__pb2.Activity.SerializeToString,
      ),
      'FindActivities': grpc.unary_unary_rpc_method_handler(
          servicer.FindActivities,
          request_deserializer=registry_dot_StageService__pb2.FindActivitiesRequest.FromString,
          response_serializer=registry_dot_StageService__pb2.FindActivitiesRequest.Response.SerializeToString,
      ),
      'FindTransitions': grpc.unary_unary_rpc_method_handler(
          servicer.FindTransitions,
          request_deserializer=registry_dot_StageService__pb2.FindTransitionsRequest.FromString,
          response_serializer=registry_dot_StageService__pb2.FindTransitionsRequest.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.registry.StageService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
