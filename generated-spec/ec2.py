from . import *

class AWS_EC2_LaunchTemplate_PrivateIpAdd(CloudFormationProperty):
  def write(self, w):
    with w.block("private_ip_add"):
      self.property(w, "PrivateIpAddress", "private_ip_address", StringValueConverter())
      self.property(w, "Primary", "primary", BasicValueConverter())


class AWS_EC2_SpotFleet_SpotFleetTagSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("spot_fleet_tag_specification"):
      self.property(w, "ResourceType", "resource_type", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_SpotFleet_PrivateIpAddressSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("private_ip_address_specification"):
      self.property(w, "Primary", "primary", BasicValueConverter())
      self.property(w, "PrivateIpAddress", "private_ip_address", StringValueConverter())


class AWS_EC2_EC2Fleet_FleetLaunchTemplateSpecificationRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("fleet_launch_template_specification_request"):
      self.property(w, "LaunchTemplateName", "launch_template_name", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())
      self.property(w, "LaunchTemplateId", "launch_template_id", StringValueConverter())


class AWS_EC2_VPNConnection_VpnTunnelOptionsSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("vpn_tunnel_options_specification"):
      self.property(w, "PreSharedKey", "pre_shared_key", StringValueConverter())
      self.property(w, "TunnelInsideCidr", "tunnel_inside_cidr", StringValueConverter())


class AWS_EC2_TrafficMirrorFilterRule_TrafficMirrorPortRange(CloudFormationProperty):
  def write(self, w):
    with w.block("traffic_mirror_port_range"):
      self.property(w, "FromPort", "from_port", BasicValueConverter())
      self.property(w, "ToPort", "to_port", BasicValueConverter())


class AWS_EC2_LaunchTemplate_SpotOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("spot_options"):
      self.property(w, "SpotInstanceType", "spot_instance_type", StringValueConverter())
      self.property(w, "InstanceInterruptionBehavior", "instance_interruption_behavior", StringValueConverter())
      self.property(w, "MaxPrice", "max_price", StringValueConverter())
      self.property(w, "BlockDurationMinutes", "block_duration_minutes", BasicValueConverter())
      self.property(w, "ValidUntil", "valid_until", StringValueConverter())


class AWS_EC2_Instance_HibernationOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("hibernation_options"):
      self.property(w, "Configured", "configured", BasicValueConverter())


class AWS_EC2_SpotFleet_SpotPlacement(CloudFormationProperty):
  def write(self, w):
    with w.block("spot_placement"):
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "GroupName", "group_name", StringValueConverter())
      self.property(w, "Tenancy", "tenancy", StringValueConverter())


class AWS_EC2_NetworkInterface_InstanceIpv6Address(CloudFormationProperty):
  def write(self, w):
    with w.block("instance_ipv6_address"):
      self.property(w, "Ipv6Address", "ipv6_address", StringValueConverter())


class AWS_EC2_SpotFleet_EbsBlockDevice(CloudFormationProperty):
  def write(self, w):
    with w.block("ebs_block_device"):
      self.property(w, "DeleteOnTermination", "delete_on_termination", BasicValueConverter())
      self.property(w, "Encrypted", "encrypted", BasicValueConverter())
      self.property(w, "Iops", "iops", BasicValueConverter())
      self.property(w, "SnapshotId", "snapshot_id", StringValueConverter())
      self.property(w, "VolumeSize", "volume_size", BasicValueConverter())
      self.property(w, "VolumeType", "volume_type", StringValueConverter())


class AWS_EC2_SpotFleet_FleetLaunchTemplateSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("fleet_launch_template_specification"):
      self.property(w, "LaunchTemplateId", "launch_template_id", StringValueConverter())
      self.property(w, "LaunchTemplateName", "launch_template_name", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())


class AWS_EC2_Instance_Volume(CloudFormationProperty):
  def write(self, w):
    with w.block("volume"):
      self.property(w, "Device", "device", StringValueConverter())
      self.property(w, "VolumeId", "volume_id", StringValueConverter())


class AWS_EC2_NetworkAclEntry_PortRange(CloudFormationProperty):
  def write(self, w):
    with w.block("port_range"):
      self.property(w, "From", "from", BasicValueConverter())
      self.property(w, "To", "to", BasicValueConverter())


class AWS_EC2_LocalGatewayRouteTableVPCAssociation_Tags(CloudFormationProperty):
  def write(self, w):
    with w.block("tags"):
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_LaunchTemplate_ElasticGpuSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("elastic_gpu_specification"):
      self.property(w, "Type", "type", StringValueConverter())


class AWS_EC2_SpotFleet_TargetGroup(CloudFormationProperty):
  def write(self, w):
    with w.block("target_group"):
      self.property(w, "Arn", "arn", StringValueConverter())


class AWS_EC2_NetworkInterface_PrivateIpAddressSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("private_ip_address_specification"):
      self.property(w, "Primary", "primary", BasicValueConverter())
      self.property(w, "PrivateIpAddress", "private_ip_address", StringValueConverter())


class AWS_EC2_ClientVpnEndpoint_ConnectionLogOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("connection_log_options"):
      self.property(w, "CloudwatchLogStream", "cloudwatch_log_stream", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "CloudwatchLogGroup", "cloudwatch_log_group", StringValueConverter())


class AWS_EC2_Instance_Ebs(CloudFormationProperty):
  def write(self, w):
    with w.block("ebs"):
      self.property(w, "DeleteOnTermination", "delete_on_termination", BasicValueConverter())
      self.property(w, "Encrypted", "encrypted", BasicValueConverter())
      self.property(w, "Iops", "iops", BasicValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "SnapshotId", "snapshot_id", StringValueConverter())
      self.property(w, "VolumeSize", "volume_size", BasicValueConverter())
      self.property(w, "VolumeType", "volume_type", StringValueConverter())


