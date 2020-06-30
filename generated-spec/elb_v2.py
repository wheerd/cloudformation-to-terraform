from . import *

class AWS_ElasticLoadBalancingV2_ListenerCertificate_Certificate(CloudFormationProperty):
  def write(self, w):
    with w.block("certificate"):
      self.property(w, "CertificateArn", "certificate_arn", StringValueConverter())


class AWS_ElasticLoadBalancingV2_TargetGroup_TargetGroupAttribute(CloudFormationProperty):
  def write(self, w):
    with w.block("target_group_attribute"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_ElasticLoadBalancingV2_Listener_AuthenticateCognitoConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("authenticate_cognito_config"):
      self.property(w, "AuthenticationRequestExtraParams", "authentication_request_extra_params", MapValueConverter(StringValueConverter()))
      self.property(w, "OnUnauthenticatedRequest", "on_unauthenticated_request", StringValueConverter())
      self.property(w, "Scope", "scope", StringValueConverter())
      self.property(w, "SessionCookieName", "session_cookie_name", StringValueConverter())
      self.property(w, "SessionTimeout", "session_timeout", BasicValueConverter())
      self.property(w, "UserPoolArn", "user_pool_arn", StringValueConverter())
      self.property(w, "UserPoolClientId", "user_pool_client_id", StringValueConverter())
      self.property(w, "UserPoolDomain", "user_pool_domain", StringValueConverter())


class AWS_ElasticLoadBalancingV2_ListenerRule_SourceIpConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("source_ip_config"):
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_ElasticLoadBalancingV2_ListenerRule_AuthenticateOidcConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("authenticate_oidc_config"):
      self.property(w, "AuthenticationRequestExtraParams", "authentication_request_extra_params", MapValueConverter(StringValueConverter()))
      self.property(w, "AuthorizationEndpoint", "authorization_endpoint", StringValueConverter())
      self.property(w, "ClientId", "client_id", StringValueConverter())
      self.property(w, "ClientSecret", "client_secret", StringValueConverter())
      self.property(w, "Issuer", "issuer", StringValueConverter())
      self.property(w, "OnUnauthenticatedRequest", "on_unauthenticated_request", StringValueConverter())
      self.property(w, "Scope", "scope", StringValueConverter())
      self.property(w, "SessionCookieName", "session_cookie_name", StringValueConverter())
      self.property(w, "SessionTimeout", "session_timeout", BasicValueConverter())
      self.property(w, "TokenEndpoint", "token_endpoint", StringValueConverter())
      self.property(w, "UserInfoEndpoint", "user_info_endpoint", StringValueConverter())


class AWS_ElasticLoadBalancingV2_ListenerRule_AuthenticateCognitoConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("authenticate_cognito_config"):
      self.property(w, "AuthenticationRequestExtraParams", "authentication_request_extra_params", MapValueConverter(StringValueConverter()))
      self.property(w, "OnUnauthenticatedRequest", "on_unauthenticated_request", StringValueConverter())
      self.property(w, "Scope", "scope", StringValueConverter())
      self.property(w, "SessionCookieName", "session_cookie_name", StringValueConverter())
      self.property(w, "SessionTimeout", "session_timeout", BasicValueConverter())
      self.property(w, "UserPoolArn", "user_pool_arn", StringValueConverter())
      self.property(w, "UserPoolClientId", "user_pool_client_id", StringValueConverter())
      self.property(w, "UserPoolDomain", "user_pool_domain", StringValueConverter())


class AWS_ElasticLoadBalancingV2_ListenerRule_FixedResponseConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("fixed_response_config"):
      self.property(w, "ContentType", "content_type", StringValueConverter())
      self.property(w, "MessageBody", "message_body", StringValueConverter())
      self.property(w, "StatusCode", "status_code", StringValueConverter())


class AWS_ElasticLoadBalancingV2_ListenerRule_QueryStringKeyValue(CloudFormationProperty):
  def write(self, w):
    with w.block("query_string_key_value"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_ElasticLoadBalancingV2_ListenerRule_QueryStringConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("query_string_config"):
      self.repeated_block(w, "Values", AWS_ElasticLoadBalancingV2_ListenerRule_QueryStringKeyValue)


class AWS_ElasticLoadBalancingV2_ListenerRule_PathPatternConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("path_pattern_config"):
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_ElasticLoadBalancingV2_LoadBalancer_LoadBalancerAttribute(CloudFormationProperty):
  def write(self, w):
    with w.block("load_balancer_attribute"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_ElasticLoadBalancingV2_TargetGroup_Matcher(CloudFormationProperty):
  def write(self, w):
    with w.block("matcher"):
      self.property(w, "HttpCode", "http_code", StringValueConverter())


class AWS_ElasticLoadBalancingV2_TargetGroup_TargetDescription(CloudFormationProperty):
  def write(self, w):
    with w.block("target_description"):
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())


class AWS_ElasticLoadBalancingV2_ListenerRule_HttpHeaderConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("http_header_config"):
      self.property(w, "HttpHeaderName", "http_header_name", StringValueConverter())
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_ElasticLoadBalancingV2_ListenerRule_TargetGroupTuple(CloudFormationProperty):
  def write(self, w):
    with w.block("target_group_tuple"):
      self.property(w, "TargetGroupArn", "target_group_arn", StringValueConverter())
      self.property(w, "Weight", "weight", BasicValueConverter())


class AWS_ElasticLoadBalancingV2_Listener_AuthenticateOidcConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("authenticate_oidc_config"):
      self.property(w, "AuthenticationRequestExtraParams", "authentication_request_extra_params", MapValueConverter(StringValueConverter()))
      self.property(w, "AuthorizationEndpoint", "authorization_endpoint", StringValueConverter())
      self.property(w, "ClientId", "client_id", StringValueConverter())
      self.property(w, "ClientSecret", "client_secret", StringValueConverter())
      self.property(w, "Issuer", "issuer", StringValueConverter())
      self.property(w, "OnUnauthenticatedRequest", "on_unauthenticated_request", StringValueConverter())
      self.property(w, "Scope", "scope", StringValueConverter())
      self.property(w, "SessionCookieName", "session_cookie_name", StringValueConverter())
      self.property(w, "SessionTimeout", "session_timeout", BasicValueConverter())
      self.property(w, "TokenEndpoint", "token_endpoint", StringValueConverter())
      self.property(w, "UserInfoEndpoint", "user_info_endpoint", StringValueConverter())


class AWS_ElasticLoadBalancingV2_Listener_RedirectConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("redirect_config"):
      self.property(w, "Host", "host", StringValueConverter())
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "Port", "port", StringValueConverter())
      self.property(w, "Protocol", "protocol", StringValueConverter())
      self.property(w, "Query", "query", StringValueConverter())
      self.property(w, "StatusCode", "status_code", StringValueConverter())


class AWS_ElasticLoadBalancingV2_ListenerRule_HttpRequestMethodConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("http_request_method_config"):
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_ElasticLoadBalancingV2_Listener_FixedResponseConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("fixed_response_config"):
      self.property(w, "ContentType", "content_type", StringValueConverter())
      self.property(w, "MessageBody", "message_body", StringValueConverter())
      self.property(w, "StatusCode", "status_code", StringValueConverter())


class AWS_ElasticLoadBalancingV2_Listener_Certificate(CloudFormationProperty):
  def write(self, w):
    with w.block("certificate"):
      self.property(w, "CertificateArn", "certificate_arn", StringValueConverter())


class AWS_ElasticLoadBalancingV2_ListenerRule_RedirectConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("redirect_config"):
      self.property(w, "Host", "host", StringValueConverter())
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "Port", "port", StringValueConverter())
      self.property(w, "Protocol", "protocol", StringValueConverter())
      self.property(w, "Query", "query", StringValueConverter())
      self.property(w, "StatusCode", "status_code", StringValueConverter())


