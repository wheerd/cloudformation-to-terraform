from . import *

class AWS_GlobalAccelerator_EndpointGroup_EndpointConfiguration(CloudFormationProperty):
  entity = "AWS::GlobalAccelerator::EndpointGroup"
  tf_block_type = "endpoint_configuration"

  props = {
    "EndpointId": (StringValueConverter(), "endpoint_id"),
    "Weight": (BasicValueConverter(), "weight"),
    "ClientIPPreservationEnabled": (BasicValueConverter(), "client_ip_preservation_enabled"),
  }

class AWS_GlobalAccelerator_Listener_PortRange(CloudFormationProperty):
  entity = "AWS::GlobalAccelerator::Listener"
  tf_block_type = "port_range"

  props = {
    "FromPort": (BasicValueConverter(), "from_port"),
    "ToPort": (BasicValueConverter(), "to_port"),
  }

class AWS_GlobalAccelerator_Accelerator(CloudFormationResource):
  terraform_resource = "aws_global_accelerator_accelerator"

  resource_type = "AWS::GlobalAccelerator::Accelerator"

  props = {
    "Name": (StringValueConverter(), "name"),
    "IpAddressType": (StringValueConverter(), "ip_address_type"),
    "IpAddresses": (ListValueConverter(StringValueConverter()), "ip_addresses"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_GlobalAccelerator_Listener(CloudFormationResource):
  terraform_resource = "aws_global_accelerator_listener"

  resource_type = "AWS::GlobalAccelerator::Listener"

  props = {
    "AcceleratorArn": (StringValueConverter(), "accelerator_arn"),
    "PortRanges": (BlockValueConverter(AWS_GlobalAccelerator_Listener_PortRange), None),
    "Protocol": (StringValueConverter(), "protocol"),
    "ClientAffinity": (StringValueConverter(), "client_affinity"),
  }

class AWS_GlobalAccelerator_EndpointGroup(CloudFormationResource):
  terraform_resource = "aws_global_accelerator_endpoint_group"

  resource_type = "AWS::GlobalAccelerator::EndpointGroup"

  props = {
    "ListenerArn": (StringValueConverter(), "listener_arn"),
    "EndpointGroupRegion": (StringValueConverter(), "endpoint_group_region"),
    "EndpointConfigurations": (BlockValueConverter(AWS_GlobalAccelerator_EndpointGroup_EndpointConfiguration), None),
    "TrafficDialPercentage": (BasicValueConverter(), "traffic_dial_percentage"),
    "HealthCheckPort": (BasicValueConverter(), "health_check_port"),
    "HealthCheckProtocol": (StringValueConverter(), "health_check_protocol"),
    "HealthCheckPath": (StringValueConverter(), "health_check_path"),
    "HealthCheckIntervalSeconds": (BasicValueConverter(), "health_check_interval_seconds"),
    "ThresholdCount": (BasicValueConverter(), "threshold_count"),
  }