class AWS_EC2_LaunchTemplate_TagSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("tag_specification"):
      self.property(w, "ResourceType", "resource_type", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_LaunchTemplate_IamInstanceProfile(CloudFormationProperty):
  def write(self, w):
    with w.block("iam_instance_profile"):
      self.property(w, "Arn", "arn", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_EC2_Instance_NoDevice(CloudFormationProperty):
  def write(self, w):
    with w.block("no_device"):
      pass


class AWS_EC2_Instance_CreditSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("credit_specification"):
      self.property(w, "CPUCredits", "cpu_credits", StringValueConverter())


class AWS_EC2_EC2Fleet_TargetCapacitySpecificationRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("target_capacity_specification_request"):
      self.property(w, "DefaultTargetCapacityType", "default_target_capacity_type", StringValueConverter())
      self.property(w, "TotalTargetCapacity", "total_target_capacity", BasicValueConverter())
      self.property(w, "OnDemandTargetCapacity", "on_demand_target_capacity", BasicValueConverter())
      self.property(w, "SpotTargetCapacity", "spot_target_capacity", BasicValueConverter())


class AWS_EC2_LaunchTemplate_LicenseSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("license_specification"):
      self.property(w, "LicenseConfigurationArn", "license_configuration_arn", StringValueConverter())


class AWS_EC2_SecurityGroup_Egress(CloudFormationProperty):
  def write(self, w):
    with w.block("egress"):
      self.property(w, "CidrIp", "cidr_ip", StringValueConverter())
      self.property(w, "CidrIpv6", "cidr_ipv6", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DestinationPrefixListId", "destination_prefix_list_id", StringValueConverter())
      self.property(w, "DestinationSecurityGroupId", "destination_security_group_id", StringValueConverter())
      self.property(w, "FromPort", "from_port", BasicValueConverter())
      self.property(w, "IpProtocol", "ip_protocol", StringValueConverter())
      self.property(w, "ToPort", "to_port", BasicValueConverter())


class AWS_EC2_SpotFleet_LaunchTemplateOverrides(CloudFormationProperty):
  def write(self, w):
    with w.block("launch_template_overrides"):
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "SpotPrice", "spot_price", StringValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())
      self.property(w, "WeightedCapacity", "weighted_capacity", BasicValueConverter())


class AWS_EC2_LaunchTemplate_Ebs(CloudFormationProperty):
  def write(self, w):
    with w.block("ebs"):
      self.property(w, "SnapshotId", "snapshot_id", StringValueConverter())
      self.property(w, "VolumeType", "volume_type", StringValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "Encrypted", "encrypted", BasicValueConverter())
      self.property(w, "Iops", "iops", BasicValueConverter())
      self.property(w, "VolumeSize", "volume_size", BasicValueConverter())
      self.property(w, "DeleteOnTermination", "delete_on_termination", BasicValueConverter())


class AWS_EC2_SpotFleet_SpotFleetMonitoring(CloudFormationProperty):
  def write(self, w):
    with w.block("spot_fleet_monitoring"):
      self.property(w, "Enabled", "enabled", BasicValueConverter())


class AWS_EC2_LaunchTemplate_HibernationOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("hibernation_options"):
      self.property(w, "Configured", "configured", BasicValueConverter())


class AWS_EC2_ClientVpnEndpoint_CertificateAuthenticationRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("certificate_authentication_request"):
      self.property(w, "ClientRootCertificateChainArn", "client_root_certificate_chain_arn", StringValueConverter())


class AWS_EC2_ClientVpnEndpoint_DirectoryServiceAuthenticationRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("directory_service_authentication_request"):
      self.property(w, "DirectoryId", "directory_id", StringValueConverter())


class AWS_EC2_SecurityGroup_Ingress(CloudFormationProperty):
  def write(self, w):
    with w.block("ingress"):
      self.property(w, "CidrIp", "cidr_ip", StringValueConverter())
      self.property(w, "CidrIpv6", "cidr_ipv6", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "FromPort", "from_port", BasicValueConverter())
      self.property(w, "IpProtocol", "ip_protocol", StringValueConverter())
      self.property(w, "SourcePrefixListId", "source_prefix_list_id", StringValueConverter())
      self.property(w, "SourceSecurityGroupId", "source_security_group_id", StringValueConverter())
      self.property(w, "SourceSecurityGroupName", "source_security_group_name", StringValueConverter())
      self.property(w, "SourceSecurityGroupOwnerId", "source_security_group_owner_id", StringValueConverter())
      self.property(w, "ToPort", "to_port", BasicValueConverter())


class AWS_EC2_SpotFleet_ClassicLoadBalancer(CloudFormationProperty):
  def write(self, w):
    with w.block("classic_load_balancer"):
      self.property(w, "Name", "name", StringValueConverter())


class AWS_EC2_SpotFleet_LaunchTemplateConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("launch_template_config"):
      self.block(w, "LaunchTemplateSpecification", AWS_EC2_SpotFleet_FleetLaunchTemplateSpecification)
      self.repeated_block(w, "Overrides", AWS_EC2_SpotFleet_LaunchTemplateOverrides)


class AWS_EC2_Instance_ElasticGpuSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("elastic_gpu_specification"):
      self.property(w, "Type", "type", StringValueConverter())


class AWS_EC2_NetworkAclEntry_Icmp(CloudFormationProperty):
  def write(self, w):
    with w.block("icmp"):
      self.property(w, "Code", "code", BasicValueConverter())
      self.property(w, "Type", "type", BasicValueConverter())


class AWS_EC2_LaunchTemplate_InstanceMarketOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("instance_market_options"):
      self.block(w, "SpotOptions", AWS_EC2_LaunchTemplate_SpotOptions)
      self.property(w, "MarketType", "market_type", StringValueConverter())


class AWS_EC2_ClientVpnEndpoint_TagSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("tag_specification"):
      self.property(w, "ResourceType", "resource_type", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_LaunchTemplate_CreditSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("credit_specification"):
      self.property(w, "CpuCredits", "cpu_credits", StringValueConverter())


class AWS_EC2_SpotFleet_IamInstanceProfileSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("iam_instance_profile_specification"):
      self.property(w, "Arn", "arn", StringValueConverter())


class AWS_EC2_EC2Fleet_CapacityReservationOptionsRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("capacity_reservation_options_request"):
      self.property(w, "UsageStrategy", "usage_strategy", StringValueConverter())


class AWS_EC2_LaunchTemplate_Monitoring(CloudFormationProperty):
  def write(self, w):
    with w.block("monitoring"):
      self.property(w, "Enabled", "enabled", BasicValueConverter())


class AWS_EC2_LaunchTemplate_MetadataOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("metadata_options"):
      self.property(w, "HttpPutResponseHopLimit", "http_put_response_hop_limit", BasicValueConverter())
      self.property(w, "HttpTokens", "http_tokens", StringValueConverter())
      self.property(w, "HttpEndpoint", "http_endpoint", StringValueConverter())


class AWS_EC2_EC2Fleet_Placement(CloudFormationProperty):
  def write(self, w):
    with w.block("placement"):
      self.property(w, "GroupName", "group_name", StringValueConverter())
      self.property(w, "Tenancy", "tenancy", StringValueConverter())
      self.property(w, "SpreadDomain", "spread_domain", StringValueConverter())
      self.property(w, "PartitionNumber", "partition_number", BasicValueConverter())
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "Affinity", "affinity", StringValueConverter())
      self.property(w, "HostId", "host_id", StringValueConverter())
      self.property(w, "HostResourceGroupArn", "host_resource_group_arn", StringValueConverter())


class AWS_EC2_SpotFleet_ClassicLoadBalancersConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("classic_load_balancers_config"):
      self.repeated_block(w, "ClassicLoadBalancers", AWS_EC2_SpotFleet_ClassicLoadBalancer)


class AWS_EC2_LaunchTemplate_Placement(CloudFormationProperty):
  def write(self, w):
    with w.block("placement"):
      self.property(w, "GroupName", "group_name", StringValueConverter())
      self.property(w, "Tenancy", "tenancy", StringValueConverter())
      self.property(w, "SpreadDomain", "spread_domain", StringValueConverter())
      self.property(w, "PartitionNumber", "partition_number", BasicValueConverter())
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "Affinity", "affinity", StringValueConverter())
      self.property(w, "HostId", "host_id", StringValueConverter())
      self.property(w, "HostResourceGroupArn", "host_resource_group_arn", StringValueConverter())


class AWS_EC2_ClientVpnEndpoint_FederatedAuthenticationRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("federated_authentication_request"):
      self.property(w, "SAMLProviderArn", "saml_provider_arn", StringValueConverter())


class AWS_EC2_Instance_InstanceIpv6Address(CloudFormationProperty):
  def write(self, w):
    with w.block("instance_ipv6_address"):
      self.property(w, "Ipv6Address", "ipv6_address", StringValueConverter())


class AWS_EC2_Instance_AssociationParameter(CloudFormationProperty):
  def write(self, w):
    with w.block("association_parameter"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", ListValueConverter(StringValueConverter()))


class AWS_EC2_Instance_CpuOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("cpu_options"):
      self.property(w, "CoreCount", "core_count", BasicValueConverter())
      self.property(w, "ThreadsPerCore", "threads_per_core", BasicValueConverter())


class AWS_EC2_Instance_LaunchTemplateSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("launch_template_specification"):
      self.property(w, "LaunchTemplateId", "launch_template_id", StringValueConverter())
      self.property(w, "LaunchTemplateName", "launch_template_name", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())


class AWS_EC2_LaunchTemplate_Ipv6Add(CloudFormationProperty):
  def write(self, w):
    with w.block("ipv6_add"):
      self.property(w, "Ipv6Address", "ipv6_address", StringValueConverter())


class AWS_EC2_Instance_LicenseSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("license_specification"):
      self.property(w, "LicenseConfigurationArn", "license_configuration_arn", StringValueConverter())


class AWS_EC2_Instance_SsmAssociation(CloudFormationProperty):
  def write(self, w):
    with w.block("ssm_association"):
      self.repeated_block(w, "AssociationParameters", AWS_EC2_Instance_AssociationParameter)
      self.property(w, "DocumentName", "document_name", StringValueConverter())


class AWS_EC2_LaunchTemplate_CapacityReservationTarget(CloudFormationProperty):
  def write(self, w):
    with w.block("capacity_reservation_target"):
      self.property(w, "CapacityReservationId", "capacity_reservation_id", StringValueConverter())


class AWS_EC2_LaunchTemplate_NetworkInterface(CloudFormationProperty):
  def write(self, w):
    with w.block("network_interface"):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "PrivateIpAddress", "private_ip_address", StringValueConverter())
      self.repeated_block(w, "PrivateIpAddresses", AWS_EC2_LaunchTemplate_PrivateIpAdd)
      self.property(w, "SecondaryPrivateIpAddressCount", "secondary_private_ip_address_count", BasicValueConverter())
      self.property(w, "DeviceIndex", "device_index", BasicValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())
      self.repeated_block(w, "Ipv6Addresses", AWS_EC2_LaunchTemplate_Ipv6Add)
      self.property(w, "AssociatePublicIpAddress", "associate_public_ip_address", BasicValueConverter())
      self.property(w, "NetworkInterfaceId", "network_interface_id", StringValueConverter())
      self.property(w, "InterfaceType", "interface_type", StringValueConverter())
      self.property(w, "Ipv6AddressCount", "ipv6_address_count", BasicValueConverter())
      self.property(w, "Groups", "groups", ListValueConverter(StringValueConverter()))
      self.property(w, "DeleteOnTermination", "delete_on_termination", BasicValueConverter())


class AWS_EC2_SpotFleet_InstanceIpv6Address(CloudFormationProperty):
  def write(self, w):
    with w.block("instance_ipv6_address"):
      self.property(w, "Ipv6Address", "ipv6_address", StringValueConverter())


class AWS_EC2_SpotFleet_TargetGroupsConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("target_groups_config"):
      self.repeated_block(w, "TargetGroups", AWS_EC2_SpotFleet_TargetGroup)


class AWS_EC2_CapacityReservation_TagSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("tag_specification"):
      self.property(w, "ResourceType", "resource_type", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_LaunchTemplate_CpuOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("cpu_options"):
      self.property(w, "ThreadsPerCore", "threads_per_core", BasicValueConverter())
      self.property(w, "CoreCount", "core_count", BasicValueConverter())


class AWS_EC2_Instance_ElasticInferenceAccelerator(CloudFormationProperty):
  def write(self, w):
    with w.block("elastic_inference_accelerator"):
      self.property(w, "Count", "count", BasicValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_EC2_SpotFleet_GroupIdentifier(CloudFormationProperty):
  def write(self, w):
    with w.block("group_identifier"):
      self.property(w, "GroupId", "group_id", StringValueConverter())


class AWS_EC2_Instance_BlockDeviceMapping(CloudFormationProperty):
  def write(self, w):
    with w.block("block_device_mapping"):
      self.property(w, "DeviceName", "device_name", StringValueConverter())
      self.block(w, "Ebs", AWS_EC2_Instance_Ebs)
      self.block(w, "NoDevice", AWS_EC2_Instance_NoDevice)
      self.property(w, "VirtualName", "virtual_name", StringValueConverter())


class AWS_EC2_SpotFleet_BlockDeviceMapping(CloudFormationProperty):
  def write(self, w):
    with w.block("block_device_mapping"):
      self.property(w, "DeviceName", "device_name", StringValueConverter())
      self.block(w, "Ebs", AWS_EC2_SpotFleet_EbsBlockDevice)
      self.property(w, "NoDevice", "no_device", StringValueConverter())
      self.property(w, "VirtualName", "virtual_name", StringValueConverter())


class AWS_EC2_Instance_PrivateIpAddressSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("private_ip_address_specification"):
      self.property(w, "Primary", "primary", BasicValueConverter())
      self.property(w, "PrivateIpAddress", "private_ip_address", StringValueConverter())


class AWS_EC2_EC2Fleet_TagSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("tag_specification"):
      self.property(w, "ResourceType", "resource_type", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_LaunchTemplate_LaunchTemplateElasticInferenceAccelerator(CloudFormationProperty):
  def write(self, w):
    with w.block("launch_template_elastic_inference_accelerator"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Count", "count", BasicValueConverter())


class AWS_EC2_EC2Fleet_SpotOptionsRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("spot_options_request"):
      self.property(w, "SingleAvailabilityZone", "single_availability_zone", BasicValueConverter())
      self.property(w, "AllocationStrategy", "allocation_strategy", StringValueConverter())
      self.property(w, "SingleInstanceType", "single_instance_type", BasicValueConverter())
      self.property(w, "MinTargetCapacity", "min_target_capacity", BasicValueConverter())
      self.property(w, "MaxTotalPrice", "max_total_price", StringValueConverter())
      self.property(w, "InstanceInterruptionBehavior", "instance_interruption_behavior", StringValueConverter())
      self.property(w, "InstancePoolsToUseCount", "instance_pools_to_use_count", BasicValueConverter())


class AWS_EC2_RouteTable(CloudFormationResource):
  cfn_type = "AWS::EC2::RouteTable"
  tf_type = "aws_route_table"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "VpcId", "vpc_id", StringValueConverter())


class AWS_EC2_VPCPeeringConnection(CloudFormationResource):
  cfn_type = "AWS::EC2::VPCPeeringConnection"
  tf_type = "aws_vpc_peering_connection"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PeerOwnerId", "peer_owner_id", StringValueConverter())
      self.property(w, "PeerRegion", "peer_region", StringValueConverter())
      self.property(w, "PeerRoleArn", "peer_role_arn", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "PeerVpcId", "peer_vpc_id", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "VpcId", "vpc_id", StringValueConverter())


class AWS_EC2_TransitGateway(CloudFormationResource):
  cfn_type = "AWS::EC2::TransitGateway"
  tf_type = "aws_ec2_transit_gateway_peering_attachment"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DefaultRouteTablePropagation", "default_route_table_propagation", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Description", "description", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "AutoAcceptSharedAttachments", "auto_accept_shared_attachments", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "DefaultRouteTableAssociation", "default_route_table_association", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "VpnEcmpSupport", "vpn_ecmp_support", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "DnsSupport", "dns_support", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "AmazonSideAsn", "id", BasicValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_CapacityReservation(CloudFormationResource):
  cfn_type = "AWS::EC2::CapacityReservation"
  tf_type = "aws_ec2_capacity_reservation"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Tenancy", "tenancy", StringValueConverter())
      self.property(w, "EndDateType", "end_date_type", StringValueConverter())
      self.property(w, "InstanceCount", "instance_count", BasicValueConverter())
      self.repeated_block(w, "TagSpecifications", AWS_EC2_CapacityReservation_TagSpecification) # TODO: Probably not the correct mapping
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "InstancePlatform", "instance_platform", StringValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "EphemeralStorage", "ephemeral_storage", BasicValueConverter())
      self.property(w, "InstanceMatchCriteria", "instance_match_criteria", StringValueConverter())
      self.property(w, "EndDate", "end_date", StringValueConverter())
      self.property(w, "EbsOptimized", "ebs_optimized", BasicValueConverter())


class AWS_EC2_VPCEndpointServicePermissions(CloudFormationResource):
  cfn_type = "AWS::EC2::VPCEndpointServicePermissions"
  tf_type = "aws_ec2_vpc_endpoint_service_permissions" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AllowedPrincipals", "allowed_principals", ListValueConverter(StringValueConverter()))
      self.property(w, "ServiceId", "service_id", StringValueConverter())


class AWS_EC2_TransitGatewayRouteTableAssociation(CloudFormationResource):
  cfn_type = "AWS::EC2::TransitGatewayRouteTableAssociation"
  tf_type = "aws_ec2_transit_gateway"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "TransitGatewayRouteTableId", "transit_gateway_route_table_id", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "TransitGatewayAttachmentId", "transit_gateway_attachment_id", StringValueConverter()) # TODO: Probably not the correct mapping


class AWS_EC2_Volume(CloudFormationResource):
  cfn_type = "AWS::EC2::Volume"
  tf_type = "aws_ebs_volume"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AutoEnableIO", "auto_enable_io", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "Encrypted", "encrypted", BasicValueConverter())
      self.property(w, "Iops", "iops", BasicValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "MultiAttachEnabled", "multi_attach_enabled", BasicValueConverter())
      self.property(w, "OutpostArn", "outpost_arn", StringValueConverter())
      self.property(w, "Size", "size", BasicValueConverter())
      self.property(w, "SnapshotId", "snapshot_id", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "VolumeType", "type", StringValueConverter())


class AWS_EC2_EIP(CloudFormationResource):
  cfn_type = "AWS::EC2::EIP"
  tf_type = "aws_ec2_eip" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Domain", "domain", StringValueConverter())
      self.property(w, "InstanceId", "instance_id", StringValueConverter())
      self.property(w, "PublicIpv4Pool", "public_ipv4_pool", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_LocalGatewayRoute(CloudFormationResource):
  cfn_type = "AWS::EC2::LocalGatewayRoute"
  tf_type = "aws_ec2_local_gateway_route"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DestinationCidrBlock", "destination_cidr_block", StringValueConverter())
      self.property(w, "LocalGatewayRouteTableId", "local_gateway_route_table_id", StringValueConverter())
      self.property(w, "LocalGatewayVirtualInterfaceGroupId", "local_gateway_virtual_interface_group_id", StringValueConverter())


class AWS_EC2_VPCEndpointConnectionNotification(CloudFormationResource):
  cfn_type = "AWS::EC2::VPCEndpointConnectionNotification"
  tf_type = "aws_vpc_endpoint_connection_notification"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ConnectionEvents", "connection_events", ListValueConverter(StringValueConverter()))
      self.property(w, "VPCEndpointId", "vpc_endpoint_id", StringValueConverter())
      self.property(w, "ServiceId", "id", StringValueConverter())
      self.property(w, "ConnectionNotificationArn", "connection_notification_arn", StringValueConverter())


class AWS_EC2_FlowLog(CloudFormationResource):
  cfn_type = "AWS::EC2::FlowLog"
  tf_type = "aws_flow_log"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DeliverLogsPermissionArn", "deliver_logs_permission_arn", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "LogDestination", "log_destination", StringValueConverter())
      self.property(w, "LogDestinationType", "log_destination_type", StringValueConverter())
      self.property(w, "LogGroupName", "log_group_name", StringValueConverter())
      self.property(w, "ResourceId", "id", StringValueConverter())
      self.property(w, "ResourceType", "resource_type", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "TrafficType", "traffic_type", StringValueConverter())


class AWS_EC2_SecurityGroupEgress(CloudFormationResource):
  cfn_type = "AWS::EC2::SecurityGroupEgress"
  tf_type = "aws_ec2_security_group_egress" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CidrIp", "cidr_ip", StringValueConverter())
      self.property(w, "CidrIpv6", "cidr_ipv6", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DestinationPrefixListId", "destination_prefix_list_id", StringValueConverter())
      self.property(w, "DestinationSecurityGroupId", "destination_security_group_id", StringValueConverter())
      self.property(w, "FromPort", "from_port", BasicValueConverter())
      self.property(w, "GroupId", "group_id", StringValueConverter())
      self.property(w, "IpProtocol", "ip_protocol", StringValueConverter())
      self.property(w, "ToPort", "to_port", BasicValueConverter())


class AWS_EC2_TransitGatewayAttachment(CloudFormationResource):
  cfn_type = "AWS::EC2::TransitGatewayAttachment"
  tf_type = "aws_ec2_transit_gateway_vpc_attachment"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "TransitGatewayId", "transit_gateway_id", StringValueConverter())
      self.property(w, "VpcId", "vpc_id", StringValueConverter())
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_Subnet(CloudFormationResource):
  cfn_type = "AWS::EC2::Subnet"
  tf_type = "aws_ec2_subnet" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AssignIpv6AddressOnCreation", "assign_ipv6_address_on_creation", BasicValueConverter())
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "CidrBlock", "cidr_block", StringValueConverter())
      self.property(w, "Ipv6CidrBlock", "ipv6_cidr_block", StringValueConverter())
      self.property(w, "MapPublicIpOnLaunch", "map_public_ip_on_launch", BasicValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "VpcId", "vpc_id", StringValueConverter())


class AWS_EC2_DHCPOptions(CloudFormationResource):
  cfn_type = "AWS::EC2::DHCPOptions"
  tf_type = "aws_vpc_dhcp_options"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DomainName", "domain_name", StringValueConverter())
      self.property(w, "DomainNameServers", "domain_name_servers", ListValueConverter(StringValueConverter()))
      self.property(w, "NetbiosNameServers", "netbios_name_servers", ListValueConverter(StringValueConverter()))
      self.property(w, "NetbiosNodeType", "netbios_node_type", BasicValueConverter())
      self.property(w, "NtpServers", "ntp_servers", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_EgressOnlyInternetGateway(CloudFormationResource):
  cfn_type = "AWS::EC2::EgressOnlyInternetGateway"
  tf_type = "aws_egress_only_internet_gateway"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "VpcId", "vpc_id", StringValueConverter())


class AWS_EC2_NetworkInterfaceAttachment(CloudFormationResource):
  cfn_type = "AWS::EC2::NetworkInterfaceAttachment"
  tf_type = "aws_network_interface_attachment"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DeleteOnTermination", "delete_on_termination", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "DeviceIndex", "device_index", StringValueConverter())
      self.property(w, "InstanceId", "instance_id", StringValueConverter())
      self.property(w, "NetworkInterfaceId", "network_interface_id", StringValueConverter())


class AWS_EC2_CustomerGateway(CloudFormationResource):
  cfn_type = "AWS::EC2::CustomerGateway"
  tf_type = "aws_customer_gateway"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "BgpAsn", "bgp_asn", BasicValueConverter())
      self.property(w, "IpAddress", "ip_address", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Type", "type", StringValueConverter())


class AWS_EC2_EIPAssociation(CloudFormationResource):
  cfn_type = "AWS::EC2::EIPAssociation"
  tf_type = "aws_eip_association"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AllocationId", "allocation_id", StringValueConverter())
      self.property(w, "EIP", "eip", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "InstanceId", "instance_id", StringValueConverter())
      self.property(w, "NetworkInterfaceId", "network_interface_id", StringValueConverter())
      self.property(w, "PrivateIpAddress", "private_ip_address", StringValueConverter())


class AWS_EC2_VPNGateway(CloudFormationResource):
  cfn_type = "AWS::EC2::VPNGateway"
  tf_type = "aws_vpn_gateway"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AmazonSideAsn", "amazon_side_asn", BasicValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Type", "type", StringValueConverter()) # TODO: Probably not the correct mapping


class AWS_EC2_VPNConnection(CloudFormationResource):
  cfn_type = "AWS::EC2::VPNConnection"
  tf_type = "aws_vpn_connection"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CustomerGatewayId", "customer_gateway_id", StringValueConverter())
      self.property(w, "StaticRoutesOnly", "static_routes_only", BasicValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "TransitGatewayId", "transit_gateway_id", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "VpnGatewayId", "vpn_gateway_id", StringValueConverter())
      self.repeated_block(w, "VpnTunnelOptionsSpecifications", AWS_EC2_VPNConnection_VpnTunnelOptionsSpecification) # TODO: Probably not the correct mapping


class AWS_EC2_TransitGatewayRouteTable(CloudFormationResource):
  cfn_type = "AWS::EC2::TransitGatewayRouteTable"
  tf_type = "aws_ec2_transit_gateway_route_table"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "TransitGatewayId", "transit_gateway_id", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_VPCEndpointService(CloudFormationResource):
  cfn_type = "AWS::EC2::VPCEndpointService"
  tf_type = "aws_vpc_endpoint_service"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "NetworkLoadBalancerArns", "network_load_balancer_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "AcceptanceRequired", "acceptance_required", BasicValueConverter())


class AWS_EC2_ClientVpnRoute(CloudFormationResource):
  cfn_type = "AWS::EC2::ClientVpnRoute"
  tf_type = "aws_ec2_client_vpn_route" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ClientVpnEndpointId", "client_vpn_endpoint_id", StringValueConverter())
      self.property(w, "TargetVpcSubnetId", "target_vpc_subnet_id", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DestinationCidrBlock", "destination_cidr_block", StringValueConverter())


class AWS_EC2_PlacementGroup(CloudFormationResource):
  cfn_type = "AWS::EC2::PlacementGroup"
  tf_type = "aws_placement_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Strategy", "strategy", StringValueConverter())


class AWS_EC2_GatewayRouteTableAssociation(CloudFormationResource):
  cfn_type = "AWS::EC2::GatewayRouteTableAssociation"
  tf_type = "aws_ec2_transit_gateway_route_table_association"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "RouteTableId", "transit_gateway_route_table_id", StringValueConverter())
      self.property(w, "GatewayId", "id", StringValueConverter())