class AWS_ElasticLoadBalancingV2_ListenerRule_TargetGroupStickinessConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("target_group_stickiness_config"):
      self.property(w, "DurationSeconds", "duration_seconds", BasicValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())


class AWS_ElasticLoadBalancingV2_LoadBalancer_SubnetMapping(CloudFormationProperty):
  def write(self, w):
    with w.block("subnet_mapping"):
      self.property(w, "AllocationId", "allocation_id", StringValueConverter())
      self.property(w, "PrivateIPv4Address", "private_i_pv4_address", StringValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())


class AWS_ElasticLoadBalancingV2_ListenerRule_HostHeaderConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("host_header_config"):
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_ElasticLoadBalancingV2_Listener_TargetGroupStickinessConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("target_group_stickiness_config"):
      self.property(w, "DurationSeconds", "duration_seconds", BasicValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())


class AWS_ElasticLoadBalancingV2_Listener_TargetGroupTuple(CloudFormationProperty):
  def write(self, w):
    with w.block("target_group_tuple"):
      self.property(w, "TargetGroupArn", "target_group_arn", StringValueConverter())
      self.property(w, "Weight", "weight", BasicValueConverter())


class AWS_ElasticLoadBalancingV2_LoadBalancer(CloudFormationResource):
  cfn_type = "AWS::ElasticLoadBalancingV2::LoadBalancer"
  tf_type = "aws_elb_v2_load_balancer" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "CanonicalHostedZoneID": "canonical_hosted_zone_id",
    "DNSName": "dns_name",
    "LoadBalancerFullName": "load_balancer_full_name",
    "LoadBalancerName": "load_balancer_name",
    "SecurityGroups": "security_groups",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "IpAddressType", "ip_address_type", StringValueConverter())
      self.repeated_block(w, "LoadBalancerAttributes", AWS_ElasticLoadBalancingV2_LoadBalancer_LoadBalancerAttribute)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Scheme", "scheme", StringValueConverter())
      self.property(w, "SecurityGroups", "security_groups", ListValueConverter(StringValueConverter()))
      self.repeated_block(w, "SubnetMappings", AWS_ElasticLoadBalancingV2_LoadBalancer_SubnetMapping)
      self.property(w, "Subnets", "subnets", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Type", "type", StringValueConverter())


class AWS_ElasticLoadBalancingV2_ListenerCertificate(CloudFormationResource):
  cfn_type = "AWS::ElasticLoadBalancingV2::ListenerCertificate"
  tf_type = "aws_lb_listener_certificate"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "Certificates", AWS_ElasticLoadBalancingV2_ListenerCertificate_Certificate) # TODO: Probably not the correct mapping
      self.property(w, "ListenerArn", "listener_arn", StringValueConverter())


