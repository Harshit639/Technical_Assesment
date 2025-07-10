"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from browserstack_sdk import sdk_pb2 as browserstack__sdk_dot_sdk__pb2
class SDKStub(object):
    """import "google/protobuf/struct.proto";
    """
    def __init__(self, channel):
        """Constructor.
        Args:
            channel: A grpc.Channel.
        """
        self.StartBinSession = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/StartBinSession',
                request_serializer=browserstack__sdk_dot_sdk__pb2.StartBinSessionRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.StartBinSessionResponse.FromString,
                )
        self.ConnectBinSession = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/ConnectBinSession',
                request_serializer=browserstack__sdk_dot_sdk__pb2.ConnectBinSessionRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.ConnectBinSessionResponse.FromString,
                )
        self.StopBinSession = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/StopBinSession',
                request_serializer=browserstack__sdk_dot_sdk__pb2.StopBinSessionRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.StopBinSessionResponse.FromString,
                )
        self.DriverInit = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/DriverInit',
                request_serializer=browserstack__sdk_dot_sdk__pb2.DriverInitRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.DriverInitResponse.FromString,
                )
        self.AutomationFrameworkInit = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/AutomationFrameworkInit',
                request_serializer=browserstack__sdk_dot_sdk__pb2.AutomationFrameworkInitRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.AutomationFrameworkInitResponse.FromString,
                )
        self.AutomationFrameworkStart = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/AutomationFrameworkStart',
                request_serializer=browserstack__sdk_dot_sdk__pb2.AutomationFrameworkStartRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.AutomationFrameworkStartResponse.FromString,
                )
        self.AutomationFrameworkStop = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/AutomationFrameworkStop',
                request_serializer=browserstack__sdk_dot_sdk__pb2.AutomationFrameworkStopRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.AutomationFrameworkStopResponse.FromString,
                )
        self.TestOrchestration = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/TestOrchestration',
                request_serializer=browserstack__sdk_dot_sdk__pb2.TestOrchestrationRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.TestOrchestrationResponse.FromString,
                )
        self.FindNearestHub = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/FindNearestHub',
                request_serializer=browserstack__sdk_dot_sdk__pb2.FindNearestHubRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.FindNearestHubResponse.FromString,
                )
        self.AIBrowserExtension = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/AIBrowserExtension',
                request_serializer=browserstack__sdk_dot_sdk__pb2.AIBrowserExtensionRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.AIBrowserExtensionResponse.FromString,
                )
        self.AISelfHealStep = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/AISelfHealStep',
                request_serializer=browserstack__sdk_dot_sdk__pb2.AISelfHealStepRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.AISelfHealStepResponse.FromString,
                )
        self.AISelfHealGetResult = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/AISelfHealGetResult',
                request_serializer=browserstack__sdk_dot_sdk__pb2.AISelfHealGetRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.AISelfHealGetResponse.FromString,
                )
        self.AccessibilityConfig = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/AccessibilityConfig',
                request_serializer=browserstack__sdk_dot_sdk__pb2.AccessibilityConfigRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.AccessibilityConfigResponse.FromString,
                )
        self.ObservabilityConfig = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/ObservabilityConfig',
                request_serializer=browserstack__sdk_dot_sdk__pb2.ObservabilityConfigRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.ObservabilityConfigResponse.FromString,
                )
        self.AccessibilityResult = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/AccessibilityResult',
                request_serializer=browserstack__sdk_dot_sdk__pb2.AccessibilityResultRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.AccessibilityResultResponse.FromString,
                )
        self.TestFrameworkEvent = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/TestFrameworkEvent',
                request_serializer=browserstack__sdk_dot_sdk__pb2.TestFrameworkEventRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.TestFrameworkEventResponse.FromString,
                )
        self.TestSessionEvent = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/TestSessionEvent',
                request_serializer=browserstack__sdk_dot_sdk__pb2.TestSessionEventRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.TestSessionEventResponse.FromString,
                )
        self.EnqueueTestEvent = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/EnqueueTestEvent',
                request_serializer=browserstack__sdk_dot_sdk__pb2.EnqueueTestEventRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.EnqueueTestEventResponse.FromString,
                )
        self.LogCreatedEvent = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/LogCreatedEvent',
                request_serializer=browserstack__sdk_dot_sdk__pb2.LogCreatedEventRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.LogCreatedEventResponse.FromString,
                )
        self.FetchDriverExecuteParamsEvent = channel.unary_unary(
                '/browserstack.sdk.v1.SDK/FetchDriverExecuteParamsEvent',
                request_serializer=browserstack__sdk_dot_sdk__pb2.FetchDriverExecuteParamsEventRequest.SerializeToString,
                response_deserializer=browserstack__sdk_dot_sdk__pb2.FetchDriverExecuteParamsEventResponse.FromString,
                )