class AWS_EC2_NetworkAclEntry(CloudFormationResource):
  cfn_type = "AWS::EC2::NetworkAclEntry"
  tf_type = "aws_ec2_network_acl_entry" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CidrBlock", "cidr_block", StringValueConverter())
      self.property(w, "Egress", "egress", BasicValueConverter())
      self.block(w, "Icmp", AWS_EC2_NetworkAclEntry_Icmp)
      self.property(w, "Ipv6CidrBlock", "ipv6_cidr_block", StringValueConverter())
      self.property(w, "NetworkAclId", "network_acl_id", StringValueConverter())
      self.block(w, "PortRange", AWS_EC2_NetworkAclEntry_PortRange)
      self.property(w, "Protocol", "protocol", BasicValueConverter())
      self.property(w, "RuleAction", "rule_action", StringValueConverter())
      self.property(w, "RuleNumber", "rule_number", BasicValueConverter())


class AWS_EC2_InternetGateway(CloudFormationResource):
  cfn_type = "AWS::EC2::InternetGateway"
  tf_type = "aws_internet_gateway"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_VPNConnectionRoute(CloudFormationResource):
  cfn_type = "AWS::EC2::VPNConnectionRoute"
  tf_type = "aws_vpn_connection_route"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DestinationCidrBlock", "destination_cidr_block", StringValueConverter())
      self.property(w, "VpnConnectionId", "vpn_connection_id", StringValueConverter())