class AWS_ElasticLoadBalancingV2_TargetGroup(CloudFormationResource):
  cfn_type = "AWS::ElasticLoadBalancingV2::TargetGroup"
  tf_type = "aws_lb_target_group"
  ref = "id"
  attrs = {
    "LoadBalancerArns": "arn",
    "TargetGroupFullName": "name",
    "TargetGroupName": "target_group_name", # TODO: Probably not the correct mapping
    # Additional TF attributes: arn_suffix, load_balancing_algorithm_type
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "HealthCheckEnabled", "health_check", BasicValueConverter())
      self.property(w, "HealthCheckIntervalSeconds", "health_check_interval_seconds", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "HealthCheckPath", "health_check_path", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "HealthCheckPort", "health_check_port", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "HealthCheckProtocol", "protocol", StringValueConverter())
      self.property(w, "HealthCheckTimeoutSeconds", "health_check_timeout_seconds", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "HealthyThresholdCount", "healthy_threshold_count", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "Matcher", AWS_ElasticLoadBalancingV2_TargetGroup_Matcher) # TODO: Probably not the correct mapping
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "Protocol", "proxy_protocol_v2", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.repeated_block(w, "TargetGroupAttributes", AWS_ElasticLoadBalancingV2_TargetGroup_TargetGroupAttribute) # TODO: Probably not the correct mapping
      self.property(w, "TargetType", "target_type", StringValueConverter())
      self.repeated_block(w, "Targets", AWS_ElasticLoadBalancingV2_TargetGroup_TargetDescription) # TODO: Probably not the correct mapping
      self.property(w, "UnhealthyThresholdCount", "unhealthy_threshold_count", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "VpcId", "vpc_id", StringValueConverter())


class AWS_ElasticLoadBalancingV2_Listener_ForwardConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("forward_config"):
      self.block(w, "TargetGroupStickinessConfig", AWS_ElasticLoadBalancingV2_Listener_TargetGroupStickinessConfig)
      self.repeated_block(w, "TargetGroups", AWS_ElasticLoadBalancingV2_Listener_TargetGroupTuple)


