from . import *

class AWS_ElasticLoadBalancingV2_ListenerCertificate_Certificate(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerCertificate"
  tf_block_type = "certificate"

  props = {
    "CertificateArn": (StringValueConverter(), "certificate_arn"),
  }

class AWS_ElasticLoadBalancingV2_TargetGroup_TargetGroupAttribute(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::TargetGroup"
  tf_block_type = "target_group_attribute"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_ElasticLoadBalancingV2_Listener_AuthenticateCognitoConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::Listener"
  tf_block_type = "authenticate_cognito_config"

  props = {
    "AuthenticationRequestExtraParams": (MapValueConverter(StringValueConverter()), "authentication_request_extra_params"),
    "OnUnauthenticatedRequest": (StringValueConverter(), "on_unauthenticated_request"),
    "Scope": (StringValueConverter(), "scope"),
    "SessionCookieName": (StringValueConverter(), "session_cookie_name"),
    "SessionTimeout": (BasicValueConverter(), "session_timeout"),
    "UserPoolArn": (StringValueConverter(), "user_pool_arn"),
    "UserPoolClientId": (StringValueConverter(), "user_pool_client_id"),
    "UserPoolDomain": (StringValueConverter(), "user_pool_domain"),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_SourceIpConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "source_ip_config"

  props = {
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_AuthenticateOidcConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "authenticate_oidc_config"

  props = {
    "AuthenticationRequestExtraParams": (MapValueConverter(StringValueConverter()), "authentication_request_extra_params"),
    "AuthorizationEndpoint": (StringValueConverter(), "authorization_endpoint"),
    "ClientId": (StringValueConverter(), "client_id"),
    "ClientSecret": (StringValueConverter(), "client_secret"),
    "Issuer": (StringValueConverter(), "issuer"),
    "OnUnauthenticatedRequest": (StringValueConverter(), "on_unauthenticated_request"),
    "Scope": (StringValueConverter(), "scope"),
    "SessionCookieName": (StringValueConverter(), "session_cookie_name"),
    "SessionTimeout": (BasicValueConverter(), "session_timeout"),
    "TokenEndpoint": (StringValueConverter(), "token_endpoint"),
    "UserInfoEndpoint": (StringValueConverter(), "user_info_endpoint"),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_AuthenticateCognitoConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "authenticate_cognito_config"

  props = {
    "AuthenticationRequestExtraParams": (MapValueConverter(StringValueConverter()), "authentication_request_extra_params"),
    "OnUnauthenticatedRequest": (StringValueConverter(), "on_unauthenticated_request"),
    "Scope": (StringValueConverter(), "scope"),
    "SessionCookieName": (StringValueConverter(), "session_cookie_name"),
    "SessionTimeout": (BasicValueConverter(), "session_timeout"),
    "UserPoolArn": (StringValueConverter(), "user_pool_arn"),
    "UserPoolClientId": (StringValueConverter(), "user_pool_client_id"),
    "UserPoolDomain": (StringValueConverter(), "user_pool_domain"),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_FixedResponseConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "fixed_response_config"

  props = {
    "ContentType": (StringValueConverter(), "content_type"),
    "MessageBody": (StringValueConverter(), "message_body"),
    "StatusCode": (StringValueConverter(), "status_code"),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_QueryStringKeyValue(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "query_string_key_value"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_QueryStringConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "query_string_config"

  props = {
    "Values": (BlockValueConverter(AWS_ElasticLoadBalancingV2_ListenerRule_QueryStringKeyValue), None),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_PathPatternConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "path_pattern_config"

  props = {
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_ElasticLoadBalancingV2_LoadBalancer_LoadBalancerAttribute(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::LoadBalancer"
  tf_block_type = "load_balancer_attribute"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_ElasticLoadBalancingV2_TargetGroup_Matcher(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::TargetGroup"
  tf_block_type = "matcher"

  props = {
    "HttpCode": (StringValueConverter(), "http_code"),
  }

class AWS_ElasticLoadBalancingV2_TargetGroup_TargetDescription(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::TargetGroup"
  tf_block_type = "target_description"

  props = {
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "Id": (StringValueConverter(), "id"),
    "Port": (BasicValueConverter(), "port"),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_HttpHeaderConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "http_header_config"

  props = {
    "HttpHeaderName": (StringValueConverter(), "http_header_name"),
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_TargetGroupTuple(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "target_group_tuple"

  props = {
    "TargetGroupArn": (StringValueConverter(), "target_group_arn"),
    "Weight": (BasicValueConverter(), "weight"),
  }

class AWS_ElasticLoadBalancingV2_Listener_AuthenticateOidcConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::Listener"
  tf_block_type = "authenticate_oidc_config"

  props = {
    "AuthenticationRequestExtraParams": (MapValueConverter(StringValueConverter()), "authentication_request_extra_params"),
    "AuthorizationEndpoint": (StringValueConverter(), "authorization_endpoint"),
    "ClientId": (StringValueConverter(), "client_id"),
    "ClientSecret": (StringValueConverter(), "client_secret"),
    "Issuer": (StringValueConverter(), "issuer"),
    "OnUnauthenticatedRequest": (StringValueConverter(), "on_unauthenticated_request"),
    "Scope": (StringValueConverter(), "scope"),
    "SessionCookieName": (StringValueConverter(), "session_cookie_name"),
    "SessionTimeout": (BasicValueConverter(), "session_timeout"),
    "TokenEndpoint": (StringValueConverter(), "token_endpoint"),
    "UserInfoEndpoint": (StringValueConverter(), "user_info_endpoint"),
  }

class AWS_ElasticLoadBalancingV2_Listener_RedirectConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::Listener"
  tf_block_type = "redirect_config"

  props = {
    "Host": (StringValueConverter(), "host"),
    "Path": (StringValueConverter(), "path"),
    "Port": (StringValueConverter(), "port"),
    "Protocol": (StringValueConverter(), "protocol"),
    "Query": (StringValueConverter(), "query"),
    "StatusCode": (StringValueConverter(), "status_code"),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_HttpRequestMethodConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "http_request_method_config"

  props = {
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_ElasticLoadBalancingV2_Listener_FixedResponseConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::Listener"
  tf_block_type = "fixed_response_config"

  props = {
    "ContentType": (StringValueConverter(), "content_type"),
    "MessageBody": (StringValueConverter(), "message_body"),
    "StatusCode": (StringValueConverter(), "status_code"),
  }

class AWS_ElasticLoadBalancingV2_Listener_Certificate(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::Listener"
  tf_block_type = "certificate"

  props = {
    "CertificateArn": (StringValueConverter(), "certificate_arn"),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_RedirectConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "redirect_config"

  props = {
    "Host": (StringValueConverter(), "host"),
    "Path": (StringValueConverter(), "path"),
    "Port": (StringValueConverter(), "port"),
    "Protocol": (StringValueConverter(), "protocol"),
    "Query": (StringValueConverter(), "query"),
    "StatusCode": (StringValueConverter(), "status_code"),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_TargetGroupStickinessConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "target_group_stickiness_config"

  props = {
    "DurationSeconds": (BasicValueConverter(), "duration_seconds"),
    "Enabled": (BasicValueConverter(), "enabled"),
  }

class AWS_ElasticLoadBalancingV2_LoadBalancer_SubnetMapping(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::LoadBalancer"
  tf_block_type = "subnet_mapping"

  props = {
    "AllocationId": (StringValueConverter(), "allocation_id"),
    "PrivateIPv4Address": (StringValueConverter(), "private_i_pv4_address"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_HostHeaderConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "host_header_config"

  props = {
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_ElasticLoadBalancingV2_Listener_TargetGroupStickinessConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::Listener"
  tf_block_type = "target_group_stickiness_config"

  props = {
    "DurationSeconds": (BasicValueConverter(), "duration_seconds"),
    "Enabled": (BasicValueConverter(), "enabled"),
  }

class AWS_ElasticLoadBalancingV2_Listener_TargetGroupTuple(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::Listener"
  tf_block_type = "target_group_tuple"

  props = {
    "TargetGroupArn": (StringValueConverter(), "target_group_arn"),
    "Weight": (BasicValueConverter(), "weight"),
  }

class AWS_ElasticLoadBalancingV2_LoadBalancer(CloudFormationResource):
  terraform_resource = "aws_elastic_load_balancing_v2_load_balancer"

  resource_type = "AWS::ElasticLoadBalancingV2::LoadBalancer"

  props = {
    "IpAddressType": (StringValueConverter(), "ip_address_type"),
    "LoadBalancerAttributes": (BlockValueConverter(AWS_ElasticLoadBalancingV2_LoadBalancer_LoadBalancerAttribute), None),
    "Name": (StringValueConverter(), "name"),
    "Scheme": (StringValueConverter(), "scheme"),
    "SecurityGroups": (ListValueConverter(StringValueConverter()), "security_groups"),
    "SubnetMappings": (BlockValueConverter(AWS_ElasticLoadBalancingV2_LoadBalancer_SubnetMapping), None),
    "Subnets": (ListValueConverter(StringValueConverter()), "subnets"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_ElasticLoadBalancingV2_ListenerCertificate(CloudFormationResource):
  terraform_resource = "aws_elastic_load_balancing_v2_listener_certificate"

  resource_type = "AWS::ElasticLoadBalancingV2::ListenerCertificate"

  props = {
    "Certificates": (BlockValueConverter(AWS_ElasticLoadBalancingV2_ListenerCertificate_Certificate), None),
    "ListenerArn": (StringValueConverter(), "listener_arn"),
  }

class AWS_ElasticLoadBalancingV2_TargetGroup(CloudFormationResource):
  terraform_resource = "aws_elastic_load_balancing_v2_target_group"

  resource_type = "AWS::ElasticLoadBalancingV2::TargetGroup"

  props = {
    "HealthCheckEnabled": (BasicValueConverter(), "health_check_enabled"),
    "HealthCheckIntervalSeconds": (BasicValueConverter(), "health_check_interval_seconds"),
    "HealthCheckPath": (StringValueConverter(), "health_check_path"),
    "HealthCheckPort": (StringValueConverter(), "health_check_port"),
    "HealthCheckProtocol": (StringValueConverter(), "health_check_protocol"),
    "HealthCheckTimeoutSeconds": (BasicValueConverter(), "health_check_timeout_seconds"),
    "HealthyThresholdCount": (BasicValueConverter(), "healthy_threshold_count"),
    "Matcher": (AWS_ElasticLoadBalancingV2_TargetGroup_Matcher, "matcher"),
    "Name": (StringValueConverter(), "name"),
    "Port": (BasicValueConverter(), "port"),
    "Protocol": (StringValueConverter(), "protocol"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "TargetGroupAttributes": (BlockValueConverter(AWS_ElasticLoadBalancingV2_TargetGroup_TargetGroupAttribute), None),
    "TargetType": (StringValueConverter(), "target_type"),
    "Targets": (BlockValueConverter(AWS_ElasticLoadBalancingV2_TargetGroup_TargetDescription), None),
    "UnhealthyThresholdCount": (BasicValueConverter(), "unhealthy_threshold_count"),
    "VpcId": (StringValueConverter(), "vpc_id"),
  }

class AWS_ElasticLoadBalancingV2_Listener_ForwardConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::Listener"
  tf_block_type = "forward_config"

  props = {
    "TargetGroupStickinessConfig": (AWS_ElasticLoadBalancingV2_Listener_TargetGroupStickinessConfig, "target_group_stickiness_config"),
    "TargetGroups": (BlockValueConverter(AWS_ElasticLoadBalancingV2_Listener_TargetGroupTuple), None),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_ForwardConfig(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "forward_config"

  props = {
    "TargetGroupStickinessConfig": (AWS_ElasticLoadBalancingV2_ListenerRule_TargetGroupStickinessConfig, "target_group_stickiness_config"),
    "TargetGroups": (BlockValueConverter(AWS_ElasticLoadBalancingV2_ListenerRule_TargetGroupTuple), None),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_RuleCondition(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "rule_condition"

  props = {
    "Field": (StringValueConverter(), "field"),
    "HostHeaderConfig": (AWS_ElasticLoadBalancingV2_ListenerRule_HostHeaderConfig, "host_header_config"),
    "HttpHeaderConfig": (AWS_ElasticLoadBalancingV2_ListenerRule_HttpHeaderConfig, "http_header_config"),
    "HttpRequestMethodConfig": (AWS_ElasticLoadBalancingV2_ListenerRule_HttpRequestMethodConfig, "http_request_method_config"),
    "PathPatternConfig": (AWS_ElasticLoadBalancingV2_ListenerRule_PathPatternConfig, "path_pattern_config"),
    "QueryStringConfig": (AWS_ElasticLoadBalancingV2_ListenerRule_QueryStringConfig, "query_string_config"),
    "SourceIpConfig": (AWS_ElasticLoadBalancingV2_ListenerRule_SourceIpConfig, "source_ip_config"),
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_ElasticLoadBalancingV2_Listener_Action(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::Listener"
  tf_block_type = "action"

  props = {
    "AuthenticateCognitoConfig": (AWS_ElasticLoadBalancingV2_Listener_AuthenticateCognitoConfig, "authenticate_cognito_config"),
    "AuthenticateOidcConfig": (AWS_ElasticLoadBalancingV2_Listener_AuthenticateOidcConfig, "authenticate_oidc_config"),
    "FixedResponseConfig": (AWS_ElasticLoadBalancingV2_Listener_FixedResponseConfig, "fixed_response_config"),
    "ForwardConfig": (AWS_ElasticLoadBalancingV2_Listener_ForwardConfig, "forward_config"),
    "Order": (BasicValueConverter(), "order"),
    "RedirectConfig": (AWS_ElasticLoadBalancingV2_Listener_RedirectConfig, "redirect_config"),
    "TargetGroupArn": (StringValueConverter(), "target_group_arn"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule_Action(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancingV2::ListenerRule"
  tf_block_type = "action"

  props = {
    "AuthenticateCognitoConfig": (AWS_ElasticLoadBalancingV2_ListenerRule_AuthenticateCognitoConfig, "authenticate_cognito_config"),
    "AuthenticateOidcConfig": (AWS_ElasticLoadBalancingV2_ListenerRule_AuthenticateOidcConfig, "authenticate_oidc_config"),
    "FixedResponseConfig": (AWS_ElasticLoadBalancingV2_ListenerRule_FixedResponseConfig, "fixed_response_config"),
    "ForwardConfig": (AWS_ElasticLoadBalancingV2_ListenerRule_ForwardConfig, "forward_config"),
    "Order": (BasicValueConverter(), "order"),
    "RedirectConfig": (AWS_ElasticLoadBalancingV2_ListenerRule_RedirectConfig, "redirect_config"),
    "TargetGroupArn": (StringValueConverter(), "target_group_arn"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_ElasticLoadBalancingV2_Listener(CloudFormationResource):
  terraform_resource = "aws_elastic_load_balancing_v2_listener"

  resource_type = "AWS::ElasticLoadBalancingV2::Listener"

  props = {
    "Certificates": (BlockValueConverter(AWS_ElasticLoadBalancingV2_Listener_Certificate), None),
    "DefaultActions": (BlockValueConverter(AWS_ElasticLoadBalancingV2_Listener_Action), None),
    "LoadBalancerArn": (StringValueConverter(), "load_balancer_arn"),
    "Port": (BasicValueConverter(), "port"),
    "Protocol": (StringValueConverter(), "protocol"),
    "SslPolicy": (StringValueConverter(), "ssl_policy"),
  }

class AWS_ElasticLoadBalancingV2_ListenerRule(CloudFormationResource):
  terraform_resource = "aws_elastic_load_balancing_v2_listener_rule"

  resource_type = "AWS::ElasticLoadBalancingV2::ListenerRule"

  props = {
    "Actions": (BlockValueConverter(AWS_ElasticLoadBalancingV2_ListenerRule_Action), None),
    "Conditions": (BlockValueConverter(AWS_ElasticLoadBalancingV2_ListenerRule_RuleCondition), None),
    "ListenerArn": (StringValueConverter(), "listener_arn"),
    "Priority": (BasicValueConverter(), "priority"),
  }