class AWS_EC2_NetworkInterfacePermission(CloudFormationResource):
  cfn_type = "AWS::EC2::NetworkInterfacePermission"
  tf_type = "aws_ec2_network_interface_permission" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AwsAccountId", "aws_account_id", StringValueConverter())
      self.property(w, "NetworkInterfaceId", "network_interface_id", StringValueConverter())
      self.property(w, "Permission", "permission", StringValueConverter())


class AWS_EC2_TrafficMirrorFilter(CloudFormationResource):
  cfn_type = "AWS::EC2::TrafficMirrorFilter"
  tf_type = "aws_ec2_traffic_mirror_filter"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "NetworkServices", "network_services", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_SecurityGroupIngress(CloudFormationResource):
  cfn_type = "AWS::EC2::SecurityGroupIngress"
  tf_type = "aws_ec2_security_group_ingress" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CidrIp", "cidr_ip", StringValueConverter())
      self.property(w, "CidrIpv6", "cidr_ipv6", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "FromPort", "from_port", BasicValueConverter())
      self.property(w, "GroupId", "group_id", StringValueConverter())
      self.property(w, "GroupName", "group_name", StringValueConverter())
      self.property(w, "IpProtocol", "ip_protocol", StringValueConverter())
      self.property(w, "SourcePrefixListId", "source_prefix_list_id", StringValueConverter())
      self.property(w, "SourceSecurityGroupId", "source_security_group_id", StringValueConverter())
      self.property(w, "SourceSecurityGroupName", "source_security_group_name", StringValueConverter())
      self.property(w, "SourceSecurityGroupOwnerId", "source_security_group_owner_id", StringValueConverter())
      self.property(w, "ToPort", "to_port", BasicValueConverter())