class AWS_ElasticLoadBalancingV2_ListenerRule_ForwardConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("forward_config"):
      self.block(w, "TargetGroupStickinessConfig", AWS_ElasticLoadBalancingV2_ListenerRule_TargetGroupStickinessConfig)
      self.repeated_block(w, "TargetGroups", AWS_ElasticLoadBalancingV2_ListenerRule_TargetGroupTuple)


class AWS_ElasticLoadBalancingV2_ListenerRule_RuleCondition(CloudFormationProperty):
  def write(self, w):
    with w.block("rule_condition"):
      self.property(w, "Field", "field", StringValueConverter())
      self.block(w, "HostHeaderConfig", AWS_ElasticLoadBalancingV2_ListenerRule_HostHeaderConfig)
      self.block(w, "HttpHeaderConfig", AWS_ElasticLoadBalancingV2_ListenerRule_HttpHeaderConfig)
      self.block(w, "HttpRequestMethodConfig", AWS_ElasticLoadBalancingV2_ListenerRule_HttpRequestMethodConfig)
      self.block(w, "PathPatternConfig", AWS_ElasticLoadBalancingV2_ListenerRule_PathPatternConfig)
      self.block(w, "QueryStringConfig", AWS_ElasticLoadBalancingV2_ListenerRule_QueryStringConfig)
      self.block(w, "SourceIpConfig", AWS_ElasticLoadBalancingV2_ListenerRule_SourceIpConfig)
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_ElasticLoadBalancingV2_Listener_Action(CloudFormationProperty):
  def write(self, w):
    with w.block("action"):
      self.block(w, "AuthenticateCognitoConfig", AWS_ElasticLoadBalancingV2_Listener_AuthenticateCognitoConfig)
      self.block(w, "AuthenticateOidcConfig", AWS_ElasticLoadBalancingV2_Listener_AuthenticateOidcConfig)
      self.block(w, "FixedResponseConfig", AWS_ElasticLoadBalancingV2_Listener_FixedResponseConfig)
      self.block(w, "ForwardConfig", AWS_ElasticLoadBalancingV2_Listener_ForwardConfig)
      self.property(w, "Order", "order", BasicValueConverter())
      self.block(w, "RedirectConfig", AWS_ElasticLoadBalancingV2_Listener_RedirectConfig)
      self.property(w, "TargetGroupArn", "target_group_arn", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_ElasticLoadBalancingV2_ListenerRule_Action(CloudFormationProperty):
  def write(self, w):
    with w.block("action"):
      self.block(w, "AuthenticateCognitoConfig", AWS_ElasticLoadBalancingV2_ListenerRule_AuthenticateCognitoConfig)
      self.block(w, "AuthenticateOidcConfig", AWS_ElasticLoadBalancingV2_ListenerRule_AuthenticateOidcConfig)
      self.block(w, "FixedResponseConfig", AWS_ElasticLoadBalancingV2_ListenerRule_FixedResponseConfig)
      self.block(w, "ForwardConfig", AWS_ElasticLoadBalancingV2_ListenerRule_ForwardConfig)
      self.property(w, "Order", "order", BasicValueConverter())
      self.block(w, "RedirectConfig", AWS_ElasticLoadBalancingV2_ListenerRule_RedirectConfig)
      self.property(w, "TargetGroupArn", "target_group_arn", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_ElasticLoadBalancingV2_Listener(CloudFormationResource):
  cfn_type = "AWS::ElasticLoadBalancingV2::Listener"
  tf_type = "aws_lb_listener"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, ssl_policy

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "Certificates", AWS_ElasticLoadBalancingV2_Listener_Certificate) # TODO: Probably not the correct mapping
      self.repeated_block(w, "DefaultActions", AWS_ElasticLoadBalancingV2_Listener_Action)
      self.property(w, "LoadBalancerArn", "load_balancer_arn", StringValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "Protocol", "protocol", StringValueConverter())
      self.property(w, "SslPolicy", "ssl_policy", StringValueConverter())


class AWS_ElasticLoadBalancingV2_ListenerRule(CloudFormationResource):
  cfn_type = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_type = "aws_lb_listener_rule"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, priority

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "Actions", AWS_ElasticLoadBalancingV2_ListenerRule_Action)
      self.repeated_block(w, "Conditions", AWS_ElasticLoadBalancingV2_ListenerRule_RuleCondition)
      self.property(w, "ListenerArn", "listener_arn", StringValueConverter())
      self.property(w, "Priority", "priority", BasicValueConverter())


