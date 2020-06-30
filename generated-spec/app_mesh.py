from . import *

class AWS_AppMesh_VirtualRouter_PortMapping(CloudFormationProperty):
  def write(self, w):
    with w.block("port_mapping"):
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "Protocol", "protocol", StringValueConverter())


class AWS_AppMesh_VirtualRouter_VirtualRouterListener(CloudFormationProperty):
  def write(self, w):
    with w.block("virtual_router_listener"):
      self.block(w, "PortMapping", AWS_AppMesh_VirtualRouter_PortMapping)


class AWS_AppMesh_Route_Duration(CloudFormationProperty):
  def write(self, w):
    with w.block("duration"):
      self.property(w, "Value", "value", BasicValueConverter())
      self.property(w, "Unit", "unit", StringValueConverter())


class AWS_AppMesh_Route_WeightedTarget(CloudFormationProperty):
  def write(self, w):
    with w.block("weighted_target"):
      self.property(w, "VirtualNode", "virtual_node", StringValueConverter())
      self.property(w, "Weight", "weight", BasicValueConverter())


class AWS_AppMesh_VirtualNode_Duration(CloudFormationProperty):
  def write(self, w):
    with w.block("duration"):
      self.property(w, "Value", "value", BasicValueConverter())
      self.property(w, "Unit", "unit", StringValueConverter())


class AWS_AppMesh_Route_HttpRetryPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("http_retry_policy"):
      self.property(w, "MaxRetries", "max_retries", BasicValueConverter())
      self.block(w, "PerRetryTimeout", AWS_AppMesh_Route_Duration)
      self.property(w, "HttpRetryEvents", "http_retry_events", ListValueConverter(StringValueConverter()))
      self.property(w, "TcpRetryEvents", "tcp_retry_events", ListValueConverter(StringValueConverter()))


class AWS_AppMesh_VirtualNode_FileAccessLog(CloudFormationProperty):
  def write(self, w):
    with w.block("file_access_log"):
      self.property(w, "Path", "path", StringValueConverter())


class AWS_AppMesh_VirtualNode_AwsCloudMapInstanceAttribute(CloudFormationProperty):
  def write(self, w):
    with w.block("aws_cloud_map_instance_attribute"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_AppMesh_VirtualNode_ListenerTlsAcmCertificate(CloudFormationProperty):
  def write(self, w):
    with w.block("listener_tls_acm_certificate"):
      self.property(w, "CertificateArn", "certificate_arn", StringValueConverter())


class AWS_AppMesh_Route_GrpcTimeout(CloudFormationProperty):
  def write(self, w):
    with w.block("grpc_timeout"):
      self.block(w, "PerRequest", AWS_AppMesh_Route_Duration)
      self.block(w, "Idle", AWS_AppMesh_Route_Duration)


class AWS_AppMesh_VirtualNode_TcpTimeout(CloudFormationProperty):
  def write(self, w):
    with w.block("tcp_timeout"):
      self.block(w, "Idle", AWS_AppMesh_VirtualNode_Duration)


class AWS_AppMesh_Route_TcpTimeout(CloudFormationProperty):
  def write(self, w):
    with w.block("tcp_timeout"):
      self.block(w, "Idle", AWS_AppMesh_Route_Duration)


class AWS_AppMesh_VirtualNode_PortMapping(CloudFormationProperty):
  def write(self, w):
    with w.block("port_mapping"):
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "Protocol", "protocol", StringValueConverter())


class AWS_AppMesh_Route_HttpTimeout(CloudFormationProperty):
  def write(self, w):
    with w.block("http_timeout"):
      self.block(w, "PerRequest", AWS_AppMesh_Route_Duration)
      self.block(w, "Idle", AWS_AppMesh_Route_Duration)


class AWS_AppMesh_VirtualService_VirtualRouterServiceProvider(CloudFormationProperty):
  def write(self, w):
    with w.block("virtual_router_service_provider"):
      self.property(w, "VirtualRouterName", "virtual_router_name", StringValueConverter())