class SDKServicer(object):
    """import "google/protobuf/struct.proto";
    """
    def StartBinSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def ConnectBinSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def StopBinSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def DriverInit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def AutomationFrameworkInit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def AutomationFrameworkStart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def AutomationFrameworkStop(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def TestOrchestration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def FindNearestHub(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def AIBrowserExtension(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def AISelfHealStep(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def AISelfHealGetResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def AccessibilityConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def ObservabilityConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def AccessibilityResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def TestFrameworkEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def TestSessionEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def EnqueueTestEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def LogCreatedEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    def FetchDriverExecuteParamsEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
def add_SDKServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartBinSession': grpc.unary_unary_rpc_method_handler(
                    servicer.StartBinSession,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.StartBinSessionRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.StartBinSessionResponse.SerializeToString,
            ),
            'ConnectBinSession': grpc.unary_unary_rpc_method_handler(
                    servicer.ConnectBinSession,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.ConnectBinSessionRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.ConnectBinSessionResponse.SerializeToString,
            ),
            'StopBinSession': grpc.unary_unary_rpc_method_handler(
                    servicer.StopBinSession,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.StopBinSessionRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.StopBinSessionResponse.SerializeToString,
            ),
            'DriverInit': grpc.unary_unary_rpc_method_handler(
                    servicer.DriverInit,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.DriverInitRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.DriverInitResponse.SerializeToString,
            ),
            'AutomationFrameworkInit': grpc.unary_unary_rpc_method_handler(
                    servicer.AutomationFrameworkInit,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.AutomationFrameworkInitRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.AutomationFrameworkInitResponse.SerializeToString,
            ),
            'AutomationFrameworkStart': grpc.unary_unary_rpc_method_handler(
                    servicer.AutomationFrameworkStart,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.AutomationFrameworkStartRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.AutomationFrameworkStartResponse.SerializeToString,
            ),
            'AutomationFrameworkStop': grpc.unary_unary_rpc_method_handler(
                    servicer.AutomationFrameworkStop,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.AutomationFrameworkStopRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.AutomationFrameworkStopResponse.SerializeToString,
            ),
            'TestOrchestration': grpc.unary_unary_rpc_method_handler(
                    servicer.TestOrchestration,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.TestOrchestrationRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.TestOrchestrationResponse.SerializeToString,
            ),
            'FindNearestHub': grpc.unary_unary_rpc_method_handler(
                    servicer.FindNearestHub,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.FindNearestHubRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.FindNearestHubResponse.SerializeToString,
            ),
            'AIBrowserExtension': grpc.unary_unary_rpc_method_handler(
                    servicer.AIBrowserExtension,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.AIBrowserExtensionRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.AIBrowserExtensionResponse.SerializeToString,
            ),
            'AISelfHealStep': grpc.unary_unary_rpc_method_handler(
                    servicer.AISelfHealStep,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.AISelfHealStepRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.AISelfHealStepResponse.SerializeToString,
            ),
            'AISelfHealGetResult': grpc.unary_unary_rpc_method_handler(
                    servicer.AISelfHealGetResult,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.AISelfHealGetRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.AISelfHealGetResponse.SerializeToString,
            ),
            'AccessibilityConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.AccessibilityConfig,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.AccessibilityConfigRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.AccessibilityConfigResponse.SerializeToString,
            ),
            'ObservabilityConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.ObservabilityConfig,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.ObservabilityConfigRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.ObservabilityConfigResponse.SerializeToString,
            ),
            'AccessibilityResult': grpc.unary_unary_rpc_method_handler(
                    servicer.AccessibilityResult,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.AccessibilityResultRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.AccessibilityResultResponse.SerializeToString,
            ),
            'TestFrameworkEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.TestFrameworkEvent,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.TestFrameworkEventRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.TestFrameworkEventResponse.SerializeToString,
            ),
            'TestSessionEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.TestSessionEvent,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.TestSessionEventRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.TestSessionEventResponse.SerializeToString,
            ),
            'EnqueueTestEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.EnqueueTestEvent,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.EnqueueTestEventRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.EnqueueTestEventResponse.SerializeToString,
            ),
            'LogCreatedEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.LogCreatedEvent,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.LogCreatedEventRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.LogCreatedEventResponse.SerializeToString,
            ),
            'FetchDriverExecuteParamsEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchDriverExecuteParamsEvent,
                    request_deserializer=browserstack__sdk_dot_sdk__pb2.FetchDriverExecuteParamsEventRequest.FromString,
                    response_serializer=browserstack__sdk_dot_sdk__pb2.FetchDriverExecuteParamsEventResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'browserstack.sdk.v1.SDK', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
