from . import *

class AWS_ServiceDiscovery_Service_HealthCheckCustomConfig(CloudFormationProperty):
  entity = "AWS::ServiceDiscovery::Service"
  tf_block_type = "health_check_custom_config"

  props = {
    "FailureThreshold": (BasicValueConverter(), "failure_threshold"),
  }

class AWS_ServiceDiscovery_Service_DnsRecord(CloudFormationProperty):
  entity = "AWS::ServiceDiscovery::Service"
  tf_block_type = "dns_record"

  props = {
    "Type": (StringValueConverter(), "type"),
    "TTL": (BasicValueConverter(), "ttl"),
  }

class AWS_ServiceDiscovery_Service_HealthCheckConfig(CloudFormationProperty):
  entity = "AWS::ServiceDiscovery::Service"
  tf_block_type = "health_check_config"

  props = {
    "Type": (StringValueConverter(), "type"),
    "ResourcePath": (StringValueConverter(), "resource_path"),
    "FailureThreshold": (BasicValueConverter(), "failure_threshold"),
  }

class AWS_ServiceDiscovery_Instance(CloudFormationResource):
  terraform_resource = "aws_service_discovery_instance"

  resource_type = "AWS::ServiceDiscovery::Instance"

  props = {
    "InstanceAttributes": (StringValueConverter(), "instance_attributes"),
    "InstanceId": (StringValueConverter(), "instance_id"),
    "ServiceId": (StringValueConverter(), "service_id"),
  }

class AWS_ServiceDiscovery_HttpNamespace(CloudFormationResource):
  terraform_resource = "aws_service_discovery_http_namespace"

  resource_type = "AWS::ServiceDiscovery::HttpNamespace"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_ServiceDiscovery_PrivateDnsNamespace(CloudFormationResource):
  terraform_resource = "aws_service_discovery_private_dns_namespace"

  resource_type = "AWS::ServiceDiscovery::PrivateDnsNamespace"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Vpc": (StringValueConverter(), "vpc"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_ServiceDiscovery_PublicDnsNamespace(CloudFormationResource):
  terraform_resource = "aws_service_discovery_public_dns_namespace"

  resource_type = "AWS::ServiceDiscovery::PublicDnsNamespace"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_ServiceDiscovery_Service_DnsConfig(CloudFormationProperty):
  entity = "AWS::ServiceDiscovery::Service"
  tf_block_type = "dns_config"

  props = {
    "DnsRecords": (BlockValueConverter(AWS_ServiceDiscovery_Service_DnsRecord), None),
    "RoutingPolicy": (StringValueConverter(), "routing_policy"),
    "NamespaceId": (StringValueConverter(), "namespace_id"),
  }

class AWS_ServiceDiscovery_Service(CloudFormationResource):
  terraform_resource = "aws_service_discovery_service"

  resource_type = "AWS::ServiceDiscovery::Service"

  props = {
    "Description": (StringValueConverter(), "description"),
    "HealthCheckCustomConfig": (AWS_ServiceDiscovery_Service_HealthCheckCustomConfig, "health_check_custom_config"),
    "DnsConfig": (AWS_ServiceDiscovery_Service_DnsConfig, "dns_config"),
    "NamespaceId": (StringValueConverter(), "namespace_id"),
    "HealthCheckConfig": (AWS_ServiceDiscovery_Service_HealthCheckConfig, "health_check_config"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

