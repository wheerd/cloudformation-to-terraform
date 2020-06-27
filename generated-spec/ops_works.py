from . import *

class AWS_OpsWorks_Layer_ShutdownEventConfiguration(CloudFormationProperty):
  entity = "AWS::OpsWorks::Layer"
  tf_block_type = "shutdown_event_configuration"

  props = {
    "DelayUntilElbConnectionsDrained": (BasicValueConverter(), "delay_until_elb_connections_drained"),
    "ExecutionTimeout": (BasicValueConverter(), "execution_timeout"),
  }

class AWS_OpsWorks_App_DataSource(CloudFormationProperty):
  entity = "AWS::OpsWorks::App"
  tf_block_type = "data_source"

  props = {
    "Arn": (StringValueConverter(), "arn"),
    "DatabaseName": (StringValueConverter(), "database_name"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_OpsWorks_Layer_VolumeConfiguration(CloudFormationProperty):
  entity = "AWS::OpsWorks::Layer"
  tf_block_type = "volume_configuration"

  props = {
    "Encrypted": (BasicValueConverter(), "encrypted"),
    "Iops": (BasicValueConverter(), "iops"),
    "MountPoint": (StringValueConverter(), "mount_point"),
    "NumberOfDisks": (BasicValueConverter(), "number_of_disks"),
    "RaidLevel": (BasicValueConverter(), "raid_level"),
    "Size": (BasicValueConverter(), "size"),
    "VolumeType": (StringValueConverter(), "volume_type"),
  }

class AWS_OpsWorks_App_EnvironmentVariable(CloudFormationProperty):
  entity = "AWS::OpsWorks::App"
  tf_block_type = "environment_variable"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Secure": (BasicValueConverter(), "secure"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_OpsWorks_Instance_EbsBlockDevice(CloudFormationProperty):
  entity = "AWS::OpsWorks::Instance"
  tf_block_type = "ebs_block_device"

  props = {
    "DeleteOnTermination": (BasicValueConverter(), "delete_on_termination"),
    "Iops": (BasicValueConverter(), "iops"),
    "SnapshotId": (StringValueConverter(), "snapshot_id"),
    "VolumeSize": (BasicValueConverter(), "volume_size"),
    "VolumeType": (StringValueConverter(), "volume_type"),
  }

class AWS_OpsWorks_Stack_StackConfigurationManager(CloudFormationProperty):
  entity = "AWS::OpsWorks::Stack"
  tf_block_type = "stack_configuration_manager"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Version": (StringValueConverter(), "version"),
  }

class AWS_OpsWorks_Layer_LifecycleEventConfiguration(CloudFormationProperty):
  entity = "AWS::OpsWorks::Layer"
  tf_block_type = "lifecycle_event_configuration"

  props = {
    "ShutdownEventConfiguration": (AWS_OpsWorks_Layer_ShutdownEventConfiguration, "shutdown_event_configuration"),
  }

class AWS_OpsWorks_Stack_RdsDbInstance(CloudFormationProperty):
  entity = "AWS::OpsWorks::Stack"
  tf_block_type = "rds_db_instance"

  props = {
    "DbPassword": (StringValueConverter(), "db_password"),
    "DbUser": (StringValueConverter(), "db_user"),
    "RdsDbInstanceArn": (StringValueConverter(), "rds_db_instance_arn"),
  }

class AWS_OpsWorks_Stack_Source(CloudFormationProperty):
  entity = "AWS::OpsWorks::Stack"
  tf_block_type = "source"

  props = {
    "Password": (StringValueConverter(), "password"),
    "Revision": (StringValueConverter(), "revision"),
    "SshKey": (StringValueConverter(), "ssh_key"),
    "Type": (StringValueConverter(), "type"),
    "Url": (StringValueConverter(), "url"),
    "Username": (StringValueConverter(), "username"),
  }

class AWS_OpsWorks_Stack_ChefConfiguration(CloudFormationProperty):
  entity = "AWS::OpsWorks::Stack"
  tf_block_type = "chef_configuration"

  props = {
    "BerkshelfVersion": (StringValueConverter(), "berkshelf_version"),
    "ManageBerkshelf": (BasicValueConverter(), "manage_berkshelf"),
  }

class AWS_OpsWorks_App_SslConfiguration(CloudFormationProperty):
  entity = "AWS::OpsWorks::App"
  tf_block_type = "ssl_configuration"

  props = {
    "Certificate": (StringValueConverter(), "certificate"),
    "Chain": (StringValueConverter(), "chain"),
    "PrivateKey": (StringValueConverter(), "private_key"),
  }

class AWS_OpsWorks_Layer_AutoScalingThresholds(CloudFormationProperty):
  entity = "AWS::OpsWorks::Layer"
  tf_block_type = "auto_scaling_thresholds"

  props = {
    "CpuThreshold": (BasicValueConverter(), "cpu_threshold"),
    "IgnoreMetricsTime": (BasicValueConverter(), "ignore_metrics_time"),
    "InstanceCount": (BasicValueConverter(), "instance_count"),
    "LoadThreshold": (BasicValueConverter(), "load_threshold"),
    "MemoryThreshold": (BasicValueConverter(), "memory_threshold"),
    "ThresholdsWaitTime": (BasicValueConverter(), "thresholds_wait_time"),
  }

class AWS_OpsWorks_Layer_Recipes(CloudFormationProperty):
  entity = "AWS::OpsWorks::Layer"
  tf_block_type = "recipes"

  props = {
    "Configure": (ListValueConverter(StringValueConverter()), "configure"),
    "Deploy": (ListValueConverter(StringValueConverter()), "deploy"),
    "Setup": (ListValueConverter(StringValueConverter()), "setup"),
    "Shutdown": (ListValueConverter(StringValueConverter()), "shutdown"),
    "Undeploy": (ListValueConverter(StringValueConverter()), "undeploy"),
  }

class AWS_OpsWorks_Stack_ElasticIp(CloudFormationProperty):
  entity = "AWS::OpsWorks::Stack"
  tf_block_type = "elastic_ip"

  props = {
    "Ip": (StringValueConverter(), "ip"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_OpsWorks_Instance_TimeBasedAutoScaling(CloudFormationProperty):
  entity = "AWS::OpsWorks::Instance"
  tf_block_type = "time_based_auto_scaling"

  props = {
    "Friday": (MapValueConverter(StringValueConverter()), "friday"),
    "Monday": (MapValueConverter(StringValueConverter()), "monday"),
    "Saturday": (MapValueConverter(StringValueConverter()), "saturday"),
    "Sunday": (MapValueConverter(StringValueConverter()), "sunday"),
    "Thursday": (MapValueConverter(StringValueConverter()), "thursday"),
    "Tuesday": (MapValueConverter(StringValueConverter()), "tuesday"),
    "Wednesday": (MapValueConverter(StringValueConverter()), "wednesday"),
  }

class AWS_OpsWorks_App_Source(CloudFormationProperty):
  entity = "AWS::OpsWorks::App"
  tf_block_type = "source"

  props = {
    "Password": (StringValueConverter(), "password"),
    "Revision": (StringValueConverter(), "revision"),
    "SshKey": (StringValueConverter(), "ssh_key"),
    "Type": (StringValueConverter(), "type"),
    "Url": (StringValueConverter(), "url"),
    "Username": (StringValueConverter(), "username"),
  }

class AWS_OpsWorks_App(CloudFormationResource):
  terraform_resource = "aws_ops_works_app"

  resource_type = "AWS::OpsWorks::App"

  props = {
    "AppSource": (AWS_OpsWorks_App_Source, "app_source"),
    "Attributes": (MapValueConverter(StringValueConverter()), "attributes"),
    "DataSources": (BlockValueConverter(AWS_OpsWorks_App_DataSource), None),
    "Description": (StringValueConverter(), "description"),
    "Domains": (ListValueConverter(StringValueConverter()), "domains"),
    "EnableSsl": (BasicValueConverter(), "enable_ssl"),
    "Environment": (BlockValueConverter(AWS_OpsWorks_App_EnvironmentVariable), None),
    "Name": (StringValueConverter(), "name"),
    "Shortname": (StringValueConverter(), "shortname"),
    "SslConfiguration": (AWS_OpsWorks_App_SslConfiguration, "ssl_configuration"),
    "StackId": (StringValueConverter(), "stack_id"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_OpsWorks_ElasticLoadBalancerAttachment(CloudFormationResource):
  terraform_resource = "aws_ops_works_elastic_load_balancer_attachment"

  resource_type = "AWS::OpsWorks::ElasticLoadBalancerAttachment"

  props = {
    "ElasticLoadBalancerName": (StringValueConverter(), "elastic_load_balancer_name"),
    "LayerId": (StringValueConverter(), "layer_id"),
  }

class AWS_OpsWorks_UserProfile(CloudFormationResource):
  terraform_resource = "aws_ops_works_user_profile"

  resource_type = "AWS::OpsWorks::UserProfile"

  props = {
    "AllowSelfManagement": (BasicValueConverter(), "allow_self_management"),
    "IamUserArn": (StringValueConverter(), "iam_user_arn"),
    "SshPublicKey": (StringValueConverter(), "ssh_public_key"),
    "SshUsername": (StringValueConverter(), "ssh_username"),
  }

class AWS_OpsWorks_Volume(CloudFormationResource):
  terraform_resource = "aws_ops_works_volume"

  resource_type = "AWS::OpsWorks::Volume"

  props = {
    "Ec2VolumeId": (StringValueConverter(), "ec2_volume_id"),
    "MountPoint": (StringValueConverter(), "mount_point"),
    "Name": (StringValueConverter(), "name"),
    "StackId": (StringValueConverter(), "stack_id"),
  }

class AWS_OpsWorks_Stack(CloudFormationResource):
  terraform_resource = "aws_ops_works_stack"

  resource_type = "AWS::OpsWorks::Stack"

  props = {
    "AgentVersion": (StringValueConverter(), "agent_version"),
    "Attributes": (MapValueConverter(StringValueConverter()), "attributes"),
    "ChefConfiguration": (AWS_OpsWorks_Stack_ChefConfiguration, "chef_configuration"),
    "CloneAppIds": (ListValueConverter(StringValueConverter()), "clone_app_ids"),
    "ClonePermissions": (BasicValueConverter(), "clone_permissions"),
    "ConfigurationManager": (AWS_OpsWorks_Stack_StackConfigurationManager, "configuration_manager"),
    "CustomCookbooksSource": (AWS_OpsWorks_Stack_Source, "custom_cookbooks_source"),
    "CustomJson": (StringValueConverter(), "custom_json"),
    "DefaultAvailabilityZone": (StringValueConverter(), "default_availability_zone"),
    "DefaultInstanceProfileArn": (StringValueConverter(), "default_instance_profile_arn"),
    "DefaultOs": (StringValueConverter(), "default_os"),
    "DefaultRootDeviceType": (StringValueConverter(), "default_root_device_type"),
    "DefaultSshKeyName": (StringValueConverter(), "default_ssh_key_name"),
    "DefaultSubnetId": (StringValueConverter(), "default_subnet_id"),
    "EcsClusterArn": (StringValueConverter(), "ecs_cluster_arn"),
    "ElasticIps": (BlockValueConverter(AWS_OpsWorks_Stack_ElasticIp), None),
    "HostnameTheme": (StringValueConverter(), "hostname_theme"),
    "Name": (StringValueConverter(), "name"),
    "RdsDbInstances": (BlockValueConverter(AWS_OpsWorks_Stack_RdsDbInstance), None),
    "ServiceRoleArn": (StringValueConverter(), "service_role_arn"),
    "SourceStackId": (StringValueConverter(), "source_stack_id"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "UseCustomCookbooks": (BasicValueConverter(), "use_custom_cookbooks"),
    "UseOpsworksSecurityGroups": (BasicValueConverter(), "use_opsworks_security_groups"),
    "VpcId": (StringValueConverter(), "vpc_id"),
  }

class AWS_OpsWorks_Instance_BlockDeviceMapping(CloudFormationProperty):
  entity = "AWS::OpsWorks::Instance"
  tf_block_type = "block_device_mapping"

  props = {
    "DeviceName": (StringValueConverter(), "device_name"),
    "Ebs": (AWS_OpsWorks_Instance_EbsBlockDevice, "ebs"),
    "NoDevice": (StringValueConverter(), "no_device"),
    "VirtualName": (StringValueConverter(), "virtual_name"),
  }

class AWS_OpsWorks_Layer_LoadBasedAutoScaling(CloudFormationProperty):
  entity = "AWS::OpsWorks::Layer"
  tf_block_type = "load_based_auto_scaling"

  props = {
    "DownScaling": (AWS_OpsWorks_Layer_AutoScalingThresholds, "down_scaling"),
    "Enable": (BasicValueConverter(), "enable"),
    "UpScaling": (AWS_OpsWorks_Layer_AutoScalingThresholds, "up_scaling"),
  }

class AWS_OpsWorks_Instance(CloudFormationResource):
  terraform_resource = "aws_ops_works_instance"

  resource_type = "AWS::OpsWorks::Instance"

  props = {
    "AgentVersion": (StringValueConverter(), "agent_version"),
    "AmiId": (StringValueConverter(), "ami_id"),
    "Architecture": (StringValueConverter(), "architecture"),
    "AutoScalingType": (StringValueConverter(), "auto_scaling_type"),
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "BlockDeviceMappings": (BlockValueConverter(AWS_OpsWorks_Instance_BlockDeviceMapping), None),
    "EbsOptimized": (BasicValueConverter(), "ebs_optimized"),
    "ElasticIps": (ListValueConverter(StringValueConverter()), "elastic_ips"),
    "Hostname": (StringValueConverter(), "hostname"),
    "InstallUpdatesOnBoot": (BasicValueConverter(), "install_updates_on_boot"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "LayerIds": (ListValueConverter(StringValueConverter()), "layer_ids"),
    "Os": (StringValueConverter(), "os"),
    "RootDeviceType": (StringValueConverter(), "root_device_type"),
    "SshKeyName": (StringValueConverter(), "ssh_key_name"),
    "StackId": (StringValueConverter(), "stack_id"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
    "Tenancy": (StringValueConverter(), "tenancy"),
    "TimeBasedAutoScaling": (AWS_OpsWorks_Instance_TimeBasedAutoScaling, "time_based_auto_scaling"),
    "VirtualizationType": (StringValueConverter(), "virtualization_type"),
    "Volumes": (ListValueConverter(StringValueConverter()), "volumes"),
  }

class AWS_OpsWorks_Layer(CloudFormationResource):
  terraform_resource = "aws_ops_works_layer"

  resource_type = "AWS::OpsWorks::Layer"

  props = {
    "Attributes": (MapValueConverter(StringValueConverter()), "attributes"),
    "AutoAssignElasticIps": (BasicValueConverter(), "auto_assign_elastic_ips"),
    "AutoAssignPublicIps": (BasicValueConverter(), "auto_assign_public_ips"),
    "CustomInstanceProfileArn": (StringValueConverter(), "custom_instance_profile_arn"),
    "CustomJson": (StringValueConverter(), "custom_json"),
    "CustomRecipes": (AWS_OpsWorks_Layer_Recipes, "custom_recipes"),
    "CustomSecurityGroupIds": (ListValueConverter(StringValueConverter()), "custom_security_group_ids"),
    "EnableAutoHealing": (BasicValueConverter(), "enable_auto_healing"),
    "InstallUpdatesOnBoot": (BasicValueConverter(), "install_updates_on_boot"),
    "LifecycleEventConfiguration": (AWS_OpsWorks_Layer_LifecycleEventConfiguration, "lifecycle_event_configuration"),
    "LoadBasedAutoScaling": (AWS_OpsWorks_Layer_LoadBasedAutoScaling, "load_based_auto_scaling"),
    "Name": (StringValueConverter(), "name"),
    "Packages": (ListValueConverter(StringValueConverter()), "packages"),
    "Shortname": (StringValueConverter(), "shortname"),
    "StackId": (StringValueConverter(), "stack_id"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Type": (StringValueConverter(), "type"),
    "UseEbsOptimizedInstances": (BasicValueConverter(), "use_ebs_optimized_instances"),
    "VolumeConfigurations": (BlockValueConverter(AWS_OpsWorks_Layer_VolumeConfiguration), None),
  }

