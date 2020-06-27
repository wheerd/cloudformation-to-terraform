from . import *

class AWS_AppMesh_VirtualRouter_PortMapping(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualRouter"
  tf_block_type = "port_mapping"

  props = {
    "Port": (BasicValueConverter(), "port"),
    "Protocol": (StringValueConverter(), "protocol"),
  }

class AWS_AppMesh_VirtualRouter_VirtualRouterListener(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualRouter"
  tf_block_type = "virtual_router_listener"

  props = {
    "PortMapping": (AWS_AppMesh_VirtualRouter_PortMapping, "port_mapping"),
  }

class AWS_AppMesh_Route_Duration(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "duration"

  props = {
    "Value": (BasicValueConverter(), "value"),
    "Unit": (StringValueConverter(), "unit"),
  }

class AWS_AppMesh_Route_WeightedTarget(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "weighted_target"

  props = {
    "VirtualNode": (StringValueConverter(), "virtual_node"),
    "Weight": (BasicValueConverter(), "weight"),
  }

class AWS_AppMesh_VirtualNode_Duration(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "duration"

  props = {
    "Value": (BasicValueConverter(), "value"),
    "Unit": (StringValueConverter(), "unit"),
  }

class AWS_AppMesh_Route_HttpRetryPolicy(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "http_retry_policy"

  props = {
    "MaxRetries": (BasicValueConverter(), "max_retries"),
    "PerRetryTimeout": (AWS_AppMesh_Route_Duration, "per_retry_timeout"),
    "HttpRetryEvents": (ListValueConverter(StringValueConverter()), "http_retry_events"),
    "TcpRetryEvents": (ListValueConverter(StringValueConverter()), "tcp_retry_events"),
  }

class AWS_AppMesh_VirtualNode_FileAccessLog(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "file_access_log"

  props = {
    "Path": (StringValueConverter(), "path"),
  }

class AWS_AppMesh_VirtualNode_AwsCloudMapInstanceAttribute(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "aws_cloud_map_instance_attribute"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_AppMesh_VirtualNode_ListenerTlsAcmCertificate(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "listener_tls_acm_certificate"

  props = {
    "CertificateArn": (StringValueConverter(), "certificate_arn"),
  }

class AWS_AppMesh_Route_GrpcTimeout(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "grpc_timeout"

  props = {
    "PerRequest": (AWS_AppMesh_Route_Duration, "per_request"),
    "Idle": (AWS_AppMesh_Route_Duration, "idle"),
  }

class AWS_AppMesh_VirtualNode_TcpTimeout(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "tcp_timeout"

  props = {
    "Idle": (AWS_AppMesh_VirtualNode_Duration, "idle"),
  }

class AWS_AppMesh_Route_TcpTimeout(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "tcp_timeout"

  props = {
    "Idle": (AWS_AppMesh_Route_Duration, "idle"),
  }

class AWS_AppMesh_VirtualNode_PortMapping(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "port_mapping"

  props = {
    "Port": (BasicValueConverter(), "port"),
    "Protocol": (StringValueConverter(), "protocol"),
  }

class AWS_AppMesh_Route_HttpTimeout(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "http_timeout"

  props = {
    "PerRequest": (AWS_AppMesh_Route_Duration, "per_request"),
    "Idle": (AWS_AppMesh_Route_Duration, "idle"),
  }

class AWS_AppMesh_VirtualService_VirtualRouterServiceProvider(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualService"
  tf_block_type = "virtual_router_service_provider"

  props = {
    "VirtualRouterName": (StringValueConverter(), "virtual_router_name"),
  }

class AWS_AppMesh_VirtualNode_HttpTimeout(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "http_timeout"

  props = {
    "PerRequest": (AWS_AppMesh_VirtualNode_Duration, "per_request"),
    "Idle": (AWS_AppMesh_VirtualNode_Duration, "idle"),
  }

class AWS_AppMesh_VirtualNode_HealthCheck(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "health_check"

  props = {
    "Path": (StringValueConverter(), "path"),
    "UnhealthyThreshold": (BasicValueConverter(), "unhealthy_threshold"),
    "Port": (BasicValueConverter(), "port"),
    "HealthyThreshold": (BasicValueConverter(), "healthy_threshold"),
    "TimeoutMillis": (BasicValueConverter(), "timeout_millis"),
    "Protocol": (StringValueConverter(), "protocol"),
    "IntervalMillis": (BasicValueConverter(), "interval_millis"),
  }

class AWS_AppMesh_VirtualNode_AwsCloudMapServiceDiscovery(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "aws_cloud_map_service_discovery"

  props = {
    "NamespaceName": (StringValueConverter(), "namespace_name"),
    "ServiceName": (StringValueConverter(), "service_name"),
    "Attributes": (BlockValueConverter(AWS_AppMesh_VirtualNode_AwsCloudMapInstanceAttribute), None),
  }

class AWS_AppMesh_VirtualNode_TlsValidationContextAcmTrust(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "tls_validation_context_acm_trust"

  props = {
    "CertificateAuthorityArns": (ListValueConverter(StringValueConverter()), "certificate_authority_arns"),
  }

class AWS_AppMesh_Mesh_EgressFilter(CloudFormationProperty):
  entity = "AWS::AppMesh::Mesh"
  tf_block_type = "egress_filter"

  props = {
    "Type": (StringValueConverter(), "type"),
  }

class AWS_AppMesh_VirtualService_VirtualNodeServiceProvider(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualService"
  tf_block_type = "virtual_node_service_provider"

  props = {
    "VirtualNodeName": (StringValueConverter(), "virtual_node_name"),
  }

class AWS_AppMesh_VirtualNode_ListenerTlsFileCertificate(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "listener_tls_file_certificate"

  props = {
    "PrivateKey": (StringValueConverter(), "private_key"),
    "CertificateChain": (StringValueConverter(), "certificate_chain"),
  }

class AWS_AppMesh_Route_HttpRouteAction(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "http_route_action"

  props = {
    "WeightedTargets": (BlockValueConverter(AWS_AppMesh_Route_WeightedTarget), None),
  }

class AWS_AppMesh_VirtualRouter_VirtualRouterSpec(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualRouter"
  tf_block_type = "virtual_router_spec"

  props = {
    "Listeners": (BlockValueConverter(AWS_AppMesh_VirtualRouter_VirtualRouterListener), None),
  }

class AWS_AppMesh_VirtualNode_AccessLog(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "access_log"

  props = {
    "File": (AWS_AppMesh_VirtualNode_FileAccessLog, "file"),
  }

class AWS_AppMesh_Route_GrpcRouteAction(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "grpc_route_action"

  props = {
    "WeightedTargets": (BlockValueConverter(AWS_AppMesh_Route_WeightedTarget), None),
  }

class AWS_AppMesh_VirtualService_VirtualServiceProvider(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualService"
  tf_block_type = "virtual_service_provider"

  props = {
    "VirtualNode": (AWS_AppMesh_VirtualService_VirtualNodeServiceProvider, "virtual_node"),
    "VirtualRouter": (AWS_AppMesh_VirtualService_VirtualRouterServiceProvider, "virtual_router"),
  }

class AWS_AppMesh_VirtualNode_DnsServiceDiscovery(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "dns_service_discovery"

  props = {
    "Hostname": (StringValueConverter(), "hostname"),
  }

class AWS_AppMesh_VirtualNode_TlsValidationContextFileTrust(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "tls_validation_context_file_trust"

  props = {
    "CertificateChain": (StringValueConverter(), "certificate_chain"),
  }

class AWS_AppMesh_Route_MatchRange(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "match_range"

  props = {
    "Start": (BasicValueConverter(), "start"),
    "End": (BasicValueConverter(), "end"),
  }

class AWS_AppMesh_Route_TcpRouteAction(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "tcp_route_action"

  props = {
    "WeightedTargets": (BlockValueConverter(AWS_AppMesh_Route_WeightedTarget), None),
  }

class AWS_AppMesh_VirtualRouter(CloudFormationResource):
  terraform_resource = "aws_app_mesh_virtual_router"

  resource_type = "AWS::AppMesh::VirtualRouter"

  props = {
    "MeshName": (StringValueConverter(), "mesh_name"),
    "VirtualRouterName": (StringValueConverter(), "virtual_router_name"),
    "MeshOwner": (StringValueConverter(), "mesh_owner"),
    "Spec": (AWS_AppMesh_VirtualRouter_VirtualRouterSpec, "spec"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_AppMesh_VirtualNode_GrpcTimeout(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "grpc_timeout"

  props = {
    "PerRequest": (AWS_AppMesh_VirtualNode_Duration, "per_request"),
    "Idle": (AWS_AppMesh_VirtualNode_Duration, "idle"),
  }

class AWS_AppMesh_VirtualNode_Logging(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "logging"

  props = {
    "AccessLog": (AWS_AppMesh_VirtualNode_AccessLog, "access_log"),
  }

class AWS_AppMesh_Route_GrpcRetryPolicy(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "grpc_retry_policy"

  props = {
    "MaxRetries": (BasicValueConverter(), "max_retries"),
    "PerRetryTimeout": (AWS_AppMesh_Route_Duration, "per_retry_timeout"),
    "GrpcRetryEvents": (ListValueConverter(StringValueConverter()), "grpc_retry_events"),
    "HttpRetryEvents": (ListValueConverter(StringValueConverter()), "http_retry_events"),
    "TcpRetryEvents": (ListValueConverter(StringValueConverter()), "tcp_retry_events"),
  }

class AWS_AppMesh_VirtualNode_ServiceDiscovery(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "service_discovery"

  props = {
    "DNS": (AWS_AppMesh_VirtualNode_DnsServiceDiscovery, "dns"),
    "AWSCloudMap": (AWS_AppMesh_VirtualNode_AwsCloudMapServiceDiscovery, "aws_cloud_map"),
  }

class AWS_AppMesh_Route_TcpRoute(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "tcp_route"

  props = {
    "Action": (AWS_AppMesh_Route_TcpRouteAction, "action"),
    "Timeout": (AWS_AppMesh_Route_TcpTimeout, "timeout"),
  }

class AWS_AppMesh_Route_GrpcRouteMetadataMatchMethod(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "grpc_route_metadata_match_method"

  props = {
    "Suffix": (StringValueConverter(), "suffix"),
    "Regex": (StringValueConverter(), "regex"),
    "Exact": (StringValueConverter(), "exact"),
    "Prefix": (StringValueConverter(), "prefix"),
    "Range": (AWS_AppMesh_Route_MatchRange, "range"),
  }

class AWS_AppMesh_VirtualNode_TlsValidationContextTrust(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "tls_validation_context_trust"

  props = {
    "ACM": (AWS_AppMesh_VirtualNode_TlsValidationContextAcmTrust, "acm"),
    "File": (AWS_AppMesh_VirtualNode_TlsValidationContextFileTrust, "file"),
  }

class AWS_AppMesh_Route_HeaderMatchMethod(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "header_match_method"

  props = {
    "Suffix": (StringValueConverter(), "suffix"),
    "Regex": (StringValueConverter(), "regex"),
    "Exact": (StringValueConverter(), "exact"),
    "Prefix": (StringValueConverter(), "prefix"),
    "Range": (AWS_AppMesh_Route_MatchRange, "range"),
  }

class AWS_AppMesh_Mesh_MeshSpec(CloudFormationProperty):
  entity = "AWS::AppMesh::Mesh"
  tf_block_type = "mesh_spec"

  props = {
    "EgressFilter": (AWS_AppMesh_Mesh_EgressFilter, "egress_filter"),
  }

class AWS_AppMesh_VirtualNode_ListenerTlsCertificate(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "listener_tls_certificate"

  props = {
    "ACM": (AWS_AppMesh_VirtualNode_ListenerTlsAcmCertificate, "acm"),
    "File": (AWS_AppMesh_VirtualNode_ListenerTlsFileCertificate, "file"),
  }

class AWS_AppMesh_VirtualNode_ListenerTimeout(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "listener_timeout"

  props = {
    "TCP": (AWS_AppMesh_VirtualNode_TcpTimeout, "tcp"),
    "HTTP2": (AWS_AppMesh_VirtualNode_HttpTimeout, "http2"),
    "HTTP": (AWS_AppMesh_VirtualNode_HttpTimeout, "http"),
    "GRPC": (AWS_AppMesh_VirtualNode_GrpcTimeout, "grpc"),
  }

class AWS_AppMesh_VirtualNode_ListenerTls(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "listener_tls"

  props = {
    "Mode": (StringValueConverter(), "mode"),
    "Certificate": (AWS_AppMesh_VirtualNode_ListenerTlsCertificate, "certificate"),
  }

class AWS_AppMesh_VirtualService_VirtualServiceSpec(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualService"
  tf_block_type = "virtual_service_spec"

  props = {
    "Provider": (AWS_AppMesh_VirtualService_VirtualServiceProvider, "provider"),
  }

class AWS_AppMesh_Route_HttpRouteHeader(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "http_route_header"

  props = {
    "Invert": (BasicValueConverter(), "invert"),
    "Name": (StringValueConverter(), "name"),
    "Match": (AWS_AppMesh_Route_HeaderMatchMethod, "match"),
  }

class AWS_AppMesh_Route_GrpcRouteMetadata(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "grpc_route_metadata"

  props = {
    "Invert": (BasicValueConverter(), "invert"),
    "Name": (StringValueConverter(), "name"),
    "Match": (AWS_AppMesh_Route_GrpcRouteMetadataMatchMethod, "match"),
  }

class AWS_AppMesh_Route_HttpRouteMatch(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "http_route_match"

  props = {
    "Scheme": (StringValueConverter(), "scheme"),
    "Headers": (BlockValueConverter(AWS_AppMesh_Route_HttpRouteHeader), None),
    "Prefix": (StringValueConverter(), "prefix"),
    "Method": (StringValueConverter(), "method"),
  }

class AWS_AppMesh_VirtualNode_TlsValidationContext(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "tls_validation_context"

  props = {
    "Trust": (AWS_AppMesh_VirtualNode_TlsValidationContextTrust, "trust"),
  }

class AWS_AppMesh_Route_GrpcRouteMatch(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "grpc_route_match"

  props = {
    "ServiceName": (StringValueConverter(), "service_name"),
    "Metadata": (BlockValueConverter(AWS_AppMesh_Route_GrpcRouteMetadata), None),
    "MethodName": (StringValueConverter(), "method_name"),
  }

class AWS_AppMesh_VirtualNode_Listener(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "listener"

  props = {
    "Timeout": (AWS_AppMesh_VirtualNode_ListenerTimeout, "timeout"),
    "HealthCheck": (AWS_AppMesh_VirtualNode_HealthCheck, "health_check"),
    "TLS": (AWS_AppMesh_VirtualNode_ListenerTls, "tls"),
    "PortMapping": (AWS_AppMesh_VirtualNode_PortMapping, "port_mapping"),
  }

class AWS_AppMesh_Route_HttpRoute(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "http_route"

  props = {
    "Action": (AWS_AppMesh_Route_HttpRouteAction, "action"),
    "Timeout": (AWS_AppMesh_Route_HttpTimeout, "timeout"),
    "RetryPolicy": (AWS_AppMesh_Route_HttpRetryPolicy, "retry_policy"),
    "Match": (AWS_AppMesh_Route_HttpRouteMatch, "match"),
  }

class AWS_AppMesh_VirtualService(CloudFormationResource):
  terraform_resource = "aws_app_mesh_virtual_service"

  resource_type = "AWS::AppMesh::VirtualService"

  props = {
    "MeshName": (StringValueConverter(), "mesh_name"),
    "MeshOwner": (StringValueConverter(), "mesh_owner"),
    "VirtualServiceName": (StringValueConverter(), "virtual_service_name"),
    "Spec": (AWS_AppMesh_VirtualService_VirtualServiceSpec, "spec"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_AppMesh_Mesh(CloudFormationResource):
  terraform_resource = "aws_app_mesh_mesh"

  resource_type = "AWS::AppMesh::Mesh"

  props = {
    "MeshName": (StringValueConverter(), "mesh_name"),
    "Spec": (AWS_AppMesh_Mesh_MeshSpec, "spec"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_AppMesh_VirtualNode_ClientPolicyTls(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "client_policy_tls"

  props = {
    "Validation": (AWS_AppMesh_VirtualNode_TlsValidationContext, "validation"),
    "Enforce": (BasicValueConverter(), "enforce"),
    "Ports": (ListValueConverter(BasicValueConverter()), "ports"),
  }

class AWS_AppMesh_Route_GrpcRoute(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "grpc_route"

  props = {
    "Action": (AWS_AppMesh_Route_GrpcRouteAction, "action"),
    "Timeout": (AWS_AppMesh_Route_GrpcTimeout, "timeout"),
    "RetryPolicy": (AWS_AppMesh_Route_GrpcRetryPolicy, "retry_policy"),
    "Match": (AWS_AppMesh_Route_GrpcRouteMatch, "match"),
  }

class AWS_AppMesh_VirtualNode_ClientPolicy(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "client_policy"

  props = {
    "TLS": (AWS_AppMesh_VirtualNode_ClientPolicyTls, "tls"),
  }

class AWS_AppMesh_Route_RouteSpec(CloudFormationProperty):
  entity = "AWS::AppMesh::Route"
  tf_block_type = "route_spec"

  props = {
    "HttpRoute": (AWS_AppMesh_Route_HttpRoute, "http_route"),
    "Priority": (BasicValueConverter(), "priority"),
    "Http2Route": (AWS_AppMesh_Route_HttpRoute, "http2_route"),
    "GrpcRoute": (AWS_AppMesh_Route_GrpcRoute, "grpc_route"),
    "TcpRoute": (AWS_AppMesh_Route_TcpRoute, "tcp_route"),
  }

class AWS_AppMesh_VirtualNode_VirtualServiceBackend(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "virtual_service_backend"

  props = {
    "ClientPolicy": (AWS_AppMesh_VirtualNode_ClientPolicy, "client_policy"),
    "VirtualServiceName": (StringValueConverter(), "virtual_service_name"),
  }

class AWS_AppMesh_VirtualNode_BackendDefaults(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "backend_defaults"

  props = {
    "ClientPolicy": (AWS_AppMesh_VirtualNode_ClientPolicy, "client_policy"),
  }

class AWS_AppMesh_Route(CloudFormationResource):
  terraform_resource = "aws_app_mesh_route"

  resource_type = "AWS::AppMesh::Route"

  props = {
    "MeshName": (StringValueConverter(), "mesh_name"),
    "VirtualRouterName": (StringValueConverter(), "virtual_router_name"),
    "MeshOwner": (StringValueConverter(), "mesh_owner"),
    "RouteName": (StringValueConverter(), "route_name"),
    "Spec": (AWS_AppMesh_Route_RouteSpec, "spec"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_AppMesh_VirtualNode_Backend(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "backend"

  props = {
    "VirtualService": (AWS_AppMesh_VirtualNode_VirtualServiceBackend, "virtual_service"),
  }

class AWS_AppMesh_VirtualNode_VirtualNodeSpec(CloudFormationProperty):
  entity = "AWS::AppMesh::VirtualNode"
  tf_block_type = "virtual_node_spec"

  props = {
    "Logging": (AWS_AppMesh_VirtualNode_Logging, "logging"),
    "Backends": (BlockValueConverter(AWS_AppMesh_VirtualNode_Backend), None),
    "Listeners": (BlockValueConverter(AWS_AppMesh_VirtualNode_Listener), None),
    "BackendDefaults": (AWS_AppMesh_VirtualNode_BackendDefaults, "backend_defaults"),
    "ServiceDiscovery": (AWS_AppMesh_VirtualNode_ServiceDiscovery, "service_discovery"),
  }

class AWS_AppMesh_VirtualNode(CloudFormationResource):
  terraform_resource = "aws_app_mesh_virtual_node"

  resource_type = "AWS::AppMesh::VirtualNode"

  props = {
    "MeshName": (StringValueConverter(), "mesh_name"),
    "MeshOwner": (StringValueConverter(), "mesh_owner"),
    "Spec": (AWS_AppMesh_VirtualNode_VirtualNodeSpec, "spec"),
    "VirtualNodeName": (StringValueConverter(), "virtual_node_name"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