class AWS_AppMesh_VirtualNode_HttpTimeout(CloudFormationProperty):
  def write(self, w):
    with w.block("http_timeout"):
      self.block(w, "PerRequest", AWS_AppMesh_VirtualNode_Duration)
      self.block(w, "Idle", AWS_AppMesh_VirtualNode_Duration)


class AWS_AppMesh_VirtualNode_HealthCheck(CloudFormationProperty):
  def write(self, w):
    with w.block("health_check"):
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "UnhealthyThreshold", "unhealthy_threshold", BasicValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "HealthyThreshold", "healthy_threshold", BasicValueConverter())
      self.property(w, "TimeoutMillis", "timeout_millis", BasicValueConverter())
      self.property(w, "Protocol", "protocol", StringValueConverter())
      self.property(w, "IntervalMillis", "interval_millis", BasicValueConverter())


class AWS_AppMesh_VirtualNode_AwsCloudMapServiceDiscovery(CloudFormationProperty):
  def write(self, w):
    with w.block("aws_cloud_map_service_discovery"):
      self.property(w, "NamespaceName", "namespace_name", StringValueConverter())
      self.property(w, "ServiceName", "service_name", StringValueConverter())
      self.repeated_block(w, "Attributes", AWS_AppMesh_VirtualNode_AwsCloudMapInstanceAttribute)


class AWS_AppMesh_VirtualNode_TlsValidationContextAcmTrust(CloudFormationProperty):
  def write(self, w):
    with w.block("tls_validation_context_acm_trust"):
      self.property(w, "CertificateAuthorityArns", "certificate_authority_arns", ListValueConverter(StringValueConverter()))


class AWS_AppMesh_Mesh_EgressFilter(CloudFormationProperty):
  def write(self, w):
    with w.block("egress_filter"):
      self.property(w, "Type", "type", StringValueConverter())


class AWS_AppMesh_VirtualService_VirtualNodeServiceProvider(CloudFormationProperty):
  def write(self, w):
    with w.block("virtual_node_service_provider"):
      self.property(w, "VirtualNodeName", "virtual_node_name", StringValueConverter())


class AWS_AppMesh_VirtualNode_ListenerTlsFileCertificate(CloudFormationProperty):
  def write(self, w):
    with w.block("listener_tls_file_certificate"):
      self.property(w, "PrivateKey", "private_key", StringValueConverter())
      self.property(w, "CertificateChain", "certificate_chain", StringValueConverter())


class AWS_AppMesh_Route_HttpRouteAction(CloudFormationProperty):
  def write(self, w):
    with w.block("http_route_action"):
      self.repeated_block(w, "WeightedTargets", AWS_AppMesh_Route_WeightedTarget)


class AWS_AppMesh_VirtualRouter_VirtualRouterSpec(CloudFormationProperty):
  def write(self, w):
    with w.block("virtual_router_spec"):
      self.repeated_block(w, "Listeners", AWS_AppMesh_VirtualRouter_VirtualRouterListener)


class AWS_AppMesh_VirtualNode_AccessLog(CloudFormationProperty):
  def write(self, w):
    with w.block("access_log"):
      self.block(w, "File", AWS_AppMesh_VirtualNode_FileAccessLog)


class AWS_AppMesh_Route_GrpcRouteAction(CloudFormationProperty):
  def write(self, w):
    with w.block("grpc_route_action"):
      self.repeated_block(w, "WeightedTargets", AWS_AppMesh_Route_WeightedTarget)


class AWS_AppMesh_VirtualService_VirtualServiceProvider(CloudFormationProperty):
  def write(self, w):
    with w.block("virtual_service_provider"):
      self.block(w, "VirtualNode", AWS_AppMesh_VirtualService_VirtualNodeServiceProvider)
      self.block(w, "VirtualRouter", AWS_AppMesh_VirtualService_VirtualRouterServiceProvider)


class AWS_AppMesh_VirtualNode_DnsServiceDiscovery(CloudFormationProperty):
  def write(self, w):
    with w.block("dns_service_discovery"):
      self.property(w, "Hostname", "hostname", StringValueConverter())


