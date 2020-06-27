from . import *

class AWS_EC2_LaunchTemplate_PrivateIpAdd(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "private_ip_add"

  props = {
    "PrivateIpAddress": (StringValueConverter(), "private_ip_address"),
    "Primary": (BasicValueConverter(), "primary"),
  }

class AWS_EC2_SpotFleet_SpotFleetTagSpecification(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "spot_fleet_tag_specification"

  props = {
    "ResourceType": (StringValueConverter(), "resource_type"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_SpotFleet_PrivateIpAddressSpecification(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "private_ip_address_specification"

  props = {
    "Primary": (BasicValueConverter(), "primary"),
    "PrivateIpAddress": (StringValueConverter(), "private_ip_address"),
  }

class AWS_EC2_EC2Fleet_FleetLaunchTemplateSpecificationRequest(CloudFormationProperty):
  entity = "AWS::EC2::EC2Fleet"
  tf_block_type = "fleet_launch_template_specification_request"

  props = {
    "LaunchTemplateName": (StringValueConverter(), "launch_template_name"),
    "Version": (StringValueConverter(), "version"),
    "LaunchTemplateId": (StringValueConverter(), "launch_template_id"),
  }

class AWS_EC2_VPNConnection_VpnTunnelOptionsSpecification(CloudFormationProperty):
  entity = "AWS::EC2::VPNConnection"
  tf_block_type = "vpn_tunnel_options_specification"

  props = {
    "PreSharedKey": (StringValueConverter(), "pre_shared_key"),
    "TunnelInsideCidr": (StringValueConverter(), "tunnel_inside_cidr"),
  }

class AWS_EC2_TrafficMirrorFilterRule_TrafficMirrorPortRange(CloudFormationProperty):
  entity = "AWS::EC2::TrafficMirrorFilterRule"
  tf_block_type = "traffic_mirror_port_range"

  props = {
    "FromPort": (BasicValueConverter(), "from_port"),
    "ToPort": (BasicValueConverter(), "to_port"),
  }

class AWS_EC2_LaunchTemplate_SpotOptions(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "spot_options"

  props = {
    "SpotInstanceType": (StringValueConverter(), "spot_instance_type"),
    "InstanceInterruptionBehavior": (StringValueConverter(), "instance_interruption_behavior"),
    "MaxPrice": (StringValueConverter(), "max_price"),
    "BlockDurationMinutes": (BasicValueConverter(), "block_duration_minutes"),
    "ValidUntil": (StringValueConverter(), "valid_until"),
  }

class AWS_EC2_Instance_HibernationOptions(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "hibernation_options"

  props = {
    "Configured": (BasicValueConverter(), "configured"),
  }

class AWS_EC2_SpotFleet_SpotPlacement(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "spot_placement"

  props = {
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "GroupName": (StringValueConverter(), "group_name"),
    "Tenancy": (StringValueConverter(), "tenancy"),
  }

class AWS_EC2_NetworkInterface_InstanceIpv6Address(CloudFormationProperty):
  entity = "AWS::EC2::NetworkInterface"
  tf_block_type = "instance_ipv6_address"

  props = {
    "Ipv6Address": (StringValueConverter(), "ipv6_address"),
  }

class AWS_EC2_SpotFleet_EbsBlockDevice(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "ebs_block_device"

  props = {
    "DeleteOnTermination": (BasicValueConverter(), "delete_on_termination"),
    "Encrypted": (BasicValueConverter(), "encrypted"),
    "Iops": (BasicValueConverter(), "iops"),
    "SnapshotId": (StringValueConverter(), "snapshot_id"),
    "VolumeSize": (BasicValueConverter(), "volume_size"),
    "VolumeType": (StringValueConverter(), "volume_type"),
  }

class AWS_EC2_SpotFleet_FleetLaunchTemplateSpecification(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "fleet_launch_template_specification"

  props = {
    "LaunchTemplateId": (StringValueConverter(), "launch_template_id"),
    "LaunchTemplateName": (StringValueConverter(), "launch_template_name"),
    "Version": (StringValueConverter(), "version"),
  }

class AWS_EC2_Instance_Volume(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "volume"

  props = {
    "Device": (StringValueConverter(), "device"),
    "VolumeId": (StringValueConverter(), "volume_id"),
  }

class AWS_EC2_NetworkAclEntry_PortRange(CloudFormationProperty):
  entity = "AWS::EC2::NetworkAclEntry"
  tf_block_type = "port_range"

  props = {
    "From": (BasicValueConverter(), "from"),
    "To": (BasicValueConverter(), "to"),
  }

class AWS_EC2_LocalGatewayRouteTableVPCAssociation_Tags(CloudFormationProperty):
  entity = "AWS::EC2::LocalGatewayRouteTableVPCAssociation"
  tf_block_type = "tags"

  props = {
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_LaunchTemplate_ElasticGpuSpecification(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "elastic_gpu_specification"

  props = {
    "Type": (StringValueConverter(), "type"),
  }

class AWS_EC2_SpotFleet_TargetGroup(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "target_group"

  props = {
    "Arn": (StringValueConverter(), "arn"),
  }

class AWS_EC2_NetworkInterface_PrivateIpAddressSpecification(CloudFormationProperty):
  entity = "AWS::EC2::NetworkInterface"
  tf_block_type = "private_ip_address_specification"

  props = {
    "Primary": (BasicValueConverter(), "primary"),
    "PrivateIpAddress": (StringValueConverter(), "private_ip_address"),
  }

class AWS_EC2_ClientVpnEndpoint_ConnectionLogOptions(CloudFormationProperty):
  entity = "AWS::EC2::ClientVpnEndpoint"
  tf_block_type = "connection_log_options"

  props = {
    "CloudwatchLogStream": (StringValueConverter(), "cloudwatch_log_stream"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "CloudwatchLogGroup": (StringValueConverter(), "cloudwatch_log_group"),
  }

class AWS_EC2_Instance_Ebs(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "ebs"

  props = {
    "DeleteOnTermination": (BasicValueConverter(), "delete_on_termination"),
    "Encrypted": (BasicValueConverter(), "encrypted"),
    "Iops": (BasicValueConverter(), "iops"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "SnapshotId": (StringValueConverter(), "snapshot_id"),
    "VolumeSize": (BasicValueConverter(), "volume_size"),
    "VolumeType": (StringValueConverter(), "volume_type"),
  }

class AWS_EC2_LaunchTemplate_TagSpecification(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "tag_specification"

  props = {
    "ResourceType": (StringValueConverter(), "resource_type"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_LaunchTemplate_IamInstanceProfile(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "iam_instance_profile"

  props = {
    "Arn": (StringValueConverter(), "arn"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_EC2_Instance_NoDevice(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "no_device"

  props = {
  }

class AWS_EC2_Instance_CreditSpecification(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "credit_specification"

  props = {
    "CPUCredits": (StringValueConverter(), "cpu_credits"),
  }

class AWS_EC2_EC2Fleet_TargetCapacitySpecificationRequest(CloudFormationProperty):
  entity = "AWS::EC2::EC2Fleet"
  tf_block_type = "target_capacity_specification_request"

  props = {
    "DefaultTargetCapacityType": (StringValueConverter(), "default_target_capacity_type"),
    "TotalTargetCapacity": (BasicValueConverter(), "total_target_capacity"),
    "OnDemandTargetCapacity": (BasicValueConverter(), "on_demand_target_capacity"),
    "SpotTargetCapacity": (BasicValueConverter(), "spot_target_capacity"),
  }

class AWS_EC2_LaunchTemplate_LicenseSpecification(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "license_specification"

  props = {
    "LicenseConfigurationArn": (StringValueConverter(), "license_configuration_arn"),
  }

class AWS_EC2_SecurityGroup_Egress(CloudFormationProperty):
  entity = "AWS::EC2::SecurityGroup"
  tf_block_type = "egress"

  props = {
    "CidrIp": (StringValueConverter(), "cidr_ip"),
    "CidrIpv6": (StringValueConverter(), "cidr_ipv6"),
    "Description": (StringValueConverter(), "description"),
    "DestinationPrefixListId": (StringValueConverter(), "destination_prefix_list_id"),
    "DestinationSecurityGroupId": (StringValueConverter(), "destination_security_group_id"),
    "FromPort": (BasicValueConverter(), "from_port"),
    "IpProtocol": (StringValueConverter(), "ip_protocol"),
    "ToPort": (BasicValueConverter(), "to_port"),
  }

class AWS_EC2_SpotFleet_LaunchTemplateOverrides(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "launch_template_overrides"

  props = {
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "SpotPrice": (StringValueConverter(), "spot_price"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
    "WeightedCapacity": (BasicValueConverter(), "weighted_capacity"),
  }

class AWS_EC2_LaunchTemplate_Ebs(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "ebs"

  props = {
    "SnapshotId": (StringValueConverter(), "snapshot_id"),
    "VolumeType": (StringValueConverter(), "volume_type"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "Encrypted": (BasicValueConverter(), "encrypted"),
    "Iops": (BasicValueConverter(), "iops"),
    "VolumeSize": (BasicValueConverter(), "volume_size"),
    "DeleteOnTermination": (BasicValueConverter(), "delete_on_termination"),
  }

class AWS_EC2_SpotFleet_SpotFleetMonitoring(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "spot_fleet_monitoring"

  props = {
    "Enabled": (BasicValueConverter(), "enabled"),
  }

class AWS_EC2_LaunchTemplate_HibernationOptions(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "hibernation_options"

  props = {
    "Configured": (BasicValueConverter(), "configured"),
  }

class AWS_EC2_ClientVpnEndpoint_CertificateAuthenticationRequest(CloudFormationProperty):
  entity = "AWS::EC2::ClientVpnEndpoint"
  tf_block_type = "certificate_authentication_request"

  props = {
    "ClientRootCertificateChainArn": (StringValueConverter(), "client_root_certificate_chain_arn"),
  }

class AWS_EC2_ClientVpnEndpoint_DirectoryServiceAuthenticationRequest(CloudFormationProperty):
  entity = "AWS::EC2::ClientVpnEndpoint"
  tf_block_type = "directory_service_authentication_request"

  props = {
    "DirectoryId": (StringValueConverter(), "directory_id"),
  }

class AWS_EC2_SecurityGroup_Ingress(CloudFormationProperty):
  entity = "AWS::EC2::SecurityGroup"
  tf_block_type = "ingress"

  props = {
    "CidrIp": (StringValueConverter(), "cidr_ip"),
    "CidrIpv6": (StringValueConverter(), "cidr_ipv6"),
    "Description": (StringValueConverter(), "description"),
    "FromPort": (BasicValueConverter(), "from_port"),
    "IpProtocol": (StringValueConverter(), "ip_protocol"),
    "SourcePrefixListId": (StringValueConverter(), "source_prefix_list_id"),
    "SourceSecurityGroupId": (StringValueConverter(), "source_security_group_id"),
    "SourceSecurityGroupName": (StringValueConverter(), "source_security_group_name"),
    "SourceSecurityGroupOwnerId": (StringValueConverter(), "source_security_group_owner_id"),
    "ToPort": (BasicValueConverter(), "to_port"),
  }

class AWS_EC2_SpotFleet_ClassicLoadBalancer(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "classic_load_balancer"

  props = {
    "Name": (StringValueConverter(), "name"),
  }

class AWS_EC2_SpotFleet_LaunchTemplateConfig(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "launch_template_config"

  props = {
    "LaunchTemplateSpecification": (AWS_EC2_SpotFleet_FleetLaunchTemplateSpecification, "launch_template_specification"),
    "Overrides": (BlockValueConverter(AWS_EC2_SpotFleet_LaunchTemplateOverrides), None),
  }

class AWS_EC2_Instance_ElasticGpuSpecification(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "elastic_gpu_specification"

  props = {
    "Type": (StringValueConverter(), "type"),
  }

class AWS_EC2_NetworkAclEntry_Icmp(CloudFormationProperty):
  entity = "AWS::EC2::NetworkAclEntry"
  tf_block_type = "icmp"

  props = {
    "Code": (BasicValueConverter(), "code"),
    "Type": (BasicValueConverter(), "type"),
  }

class AWS_EC2_LaunchTemplate_InstanceMarketOptions(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "instance_market_options"

  props = {
    "SpotOptions": (AWS_EC2_LaunchTemplate_SpotOptions, "spot_options"),
    "MarketType": (StringValueConverter(), "market_type"),
  }

class AWS_EC2_ClientVpnEndpoint_TagSpecification(CloudFormationProperty):
  entity = "AWS::EC2::ClientVpnEndpoint"
  tf_block_type = "tag_specification"

  props = {
    "ResourceType": (StringValueConverter(), "resource_type"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_LaunchTemplate_CreditSpecification(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "credit_specification"

  props = {
    "CpuCredits": (StringValueConverter(), "cpu_credits"),
  }

class AWS_EC2_SpotFleet_IamInstanceProfileSpecification(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "iam_instance_profile_specification"

  props = {
    "Arn": (StringValueConverter(), "arn"),
  }

class AWS_EC2_EC2Fleet_CapacityReservationOptionsRequest(CloudFormationProperty):
  entity = "AWS::EC2::EC2Fleet"
  tf_block_type = "capacity_reservation_options_request"

  props = {
    "UsageStrategy": (StringValueConverter(), "usage_strategy"),
  }

class AWS_EC2_LaunchTemplate_Monitoring(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "monitoring"

  props = {
    "Enabled": (BasicValueConverter(), "enabled"),
  }

class AWS_EC2_LaunchTemplate_MetadataOptions(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "metadata_options"

  props = {
    "HttpPutResponseHopLimit": (BasicValueConverter(), "http_put_response_hop_limit"),
    "HttpTokens": (StringValueConverter(), "http_tokens"),
    "HttpEndpoint": (StringValueConverter(), "http_endpoint"),
  }

class AWS_EC2_EC2Fleet_Placement(CloudFormationProperty):
  entity = "AWS::EC2::EC2Fleet"
  tf_block_type = "placement"

  props = {
    "GroupName": (StringValueConverter(), "group_name"),
    "Tenancy": (StringValueConverter(), "tenancy"),
    "SpreadDomain": (StringValueConverter(), "spread_domain"),
    "PartitionNumber": (BasicValueConverter(), "partition_number"),
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "Affinity": (StringValueConverter(), "affinity"),
    "HostId": (StringValueConverter(), "host_id"),
    "HostResourceGroupArn": (StringValueConverter(), "host_resource_group_arn"),
  }

class AWS_EC2_SpotFleet_ClassicLoadBalancersConfig(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "classic_load_balancers_config"

  props = {
    "ClassicLoadBalancers": (BlockValueConverter(AWS_EC2_SpotFleet_ClassicLoadBalancer), None),
  }

class AWS_EC2_LaunchTemplate_Placement(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "placement"

  props = {
    "GroupName": (StringValueConverter(), "group_name"),
    "Tenancy": (StringValueConverter(), "tenancy"),
    "SpreadDomain": (StringValueConverter(), "spread_domain"),
    "PartitionNumber": (BasicValueConverter(), "partition_number"),
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "Affinity": (StringValueConverter(), "affinity"),
    "HostId": (StringValueConverter(), "host_id"),
    "HostResourceGroupArn": (StringValueConverter(), "host_resource_group_arn"),
  }

class AWS_EC2_ClientVpnEndpoint_FederatedAuthenticationRequest(CloudFormationProperty):
  entity = "AWS::EC2::ClientVpnEndpoint"
  tf_block_type = "federated_authentication_request"

  props = {
    "SAMLProviderArn": (StringValueConverter(), "saml_provider_arn"),
  }

class AWS_EC2_Instance_InstanceIpv6Address(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "instance_ipv6_address"

  props = {
    "Ipv6Address": (StringValueConverter(), "ipv6_address"),
  }

class AWS_EC2_Instance_AssociationParameter(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "association_parameter"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (ListValueConverter(StringValueConverter()), "value"),
  }

class AWS_EC2_Instance_CpuOptions(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "cpu_options"

  props = {
    "CoreCount": (BasicValueConverter(), "core_count"),
    "ThreadsPerCore": (BasicValueConverter(), "threads_per_core"),
  }

class AWS_EC2_Instance_LaunchTemplateSpecification(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "launch_template_specification"

  props = {
    "LaunchTemplateId": (StringValueConverter(), "launch_template_id"),
    "LaunchTemplateName": (StringValueConverter(), "launch_template_name"),
    "Version": (StringValueConverter(), "version"),
  }

class AWS_EC2_LaunchTemplate_Ipv6Add(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "ipv6_add"

  props = {
    "Ipv6Address": (StringValueConverter(), "ipv6_address"),
  }

class AWS_EC2_Instance_LicenseSpecification(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "license_specification"

  props = {
    "LicenseConfigurationArn": (StringValueConverter(), "license_configuration_arn"),
  }

class AWS_EC2_Instance_SsmAssociation(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "ssm_association"

  props = {
    "AssociationParameters": (BlockValueConverter(AWS_EC2_Instance_AssociationParameter), None),
    "DocumentName": (StringValueConverter(), "document_name"),
  }

class AWS_EC2_LaunchTemplate_CapacityReservationTarget(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "capacity_reservation_target"

  props = {
    "CapacityReservationId": (StringValueConverter(), "capacity_reservation_id"),
  }

class AWS_EC2_LaunchTemplate_NetworkInterface(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "network_interface"

  props = {
    "Description": (StringValueConverter(), "description"),
    "PrivateIpAddress": (StringValueConverter(), "private_ip_address"),
    "PrivateIpAddresses": (BlockValueConverter(AWS_EC2_LaunchTemplate_PrivateIpAdd), None),
    "SecondaryPrivateIpAddressCount": (BasicValueConverter(), "secondary_private_ip_address_count"),
    "DeviceIndex": (BasicValueConverter(), "device_index"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
    "Ipv6Addresses": (BlockValueConverter(AWS_EC2_LaunchTemplate_Ipv6Add), None),
    "AssociatePublicIpAddress": (BasicValueConverter(), "associate_public_ip_address"),
    "NetworkInterfaceId": (StringValueConverter(), "network_interface_id"),
    "InterfaceType": (StringValueConverter(), "interface_type"),
    "Ipv6AddressCount": (BasicValueConverter(), "ipv6_address_count"),
    "Groups": (ListValueConverter(StringValueConverter()), "groups"),
    "DeleteOnTermination": (BasicValueConverter(), "delete_on_termination"),
  }

class AWS_EC2_SpotFleet_InstanceIpv6Address(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "instance_ipv6_address"

  props = {
    "Ipv6Address": (StringValueConverter(), "ipv6_address"),
  }

class AWS_EC2_SpotFleet_TargetGroupsConfig(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "target_groups_config"

  props = {
    "TargetGroups": (BlockValueConverter(AWS_EC2_SpotFleet_TargetGroup), None),
  }

class AWS_EC2_CapacityReservation_TagSpecification(CloudFormationProperty):
  entity = "AWS::EC2::CapacityReservation"
  tf_block_type = "tag_specification"

  props = {
    "ResourceType": (StringValueConverter(), "resource_type"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_LaunchTemplate_CpuOptions(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "cpu_options"

  props = {
    "ThreadsPerCore": (BasicValueConverter(), "threads_per_core"),
    "CoreCount": (BasicValueConverter(), "core_count"),
  }

class AWS_EC2_Instance_ElasticInferenceAccelerator(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "elastic_inference_accelerator"

  props = {
    "Count": (BasicValueConverter(), "count"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_EC2_SpotFleet_GroupIdentifier(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "group_identifier"

  props = {
    "GroupId": (StringValueConverter(), "group_id"),
  }

class AWS_EC2_Instance_BlockDeviceMapping(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "block_device_mapping"

  props = {
    "DeviceName": (StringValueConverter(), "device_name"),
    "Ebs": (AWS_EC2_Instance_Ebs, "ebs"),
    "NoDevice": (AWS_EC2_Instance_NoDevice, "no_device"),
    "VirtualName": (StringValueConverter(), "virtual_name"),
  }

class AWS_EC2_SpotFleet_BlockDeviceMapping(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "block_device_mapping"

  props = {
    "DeviceName": (StringValueConverter(), "device_name"),
    "Ebs": (AWS_EC2_SpotFleet_EbsBlockDevice, "ebs"),
    "NoDevice": (StringValueConverter(), "no_device"),
    "VirtualName": (StringValueConverter(), "virtual_name"),
  }

class AWS_EC2_Instance_PrivateIpAddressSpecification(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "private_ip_address_specification"

  props = {
    "Primary": (BasicValueConverter(), "primary"),
    "PrivateIpAddress": (StringValueConverter(), "private_ip_address"),
  }

class AWS_EC2_EC2Fleet_TagSpecification(CloudFormationProperty):
  entity = "AWS::EC2::EC2Fleet"
  tf_block_type = "tag_specification"

  props = {
    "ResourceType": (StringValueConverter(), "resource_type"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_LaunchTemplate_LaunchTemplateElasticInferenceAccelerator(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "launch_template_elastic_inference_accelerator"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Count": (BasicValueConverter(), "count"),
  }

class AWS_EC2_EC2Fleet_SpotOptionsRequest(CloudFormationProperty):
  entity = "AWS::EC2::EC2Fleet"
  tf_block_type = "spot_options_request"

  props = {
    "SingleAvailabilityZone": (BasicValueConverter(), "single_availability_zone"),
    "AllocationStrategy": (StringValueConverter(), "allocation_strategy"),
    "SingleInstanceType": (BasicValueConverter(), "single_instance_type"),
    "MinTargetCapacity": (BasicValueConverter(), "min_target_capacity"),
    "MaxTotalPrice": (StringValueConverter(), "max_total_price"),
    "InstanceInterruptionBehavior": (StringValueConverter(), "instance_interruption_behavior"),
    "InstancePoolsToUseCount": (BasicValueConverter(), "instance_pools_to_use_count"),
  }

class AWS_EC2_RouteTable(CloudFormationResource):
  terraform_resource = "aws_ec2_route_table"

  resource_type = "AWS::EC2::RouteTable"

  props = {
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "VpcId": (StringValueConverter(), "vpc_id"),
  }

class AWS_EC2_VPCPeeringConnection(CloudFormationResource):
  terraform_resource = "aws_ec2_vpc_peering_connection"

  resource_type = "AWS::EC2::VPCPeeringConnection"

  props = {
    "PeerOwnerId": (StringValueConverter(), "peer_owner_id"),
    "PeerRegion": (StringValueConverter(), "peer_region"),
    "PeerRoleArn": (StringValueConverter(), "peer_role_arn"),
    "PeerVpcId": (StringValueConverter(), "peer_vpc_id"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "VpcId": (StringValueConverter(), "vpc_id"),
  }

class AWS_EC2_TransitGateway(CloudFormationResource):
  terraform_resource = "aws_ec2_transit_gateway"

  resource_type = "AWS::EC2::TransitGateway"

  props = {
    "DefaultRouteTablePropagation": (StringValueConverter(), "default_route_table_propagation"),
    "Description": (StringValueConverter(), "description"),
    "AutoAcceptSharedAttachments": (StringValueConverter(), "auto_accept_shared_attachments"),
    "DefaultRouteTableAssociation": (StringValueConverter(), "default_route_table_association"),
    "VpnEcmpSupport": (StringValueConverter(), "vpn_ecmp_support"),
    "DnsSupport": (StringValueConverter(), "dns_support"),
    "AmazonSideAsn": (BasicValueConverter(), "amazon_side_asn"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_CapacityReservation(CloudFormationResource):
  terraform_resource = "aws_ec2_capacity_reservation"

  resource_type = "AWS::EC2::CapacityReservation"

  props = {
    "Tenancy": (StringValueConverter(), "tenancy"),
    "EndDateType": (StringValueConverter(), "end_date_type"),
    "InstanceCount": (BasicValueConverter(), "instance_count"),
    "TagSpecifications": (BlockValueConverter(AWS_EC2_CapacityReservation_TagSpecification), None),
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "InstancePlatform": (StringValueConverter(), "instance_platform"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "EphemeralStorage": (BasicValueConverter(), "ephemeral_storage"),
    "InstanceMatchCriteria": (StringValueConverter(), "instance_match_criteria"),
    "EndDate": (StringValueConverter(), "end_date"),
    "EbsOptimized": (BasicValueConverter(), "ebs_optimized"),
  }

class AWS_EC2_VPCEndpointServicePermissions(CloudFormationResource):
  terraform_resource = "aws_ec2_vpc_endpoint_service_permissions"

  resource_type = "AWS::EC2::VPCEndpointServicePermissions"

  props = {
    "AllowedPrincipals": (ListValueConverter(StringValueConverter()), "allowed_principals"),
    "ServiceId": (StringValueConverter(), "service_id"),
  }

class AWS_EC2_TransitGatewayRouteTableAssociation(CloudFormationResource):
  terraform_resource = "aws_ec2_transit_gateway_route_table_association"

  resource_type = "AWS::EC2::TransitGatewayRouteTableAssociation"

  props = {
    "TransitGatewayRouteTableId": (StringValueConverter(), "transit_gateway_route_table_id"),
    "TransitGatewayAttachmentId": (StringValueConverter(), "transit_gateway_attachment_id"),
  }

class AWS_EC2_Volume(CloudFormationResource):
  terraform_resource = "aws_ec2_volume"

  resource_type = "AWS::EC2::Volume"

  props = {
    "AutoEnableIO": (BasicValueConverter(), "auto_enable_io"),
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "Encrypted": (BasicValueConverter(), "encrypted"),
    "Iops": (BasicValueConverter(), "iops"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "MultiAttachEnabled": (BasicValueConverter(), "multi_attach_enabled"),
    "OutpostArn": (StringValueConverter(), "outpost_arn"),
    "Size": (BasicValueConverter(), "size"),
    "SnapshotId": (StringValueConverter(), "snapshot_id"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "VolumeType": (StringValueConverter(), "volume_type"),
  }

class AWS_EC2_EIP(CloudFormationResource):
  terraform_resource = "aws_ec2_eip"

  resource_type = "AWS::EC2::EIP"

  props = {
    "Domain": (StringValueConverter(), "domain"),
    "InstanceId": (StringValueConverter(), "instance_id"),
    "PublicIpv4Pool": (StringValueConverter(), "public_ipv4_pool"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_LocalGatewayRoute(CloudFormationResource):
  terraform_resource = "aws_ec2_local_gateway_route"

  resource_type = "AWS::EC2::LocalGatewayRoute"

  props = {
    "DestinationCidrBlock": (StringValueConverter(), "destination_cidr_block"),
    "LocalGatewayRouteTableId": (StringValueConverter(), "local_gateway_route_table_id"),
    "LocalGatewayVirtualInterfaceGroupId": (StringValueConverter(), "local_gateway_virtual_interface_group_id"),
  }

class AWS_EC2_VPCEndpointConnectionNotification(CloudFormationResource):
  terraform_resource = "aws_ec2_vpc_endpoint_connection_notification"

  resource_type = "AWS::EC2::VPCEndpointConnectionNotification"

  props = {
    "ConnectionEvents": (ListValueConverter(StringValueConverter()), "connection_events"),
    "VPCEndpointId": (StringValueConverter(), "vpc_endpoint_id"),
    "ServiceId": (StringValueConverter(), "service_id"),
    "ConnectionNotificationArn": (StringValueConverter(), "connection_notification_arn"),
  }

class AWS_EC2_FlowLog(CloudFormationResource):
  terraform_resource = "aws_ec2_flow_log"

  resource_type = "AWS::EC2::FlowLog"

  props = {
    "DeliverLogsPermissionArn": (StringValueConverter(), "deliver_logs_permission_arn"),
    "LogDestination": (StringValueConverter(), "log_destination"),
    "LogDestinationType": (StringValueConverter(), "log_destination_type"),
    "LogGroupName": (StringValueConverter(), "log_group_name"),
    "ResourceId": (StringValueConverter(), "resource_id"),
    "ResourceType": (StringValueConverter(), "resource_type"),
    "TrafficType": (StringValueConverter(), "traffic_type"),
  }

class AWS_EC2_SecurityGroupEgress(CloudFormationResource):
  terraform_resource = "aws_ec2_security_group_egress"

  resource_type = "AWS::EC2::SecurityGroupEgress"

  props = {
    "CidrIp": (StringValueConverter(), "cidr_ip"),
    "CidrIpv6": (StringValueConverter(), "cidr_ipv6"),
    "Description": (StringValueConverter(), "description"),
    "DestinationPrefixListId": (StringValueConverter(), "destination_prefix_list_id"),
    "DestinationSecurityGroupId": (StringValueConverter(), "destination_security_group_id"),
    "FromPort": (BasicValueConverter(), "from_port"),
    "GroupId": (StringValueConverter(), "group_id"),
    "IpProtocol": (StringValueConverter(), "ip_protocol"),
    "ToPort": (BasicValueConverter(), "to_port"),
  }

class AWS_EC2_TransitGatewayAttachment(CloudFormationResource):
  terraform_resource = "aws_ec2_transit_gateway_attachment"

  resource_type = "AWS::EC2::TransitGatewayAttachment"

  props = {
    "TransitGatewayId": (StringValueConverter(), "transit_gateway_id"),
    "VpcId": (StringValueConverter(), "vpc_id"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_Subnet(CloudFormationResource):
  terraform_resource = "aws_ec2_subnet"

  resource_type = "AWS::EC2::Subnet"

  props = {
    "AssignIpv6AddressOnCreation": (BasicValueConverter(), "assign_ipv6_address_on_creation"),
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "CidrBlock": (StringValueConverter(), "cidr_block"),
    "Ipv6CidrBlock": (StringValueConverter(), "ipv6_cidr_block"),
    "MapPublicIpOnLaunch": (BasicValueConverter(), "map_public_ip_on_launch"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "VpcId": (StringValueConverter(), "vpc_id"),
  }

class AWS_EC2_DHCPOptions(CloudFormationResource):
  terraform_resource = "aws_ec2_dhcp_options"

  resource_type = "AWS::EC2::DHCPOptions"

  props = {
    "DomainName": (StringValueConverter(), "domain_name"),
    "DomainNameServers": (ListValueConverter(StringValueConverter()), "domain_name_servers"),
    "NetbiosNameServers": (ListValueConverter(StringValueConverter()), "netbios_name_servers"),
    "NetbiosNodeType": (BasicValueConverter(), "netbios_node_type"),
    "NtpServers": (ListValueConverter(StringValueConverter()), "ntp_servers"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_EgressOnlyInternetGateway(CloudFormationResource):
  terraform_resource = "aws_ec2_egress_only_internet_gateway"

  resource_type = "AWS::EC2::EgressOnlyInternetGateway"

  props = {
    "VpcId": (StringValueConverter(), "vpc_id"),
  }

class AWS_EC2_NetworkInterfaceAttachment(CloudFormationResource):
  terraform_resource = "aws_ec2_network_interface_attachment"

  resource_type = "AWS::EC2::NetworkInterfaceAttachment"

  props = {
    "DeleteOnTermination": (BasicValueConverter(), "delete_on_termination"),
    "DeviceIndex": (StringValueConverter(), "device_index"),
    "InstanceId": (StringValueConverter(), "instance_id"),
    "NetworkInterfaceId": (StringValueConverter(), "network_interface_id"),
  }

class AWS_EC2_CustomerGateway(CloudFormationResource):
  terraform_resource = "aws_ec2_customer_gateway"

  resource_type = "AWS::EC2::CustomerGateway"

  props = {
    "BgpAsn": (BasicValueConverter(), "bgp_asn"),
    "IpAddress": (StringValueConverter(), "ip_address"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_EC2_EIPAssociation(CloudFormationResource):
  terraform_resource = "aws_ec2_eip_association"

  resource_type = "AWS::EC2::EIPAssociation"

  props = {
    "AllocationId": (StringValueConverter(), "allocation_id"),
    "EIP": (StringValueConverter(), "eip"),
    "InstanceId": (StringValueConverter(), "instance_id"),
    "NetworkInterfaceId": (StringValueConverter(), "network_interface_id"),
    "PrivateIpAddress": (StringValueConverter(), "private_ip_address"),
  }

class AWS_EC2_VPNGateway(CloudFormationResource):
  terraform_resource = "aws_ec2_vpn_gateway"

  resource_type = "AWS::EC2::VPNGateway"

  props = {
    "AmazonSideAsn": (BasicValueConverter(), "amazon_side_asn"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_EC2_VPNConnection(CloudFormationResource):
  terraform_resource = "aws_ec2_vpn_connection"

  resource_type = "AWS::EC2::VPNConnection"

  props = {
    "CustomerGatewayId": (StringValueConverter(), "customer_gateway_id"),
    "StaticRoutesOnly": (BasicValueConverter(), "static_routes_only"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "TransitGatewayId": (StringValueConverter(), "transit_gateway_id"),
    "Type": (StringValueConverter(), "type"),
    "VpnGatewayId": (StringValueConverter(), "vpn_gateway_id"),
    "VpnTunnelOptionsSpecifications": (BlockValueConverter(AWS_EC2_VPNConnection_VpnTunnelOptionsSpecification), None),
  }

class AWS_EC2_TransitGatewayRouteTable(CloudFormationResource):
  terraform_resource = "aws_ec2_transit_gateway_route_table"

  resource_type = "AWS::EC2::TransitGatewayRouteTable"

  props = {
    "TransitGatewayId": (StringValueConverter(), "transit_gateway_id"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_VPCEndpointService(CloudFormationResource):
  terraform_resource = "aws_ec2_vpc_endpoint_service"

  resource_type = "AWS::EC2::VPCEndpointService"

  props = {
    "NetworkLoadBalancerArns": (ListValueConverter(StringValueConverter()), "network_load_balancer_arns"),
    "AcceptanceRequired": (BasicValueConverter(), "acceptance_required"),
  }

class AWS_EC2_ClientVpnRoute(CloudFormationResource):
  terraform_resource = "aws_ec2_client_vpn_route"

  resource_type = "AWS::EC2::ClientVpnRoute"

  props = {
    "ClientVpnEndpointId": (StringValueConverter(), "client_vpn_endpoint_id"),
    "TargetVpcSubnetId": (StringValueConverter(), "target_vpc_subnet_id"),
    "Description": (StringValueConverter(), "description"),
    "DestinationCidrBlock": (StringValueConverter(), "destination_cidr_block"),
  }

class AWS_EC2_PlacementGroup(CloudFormationResource):
  terraform_resource = "aws_ec2_placement_group"

  resource_type = "AWS::EC2::PlacementGroup"

  props = {
    "Strategy": (StringValueConverter(), "strategy"),
  }

class AWS_EC2_GatewayRouteTableAssociation(CloudFormationResource):
  terraform_resource = "aws_ec2_gateway_route_table_association"

  resource_type = "AWS::EC2::GatewayRouteTableAssociation"

  props = {
    "RouteTableId": (StringValueConverter(), "route_table_id"),
    "GatewayId": (StringValueConverter(), "gateway_id"),
  }

class AWS_EC2_NetworkAclEntry(CloudFormationResource):
  terraform_resource = "aws_ec2_network_acl_entry"

  resource_type = "AWS::EC2::NetworkAclEntry"

  props = {
    "CidrBlock": (StringValueConverter(), "cidr_block"),
    "Egress": (BasicValueConverter(), "egress"),
    "Icmp": (AWS_EC2_NetworkAclEntry_Icmp, "icmp"),
    "Ipv6CidrBlock": (StringValueConverter(), "ipv6_cidr_block"),
    "NetworkAclId": (StringValueConverter(), "network_acl_id"),
    "PortRange": (AWS_EC2_NetworkAclEntry_PortRange, "port_range"),
    "Protocol": (BasicValueConverter(), "protocol"),
    "RuleAction": (StringValueConverter(), "rule_action"),
    "RuleNumber": (BasicValueConverter(), "rule_number"),
  }

class AWS_EC2_InternetGateway(CloudFormationResource):
  terraform_resource = "aws_ec2_internet_gateway"

  resource_type = "AWS::EC2::InternetGateway"

  props = {
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_VPNConnectionRoute(CloudFormationResource):
  terraform_resource = "aws_ec2_vpn_connection_route"

  resource_type = "AWS::EC2::VPNConnectionRoute"

  props = {
    "DestinationCidrBlock": (StringValueConverter(), "destination_cidr_block"),
    "VpnConnectionId": (StringValueConverter(), "vpn_connection_id"),
  }

class AWS_EC2_NetworkInterfacePermission(CloudFormationResource):
  terraform_resource = "aws_ec2_network_interface_permission"

  resource_type = "AWS::EC2::NetworkInterfacePermission"

  props = {
    "AwsAccountId": (StringValueConverter(), "aws_account_id"),
    "NetworkInterfaceId": (StringValueConverter(), "network_interface_id"),
    "Permission": (StringValueConverter(), "permission"),
  }

class AWS_EC2_TrafficMirrorFilter(CloudFormationResource):
  terraform_resource = "aws_ec2_traffic_mirror_filter"

  resource_type = "AWS::EC2::TrafficMirrorFilter"

  props = {
    "Description": (StringValueConverter(), "description"),
    "NetworkServices": (ListValueConverter(StringValueConverter()), "network_services"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_SecurityGroupIngress(CloudFormationResource):
  terraform_resource = "aws_ec2_security_group_ingress"

  resource_type = "AWS::EC2::SecurityGroupIngress"

  props = {
    "CidrIp": (StringValueConverter(), "cidr_ip"),
    "CidrIpv6": (StringValueConverter(), "cidr_ipv6"),
    "Description": (StringValueConverter(), "description"),
    "FromPort": (BasicValueConverter(), "from_port"),
    "GroupId": (StringValueConverter(), "group_id"),
    "GroupName": (StringValueConverter(), "group_name"),
    "IpProtocol": (StringValueConverter(), "ip_protocol"),
    "SourcePrefixListId": (StringValueConverter(), "source_prefix_list_id"),
    "SourceSecurityGroupId": (StringValueConverter(), "source_security_group_id"),
    "SourceSecurityGroupName": (StringValueConverter(), "source_security_group_name"),
    "SourceSecurityGroupOwnerId": (StringValueConverter(), "source_security_group_owner_id"),
    "ToPort": (BasicValueConverter(), "to_port"),
  }

class AWS_EC2_SubnetRouteTableAssociation(CloudFormationResource):
  terraform_resource = "aws_ec2_subnet_route_table_association"

  resource_type = "AWS::EC2::SubnetRouteTableAssociation"

  props = {
    "RouteTableId": (StringValueConverter(), "route_table_id"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
  }

class AWS_EC2_Route(CloudFormationResource):
  terraform_resource = "aws_ec2_route"

  resource_type = "AWS::EC2::Route"

  props = {
    "DestinationCidrBlock": (StringValueConverter(), "destination_cidr_block"),
    "DestinationIpv6CidrBlock": (StringValueConverter(), "destination_ipv6_cidr_block"),
    "EgressOnlyInternetGatewayId": (StringValueConverter(), "egress_only_internet_gateway_id"),
    "GatewayId": (StringValueConverter(), "gateway_id"),
    "InstanceId": (StringValueConverter(), "instance_id"),
    "NatGatewayId": (StringValueConverter(), "nat_gateway_id"),
    "NetworkInterfaceId": (StringValueConverter(), "network_interface_id"),
    "RouteTableId": (StringValueConverter(), "route_table_id"),
    "TransitGatewayId": (StringValueConverter(), "transit_gateway_id"),
    "VpcPeeringConnectionId": (StringValueConverter(), "vpc_peering_connection_id"),
  }

class AWS_EC2_LocalGatewayRouteTableVPCAssociation(CloudFormationResource):
  terraform_resource = "aws_ec2_local_gateway_route_table_vpc_association"

  resource_type = "AWS::EC2::LocalGatewayRouteTableVPCAssociation"

  props = {
    "LocalGatewayRouteTableId": (StringValueConverter(), "local_gateway_route_table_id"),
    "VpcId": (StringValueConverter(), "vpc_id"),
    "Tags": (AWS_EC2_LocalGatewayRouteTableVPCAssociation_Tags, "tags"),
  }

class AWS_EC2_TransitGatewayRouteTablePropagation(CloudFormationResource):
  terraform_resource = "aws_ec2_transit_gateway_route_table_propagation"

  resource_type = "AWS::EC2::TransitGatewayRouteTablePropagation"

  props = {
    "TransitGatewayRouteTableId": (StringValueConverter(), "transit_gateway_route_table_id"),
    "TransitGatewayAttachmentId": (StringValueConverter(), "transit_gateway_attachment_id"),
  }

class AWS_EC2_NetworkInterface(CloudFormationResource):
  terraform_resource = "aws_ec2_network_interface"

  resource_type = "AWS::EC2::NetworkInterface"

  props = {
    "Description": (StringValueConverter(), "description"),
    "GroupSet": (ListValueConverter(StringValueConverter()), "group_set"),
    "InterfaceType": (StringValueConverter(), "interface_type"),
    "Ipv6AddressCount": (BasicValueConverter(), "ipv6_address_count"),
    "Ipv6Addresses": (AWS_EC2_NetworkInterface_InstanceIpv6Address, "ipv6_addresses"),
    "PrivateIpAddress": (StringValueConverter(), "private_ip_address"),
    "PrivateIpAddresses": (BlockValueConverter(AWS_EC2_NetworkInterface_PrivateIpAddressSpecification), None),
    "SecondaryPrivateIpAddressCount": (BasicValueConverter(), "secondary_private_ip_address_count"),
    "SourceDestCheck": (BasicValueConverter(), "source_dest_check"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_ClientVpnAuthorizationRule(CloudFormationResource):
  terraform_resource = "aws_ec2_client_vpn_authorization_rule"

  resource_type = "AWS::EC2::ClientVpnAuthorizationRule"

  props = {
    "ClientVpnEndpointId": (StringValueConverter(), "client_vpn_endpoint_id"),
    "Description": (StringValueConverter(), "description"),
    "AccessGroupId": (StringValueConverter(), "access_group_id"),
    "TargetNetworkCidr": (StringValueConverter(), "target_network_cidr"),
    "AuthorizeAllGroups": (BasicValueConverter(), "authorize_all_groups"),
  }

class AWS_EC2_SubnetNetworkAclAssociation(CloudFormationResource):
  terraform_resource = "aws_ec2_subnet_network_acl_association"

  resource_type = "AWS::EC2::SubnetNetworkAclAssociation"

  props = {
    "NetworkAclId": (StringValueConverter(), "network_acl_id"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
  }

class AWS_EC2_TrafficMirrorSession(CloudFormationResource):
  terraform_resource = "aws_ec2_traffic_mirror_session"

  resource_type = "AWS::EC2::TrafficMirrorSession"

  props = {
    "TrafficMirrorTargetId": (StringValueConverter(), "traffic_mirror_target_id"),
    "Description": (StringValueConverter(), "description"),
    "SessionNumber": (BasicValueConverter(), "session_number"),
    "VirtualNetworkId": (BasicValueConverter(), "virtual_network_id"),
    "PacketLength": (BasicValueConverter(), "packet_length"),
    "NetworkInterfaceId": (StringValueConverter(), "network_interface_id"),
    "TrafficMirrorFilterId": (StringValueConverter(), "traffic_mirror_filter_id"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_SubnetCidrBlock(CloudFormationResource):
  terraform_resource = "aws_ec2_subnet_cidr_block"

  resource_type = "AWS::EC2::SubnetCidrBlock"

  props = {
    "Ipv6CidrBlock": (StringValueConverter(), "ipv6_cidr_block"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
  }

class AWS_EC2_NatGateway(CloudFormationResource):
  terraform_resource = "aws_ec2_nat_gateway"

  resource_type = "AWS::EC2::NatGateway"

  props = {
    "AllocationId": (StringValueConverter(), "allocation_id"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_SecurityGroup(CloudFormationResource):
  terraform_resource = "aws_ec2_security_group"

  resource_type = "AWS::EC2::SecurityGroup"

  props = {
    "GroupDescription": (StringValueConverter(), "group_description"),
    "GroupName": (StringValueConverter(), "group_name"),
    "SecurityGroupEgress": (BlockValueConverter(AWS_EC2_SecurityGroup_Egress), None),
    "SecurityGroupIngress": (BlockValueConverter(AWS_EC2_SecurityGroup_Ingress), None),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "VpcId": (StringValueConverter(), "vpc_id"),
  }

class AWS_EC2_TrafficMirrorFilterRule(CloudFormationResource):
  terraform_resource = "aws_ec2_traffic_mirror_filter_rule"

  resource_type = "AWS::EC2::TrafficMirrorFilterRule"

  props = {
    "DestinationPortRange": (AWS_EC2_TrafficMirrorFilterRule_TrafficMirrorPortRange, "destination_port_range"),
    "Description": (StringValueConverter(), "description"),
    "SourcePortRange": (AWS_EC2_TrafficMirrorFilterRule_TrafficMirrorPortRange, "source_port_range"),
    "RuleAction": (StringValueConverter(), "rule_action"),
    "SourceCidrBlock": (StringValueConverter(), "source_cidr_block"),
    "RuleNumber": (BasicValueConverter(), "rule_number"),
    "DestinationCidrBlock": (StringValueConverter(), "destination_cidr_block"),
    "TrafficMirrorFilterId": (StringValueConverter(), "traffic_mirror_filter_id"),
    "TrafficDirection": (StringValueConverter(), "traffic_direction"),
    "Protocol": (BasicValueConverter(), "protocol"),
  }

class AWS_EC2_VPC(CloudFormationResource):
  terraform_resource = "aws_ec2_vpc"

  resource_type = "AWS::EC2::VPC"

  props = {
    "CidrBlock": (StringValueConverter(), "cidr_block"),
    "EnableDnsHostnames": (BasicValueConverter(), "enable_dns_hostnames"),
    "EnableDnsSupport": (BasicValueConverter(), "enable_dns_support"),
    "InstanceTenancy": (StringValueConverter(), "instance_tenancy"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_TransitGatewayRoute(CloudFormationResource):
  terraform_resource = "aws_ec2_transit_gateway_route"

  resource_type = "AWS::EC2::TransitGatewayRoute"

  props = {
    "TransitGatewayRouteTableId": (StringValueConverter(), "transit_gateway_route_table_id"),
    "DestinationCidrBlock": (StringValueConverter(), "destination_cidr_block"),
    "Blackhole": (BasicValueConverter(), "blackhole"),
    "TransitGatewayAttachmentId": (StringValueConverter(), "transit_gateway_attachment_id"),
  }

class AWS_EC2_NetworkAcl(CloudFormationResource):
  terraform_resource = "aws_ec2_network_acl"

  resource_type = "AWS::EC2::NetworkAcl"

  props = {
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "VpcId": (StringValueConverter(), "vpc_id"),
  }

class AWS_EC2_VPNGatewayRoutePropagation(CloudFormationResource):
  terraform_resource = "aws_ec2_vpn_gateway_route_propagation"

  resource_type = "AWS::EC2::VPNGatewayRoutePropagation"

  props = {
    "RouteTableIds": (ListValueConverter(StringValueConverter()), "route_table_ids"),
    "VpnGatewayId": (StringValueConverter(), "vpn_gateway_id"),
  }

class AWS_EC2_ClientVpnTargetNetworkAssociation(CloudFormationResource):
  terraform_resource = "aws_ec2_client_vpn_target_network_association"

  resource_type = "AWS::EC2::ClientVpnTargetNetworkAssociation"

  props = {
    "ClientVpnEndpointId": (StringValueConverter(), "client_vpn_endpoint_id"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
  }

class AWS_EC2_VolumeAttachment(CloudFormationResource):
  terraform_resource = "aws_ec2_volume_attachment"

  resource_type = "AWS::EC2::VolumeAttachment"

  props = {
    "Device": (StringValueConverter(), "device"),
    "InstanceId": (StringValueConverter(), "instance_id"),
    "VolumeId": (StringValueConverter(), "volume_id"),
  }

class AWS_EC2_Host(CloudFormationResource):
  terraform_resource = "aws_ec2_host"

  resource_type = "AWS::EC2::Host"

  props = {
    "AutoPlacement": (StringValueConverter(), "auto_placement"),
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "HostRecovery": (StringValueConverter(), "host_recovery"),
    "InstanceType": (StringValueConverter(), "instance_type"),
  }

class AWS_EC2_VPCEndpoint(CloudFormationResource):
  terraform_resource = "aws_ec2_vpc_endpoint"

  resource_type = "AWS::EC2::VPCEndpoint"

  props = {
    "PolicyDocument": (StringValueConverter(), "policy_document"),
    "PrivateDnsEnabled": (BasicValueConverter(), "private_dns_enabled"),
    "RouteTableIds": (ListValueConverter(StringValueConverter()), "route_table_ids"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "ServiceName": (StringValueConverter(), "service_name"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "VpcEndpointType": (StringValueConverter(), "vpc_endpoint_type"),
    "VpcId": (StringValueConverter(), "vpc_id"),
  }

class AWS_EC2_VPCGatewayAttachment(CloudFormationResource):
  terraform_resource = "aws_ec2_vpc_gateway_attachment"

  resource_type = "AWS::EC2::VPCGatewayAttachment"

  props = {
    "InternetGatewayId": (StringValueConverter(), "internet_gateway_id"),
    "VpcId": (StringValueConverter(), "vpc_id"),
    "VpnGatewayId": (StringValueConverter(), "vpn_gateway_id"),
  }

class AWS_EC2_VPCCidrBlock(CloudFormationResource):
  terraform_resource = "aws_ec2_vpc_cidr_block"

  resource_type = "AWS::EC2::VPCCidrBlock"

  props = {
    "AmazonProvidedIpv6CidrBlock": (BasicValueConverter(), "amazon_provided_ipv6_cidr_block"),
    "CidrBlock": (StringValueConverter(), "cidr_block"),
    "VpcId": (StringValueConverter(), "vpc_id"),
  }

class AWS_EC2_VPCDHCPOptionsAssociation(CloudFormationResource):
  terraform_resource = "aws_ec2_vpcdhcp_options_association"

  resource_type = "AWS::EC2::VPCDHCPOptionsAssociation"

  props = {
    "DhcpOptionsId": (StringValueConverter(), "dhcp_options_id"),
    "VpcId": (StringValueConverter(), "vpc_id"),
  }

class AWS_EC2_TrafficMirrorTarget(CloudFormationResource):
  terraform_resource = "aws_ec2_traffic_mirror_target"

  resource_type = "AWS::EC2::TrafficMirrorTarget"

  props = {
    "NetworkLoadBalancerArn": (StringValueConverter(), "network_load_balancer_arn"),
    "Description": (StringValueConverter(), "description"),
    "NetworkInterfaceId": (StringValueConverter(), "network_interface_id"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_EC2_LaunchTemplate_BlockDeviceMapping(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "block_device_mapping"

  props = {
    "Ebs": (AWS_EC2_LaunchTemplate_Ebs, "ebs"),
    "NoDevice": (StringValueConverter(), "no_device"),
    "VirtualName": (StringValueConverter(), "virtual_name"),
    "DeviceName": (StringValueConverter(), "device_name"),
  }

class AWS_EC2_SpotFleet_LoadBalancersConfig(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "load_balancers_config"

  props = {
    "ClassicLoadBalancersConfig": (AWS_EC2_SpotFleet_ClassicLoadBalancersConfig, "classic_load_balancers_config"),
    "TargetGroupsConfig": (AWS_EC2_SpotFleet_TargetGroupsConfig, "target_groups_config"),
  }

class AWS_EC2_EC2Fleet_OnDemandOptionsRequest(CloudFormationProperty):
  entity = "AWS::EC2::EC2Fleet"
  tf_block_type = "on_demand_options_request"

  props = {
    "SingleAvailabilityZone": (BasicValueConverter(), "single_availability_zone"),
    "AllocationStrategy": (StringValueConverter(), "allocation_strategy"),
    "SingleInstanceType": (BasicValueConverter(), "single_instance_type"),
    "MinTargetCapacity": (BasicValueConverter(), "min_target_capacity"),
    "MaxTotalPrice": (StringValueConverter(), "max_total_price"),
    "CapacityReservationOptions": (AWS_EC2_EC2Fleet_CapacityReservationOptionsRequest, "capacity_reservation_options"),
  }

class AWS_EC2_EC2Fleet_FleetLaunchTemplateOverridesRequest(CloudFormationProperty):
  entity = "AWS::EC2::EC2Fleet"
  tf_block_type = "fleet_launch_template_overrides_request"

  props = {
    "WeightedCapacity": (BasicValueConverter(), "weighted_capacity"),
    "Placement": (AWS_EC2_EC2Fleet_Placement, "placement"),
    "Priority": (BasicValueConverter(), "priority"),
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "MaxPrice": (StringValueConverter(), "max_price"),
  }

class AWS_EC2_Instance_NetworkInterface(CloudFormationProperty):
  entity = "AWS::EC2::Instance"
  tf_block_type = "network_interface"

  props = {
    "AssociatePublicIpAddress": (BasicValueConverter(), "associate_public_ip_address"),
    "DeleteOnTermination": (BasicValueConverter(), "delete_on_termination"),
    "Description": (StringValueConverter(), "description"),
    "DeviceIndex": (StringValueConverter(), "device_index"),
    "GroupSet": (ListValueConverter(StringValueConverter()), "group_set"),
    "Ipv6AddressCount": (BasicValueConverter(), "ipv6_address_count"),
    "Ipv6Addresses": (BlockValueConverter(AWS_EC2_Instance_InstanceIpv6Address), None),
    "NetworkInterfaceId": (StringValueConverter(), "network_interface_id"),
    "PrivateIpAddress": (StringValueConverter(), "private_ip_address"),
    "PrivateIpAddresses": (BlockValueConverter(AWS_EC2_Instance_PrivateIpAddressSpecification), None),
    "SecondaryPrivateIpAddressCount": (BasicValueConverter(), "secondary_private_ip_address_count"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
  }

class AWS_EC2_SpotFleet_InstanceNetworkInterfaceSpecification(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "instance_network_interface_specification"

  props = {
    "AssociatePublicIpAddress": (BasicValueConverter(), "associate_public_ip_address"),
    "DeleteOnTermination": (BasicValueConverter(), "delete_on_termination"),
    "Description": (StringValueConverter(), "description"),
    "DeviceIndex": (BasicValueConverter(), "device_index"),
    "Groups": (ListValueConverter(StringValueConverter()), "groups"),
    "Ipv6AddressCount": (BasicValueConverter(), "ipv6_address_count"),
    "Ipv6Addresses": (BlockValueConverter(AWS_EC2_SpotFleet_InstanceIpv6Address), None),
    "NetworkInterfaceId": (StringValueConverter(), "network_interface_id"),
    "PrivateIpAddresses": (BlockValueConverter(AWS_EC2_SpotFleet_PrivateIpAddressSpecification), None),
    "SecondaryPrivateIpAddressCount": (BasicValueConverter(), "secondary_private_ip_address_count"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
  }

class AWS_EC2_ClientVpnEndpoint_ClientAuthenticationRequest(CloudFormationProperty):
  entity = "AWS::EC2::ClientVpnEndpoint"
  tf_block_type = "client_authentication_request"

  props = {
    "MutualAuthentication": (AWS_EC2_ClientVpnEndpoint_CertificateAuthenticationRequest, "mutual_authentication"),
    "Type": (StringValueConverter(), "type"),
    "FederatedAuthentication": (AWS_EC2_ClientVpnEndpoint_FederatedAuthenticationRequest, "federated_authentication"),
    "ActiveDirectory": (AWS_EC2_ClientVpnEndpoint_DirectoryServiceAuthenticationRequest, "active_directory"),
  }

class AWS_EC2_SpotFleet_SpotFleetLaunchSpecification(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "spot_fleet_launch_specification"

  props = {
    "BlockDeviceMappings": (BlockValueConverter(AWS_EC2_SpotFleet_BlockDeviceMapping), None),
    "EbsOptimized": (BasicValueConverter(), "ebs_optimized"),
    "IamInstanceProfile": (AWS_EC2_SpotFleet_IamInstanceProfileSpecification, "iam_instance_profile"),
    "ImageId": (StringValueConverter(), "image_id"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "KernelId": (StringValueConverter(), "kernel_id"),
    "KeyName": (StringValueConverter(), "key_name"),
    "Monitoring": (AWS_EC2_SpotFleet_SpotFleetMonitoring, "monitoring"),
    "NetworkInterfaces": (BlockValueConverter(AWS_EC2_SpotFleet_InstanceNetworkInterfaceSpecification), None),
    "Placement": (AWS_EC2_SpotFleet_SpotPlacement, "placement"),
    "RamdiskId": (StringValueConverter(), "ramdisk_id"),
    "SecurityGroups": (BlockValueConverter(AWS_EC2_SpotFleet_GroupIdentifier), None),
    "SpotPrice": (StringValueConverter(), "spot_price"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
    "TagSpecifications": (BlockValueConverter(AWS_EC2_SpotFleet_SpotFleetTagSpecification), None),
    "UserData": (StringValueConverter(), "user_data"),
    "WeightedCapacity": (BasicValueConverter(), "weighted_capacity"),
  }

class AWS_EC2_SpotFleet_SpotFleetRequestConfigData(CloudFormationProperty):
  entity = "AWS::EC2::SpotFleet"
  tf_block_type = "spot_fleet_request_config_data"

  props = {
    "AllocationStrategy": (StringValueConverter(), "allocation_strategy"),
    "ExcessCapacityTerminationPolicy": (StringValueConverter(), "excess_capacity_termination_policy"),
    "IamFleetRole": (StringValueConverter(), "iam_fleet_role"),
    "InstanceInterruptionBehavior": (StringValueConverter(), "instance_interruption_behavior"),
    "LaunchSpecifications": (BlockValueConverter(AWS_EC2_SpotFleet_SpotFleetLaunchSpecification), None),
    "LaunchTemplateConfigs": (BlockValueConverter(AWS_EC2_SpotFleet_LaunchTemplateConfig), None),
    "LoadBalancersConfig": (AWS_EC2_SpotFleet_LoadBalancersConfig, "load_balancers_config"),
    "ReplaceUnhealthyInstances": (BasicValueConverter(), "replace_unhealthy_instances"),
    "SpotPrice": (StringValueConverter(), "spot_price"),
    "TargetCapacity": (BasicValueConverter(), "target_capacity"),
    "TerminateInstancesWithExpiration": (BasicValueConverter(), "terminate_instances_with_expiration"),
    "Type": (StringValueConverter(), "type"),
    "ValidFrom": (StringValueConverter(), "valid_from"),
    "ValidUntil": (StringValueConverter(), "valid_until"),
  }

class AWS_EC2_LaunchTemplate_CapacityReservationSpecification(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "capacity_reservation_specification"

  props = {
    "CapacityReservationPreference": (StringValueConverter(), "capacity_reservation_preference"),
    "CapacityReservationTarget": (AWS_EC2_LaunchTemplate_CapacityReservationTarget, "capacity_reservation_target"),
  }

class AWS_EC2_EC2Fleet_FleetLaunchTemplateConfigRequest(CloudFormationProperty):
  entity = "AWS::EC2::EC2Fleet"
  tf_block_type = "fleet_launch_template_config_request"

  props = {
    "LaunchTemplateSpecification": (AWS_EC2_EC2Fleet_FleetLaunchTemplateSpecificationRequest, "launch_template_specification"),
    "Overrides": (BlockValueConverter(AWS_EC2_EC2Fleet_FleetLaunchTemplateOverridesRequest), None),
  }

class AWS_EC2_Instance(CloudFormationResource):
  terraform_resource = "aws_ec2_instance"

  resource_type = "AWS::EC2::Instance"

  props = {
    "AdditionalInfo": (StringValueConverter(), "additional_info"),
    "Affinity": (StringValueConverter(), "affinity"),
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "BlockDeviceMappings": (BlockValueConverter(AWS_EC2_Instance_BlockDeviceMapping), None),
    "CpuOptions": (AWS_EC2_Instance_CpuOptions, "cpu_options"),
    "CreditSpecification": (AWS_EC2_Instance_CreditSpecification, "credit_specification"),
    "DisableApiTermination": (BasicValueConverter(), "disable_api_termination"),
    "EbsOptimized": (BasicValueConverter(), "ebs_optimized"),
    "ElasticGpuSpecifications": (BlockValueConverter(AWS_EC2_Instance_ElasticGpuSpecification), None),
    "ElasticInferenceAccelerators": (BlockValueConverter(AWS_EC2_Instance_ElasticInferenceAccelerator), None),
    "HibernationOptions": (AWS_EC2_Instance_HibernationOptions, "hibernation_options"),
    "HostId": (StringValueConverter(), "host_id"),
    "HostResourceGroupArn": (StringValueConverter(), "host_resource_group_arn"),
    "IamInstanceProfile": (StringValueConverter(), "iam_instance_profile"),
    "ImageId": (StringValueConverter(), "image_id"),
    "InstanceInitiatedShutdownBehavior": (StringValueConverter(), "instance_initiated_shutdown_behavior"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "Ipv6AddressCount": (BasicValueConverter(), "ipv6_address_count"),
    "Ipv6Addresses": (BlockValueConverter(AWS_EC2_Instance_InstanceIpv6Address), None),
    "KernelId": (StringValueConverter(), "kernel_id"),
    "KeyName": (StringValueConverter(), "key_name"),
    "LaunchTemplate": (AWS_EC2_Instance_LaunchTemplateSpecification, "launch_template"),
    "LicenseSpecifications": (BlockValueConverter(AWS_EC2_Instance_LicenseSpecification), None),
    "Monitoring": (BasicValueConverter(), "monitoring"),
    "NetworkInterfaces": (BlockValueConverter(AWS_EC2_Instance_NetworkInterface), None),
    "PlacementGroupName": (StringValueConverter(), "placement_group_name"),
    "PrivateIpAddress": (StringValueConverter(), "private_ip_address"),
    "RamdiskId": (StringValueConverter(), "ramdisk_id"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "SecurityGroups": (ListValueConverter(StringValueConverter()), "security_groups"),
    "SourceDestCheck": (BasicValueConverter(), "source_dest_check"),
    "SsmAssociations": (BlockValueConverter(AWS_EC2_Instance_SsmAssociation), None),
    "SubnetId": (StringValueConverter(), "subnet_id"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Tenancy": (StringValueConverter(), "tenancy"),
    "UserData": (StringValueConverter(), "user_data"),
    "Volumes": (BlockValueConverter(AWS_EC2_Instance_Volume), None),
  }

class AWS_EC2_SpotFleet(CloudFormationResource):
  terraform_resource = "aws_ec2_spot_fleet"

  resource_type = "AWS::EC2::SpotFleet"

  props = {
    "SpotFleetRequestConfigData": (AWS_EC2_SpotFleet_SpotFleetRequestConfigData, "spot_fleet_request_config_data"),
  }

class AWS_EC2_ClientVpnEndpoint(CloudFormationResource):
  terraform_resource = "aws_ec2_client_vpn_endpoint"

  resource_type = "AWS::EC2::ClientVpnEndpoint"

  props = {
    "ClientCidrBlock": (StringValueConverter(), "client_cidr_block"),
    "ConnectionLogOptions": (AWS_EC2_ClientVpnEndpoint_ConnectionLogOptions, "connection_log_options"),
    "SplitTunnel": (BasicValueConverter(), "split_tunnel"),
    "Description": (StringValueConverter(), "description"),
    "TagSpecifications": (BlockValueConverter(AWS_EC2_ClientVpnEndpoint_TagSpecification), None),
    "VpcId": (StringValueConverter(), "vpc_id"),
    "AuthenticationOptions": (BlockValueConverter(AWS_EC2_ClientVpnEndpoint_ClientAuthenticationRequest), None),
    "ServerCertificateArn": (StringValueConverter(), "server_certificate_arn"),
    "DnsServers": (ListValueConverter(StringValueConverter()), "dns_servers"),
    "TransportProtocol": (StringValueConverter(), "transport_protocol"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "VpnPort": (BasicValueConverter(), "vpn_port"),
  }

class AWS_EC2_EC2Fleet(CloudFormationResource):
  terraform_resource = "aws_ec2_ec2_fleet"

  resource_type = "AWS::EC2::EC2Fleet"

  props = {
    "TargetCapacitySpecification": (AWS_EC2_EC2Fleet_TargetCapacitySpecificationRequest, "target_capacity_specification"),
    "OnDemandOptions": (AWS_EC2_EC2Fleet_OnDemandOptionsRequest, "on_demand_options"),
    "Type": (StringValueConverter(), "type"),
    "ExcessCapacityTerminationPolicy": (StringValueConverter(), "excess_capacity_termination_policy"),
    "TagSpecifications": (BlockValueConverter(AWS_EC2_EC2Fleet_TagSpecification), None),
    "SpotOptions": (AWS_EC2_EC2Fleet_SpotOptionsRequest, "spot_options"),
    "ValidFrom": (StringValueConverter(), "valid_from"),
    "ReplaceUnhealthyInstances": (BasicValueConverter(), "replace_unhealthy_instances"),
    "LaunchTemplateConfigs": (BlockValueConverter(AWS_EC2_EC2Fleet_FleetLaunchTemplateConfigRequest), None),
    "TerminateInstancesWithExpiration": (BasicValueConverter(), "terminate_instances_with_expiration"),
    "ValidUntil": (StringValueConverter(), "valid_until"),
  }

class AWS_EC2_LaunchTemplate_LaunchTemplateData(CloudFormationProperty):
  entity = "AWS::EC2::LaunchTemplate"
  tf_block_type = "launch_template_data"

  props = {
    "SecurityGroups": (ListValueConverter(StringValueConverter()), "security_groups"),
    "TagSpecifications": (BlockValueConverter(AWS_EC2_LaunchTemplate_TagSpecification), None),
    "UserData": (StringValueConverter(), "user_data"),
    "BlockDeviceMappings": (BlockValueConverter(AWS_EC2_LaunchTemplate_BlockDeviceMapping), None),
    "IamInstanceProfile": (AWS_EC2_LaunchTemplate_IamInstanceProfile, "iam_instance_profile"),
    "KernelId": (StringValueConverter(), "kernel_id"),
    "EbsOptimized": (BasicValueConverter(), "ebs_optimized"),
    "ElasticGpuSpecifications": (BlockValueConverter(AWS_EC2_LaunchTemplate_ElasticGpuSpecification), None),
    "ElasticInferenceAccelerators": (BlockValueConverter(AWS_EC2_LaunchTemplate_LaunchTemplateElasticInferenceAccelerator), None),
    "Placement": (AWS_EC2_LaunchTemplate_Placement, "placement"),
    "NetworkInterfaces": (BlockValueConverter(AWS_EC2_LaunchTemplate_NetworkInterface), None),
    "ImageId": (StringValueConverter(), "image_id"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "Monitoring": (AWS_EC2_LaunchTemplate_Monitoring, "monitoring"),
    "HibernationOptions": (AWS_EC2_LaunchTemplate_HibernationOptions, "hibernation_options"),
    "MetadataOptions": (AWS_EC2_LaunchTemplate_MetadataOptions, "metadata_options"),
    "LicenseSpecifications": (BlockValueConverter(AWS_EC2_LaunchTemplate_LicenseSpecification), None),
    "InstanceInitiatedShutdownBehavior": (StringValueConverter(), "instance_initiated_shutdown_behavior"),
    "CpuOptions": (AWS_EC2_LaunchTemplate_CpuOptions, "cpu_options"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "KeyName": (StringValueConverter(), "key_name"),
    "DisableApiTermination": (BasicValueConverter(), "disable_api_termination"),
    "InstanceMarketOptions": (AWS_EC2_LaunchTemplate_InstanceMarketOptions, "instance_market_options"),
    "RamDiskId": (StringValueConverter(), "ram_disk_id"),
    "CapacityReservationSpecification": (AWS_EC2_LaunchTemplate_CapacityReservationSpecification, "capacity_reservation_specification"),
    "CreditSpecification": (AWS_EC2_LaunchTemplate_CreditSpecification, "credit_specification"),
  }

class AWS_EC2_LaunchTemplate(CloudFormationResource):
  terraform_resource = "aws_ec2_launch_template"

  resource_type = "AWS::EC2::LaunchTemplate"

  props = {
    "LaunchTemplateName": (StringValueConverter(), "launch_template_name"),
    "LaunchTemplateData": (AWS_EC2_LaunchTemplate_LaunchTemplateData, "launch_template_data"),
  }