class AWS_EC2_SubnetRouteTableAssociation(CloudFormationResource):
  cfn_type = "AWS::EC2::SubnetRouteTableAssociation"
  tf_type = "aws_ec2_subnet_route_table_association" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "RouteTableId", "route_table_id", StringValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())


class AWS_EC2_Route(CloudFormationResource):
  cfn_type = "AWS::EC2::Route"
  tf_type = "aws_ec2_route" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DestinationCidrBlock", "destination_cidr_block", StringValueConverter())
      self.property(w, "DestinationIpv6CidrBlock", "destination_ipv6_cidr_block", StringValueConverter())
      self.property(w, "EgressOnlyInternetGatewayId", "egress_only_internet_gateway_id", StringValueConverter())
      self.property(w, "GatewayId", "gateway_id", StringValueConverter())
      self.property(w, "InstanceId", "instance_id", StringValueConverter())
      self.property(w, "NatGatewayId", "nat_gateway_id", StringValueConverter())
      self.property(w, "NetworkInterfaceId", "network_interface_id", StringValueConverter())
      self.property(w, "RouteTableId", "route_table_id", StringValueConverter())
      self.property(w, "TransitGatewayId", "transit_gateway_id", StringValueConverter())
      self.property(w, "VpcPeeringConnectionId", "vpc_peering_connection_id", StringValueConverter())


class AWS_EC2_LocalGatewayRouteTableVPCAssociation(CloudFormationResource):
  cfn_type = "AWS::EC2::LocalGatewayRouteTableVPCAssociation"
  tf_type = "aws_ec2_local_gateway_route_table_vpc_association"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "LocalGatewayRouteTableId", "local_gateway_route_table_id", StringValueConverter())
      self.property(w, "VpcId", "vpc_id", StringValueConverter())
      self.block(w, "Tags", AWS_EC2_LocalGatewayRouteTableVPCAssociation_Tags)


class AWS_EC2_TransitGatewayRouteTablePropagation(CloudFormationResource):
  cfn_type = "AWS::EC2::TransitGatewayRouteTablePropagation"
  tf_type = "aws_ec2_transit_gateway_route_table_propagation"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "TransitGatewayRouteTableId", "transit_gateway_route_table_id", StringValueConverter())
      self.property(w, "TransitGatewayAttachmentId", "transit_gateway_attachment_id", StringValueConverter())


class AWS_EC2_NetworkInterface(CloudFormationResource):
  cfn_type = "AWS::EC2::NetworkInterface"
  tf_type = "aws_network_interface"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "GroupSet", "group_set", ListValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping
      self.property(w, "InterfaceType", "interface_type", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Ipv6AddressCount", "ipv6_address_count", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "Ipv6Addresses", AWS_EC2_NetworkInterface_InstanceIpv6Address) # TODO: Probably not the correct mapping
      self.property(w, "PrivateIpAddress", "private_ip", StringValueConverter())
      self.repeated_block(w, "PrivateIpAddresses", AWS_EC2_NetworkInterface_PrivateIpAddressSpecification) # TODO: Probably not the correct mapping
      self.property(w, "SecondaryPrivateIpAddressCount", "secondary_private_ip_address_count", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "SourceDestCheck", "source_dest_check", BasicValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_ClientVpnAuthorizationRule(CloudFormationResource):
  cfn_type = "AWS::EC2::ClientVpnAuthorizationRule"
  tf_type = "aws_ec2_client_vpn_authorization_rule" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ClientVpnEndpointId", "client_vpn_endpoint_id", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "AccessGroupId", "access_group_id", StringValueConverter())
      self.property(w, "TargetNetworkCidr", "target_network_cidr", StringValueConverter())
      self.property(w, "AuthorizeAllGroups", "authorize_all_groups", BasicValueConverter())


class AWS_EC2_SubnetNetworkAclAssociation(CloudFormationResource):
  cfn_type = "AWS::EC2::SubnetNetworkAclAssociation"
  tf_type = "aws_ec2_subnet_network_acl_association" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "NetworkAclId", "network_acl_id", StringValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())


class AWS_EC2_TrafficMirrorSession(CloudFormationResource):
  cfn_type = "AWS::EC2::TrafficMirrorSession"
  tf_type = "aws_ec2_traffic_mirror_session"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "TrafficMirrorTargetId", "traffic_mirror_target_id", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "SessionNumber", "session_number", BasicValueConverter())
      self.property(w, "VirtualNetworkId", "virtual_network_id", BasicValueConverter())
      self.property(w, "PacketLength", "packet_length", BasicValueConverter())
      self.property(w, "NetworkInterfaceId", "network_interface_id", StringValueConverter())
      self.property(w, "TrafficMirrorFilterId", "traffic_mirror_filter_id", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_SubnetCidrBlock(CloudFormationResource):
  cfn_type = "AWS::EC2::SubnetCidrBlock"
  tf_type = "aws_ec2_subnet_cidr_block" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Ipv6CidrBlock", "ipv6_cidr_block", StringValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())


class AWS_EC2_NatGateway(CloudFormationResource):
  cfn_type = "AWS::EC2::NatGateway"
  tf_type = "aws_nat_gateway"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AllocationId", "allocation_id", StringValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_SecurityGroup(CloudFormationResource):
  cfn_type = "AWS::EC2::SecurityGroup"
  tf_type = "aws_security_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "GroupDescription", "description", StringValueConverter())
      self.property(w, "GroupName", "name", StringValueConverter())
      self.repeated_block(w, "SecurityGroupEgress", AWS_EC2_SecurityGroup_Egress)
      self.repeated_block(w, "SecurityGroupIngress", AWS_EC2_SecurityGroup_Ingress)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "VpcId", "vpc_id", StringValueConverter())