class SDK(object):
    """import "google/protobuf/struct.proto";
    """
    @staticmethod
    def StartBinSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/StartBinSession',
            browserstack__sdk_dot_sdk__pb2.StartBinSessionRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.StartBinSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def ConnectBinSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/ConnectBinSession',
            browserstack__sdk_dot_sdk__pb2.ConnectBinSessionRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.ConnectBinSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def StopBinSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/StopBinSession',
            browserstack__sdk_dot_sdk__pb2.StopBinSessionRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.StopBinSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def DriverInit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/DriverInit',
            browserstack__sdk_dot_sdk__pb2.DriverInitRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.DriverInitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def AutomationFrameworkInit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/AutomationFrameworkInit',
            browserstack__sdk_dot_sdk__pb2.AutomationFrameworkInitRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.AutomationFrameworkInitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def AutomationFrameworkStart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/AutomationFrameworkStart',
            browserstack__sdk_dot_sdk__pb2.AutomationFrameworkStartRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.AutomationFrameworkStartResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def AutomationFrameworkStop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/AutomationFrameworkStop',
            browserstack__sdk_dot_sdk__pb2.AutomationFrameworkStopRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.AutomationFrameworkStopResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def TestOrchestration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/TestOrchestration',
            browserstack__sdk_dot_sdk__pb2.TestOrchestrationRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.TestOrchestrationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def FindNearestHub(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/FindNearestHub',
            browserstack__sdk_dot_sdk__pb2.FindNearestHubRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.FindNearestHubResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def AIBrowserExtension(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/AIBrowserExtension',
            browserstack__sdk_dot_sdk__pb2.AIBrowserExtensionRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.AIBrowserExtensionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def AISelfHealStep(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/AISelfHealStep',
            browserstack__sdk_dot_sdk__pb2.AISelfHealStepRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.AISelfHealStepResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def AISelfHealGetResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/AISelfHealGetResult',
            browserstack__sdk_dot_sdk__pb2.AISelfHealGetRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.AISelfHealGetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def AccessibilityConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/AccessibilityConfig',
            browserstack__sdk_dot_sdk__pb2.AccessibilityConfigRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.AccessibilityConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def ObservabilityConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/ObservabilityConfig',
            browserstack__sdk_dot_sdk__pb2.ObservabilityConfigRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.ObservabilityConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def AccessibilityResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/AccessibilityResult',
            browserstack__sdk_dot_sdk__pb2.AccessibilityResultRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.AccessibilityResultResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def TestFrameworkEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/TestFrameworkEvent',
            browserstack__sdk_dot_sdk__pb2.TestFrameworkEventRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.TestFrameworkEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def TestSessionEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/TestSessionEvent',
            browserstack__sdk_dot_sdk__pb2.TestSessionEventRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.TestSessionEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def EnqueueTestEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/EnqueueTestEvent',
            browserstack__sdk_dot_sdk__pb2.EnqueueTestEventRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.EnqueueTestEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def LogCreatedEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/LogCreatedEvent',
            browserstack__sdk_dot_sdk__pb2.LogCreatedEventRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.LogCreatedEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
    @staticmethod
    def FetchDriverExecuteParamsEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/browserstack.sdk.v1.SDK/FetchDriverExecuteParamsEvent',
            browserstack__sdk_dot_sdk__pb2.FetchDriverExecuteParamsEventRequest.SerializeToString,
            browserstack__sdk_dot_sdk__pb2.FetchDriverExecuteParamsEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