class AWS_AppMesh_VirtualNode_TlsValidationContextFileTrust(CloudFormationProperty):
  def write(self, w):
    with w.block("tls_validation_context_file_trust"):
      self.property(w, "CertificateChain", "certificate_chain", StringValueConverter())


class AWS_AppMesh_Route_MatchRange(CloudFormationProperty):
  def write(self, w):
    with w.block("match_range"):
      self.property(w, "Start", "start", BasicValueConverter())
      self.property(w, "End", "end", BasicValueConverter())


class AWS_AppMesh_Route_TcpRouteAction(CloudFormationProperty):
  def write(self, w):
    with w.block("tcp_route_action"):
      self.repeated_block(w, "WeightedTargets", AWS_AppMesh_Route_WeightedTarget)


class AWS_AppMesh_VirtualRouter(CloudFormationResource):
  cfn_type = "AWS::AppMesh::VirtualRouter"
  tf_type = "aws_appmesh_virtual_router"
  ref = "id"
  attrs = {
    "Uid": "id",
    "MeshName": "mesh_name", # TODO: Probably not the correct mapping
    "VirtualRouterName": "virtual_router_name", # TODO: Probably not the correct mapping
    "MeshOwner": "mesh_owner", # TODO: Probably not the correct mapping
    "ResourceOwner": "resource_owner", # TODO: Probably not the correct mapping
    "Arn": "arn",
    # Additional TF attributes: created_date, last_updated_date
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "MeshName", "mesh_name", StringValueConverter())
      self.property(w, "VirtualRouterName", "name", StringValueConverter())
      self.property(w, "MeshOwner", "mesh_owner", StringValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "Spec", AWS_AppMesh_VirtualRouter_VirtualRouterSpec)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_AppMesh_VirtualNode_GrpcTimeout(CloudFormationProperty):
  def write(self, w):
    with w.block("grpc_timeout"):
      self.block(w, "PerRequest", AWS_AppMesh_VirtualNode_Duration)
      self.block(w, "Idle", AWS_AppMesh_VirtualNode_Duration)


class AWS_AppMesh_VirtualNode_Logging(CloudFormationProperty):
  def write(self, w):
    with w.block("logging"):
      self.block(w, "AccessLog", AWS_AppMesh_VirtualNode_AccessLog)


class AWS_AppMesh_Route_GrpcRetryPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("grpc_retry_policy"):
      self.property(w, "MaxRetries", "max_retries", BasicValueConverter())
      self.block(w, "PerRetryTimeout", AWS_AppMesh_Route_Duration)
      self.property(w, "GrpcRetryEvents", "grpc_retry_events", ListValueConverter(StringValueConverter()))
      self.property(w, "HttpRetryEvents", "http_retry_events", ListValueConverter(StringValueConverter()))
      self.property(w, "TcpRetryEvents", "tcp_retry_events", ListValueConverter(StringValueConverter()))


class AWS_AppMesh_VirtualNode_ServiceDiscovery(CloudFormationProperty):
  def write(self, w):
    with w.block("service_discovery"):
      self.block(w, "DNS", AWS_AppMesh_VirtualNode_DnsServiceDiscovery)
      self.block(w, "AWSCloudMap", AWS_AppMesh_VirtualNode_AwsCloudMapServiceDiscovery)


class AWS_AppMesh_Route_TcpRoute(CloudFormationProperty):
  def write(self, w):
    with w.block("tcp_route"):
      self.block(w, "Action", AWS_AppMesh_Route_TcpRouteAction)
      self.block(w, "Timeout", AWS_AppMesh_Route_TcpTimeout)


class AWS_AppMesh_Route_GrpcRouteMetadataMatchMethod(CloudFormationProperty):
  def write(self, w):
    with w.block("grpc_route_metadata_match_method"):
      self.property(w, "Suffix", "suffix", StringValueConverter())
      self.property(w, "Regex", "regex", StringValueConverter())
      self.property(w, "Exact", "exact", StringValueConverter())
      self.property(w, "Prefix", "prefix", StringValueConverter())
      self.block(w, "Range", AWS_AppMesh_Route_MatchRange)