class AWS_EC2_TrafficMirrorFilterRule(CloudFormationResource):
  cfn_type = "AWS::EC2::TrafficMirrorFilterRule"
  tf_type = "aws_ec2_traffic_mirror_filter_rule"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "DestinationPortRange", AWS_EC2_TrafficMirrorFilterRule_TrafficMirrorPortRange)
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "SourcePortRange", AWS_EC2_TrafficMirrorFilterRule_TrafficMirrorPortRange)
      self.property(w, "RuleAction", "rule_action", StringValueConverter())
      self.property(w, "SourceCidrBlock", "source_cidr_block", StringValueConverter())
      self.property(w, "RuleNumber", "rule_number", BasicValueConverter())
      self.property(w, "DestinationCidrBlock", "destination_cidr_block", StringValueConverter())
      self.property(w, "TrafficMirrorFilterId", "traffic_mirror_filter_id", StringValueConverter())
      self.property(w, "TrafficDirection", "traffic_direction", StringValueConverter())
      self.property(w, "Protocol", "protocol", BasicValueConverter())


class AWS_EC2_VPC(CloudFormationResource):
  cfn_type = "AWS::EC2::VPC"
  tf_type = "aws_ec2_vpc" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CidrBlock", "cidr_block", StringValueConverter())
      self.property(w, "EnableDnsHostnames", "enable_dns_hostnames", BasicValueConverter())
      self.property(w, "EnableDnsSupport", "enable_dns_support", BasicValueConverter())
      self.property(w, "InstanceTenancy", "instance_tenancy", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_TransitGatewayRoute(CloudFormationResource):
  cfn_type = "AWS::EC2::TransitGatewayRoute"
  tf_type = "aws_ec2_transit_gateway_route"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "TransitGatewayRouteTableId", "transit_gateway_route_table_id", StringValueConverter())
      self.property(w, "DestinationCidrBlock", "destination_cidr_block", StringValueConverter())
      self.property(w, "Blackhole", "blackhole", BasicValueConverter())
      self.property(w, "TransitGatewayAttachmentId", "transit_gateway_attachment_id", StringValueConverter())


class AWS_EC2_NetworkAcl(CloudFormationResource):
  cfn_type = "AWS::EC2::NetworkAcl"
  tf_type = "aws_network_acl"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "VpcId", "vpc_id", StringValueConverter())


class AWS_EC2_VPNGatewayRoutePropagation(CloudFormationResource):
  cfn_type = "AWS::EC2::VPNGatewayRoutePropagation"
  tf_type = "aws_vpn_gateway_route_propagation"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "RouteTableIds", "route_table_id", ListValueConverter(StringValueConverter()))
      self.property(w, "VpnGatewayId", "vpn_gateway_id", StringValueConverter())


class AWS_EC2_ClientVpnTargetNetworkAssociation(CloudFormationResource):
  cfn_type = "AWS::EC2::ClientVpnTargetNetworkAssociation"
  tf_type = "aws_ec2_client_vpn_network_association"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ClientVpnEndpointId", "client_vpn_endpoint_id", StringValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())


class AWS_EC2_VolumeAttachment(CloudFormationResource):
  cfn_type = "AWS::EC2::VolumeAttachment"
  tf_type = "aws_volume_attachment"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Device", "device_name", StringValueConverter())
      self.property(w, "InstanceId", "instance_id", StringValueConverter())
      self.property(w, "VolumeId", "volume_id", StringValueConverter())


class AWS_EC2_Host(CloudFormationResource):
  cfn_type = "AWS::EC2::Host"
  tf_type = "aws_ec2_host" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AutoPlacement", "auto_placement", StringValueConverter())
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "HostRecovery", "host_recovery", StringValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())


class AWS_EC2_VPCEndpoint(CloudFormationResource):
  cfn_type = "AWS::EC2::VPCEndpoint"
  tf_type = "aws_vpc_endpoint"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PolicyDocument", "policy", JsonValueConverter())
      self.property(w, "PrivateDnsEnabled", "private_dns_enabled", BasicValueConverter())
      self.property(w, "RouteTableIds", "route_table_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "ServiceName", "service_name", StringValueConverter())
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "VpcEndpointType", "vpc_endpoint_type", StringValueConverter())
      self.property(w, "VpcId", "vpc_id", StringValueConverter())


class AWS_EC2_VPCGatewayAttachment(CloudFormationResource):
  cfn_type = "AWS::EC2::VPCGatewayAttachment"
  tf_type = "aws_vpn_gateway_attachment"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "InternetGatewayId", "internet_gateway_id", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "VpcId", "vpc_id", StringValueConverter())
      self.property(w, "VpnGatewayId", "vpn_gateway_id", StringValueConverter())


class AWS_EC2_VPCCidrBlock(CloudFormationResource):
  cfn_type = "AWS::EC2::VPCCidrBlock"
  tf_type = "aws_ec2_vpc_cidr_block" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AmazonProvidedIpv6CidrBlock", "amazon_provided_ipv6_cidr_block", BasicValueConverter())
      self.property(w, "CidrBlock", "cidr_block", StringValueConverter())
      self.property(w, "VpcId", "vpc_id", StringValueConverter())


class AWS_EC2_VPCDHCPOptionsAssociation(CloudFormationResource):
  cfn_type = "AWS::EC2::VPCDHCPOptionsAssociation"
  tf_type = "aws_vpc_dhcp_options_association"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DhcpOptionsId", "dhcp_options_id", StringValueConverter())
      self.property(w, "VpcId", "vpc_id", StringValueConverter())


class AWS_EC2_TrafficMirrorTarget(CloudFormationResource):
  cfn_type = "AWS::EC2::TrafficMirrorTarget"
  tf_type = "aws_ec2_traffic_mirror_target"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "NetworkLoadBalancerArn", "network_load_balancer_arn", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "NetworkInterfaceId", "network_interface_id", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_EC2_LaunchTemplate_BlockDeviceMapping(CloudFormationProperty):
  def write(self, w):
    with w.block("block_device_mapping"):
      self.block(w, "Ebs", AWS_EC2_LaunchTemplate_Ebs)
      self.property(w, "NoDevice", "no_device", StringValueConverter())
      self.property(w, "VirtualName", "virtual_name", StringValueConverter())
      self.property(w, "DeviceName", "device_name", StringValueConverter())


class AWS_EC2_SpotFleet_LoadBalancersConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("load_balancers_config"):
      self.block(w, "ClassicLoadBalancersConfig", AWS_EC2_SpotFleet_ClassicLoadBalancersConfig)
      self.block(w, "TargetGroupsConfig", AWS_EC2_SpotFleet_TargetGroupsConfig)


