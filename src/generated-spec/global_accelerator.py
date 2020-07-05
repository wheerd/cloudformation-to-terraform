from . import *

class AWS_GlobalAccelerator_EndpointGroup_EndpointConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("endpoint_configuration"):
      self.property(w, "EndpointId", "endpoint_id", StringValueConverter())
      self.property(w, "Weight", "weight", BasicValueConverter())
      self.property(w, "ClientIPPreservationEnabled", "client_ip_preservation_enabled", BasicValueConverter())


class AWS_GlobalAccelerator_Listener_PortRange(CloudFormationProperty):
  def write(self, w):
    with w.block("port_range"):
      self.property(w, "FromPort", "from_port", BasicValueConverter())
      self.property(w, "ToPort", "to_port", BasicValueConverter())


class AWS_GlobalAccelerator_Accelerator(CloudFormationResource):
  cfn_type = "AWS::GlobalAccelerator::Accelerator"
  tf_type = "aws_globalaccelerator_accelerator"
  ref = "id"
  attrs = {
    "DnsName": "dns_name",
    "AcceleratorArn": "accelerator_arn", # TODO: Probably not the correct mapping
    # Additional TF attributes: hosted_zone_id, ip_sets
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "IpAddressType", "ip_address_type", StringValueConverter())
      self.property(w, "IpAddresses", "ip_addresses", ListValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_GlobalAccelerator_Listener(CloudFormationResource):
  cfn_type = "AWS::GlobalAccelerator::Listener"
  tf_type = "aws_globalaccelerator_listener"
  ref = "id"
  attrs = {
    "ListenerArn": "listener_arn", # TODO: Probably not the correct mapping
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AcceleratorArn", "accelerator_arn", StringValueConverter())
      self.repeated_block(w, "PortRanges", AWS_GlobalAccelerator_Listener_PortRange)
      self.property(w, "Protocol", "protocol", StringValueConverter())
      self.property(w, "ClientAffinity", "client_affinity", StringValueConverter())


class AWS_GlobalAccelerator_EndpointGroup(CloudFormationResource):
  cfn_type = "AWS::GlobalAccelerator::EndpointGroup"
  tf_type = "aws_globalaccelerator_endpoint_group"
  ref = "id"
  attrs = {
    "EndpointGroupArn": "endpoint_group_arn", # TODO: Probably not the correct mapping
    # Additional TF attributes: endpoint_group_region
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ListenerArn", "listener_arn", StringValueConverter())
      self.property(w, "EndpointGroupRegion", "endpoint_group_region", StringValueConverter())
      self.repeated_block(w, "EndpointConfigurations", AWS_GlobalAccelerator_EndpointGroup_EndpointConfiguration)
      self.property(w, "TrafficDialPercentage", "traffic_dial_percentage", BasicValueConverter())
      self.property(w, "HealthCheckPort", "health_check_port", BasicValueConverter())
      self.property(w, "HealthCheckProtocol", "health_check_protocol", StringValueConverter())
      self.property(w, "HealthCheckPath", "health_check_path", StringValueConverter())
      self.property(w, "HealthCheckIntervalSeconds", "health_check_interval_seconds", BasicValueConverter())
      self.property(w, "ThresholdCount", "threshold_count", BasicValueConverter())


