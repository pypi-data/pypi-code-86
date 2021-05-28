# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from admobilize.proto.common import job_pb2 as admobilize_dot_common_dot_job__pb2
from admobilize.proto.signagelive.v1alpha1 import resources_pb2 as admobilize_dot_signagelive_dot_v1alpha1_dot_resources__pb2
from admobilize.proto.signagelive.v1alpha1 import signagelive_service_pb2 as admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class SignageliveServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateReport = channel.unary_unary(
                '/admobilize.signagelive.v1alpha1.SignageliveService/CreateReport',
                request_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ReportRequest.SerializeToString,
                response_deserializer=admobilize_dot_common_dot_job__pb2.Job.FromString,
                )
        self.GetCredentials = channel.unary_unary(
                '/admobilize.signagelive.v1alpha1.SignageliveService/GetCredentials',
                request_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.GetCredentialsRequest.SerializeToString,
                response_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListCredentialsResponse.FromString,
                )
        self.ListCredentials = channel.unary_unary(
                '/admobilize.signagelive.v1alpha1.SignageliveService/ListCredentials',
                request_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListCredentialsRequest.SerializeToString,
                response_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListCredentialsResponse.FromString,
                )
        self.CreateCredential = channel.unary_unary(
                '/admobilize.signagelive.v1alpha1.SignageliveService/CreateCredential',
                request_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.CreateCredentialRequest.SerializeToString,
                response_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_resources__pb2.Credential.FromString,
                )
        self.DeleteCredential = channel.unary_unary(
                '/admobilize.signagelive.v1alpha1.SignageliveService/DeleteCredential',
                request_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.DeleteCredentialRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UpdateCredential = channel.unary_unary(
                '/admobilize.signagelive.v1alpha1.SignageliveService/UpdateCredential',
                request_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.UpdateCredentialRequest.SerializeToString,
                response_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_resources__pb2.Credential.FromString,
                )
        self.CheckCredential = channel.unary_unary(
                '/admobilize.signagelive.v1alpha1.SignageliveService/CheckCredential',
                request_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.CheckCredentialRequest.SerializeToString,
                response_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.CheckCredentialResponse.FromString,
                )
        self.GetMappings = channel.unary_unary(
                '/admobilize.signagelive.v1alpha1.SignageliveService/GetMappings',
                request_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.GetMappingRequest.SerializeToString,
                response_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListMappingsResponse.FromString,
                )
        self.ListMappings = channel.unary_unary(
                '/admobilize.signagelive.v1alpha1.SignageliveService/ListMappings',
                request_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListMappingsRequest.SerializeToString,
                response_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListMappingsResponse.FromString,
                )
        self.CreateMapping = channel.unary_unary(
                '/admobilize.signagelive.v1alpha1.SignageliveService/CreateMapping',
                request_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.CreateMappingRequest.SerializeToString,
                response_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_resources__pb2.Mapping.FromString,
                )
        self.DeleteMapping = channel.unary_unary(
                '/admobilize.signagelive.v1alpha1.SignageliveService/DeleteMapping',
                request_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.DeleteMappingRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UpdateMapping = channel.unary_unary(
                '/admobilize.signagelive.v1alpha1.SignageliveService/UpdateMapping',
                request_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.UpdateMappingRequest.SerializeToString,
                response_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_resources__pb2.Mapping.FromString,
                )


class SignageliveServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateReport(self, request, context):
        """Google Jobs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCredentials(self, request, context):
        """Integrations

        ---------- Define signagelive credential accounts methods ----------
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCredentials(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCredential(self, request, context):
        """Creates a new credential
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCredential(self, request, context):
        """Deletes a credential
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCredential(self, request, context):
        """Updates a credential
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckCredential(self, request, context):
        """Check a credential auth
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMappings(self, request, context):
        """---------- Define signagelive mappings methods ----------
        Get mappings request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMappings(self, request, context):
        """List all mappings stored
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateMapping(self, request, context):
        """Creates a new mapping
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMapping(self, request, context):
        """Deletes a mapping
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateMapping(self, request, context):
        """Updates a mapping
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SignageliveServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateReport': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateReport,
                    request_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ReportRequest.FromString,
                    response_serializer=admobilize_dot_common_dot_job__pb2.Job.SerializeToString,
            ),
            'GetCredentials': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCredentials,
                    request_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.GetCredentialsRequest.FromString,
                    response_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListCredentialsResponse.SerializeToString,
            ),
            'ListCredentials': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCredentials,
                    request_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListCredentialsRequest.FromString,
                    response_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListCredentialsResponse.SerializeToString,
            ),
            'CreateCredential': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCredential,
                    request_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.CreateCredentialRequest.FromString,
                    response_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_resources__pb2.Credential.SerializeToString,
            ),
            'DeleteCredential': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCredential,
                    request_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.DeleteCredentialRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdateCredential': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCredential,
                    request_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.UpdateCredentialRequest.FromString,
                    response_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_resources__pb2.Credential.SerializeToString,
            ),
            'CheckCredential': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckCredential,
                    request_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.CheckCredentialRequest.FromString,
                    response_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.CheckCredentialResponse.SerializeToString,
            ),
            'GetMappings': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMappings,
                    request_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.GetMappingRequest.FromString,
                    response_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListMappingsResponse.SerializeToString,
            ),
            'ListMappings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListMappings,
                    request_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListMappingsRequest.FromString,
                    response_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListMappingsResponse.SerializeToString,
            ),
            'CreateMapping': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateMapping,
                    request_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.CreateMappingRequest.FromString,
                    response_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_resources__pb2.Mapping.SerializeToString,
            ),
            'DeleteMapping': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteMapping,
                    request_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.DeleteMappingRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdateMapping': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateMapping,
                    request_deserializer=admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.UpdateMappingRequest.FromString,
                    response_serializer=admobilize_dot_signagelive_dot_v1alpha1_dot_resources__pb2.Mapping.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'admobilize.signagelive.v1alpha1.SignageliveService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SignageliveService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.signagelive.v1alpha1.SignageliveService/CreateReport',
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ReportRequest.SerializeToString,
            admobilize_dot_common_dot_job__pb2.Job.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCredentials(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.signagelive.v1alpha1.SignageliveService/GetCredentials',
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.GetCredentialsRequest.SerializeToString,
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListCredentialsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCredentials(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.signagelive.v1alpha1.SignageliveService/ListCredentials',
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListCredentialsRequest.SerializeToString,
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListCredentialsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCredential(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.signagelive.v1alpha1.SignageliveService/CreateCredential',
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.CreateCredentialRequest.SerializeToString,
            admobilize_dot_signagelive_dot_v1alpha1_dot_resources__pb2.Credential.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCredential(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.signagelive.v1alpha1.SignageliveService/DeleteCredential',
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.DeleteCredentialRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCredential(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.signagelive.v1alpha1.SignageliveService/UpdateCredential',
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.UpdateCredentialRequest.SerializeToString,
            admobilize_dot_signagelive_dot_v1alpha1_dot_resources__pb2.Credential.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckCredential(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.signagelive.v1alpha1.SignageliveService/CheckCredential',
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.CheckCredentialRequest.SerializeToString,
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.CheckCredentialResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMappings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.signagelive.v1alpha1.SignageliveService/GetMappings',
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.GetMappingRequest.SerializeToString,
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListMappingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMappings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.signagelive.v1alpha1.SignageliveService/ListMappings',
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListMappingsRequest.SerializeToString,
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.ListMappingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateMapping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.signagelive.v1alpha1.SignageliveService/CreateMapping',
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.CreateMappingRequest.SerializeToString,
            admobilize_dot_signagelive_dot_v1alpha1_dot_resources__pb2.Mapping.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteMapping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.signagelive.v1alpha1.SignageliveService/DeleteMapping',
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.DeleteMappingRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateMapping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.signagelive.v1alpha1.SignageliveService/UpdateMapping',
            admobilize_dot_signagelive_dot_v1alpha1_dot_signagelive__service__pb2.UpdateMappingRequest.SerializeToString,
            admobilize_dot_signagelive_dot_v1alpha1_dot_resources__pb2.Mapping.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
