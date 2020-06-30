from . import *

class AWS_ServiceDiscovery_Service_HealthCheckCustomConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("health_check_custom_config"):
      self.property(w, "FailureThreshold", "failure_threshold", BasicValueConverter())


class AWS_ServiceDiscovery_Service_DnsRecord(CloudFormationProperty):
  def write(self, w):
    with w.block("dns_record"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "TTL", "ttl", BasicValueConverter())


class AWS_ServiceDiscovery_Service_HealthCheckConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("health_check_config"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "ResourcePath", "resource_path", StringValueConverter())
      self.property(w, "FailureThreshold", "failure_threshold", BasicValueConverter())


class AWS_ServiceDiscovery_Instance(CloudFormationResource):
  cfn_type = "AWS::ServiceDiscovery::Instance"
  tf_type = "aws_service_discovery_instance" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "InstanceAttributes", "instance_attributes", JsonValueConverter())
      self.property(w, "InstanceId", "instance_id", StringValueConverter())
      self.property(w, "ServiceId", "service_id", StringValueConverter())


class AWS_ServiceDiscovery_HttpNamespace(CloudFormationResource):
  cfn_type = "AWS::ServiceDiscovery::HttpNamespace"
  tf_type = "aws_service_discovery_http_namespace"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


class AWS_ServiceDiscovery_PrivateDnsNamespace(CloudFormationResource):
  cfn_type = "AWS::ServiceDiscovery::PrivateDnsNamespace"
  tf_type = "aws_service_discovery_private_dns_namespace"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Vpc", "vpc", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


class AWS_ServiceDiscovery_PublicDnsNamespace(CloudFormationResource):
  cfn_type = "AWS::ServiceDiscovery::PublicDnsNamespace"
  tf_type = "aws_service_discovery_public_dns_namespace"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


class AWS_ServiceDiscovery_Service_DnsConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("dns_config"):
      self.repeated_block(w, "DnsRecords", AWS_ServiceDiscovery_Service_DnsRecord)
      self.property(w, "RoutingPolicy", "routing_policy", StringValueConverter())
      self.property(w, "NamespaceId", "namespace_id", StringValueConverter())


class AWS_ServiceDiscovery_Service(CloudFormationResource):
  cfn_type = "AWS::ServiceDiscovery::Service"
  tf_type = "aws_service_discovery_service"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "HealthCheckCustomConfig", AWS_ServiceDiscovery_Service_HealthCheckCustomConfig)
      self.block(w, "DnsConfig", AWS_ServiceDiscovery_Service_DnsConfig)
      self.property(w, "NamespaceId", "namespace_id", StringValueConverter())
      self.block(w, "HealthCheckConfig", AWS_ServiceDiscovery_Service_HealthCheckConfig)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


