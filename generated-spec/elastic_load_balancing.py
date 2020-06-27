from . import *

class AWS_ElasticLoadBalancing_LoadBalancer_AccessLoggingPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("access_logging_policy"):
      self.property(w, "EmitInterval", "emit_interval", BasicValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "S3BucketName", "s3_bucket_name", StringValueConverter())
      self.property(w, "S3BucketPrefix", "s3_bucket_prefix", StringValueConverter())


class AWS_ElasticLoadBalancing_LoadBalancer_LBCookieStickinessPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("lb_cookie_stickiness_policy"):
      self.property(w, "CookieExpirationPeriod", "cookie_expiration_period", StringValueConverter())
      self.property(w, "PolicyName", "policy_name", StringValueConverter())


class AWS_ElasticLoadBalancing_LoadBalancer_Listeners(CloudFormationProperty):
  def write(self, w):
    with w.block("listeners"):
      self.property(w, "InstancePort", "instance_port", StringValueConverter())
      self.property(w, "InstanceProtocol", "instance_protocol", StringValueConverter())
      self.property(w, "LoadBalancerPort", "load_balancer_port", StringValueConverter())
      self.property(w, "PolicyNames", "policy_names", ListValueConverter(StringValueConverter()))
      self.property(w, "Protocol", "protocol", StringValueConverter())
      self.property(w, "SSLCertificateId", "ssl_certificate_id", StringValueConverter())


class AWS_ElasticLoadBalancing_LoadBalancer_HealthCheck(CloudFormationProperty):
  def write(self, w):
    with w.block("health_check"):
      self.property(w, "HealthyThreshold", "healthy_threshold", StringValueConverter())
      self.property(w, "Interval", "interval", StringValueConverter())
      self.property(w, "Target", "target", StringValueConverter())
      self.property(w, "Timeout", "timeout", StringValueConverter())
      self.property(w, "UnhealthyThreshold", "unhealthy_threshold", StringValueConverter())


class AWS_ElasticLoadBalancing_LoadBalancer_ConnectionSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("connection_settings"):
      self.property(w, "IdleTimeout", "idle_timeout", BasicValueConverter())


class AWS_ElasticLoadBalancing_LoadBalancer_ConnectionDrainingPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("connection_draining_policy"):
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "Timeout", "timeout", BasicValueConverter())


class AWS_ElasticLoadBalancing_LoadBalancer_Policies(CloudFormationProperty):
  def write(self, w):
    with w.block("policies"):
      self.property(w, "Attributes", "attributes", ListValueConverter(StringValueConverter()))
      self.property(w, "InstancePorts", "instance_ports", ListValueConverter(StringValueConverter()))
      self.property(w, "LoadBalancerPorts", "load_balancer_ports", ListValueConverter(StringValueConverter()))
      self.property(w, "PolicyName", "policy_name", StringValueConverter())
      self.property(w, "PolicyType", "policy_type", StringValueConverter())


class AWS_ElasticLoadBalancing_LoadBalancer_AppCookieStickinessPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("app_cookie_stickiness_policy"):
      self.property(w, "CookieName", "cookie_name", StringValueConverter())
      self.property(w, "PolicyName", "policy_name", StringValueConverter())


class AWS_ElasticLoadBalancing_LoadBalancer(CloudFormationResource):
  cfn_type = "AWS::ElasticLoadBalancing::LoadBalancer"
  tf_type = "aws_elastic_load_balancing_load_balancer"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "AccessLoggingPolicy", AWS_ElasticLoadBalancing_LoadBalancer_AccessLoggingPolicy)
      self.repeated_block(w, "AppCookieStickinessPolicy", AWS_ElasticLoadBalancing_LoadBalancer_AppCookieStickinessPolicy)
      self.property(w, "AvailabilityZones", "availability_zones", ListValueConverter(StringValueConverter()))
      self.block(w, "ConnectionDrainingPolicy", AWS_ElasticLoadBalancing_LoadBalancer_ConnectionDrainingPolicy)
      self.block(w, "ConnectionSettings", AWS_ElasticLoadBalancing_LoadBalancer_ConnectionSettings)
      self.property(w, "CrossZone", "cross_zone", BasicValueConverter())
      self.block(w, "HealthCheck", AWS_ElasticLoadBalancing_LoadBalancer_HealthCheck)
      self.property(w, "Instances", "instances", ListValueConverter(StringValueConverter()))
      self.repeated_block(w, "LBCookieStickinessPolicy", AWS_ElasticLoadBalancing_LoadBalancer_LBCookieStickinessPolicy)
      self.repeated_block(w, "Listeners", AWS_ElasticLoadBalancing_LoadBalancer_Listeners)
      self.property(w, "LoadBalancerName", "load_balancer_name", StringValueConverter())
      self.repeated_block(w, "Policies", AWS_ElasticLoadBalancing_LoadBalancer_Policies)
      self.property(w, "Scheme", "scheme", StringValueConverter())
      self.property(w, "SecurityGroups", "security_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "Subnets", "subnets", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


