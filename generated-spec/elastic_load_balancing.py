from . import *

class AWS_ElasticLoadBalancing_LoadBalancer_AccessLoggingPolicy(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancing::LoadBalancer"
  tf_block_type = "access_logging_policy"

  props = {
    "EmitInterval": (BasicValueConverter(), "emit_interval"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "S3BucketName": (StringValueConverter(), "s3_bucket_name"),
    "S3BucketPrefix": (StringValueConverter(), "s3_bucket_prefix"),
  }

class AWS_ElasticLoadBalancing_LoadBalancer_LBCookieStickinessPolicy(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancing::LoadBalancer"
  tf_block_type = "lb_cookie_stickiness_policy"

  props = {
    "CookieExpirationPeriod": (StringValueConverter(), "cookie_expiration_period"),
    "PolicyName": (StringValueConverter(), "policy_name"),
  }

class AWS_ElasticLoadBalancing_LoadBalancer_Listeners(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancing::LoadBalancer"
  tf_block_type = "listeners"

  props = {
    "InstancePort": (StringValueConverter(), "instance_port"),
    "InstanceProtocol": (StringValueConverter(), "instance_protocol"),
    "LoadBalancerPort": (StringValueConverter(), "load_balancer_port"),
    "PolicyNames": (ListValueConverter(StringValueConverter()), "policy_names"),
    "Protocol": (StringValueConverter(), "protocol"),
    "SSLCertificateId": (StringValueConverter(), "ssl_certificate_id"),
  }

class AWS_ElasticLoadBalancing_LoadBalancer_HealthCheck(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancing::LoadBalancer"
  tf_block_type = "health_check"

  props = {
    "HealthyThreshold": (StringValueConverter(), "healthy_threshold"),
    "Interval": (StringValueConverter(), "interval"),
    "Target": (StringValueConverter(), "target"),
    "Timeout": (StringValueConverter(), "timeout"),
    "UnhealthyThreshold": (StringValueConverter(), "unhealthy_threshold"),
  }

class AWS_ElasticLoadBalancing_LoadBalancer_ConnectionSettings(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancing::LoadBalancer"
  tf_block_type = "connection_settings"

  props = {
    "IdleTimeout": (BasicValueConverter(), "idle_timeout"),
  }

class AWS_ElasticLoadBalancing_LoadBalancer_ConnectionDrainingPolicy(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancing::LoadBalancer"
  tf_block_type = "connection_draining_policy"

  props = {
    "Enabled": (BasicValueConverter(), "enabled"),
    "Timeout": (BasicValueConverter(), "timeout"),
  }

class AWS_ElasticLoadBalancing_LoadBalancer_Policies(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancing::LoadBalancer"
  tf_block_type = "policies"

  props = {
    "Attributes": (ListValueConverter(StringValueConverter()), "attributes"),
    "InstancePorts": (ListValueConverter(StringValueConverter()), "instance_ports"),
    "LoadBalancerPorts": (ListValueConverter(StringValueConverter()), "load_balancer_ports"),
    "PolicyName": (StringValueConverter(), "policy_name"),
    "PolicyType": (StringValueConverter(), "policy_type"),
  }

class AWS_ElasticLoadBalancing_LoadBalancer_AppCookieStickinessPolicy(CloudFormationProperty):
  entity = "AWS::ElasticLoadBalancing::LoadBalancer"
  tf_block_type = "app_cookie_stickiness_policy"

  props = {
    "CookieName": (StringValueConverter(), "cookie_name"),
    "PolicyName": (StringValueConverter(), "policy_name"),
  }

class AWS_ElasticLoadBalancing_LoadBalancer(CloudFormationResource):
  terraform_resource = "aws_elastic_load_balancing_load_balancer"

  resource_type = "AWS::ElasticLoadBalancing::LoadBalancer"

  props = {
    "AccessLoggingPolicy": (AWS_ElasticLoadBalancing_LoadBalancer_AccessLoggingPolicy, "access_logging_policy"),
    "AppCookieStickinessPolicy": (BlockValueConverter(AWS_ElasticLoadBalancing_LoadBalancer_AppCookieStickinessPolicy), None),
    "AvailabilityZones": (ListValueConverter(StringValueConverter()), "availability_zones"),
    "ConnectionDrainingPolicy": (AWS_ElasticLoadBalancing_LoadBalancer_ConnectionDrainingPolicy, "connection_draining_policy"),
    "ConnectionSettings": (AWS_ElasticLoadBalancing_LoadBalancer_ConnectionSettings, "connection_settings"),
    "CrossZone": (BasicValueConverter(), "cross_zone"),
    "HealthCheck": (AWS_ElasticLoadBalancing_LoadBalancer_HealthCheck, "health_check"),
    "Instances": (ListValueConverter(StringValueConverter()), "instances"),
    "LBCookieStickinessPolicy": (BlockValueConverter(AWS_ElasticLoadBalancing_LoadBalancer_LBCookieStickinessPolicy), None),
    "Listeners": (BlockValueConverter(AWS_ElasticLoadBalancing_LoadBalancer_Listeners), None),
    "LoadBalancerName": (StringValueConverter(), "load_balancer_name"),
    "Policies": (BlockValueConverter(AWS_ElasticLoadBalancing_LoadBalancer_Policies), None),
    "Scheme": (StringValueConverter(), "scheme"),
    "SecurityGroups": (ListValueConverter(StringValueConverter()), "security_groups"),
    "Subnets": (ListValueConverter(StringValueConverter()), "subnets"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