class AWS_EC2_EC2Fleet_OnDemandOptionsRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("on_demand_options_request"):
      self.property(w, "SingleAvailabilityZone", "single_availability_zone", BasicValueConverter())
      self.property(w, "AllocationStrategy", "allocation_strategy", StringValueConverter())
      self.property(w, "SingleInstanceType", "single_instance_type", BasicValueConverter())
      self.property(w, "MinTargetCapacity", "min_target_capacity", BasicValueConverter())
      self.property(w, "MaxTotalPrice", "max_total_price", StringValueConverter())
      self.block(w, "CapacityReservationOptions", AWS_EC2_EC2Fleet_CapacityReservationOptionsRequest)


class AWS_EC2_EC2Fleet_FleetLaunchTemplateOverridesRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("fleet_launch_template_overrides_request"):
      self.property(w, "WeightedCapacity", "weighted_capacity", BasicValueConverter())
      self.block(w, "Placement", AWS_EC2_EC2Fleet_Placement)
      self.property(w, "Priority", "priority", BasicValueConverter())
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "MaxPrice", "max_price", StringValueConverter())


class AWS_EC2_Instance_NetworkInterface(CloudFormationProperty):
  def write(self, w):
    with w.block("network_interface"):
      self.property(w, "AssociatePublicIpAddress", "associate_public_ip_address", BasicValueConverter())
      self.property(w, "DeleteOnTermination", "delete_on_termination", BasicValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DeviceIndex", "device_index", StringValueConverter())
      self.property(w, "GroupSet", "group_set", ListValueConverter(StringValueConverter()))
      self.property(w, "Ipv6AddressCount", "ipv6_address_count", BasicValueConverter())
      self.repeated_block(w, "Ipv6Addresses", AWS_EC2_Instance_InstanceIpv6Address)
      self.property(w, "NetworkInterfaceId", "network_interface_id", StringValueConverter())
      self.property(w, "PrivateIpAddress", "private_ip_address", StringValueConverter())
      self.repeated_block(w, "PrivateIpAddresses", AWS_EC2_Instance_PrivateIpAddressSpecification)
      self.property(w, "SecondaryPrivateIpAddressCount", "secondary_private_ip_address_count", BasicValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())


class AWS_EC2_SpotFleet_InstanceNetworkInterfaceSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("instance_network_interface_specification"):
      self.property(w, "AssociatePublicIpAddress", "associate_public_ip_address", BasicValueConverter())
      self.property(w, "DeleteOnTermination", "delete_on_termination", BasicValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DeviceIndex", "device_index", BasicValueConverter())
      self.property(w, "Groups", "groups", ListValueConverter(StringValueConverter()))
      self.property(w, "Ipv6AddressCount", "ipv6_address_count", BasicValueConverter())
      self.repeated_block(w, "Ipv6Addresses", AWS_EC2_SpotFleet_InstanceIpv6Address)
      self.property(w, "NetworkInterfaceId", "network_interface_id", StringValueConverter())
      self.repeated_block(w, "PrivateIpAddresses", AWS_EC2_SpotFleet_PrivateIpAddressSpecification)
      self.property(w, "SecondaryPrivateIpAddressCount", "secondary_private_ip_address_count", BasicValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())


class AWS_EC2_ClientVpnEndpoint_ClientAuthenticationRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("client_authentication_request"):
      self.block(w, "MutualAuthentication", AWS_EC2_ClientVpnEndpoint_CertificateAuthenticationRequest)
      self.property(w, "Type", "type", StringValueConverter())
      self.block(w, "FederatedAuthentication", AWS_EC2_ClientVpnEndpoint_FederatedAuthenticationRequest)
      self.block(w, "ActiveDirectory", AWS_EC2_ClientVpnEndpoint_DirectoryServiceAuthenticationRequest)


class AWS_EC2_SpotFleet_SpotFleetLaunchSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("spot_fleet_launch_specification"):
      self.repeated_block(w, "BlockDeviceMappings", AWS_EC2_SpotFleet_BlockDeviceMapping)
      self.property(w, "EbsOptimized", "ebs_optimized", BasicValueConverter())
      self.block(w, "IamInstanceProfile", AWS_EC2_SpotFleet_IamInstanceProfileSpecification)
      self.property(w, "ImageId", "image_id", StringValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "KernelId", "kernel_id", StringValueConverter())
      self.property(w, "KeyName", "key_name", StringValueConverter())
      self.block(w, "Monitoring", AWS_EC2_SpotFleet_SpotFleetMonitoring)
      self.repeated_block(w, "NetworkInterfaces", AWS_EC2_SpotFleet_InstanceNetworkInterfaceSpecification)
      self.block(w, "Placement", AWS_EC2_SpotFleet_SpotPlacement)
      self.property(w, "RamdiskId", "ramdisk_id", StringValueConverter())
      self.repeated_block(w, "SecurityGroups", AWS_EC2_SpotFleet_GroupIdentifier)
      self.property(w, "SpotPrice", "spot_price", StringValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())
      self.repeated_block(w, "TagSpecifications", AWS_EC2_SpotFleet_SpotFleetTagSpecification)
      self.property(w, "UserData", "user_data", StringValueConverter())
      self.property(w, "WeightedCapacity", "weighted_capacity", BasicValueConverter())


class AWS_EC2_SpotFleet_SpotFleetRequestConfigData(CloudFormationProperty):
  def write(self, w):
    with w.block("spot_fleet_request_config_data"):
      self.property(w, "AllocationStrategy", "allocation_strategy", StringValueConverter())
      self.property(w, "ExcessCapacityTerminationPolicy", "excess_capacity_termination_policy", StringValueConverter())
      self.property(w, "IamFleetRole", "iam_fleet_role", StringValueConverter())
      self.property(w, "InstanceInterruptionBehavior", "instance_interruption_behavior", StringValueConverter())
      self.repeated_block(w, "LaunchSpecifications", AWS_EC2_SpotFleet_SpotFleetLaunchSpecification)
      self.repeated_block(w, "LaunchTemplateConfigs", AWS_EC2_SpotFleet_LaunchTemplateConfig)
      self.block(w, "LoadBalancersConfig", AWS_EC2_SpotFleet_LoadBalancersConfig)
      self.property(w, "ReplaceUnhealthyInstances", "replace_unhealthy_instances", BasicValueConverter())
      self.property(w, "SpotPrice", "spot_price", StringValueConverter())
      self.property(w, "TargetCapacity", "target_capacity", BasicValueConverter())
      self.property(w, "TerminateInstancesWithExpiration", "terminate_instances_with_expiration", BasicValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "ValidFrom", "valid_from", StringValueConverter())
      self.property(w, "ValidUntil", "valid_until", StringValueConverter())


class AWS_EC2_LaunchTemplate_CapacityReservationSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("capacity_reservation_specification"):
      self.property(w, "CapacityReservationPreference", "capacity_reservation_preference", StringValueConverter())
      self.block(w, "CapacityReservationTarget", AWS_EC2_LaunchTemplate_CapacityReservationTarget)


class AWS_EC2_EC2Fleet_FleetLaunchTemplateConfigRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("fleet_launch_template_config_request"):
      self.block(w, "LaunchTemplateSpecification", AWS_EC2_EC2Fleet_FleetLaunchTemplateSpecificationRequest)
      self.repeated_block(w, "Overrides", AWS_EC2_EC2Fleet_FleetLaunchTemplateOverridesRequest)


class AWS_EC2_Instance(CloudFormationResource):
  cfn_type = "AWS::EC2::Instance"
  tf_type = "aws_instance"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AdditionalInfo", "additional_info", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Affinity", "affinity", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.repeated_block(w, "BlockDeviceMappings", AWS_EC2_Instance_BlockDeviceMapping) # TODO: Probably not the correct mapping
      self.block(w, "CpuOptions", AWS_EC2_Instance_CpuOptions) # TODO: Probably not the correct mapping
      self.block(w, "CreditSpecification", AWS_EC2_Instance_CreditSpecification)
      self.property(w, "DisableApiTermination", "disable_api_termination", BasicValueConverter())
      self.property(w, "EbsOptimized", "ebs_optimized", BasicValueConverter())
      self.repeated_block(w, "ElasticGpuSpecifications", AWS_EC2_Instance_ElasticGpuSpecification) # TODO: Probably not the correct mapping
      self.repeated_block(w, "ElasticInferenceAccelerators", AWS_EC2_Instance_ElasticInferenceAccelerator) # TODO: Probably not the correct mapping
      self.block(w, "HibernationOptions", AWS_EC2_Instance_HibernationOptions)
      self.property(w, "HostId", "host_id", StringValueConverter())
      self.property(w, "HostResourceGroupArn", "arn", StringValueConverter())
      self.property(w, "IamInstanceProfile", "iam_instance_profile", StringValueConverter())
      self.property(w, "ImageId", "id", StringValueConverter())
      self.property(w, "InstanceInitiatedShutdownBehavior", "instance_initiated_shutdown_behavior", StringValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "Ipv6AddressCount", "ipv6_address_count", BasicValueConverter())
      self.repeated_block(w, "Ipv6Addresses", AWS_EC2_Instance_InstanceIpv6Address)
      self.property(w, "KernelId", "kernel_id", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "KeyName", "key_name", StringValueConverter())
      self.block(w, "LaunchTemplate", AWS_EC2_Instance_LaunchTemplateSpecification) # TODO: Probably not the correct mapping
      self.repeated_block(w, "LicenseSpecifications", AWS_EC2_Instance_LicenseSpecification) # TODO: Probably not the correct mapping
      self.property(w, "Monitoring", "monitoring", BasicValueConverter())
      self.repeated_block(w, "NetworkInterfaces", AWS_EC2_Instance_NetworkInterface)
      self.property(w, "PlacementGroupName", "placement_group_name", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "PrivateIpAddress", "private_ip", StringValueConverter())
      self.property(w, "RamdiskId", "ramdisk_id", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "SecurityGroupIds", "vpc_security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SecurityGroups", "security_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "SourceDestCheck", "source_dest_check", BasicValueConverter())
      self.repeated_block(w, "SsmAssociations", AWS_EC2_Instance_SsmAssociation) # TODO: Probably not the correct mapping
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Tenancy", "tenancy", StringValueConverter())
      self.property(w, "UserData", "user_data", StringValueConverter())
      self.repeated_block(w, "Volumes", AWS_EC2_Instance_Volume) # TODO: Probably not the correct mapping


class AWS_EC2_SpotFleet(CloudFormationResource):
  cfn_type = "AWS::EC2::SpotFleet"
  tf_type = "aws_ec2_spot_fleet" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "SpotFleetRequestConfigData", AWS_EC2_SpotFleet_SpotFleetRequestConfigData)


class AWS_EC2_ClientVpnEndpoint(CloudFormationResource):
  cfn_type = "AWS::EC2::ClientVpnEndpoint"
  tf_type = "aws_ec2_client_vpn_endpoint"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ClientCidrBlock", "client_cidr_block", StringValueConverter())
      self.block(w, "ConnectionLogOptions", AWS_EC2_ClientVpnEndpoint_ConnectionLogOptions)
      self.property(w, "SplitTunnel", "split_tunnel", BasicValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.repeated_block(w, "TagSpecifications", AWS_EC2_ClientVpnEndpoint_TagSpecification) # TODO: Probably not the correct mapping
      self.property(w, "VpcId", "id", StringValueConverter())
      self.repeated_block(w, "AuthenticationOptions", AWS_EC2_ClientVpnEndpoint_ClientAuthenticationRequest)
      self.property(w, "ServerCertificateArn", "server_certificate_arn", StringValueConverter())
      self.property(w, "DnsServers", "dns_servers", ListValueConverter(StringValueConverter()))
      self.property(w, "TransportProtocol", "transport_protocol", StringValueConverter())
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping
      self.property(w, "VpnPort", "vpn_port", BasicValueConverter()) # TODO: Probably not the correct mapping


class AWS_EC2_EC2Fleet(CloudFormationResource):
  cfn_type = "AWS::EC2::EC2Fleet"
  tf_type = "aws_ec2_fleet"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "TargetCapacitySpecification", AWS_EC2_EC2Fleet_TargetCapacitySpecificationRequest)
      self.block(w, "OnDemandOptions", AWS_EC2_EC2Fleet_OnDemandOptionsRequest)
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "ExcessCapacityTerminationPolicy", "excess_capacity_termination_policy", StringValueConverter())
      self.repeated_block(w, "TagSpecifications", AWS_EC2_EC2Fleet_TagSpecification) # TODO: Probably not the correct mapping
      self.block(w, "SpotOptions", AWS_EC2_EC2Fleet_SpotOptionsRequest)
      self.property(w, "ValidFrom", "id", StringValueConverter())
      self.property(w, "ReplaceUnhealthyInstances", "replace_unhealthy_instances", BasicValueConverter())
      self.repeated_block(w, "LaunchTemplateConfigs", AWS_EC2_EC2Fleet_FleetLaunchTemplateConfigRequest)
      self.property(w, "TerminateInstancesWithExpiration", "terminate_instances_with_expiration", BasicValueConverter())
      self.property(w, "ValidUntil", "valid_until", StringValueConverter()) # TODO: Probably not the correct mapping


class AWS_EC2_LaunchTemplate_LaunchTemplateData(CloudFormationProperty):
  def write(self, w):
    with w.block("launch_template_data"):
      self.property(w, "SecurityGroups", "security_groups", ListValueConverter(StringValueConverter()))
      self.repeated_block(w, "TagSpecifications", AWS_EC2_LaunchTemplate_TagSpecification)
      self.property(w, "UserData", "user_data", StringValueConverter())
      self.repeated_block(w, "BlockDeviceMappings", AWS_EC2_LaunchTemplate_BlockDeviceMapping)
      self.block(w, "IamInstanceProfile", AWS_EC2_LaunchTemplate_IamInstanceProfile)
      self.property(w, "KernelId", "kernel_id", StringValueConverter())
      self.property(w, "EbsOptimized", "ebs_optimized", BasicValueConverter())
      self.repeated_block(w, "ElasticGpuSpecifications", AWS_EC2_LaunchTemplate_ElasticGpuSpecification)
      self.repeated_block(w, "ElasticInferenceAccelerators", AWS_EC2_LaunchTemplate_LaunchTemplateElasticInferenceAccelerator)
      self.block(w, "Placement", AWS_EC2_LaunchTemplate_Placement)
      self.repeated_block(w, "NetworkInterfaces", AWS_EC2_LaunchTemplate_NetworkInterface)
      self.property(w, "ImageId", "image_id", StringValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.block(w, "Monitoring", AWS_EC2_LaunchTemplate_Monitoring)
      self.block(w, "HibernationOptions", AWS_EC2_LaunchTemplate_HibernationOptions)
      self.block(w, "MetadataOptions", AWS_EC2_LaunchTemplate_MetadataOptions)
      self.repeated_block(w, "LicenseSpecifications", AWS_EC2_LaunchTemplate_LicenseSpecification)
      self.property(w, "InstanceInitiatedShutdownBehavior", "instance_initiated_shutdown_behavior", StringValueConverter())
      self.block(w, "CpuOptions", AWS_EC2_LaunchTemplate_CpuOptions)
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "KeyName", "key_name", StringValueConverter())
      self.property(w, "DisableApiTermination", "disable_api_termination", BasicValueConverter())
      self.block(w, "InstanceMarketOptions", AWS_EC2_LaunchTemplate_InstanceMarketOptions)
      self.property(w, "RamDiskId", "ram_disk_id", StringValueConverter())
      self.block(w, "CapacityReservationSpecification", AWS_EC2_LaunchTemplate_CapacityReservationSpecification)
      self.block(w, "CreditSpecification", AWS_EC2_LaunchTemplate_CreditSpecification)


class AWS_EC2_LaunchTemplate(CloudFormationResource):
  cfn_type = "AWS::EC2::LaunchTemplate"
  tf_type = "aws_launch_template"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "LaunchTemplateName", "name", StringValueConverter())
      self.block(w, "LaunchTemplateData", AWS_EC2_LaunchTemplate_LaunchTemplateData) # TODO: Probably not the correct mapping