class AWS_AppMesh_VirtualNode_TlsValidationContextTrust(CloudFormationProperty):
  def write(self, w):
    with w.block("tls_validation_context_trust"):
      self.block(w, "ACM", AWS_AppMesh_VirtualNode_TlsValidationContextAcmTrust)
      self.block(w, "File", AWS_AppMesh_VirtualNode_TlsValidationContextFileTrust)


class AWS_AppMesh_Route_HeaderMatchMethod(CloudFormationProperty):
  def write(self, w):
    with w.block("header_match_method"):
      self.property(w, "Suffix", "suffix", StringValueConverter())
      self.property(w, "Regex", "regex", StringValueConverter())
      self.property(w, "Exact", "exact", StringValueConverter())
      self.property(w, "Prefix", "prefix", StringValueConverter())
      self.block(w, "Range", AWS_AppMesh_Route_MatchRange)


class AWS_AppMesh_Mesh_MeshSpec(CloudFormationProperty):
  def write(self, w):
    with w.block("mesh_spec"):
      self.block(w, "EgressFilter", AWS_AppMesh_Mesh_EgressFilter)


class AWS_AppMesh_VirtualNode_ListenerTlsCertificate(CloudFormationProperty):
  def write(self, w):
    with w.block("listener_tls_certificate"):
      self.block(w, "ACM", AWS_AppMesh_VirtualNode_ListenerTlsAcmCertificate)
      self.block(w, "File", AWS_AppMesh_VirtualNode_ListenerTlsFileCertificate)


class AWS_AppMesh_VirtualNode_ListenerTimeout(CloudFormationProperty):
  def write(self, w):
    with w.block("listener_timeout"):
      self.block(w, "TCP", AWS_AppMesh_VirtualNode_TcpTimeout)
      self.block(w, "HTTP2", AWS_AppMesh_VirtualNode_HttpTimeout)
      self.block(w, "HTTP", AWS_AppMesh_VirtualNode_HttpTimeout)
      self.block(w, "GRPC", AWS_AppMesh_VirtualNode_GrpcTimeout)


class AWS_AppMesh_VirtualNode_ListenerTls(CloudFormationProperty):
  def write(self, w):
    with w.block("listener_tls"):
      self.property(w, "Mode", "mode", StringValueConverter())
      self.block(w, "Certificate", AWS_AppMesh_VirtualNode_ListenerTlsCertificate)


class AWS_AppMesh_VirtualService_VirtualServiceSpec(CloudFormationProperty):
  def write(self, w):
    with w.block("virtual_service_spec"):
      self.block(w, "Provider", AWS_AppMesh_VirtualService_VirtualServiceProvider)


class AWS_AppMesh_Route_HttpRouteHeader(CloudFormationProperty):
  def write(self, w):
    with w.block("http_route_header"):
      self.property(w, "Invert", "invert", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "Match", AWS_AppMesh_Route_HeaderMatchMethod)


class AWS_AppMesh_Route_GrpcRouteMetadata(CloudFormationProperty):
  def write(self, w):
    with w.block("grpc_route_metadata"):
      self.property(w, "Invert", "invert", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "Match", AWS_AppMesh_Route_GrpcRouteMetadataMatchMethod)


class AWS_AppMesh_Route_HttpRouteMatch(CloudFormationProperty):
  def write(self, w):
    with w.block("http_route_match"):
      self.property(w, "Scheme", "scheme", StringValueConverter())
      self.repeated_block(w, "Headers", AWS_AppMesh_Route_HttpRouteHeader)
      self.property(w, "Prefix", "prefix", StringValueConverter())
      self.property(w, "Method", "method", StringValueConverter())


class AWS_AppMesh_VirtualNode_TlsValidationContext(CloudFormationProperty):
  def write(self, w):
    with w.block("tls_validation_context"):
      self.block(w, "Trust", AWS_AppMesh_VirtualNode_TlsValidationContextTrust)


class AWS_AppMesh_Route_GrpcRouteMatch(CloudFormationProperty):
  def write(self, w):
    with w.block("grpc_route_match"):
      self.property(w, "ServiceName", "service_name", StringValueConverter())
      self.repeated_block(w, "Metadata", AWS_AppMesh_Route_GrpcRouteMetadata)
      self.property(w, "MethodName", "method_name", StringValueConverter())


class AWS_AppMesh_VirtualNode_Listener(CloudFormationProperty):
  def write(self, w):
    with w.block("listener"):
      self.block(w, "Timeout", AWS_AppMesh_VirtualNode_ListenerTimeout)
      self.block(w, "HealthCheck", AWS_AppMesh_VirtualNode_HealthCheck)
      self.block(w, "TLS", AWS_AppMesh_VirtualNode_ListenerTls)
      self.block(w, "PortMapping", AWS_AppMesh_VirtualNode_PortMapping)


class AWS_AppMesh_Route_HttpRoute(CloudFormationProperty):
  def write(self, w):
    with w.block("http_route"):
      self.block(w, "Action", AWS_AppMesh_Route_HttpRouteAction)
      self.block(w, "Timeout", AWS_AppMesh_Route_HttpTimeout)
      self.block(w, "RetryPolicy", AWS_AppMesh_Route_HttpRetryPolicy)
      self.block(w, "Match", AWS_AppMesh_Route_HttpRouteMatch)


class AWS_AppMesh_VirtualService(CloudFormationResource):
  cfn_type = "AWS::AppMesh::VirtualService"
  tf_type = "aws_appmesh_virtual_service"
  ref = "id"
  attrs = {
    "Uid": "id",
    "MeshName": "mesh_name", # TODO: Probably not the correct mapping
    "MeshOwner": "mesh_owner", # TODO: Probably not the correct mapping
    "ResourceOwner": "resource_owner", # TODO: Probably not the correct mapping
    "VirtualServiceName": "virtual_service_name", # TODO: Probably not the correct mapping
    "Arn": "arn",
    # Additional TF attributes: created_date, last_updated_date
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "MeshName", "mesh_name", StringValueConverter())
      self.property(w, "MeshOwner", "mesh_owner", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "VirtualServiceName", "name", StringValueConverter())
      self.block(w, "Spec", AWS_AppMesh_VirtualService_VirtualServiceSpec)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_AppMesh_Mesh(CloudFormationResource):
  cfn_type = "AWS::AppMesh::Mesh"
  tf_type = "aws_appmesh_mesh"
  ref = "id"
  attrs = {
    "Uid": "id",
    "MeshName": "mesh_name", # TODO: Probably not the correct mapping
    "MeshOwner": "mesh_owner", # TODO: Probably not the correct mapping
    "ResourceOwner": "resource_owner", # TODO: Probably not the correct mapping
    "Arn": "arn",
    # Additional TF attributes: created_date, last_updated_date
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "MeshName", "name", StringValueConverter())
      self.block(w, "Spec", AWS_AppMesh_Mesh_MeshSpec)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_AppMesh_VirtualNode_ClientPolicyTls(CloudFormationProperty):
  def write(self, w):
    with w.block("client_policy_tls"):
      self.block(w, "Validation", AWS_AppMesh_VirtualNode_TlsValidationContext)
      self.property(w, "Enforce", "enforce", BasicValueConverter())
      self.property(w, "Ports", "ports", ListValueConverter(BasicValueConverter()))


class AWS_AppMesh_Route_GrpcRoute(CloudFormationProperty):
  def write(self, w):
    with w.block("grpc_route"):
      self.block(w, "Action", AWS_AppMesh_Route_GrpcRouteAction)
      self.block(w, "Timeout", AWS_AppMesh_Route_GrpcTimeout)
      self.block(w, "RetryPolicy", AWS_AppMesh_Route_GrpcRetryPolicy)
      self.block(w, "Match", AWS_AppMesh_Route_GrpcRouteMatch)


class AWS_AppMesh_VirtualNode_ClientPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("client_policy"):
      self.block(w, "TLS", AWS_AppMesh_VirtualNode_ClientPolicyTls)


class AWS_AppMesh_Route_RouteSpec(CloudFormationProperty):
  def write(self, w):
    with w.block("route_spec"):
      self.block(w, "HttpRoute", AWS_AppMesh_Route_HttpRoute)
      self.property(w, "Priority", "priority", BasicValueConverter())
      self.block(w, "Http2Route", AWS_AppMesh_Route_HttpRoute)
      self.block(w, "GrpcRoute", AWS_AppMesh_Route_GrpcRoute)
      self.block(w, "TcpRoute", AWS_AppMesh_Route_TcpRoute)


class AWS_AppMesh_VirtualNode_VirtualServiceBackend(CloudFormationProperty):
  def write(self, w):
    with w.block("virtual_service_backend"):
      self.block(w, "ClientPolicy", AWS_AppMesh_VirtualNode_ClientPolicy)
      self.property(w, "VirtualServiceName", "virtual_service_name", StringValueConverter())


class AWS_AppMesh_VirtualNode_BackendDefaults(CloudFormationProperty):
  def write(self, w):
    with w.block("backend_defaults"):
      self.block(w, "ClientPolicy", AWS_AppMesh_VirtualNode_ClientPolicy)


class AWS_AppMesh_Route(CloudFormationResource):
  cfn_type = "AWS::AppMesh::Route"
  tf_type = "aws_appmesh_route"
  ref = "id"
  attrs = {
    "Uid": "id",
    "MeshName": "mesh_name", # TODO: Probably not the correct mapping
    "VirtualRouterName": "virtual_router_name", # TODO: Probably not the correct mapping
    "MeshOwner": "mesh_owner", # TODO: Probably not the correct mapping
    "ResourceOwner": "resource_owner", # TODO: Probably not the correct mapping
    "RouteName": "route_name", # TODO: Probably not the correct mapping
    "Arn": "arn",
    # Additional TF attributes: created_date, last_updated_date
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "MeshName", "mesh_name", StringValueConverter())
      self.property(w, "VirtualRouterName", "virtual_router_name", StringValueConverter())
      self.property(w, "MeshOwner", "mesh_owner", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "RouteName", "name", StringValueConverter())
      self.block(w, "Spec", AWS_AppMesh_Route_RouteSpec)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_AppMesh_VirtualNode_Backend(CloudFormationProperty):
  def write(self, w):
    with w.block("backend"):
      self.block(w, "VirtualService", AWS_AppMesh_VirtualNode_VirtualServiceBackend)


class AWS_AppMesh_VirtualNode_VirtualNodeSpec(CloudFormationProperty):
  def write(self, w):
    with w.block("virtual_node_spec"):
      self.block(w, "Logging", AWS_AppMesh_VirtualNode_Logging)
      self.repeated_block(w, "Backends", AWS_AppMesh_VirtualNode_Backend)
      self.repeated_block(w, "Listeners", AWS_AppMesh_VirtualNode_Listener)
      self.block(w, "BackendDefaults", AWS_AppMesh_VirtualNode_BackendDefaults)
      self.block(w, "ServiceDiscovery", AWS_AppMesh_VirtualNode_ServiceDiscovery)


class AWS_AppMesh_VirtualNode(CloudFormationResource):
  cfn_type = "AWS::AppMesh::VirtualNode"
  tf_type = "aws_appmesh_virtual_node"
  ref = "id"
  attrs = {
    "Uid": "id",
    "MeshName": "mesh_name", # TODO: Probably not the correct mapping
    "MeshOwner": "mesh_owner", # TODO: Probably not the correct mapping
    "ResourceOwner": "resource_owner", # TODO: Probably not the correct mapping
    "Arn": "arn",
    "VirtualNodeName": "virtual_node_name", # TODO: Probably not the correct mapping
    # Additional TF attributes: created_date, last_updated_date
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "MeshName", "mesh_name", StringValueConverter())
      self.property(w, "MeshOwner", "mesh_owner", StringValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "Spec", AWS_AppMesh_VirtualNode_VirtualNodeSpec)
      self.property(w, "VirtualNodeName", "name", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


