from . import *

class AWS_OpsWorks_Layer_ShutdownEventConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("shutdown_event_configuration"):
      self.property(w, "DelayUntilElbConnectionsDrained", "delay_until_elb_connections_drained", BasicValueConverter())
      self.property(w, "ExecutionTimeout", "execution_timeout", BasicValueConverter())


class AWS_OpsWorks_App_DataSource(CloudFormationProperty):
  def write(self, w):
    with w.block("data_source"):
      self.property(w, "Arn", "arn", StringValueConverter())
      self.property(w, "DatabaseName", "database_name", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_OpsWorks_Layer_VolumeConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("volume_configuration"):
      self.property(w, "Encrypted", "encrypted", BasicValueConverter())
      self.property(w, "Iops", "iops", BasicValueConverter())
      self.property(w, "MountPoint", "mount_point", StringValueConverter())
      self.property(w, "NumberOfDisks", "number_of_disks", BasicValueConverter())
      self.property(w, "RaidLevel", "raid_level", BasicValueConverter())
      self.property(w, "Size", "size", BasicValueConverter())
      self.property(w, "VolumeType", "volume_type", StringValueConverter())


class AWS_OpsWorks_App_EnvironmentVariable(CloudFormationProperty):
  def write(self, w):
    with w.block("environment_variable"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Secure", "secure", BasicValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_OpsWorks_Instance_EbsBlockDevice(CloudFormationProperty):
  def write(self, w):
    with w.block("ebs_block_device"):
      self.property(w, "DeleteOnTermination", "delete_on_termination", BasicValueConverter())
      self.property(w, "Iops", "iops", BasicValueConverter())
      self.property(w, "SnapshotId", "snapshot_id", StringValueConverter())
      self.property(w, "VolumeSize", "volume_size", BasicValueConverter())
      self.property(w, "VolumeType", "volume_type", StringValueConverter())


class AWS_OpsWorks_Stack_StackConfigurationManager(CloudFormationProperty):
  def write(self, w):
    with w.block("stack_configuration_manager"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())


class AWS_OpsWorks_Layer_LifecycleEventConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("lifecycle_event_configuration"):
      self.block(w, "ShutdownEventConfiguration", AWS_OpsWorks_Layer_ShutdownEventConfiguration)


class AWS_OpsWorks_Stack_RdsDbInstance(CloudFormationProperty):
  def write(self, w):
    with w.block("rds_db_instance"):
      self.property(w, "DbPassword", "db_password", StringValueConverter())
      self.property(w, "DbUser", "db_user", StringValueConverter())
      self.property(w, "RdsDbInstanceArn", "rds_db_instance_arn", StringValueConverter())


class AWS_OpsWorks_Stack_Source(CloudFormationProperty):
  def write(self, w):
    with w.block("source"):
      self.property(w, "Password", "password", StringValueConverter())
      self.property(w, "Revision", "revision", StringValueConverter())
      self.property(w, "SshKey", "ssh_key", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Url", "url", StringValueConverter())
      self.property(w, "Username", "username", StringValueConverter())


class AWS_OpsWorks_Stack_ChefConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("chef_configuration"):
      self.property(w, "BerkshelfVersion", "berkshelf_version", StringValueConverter())
      self.property(w, "ManageBerkshelf", "manage_berkshelf", BasicValueConverter())


class AWS_OpsWorks_App_SslConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("ssl_configuration"):
      self.property(w, "Certificate", "certificate", StringValueConverter())
      self.property(w, "Chain", "chain", StringValueConverter())
      self.property(w, "PrivateKey", "private_key", StringValueConverter())


class AWS_OpsWorks_Layer_AutoScalingThresholds(CloudFormationProperty):
  def write(self, w):
    with w.block("auto_scaling_thresholds"):
      self.property(w, "CpuThreshold", "cpu_threshold", BasicValueConverter())
      self.property(w, "IgnoreMetricsTime", "ignore_metrics_time", BasicValueConverter())
      self.property(w, "InstanceCount", "instance_count", BasicValueConverter())
      self.property(w, "LoadThreshold", "load_threshold", BasicValueConverter())
      self.property(w, "MemoryThreshold", "memory_threshold", BasicValueConverter())
      self.property(w, "ThresholdsWaitTime", "thresholds_wait_time", BasicValueConverter())


class AWS_OpsWorks_Layer_Recipes(CloudFormationProperty):
  def write(self, w):
    with w.block("recipes"):
      self.property(w, "Configure", "configure", ListValueConverter(StringValueConverter()))
      self.property(w, "Deploy", "deploy", ListValueConverter(StringValueConverter()))
      self.property(w, "Setup", "setup", ListValueConverter(StringValueConverter()))
      self.property(w, "Shutdown", "shutdown", ListValueConverter(StringValueConverter()))
      self.property(w, "Undeploy", "undeploy", ListValueConverter(StringValueConverter()))


class AWS_OpsWorks_Stack_ElasticIp(CloudFormationProperty):
  def write(self, w):
    with w.block("elastic_ip"):
      self.property(w, "Ip", "ip", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_OpsWorks_Instance_TimeBasedAutoScaling(CloudFormationProperty):
  def write(self, w):
    with w.block("time_based_auto_scaling"):
      self.property(w, "Friday", "friday", MapValueConverter(StringValueConverter()))
      self.property(w, "Monday", "monday", MapValueConverter(StringValueConverter()))
      self.property(w, "Saturday", "saturday", MapValueConverter(StringValueConverter()))
      self.property(w, "Sunday", "sunday", MapValueConverter(StringValueConverter()))
      self.property(w, "Thursday", "thursday", MapValueConverter(StringValueConverter()))
      self.property(w, "Tuesday", "tuesday", MapValueConverter(StringValueConverter()))
      self.property(w, "Wednesday", "wednesday", MapValueConverter(StringValueConverter()))


class AWS_OpsWorks_App_Source(CloudFormationProperty):
  def write(self, w):
    with w.block("source"):
      self.property(w, "Password", "password", StringValueConverter())
      self.property(w, "Revision", "revision", StringValueConverter())
      self.property(w, "SshKey", "ssh_key", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Url", "url", StringValueConverter())
      self.property(w, "Username", "username", StringValueConverter())


class AWS_OpsWorks_App(CloudFormationResource):
  cfn_type = "AWS::OpsWorks::App"
  tf_type = "aws_ops_works_app" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "AppSource", AWS_OpsWorks_App_Source)
      self.property(w, "Attributes", "attributes", MapValueConverter(StringValueConverter()))
      self.repeated_block(w, "DataSources", AWS_OpsWorks_App_DataSource)
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Domains", "domains", ListValueConverter(StringValueConverter()))
      self.property(w, "EnableSsl", "enable_ssl", BasicValueConverter())
      self.repeated_block(w, "Environment", AWS_OpsWorks_App_EnvironmentVariable)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Shortname", "shortname", StringValueConverter())
      self.block(w, "SslConfiguration", AWS_OpsWorks_App_SslConfiguration)
      self.property(w, "StackId", "stack_id", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_OpsWorks_ElasticLoadBalancerAttachment(CloudFormationResource):
  cfn_type = "AWS::OpsWorks::ElasticLoadBalancerAttachment"
  tf_type = "aws_ops_works_elastic_load_balancer_attachment" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ElasticLoadBalancerName", "elastic_load_balancer_name", StringValueConverter())
      self.property(w, "LayerId", "layer_id", StringValueConverter())


class AWS_OpsWorks_UserProfile(CloudFormationResource):
  cfn_type = "AWS::OpsWorks::UserProfile"
  tf_type = "aws_opsworks_user_profile"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AllowSelfManagement", "allow_self_management", BasicValueConverter())
      self.property(w, "IamUserArn", "user_arn", StringValueConverter())
      self.property(w, "SshPublicKey", "ssh_public_key", StringValueConverter())
      self.property(w, "SshUsername", "ssh_username", StringValueConverter())


class AWS_OpsWorks_Volume(CloudFormationResource):
  cfn_type = "AWS::OpsWorks::Volume"
  tf_type = "aws_ops_works_volume" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Ec2VolumeId", "ec2_volume_id", StringValueConverter())
      self.property(w, "MountPoint", "mount_point", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "StackId", "stack_id", StringValueConverter())


class AWS_OpsWorks_Stack(CloudFormationResource):
  cfn_type = "AWS::OpsWorks::Stack"
  tf_type = "aws_opsworks_stack"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AgentVersion", "agent_version", StringValueConverter())
      self.property(w, "Attributes", "attributes", MapValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping
      self.block(w, "ChefConfiguration", AWS_OpsWorks_Stack_ChefConfiguration) # TODO: Probably not the correct mapping
      self.property(w, "CloneAppIds", "id", ListValueConverter(StringValueConverter()))
      self.property(w, "ClonePermissions", "clone_permissions", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "ConfigurationManager", AWS_OpsWorks_Stack_StackConfigurationManager) # TODO: Probably not the correct mapping
      self.block(w, "CustomCookbooksSource", AWS_OpsWorks_Stack_Source)
      self.property(w, "CustomJson", "custom_json", JsonValueConverter())
      self.property(w, "DefaultAvailabilityZone", "default_availability_zone", StringValueConverter())
      self.property(w, "DefaultInstanceProfileArn", "default_instance_profile_arn", StringValueConverter())
      self.property(w, "DefaultOs", "default_os", StringValueConverter())
      self.property(w, "DefaultRootDeviceType", "default_root_device_type", StringValueConverter())
      self.property(w, "DefaultSshKeyName", "default_ssh_key_name", StringValueConverter())
      self.property(w, "DefaultSubnetId", "default_subnet_id", StringValueConverter())
      self.property(w, "EcsClusterArn", "arn", StringValueConverter())
      self.repeated_block(w, "ElasticIps", AWS_OpsWorks_Stack_ElasticIp) # TODO: Probably not the correct mapping
      self.property(w, "HostnameTheme", "hostname_theme", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.repeated_block(w, "RdsDbInstances", AWS_OpsWorks_Stack_RdsDbInstance) # TODO: Probably not the correct mapping
      self.property(w, "ServiceRoleArn", "service_role_arn", StringValueConverter())
      self.property(w, "SourceStackId", "source_stack_id", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "UseCustomCookbooks", "use_custom_cookbooks", BasicValueConverter())
      self.property(w, "UseOpsworksSecurityGroups", "use_opsworks_security_groups", BasicValueConverter())
      self.property(w, "VpcId", "vpc_id", StringValueConverter())


class AWS_OpsWorks_Instance_BlockDeviceMapping(CloudFormationProperty):
  def write(self, w):
    with w.block("block_device_mapping"):
      self.property(w, "DeviceName", "device_name", StringValueConverter())
      self.block(w, "Ebs", AWS_OpsWorks_Instance_EbsBlockDevice)
      self.property(w, "NoDevice", "no_device", StringValueConverter())
      self.property(w, "VirtualName", "virtual_name", StringValueConverter())


class AWS_OpsWorks_Layer_LoadBasedAutoScaling(CloudFormationProperty):
  def write(self, w):
    with w.block("load_based_auto_scaling"):
      self.block(w, "DownScaling", AWS_OpsWorks_Layer_AutoScalingThresholds)
      self.property(w, "Enable", "enable", BasicValueConverter())
      self.block(w, "UpScaling", AWS_OpsWorks_Layer_AutoScalingThresholds)


class AWS_OpsWorks_Instance(CloudFormationResource):
  cfn_type = "AWS::OpsWorks::Instance"
  tf_type = "aws_opsworks_instance"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AgentVersion", "agent_version", StringValueConverter())
      self.property(w, "AmiId", "ami_id", StringValueConverter())
      self.property(w, "Architecture", "architecture", StringValueConverter())
      self.property(w, "AutoScalingType", "auto_scaling_type", StringValueConverter())
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.repeated_block(w, "BlockDeviceMappings", AWS_OpsWorks_Instance_BlockDeviceMapping) # TODO: Probably not the correct mapping
      self.property(w, "EbsOptimized", "ebs_optimized", BasicValueConverter())
      self.property(w, "ElasticIps", "elastic_ip", ListValueConverter(StringValueConverter()))
      self.property(w, "Hostname", "hostname", StringValueConverter())
      self.property(w, "InstallUpdatesOnBoot", "install_updates_on_boot", BasicValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "LayerIds", "layer_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "Os", "os", StringValueConverter())
      self.property(w, "RootDeviceType", "root_device_type", StringValueConverter())
      self.property(w, "SshKeyName", "ssh_key_name", StringValueConverter())
      self.property(w, "StackId", "stack_id", StringValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())
      self.property(w, "Tenancy", "tenancy", StringValueConverter())
      self.block(w, "TimeBasedAutoScaling", AWS_OpsWorks_Instance_TimeBasedAutoScaling) # TODO: Probably not the correct mapping
      self.property(w, "VirtualizationType", "virtualization_type", StringValueConverter())
      self.property(w, "Volumes", "volumes", ListValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping


class AWS_OpsWorks_Layer(CloudFormationResource):
  cfn_type = "AWS::OpsWorks::Layer"
  tf_type = "aws_ops_works_layer" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Attributes", "attributes", MapValueConverter(StringValueConverter()))
      self.property(w, "AutoAssignElasticIps", "auto_assign_elastic_ips", BasicValueConverter())
      self.property(w, "AutoAssignPublicIps", "auto_assign_public_ips", BasicValueConverter())
      self.property(w, "CustomInstanceProfileArn", "custom_instance_profile_arn", StringValueConverter())
      self.property(w, "CustomJson", "custom_json", JsonValueConverter())
      self.block(w, "CustomRecipes", AWS_OpsWorks_Layer_Recipes)
      self.property(w, "CustomSecurityGroupIds", "custom_security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "EnableAutoHealing", "enable_auto_healing", BasicValueConverter())
      self.property(w, "InstallUpdatesOnBoot", "install_updates_on_boot", BasicValueConverter())
      self.block(w, "LifecycleEventConfiguration", AWS_OpsWorks_Layer_LifecycleEventConfiguration)
      self.block(w, "LoadBasedAutoScaling", AWS_OpsWorks_Layer_LoadBasedAutoScaling)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Packages", "packages", ListValueConverter(StringValueConverter()))
      self.property(w, "Shortname", "shortname", StringValueConverter())
      self.property(w, "StackId", "stack_id", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "UseEbsOptimizedInstances", "use_ebs_optimized_instances", BasicValueConverter())
      self.repeated_block(w, "VolumeConfigurations", AWS_OpsWorks_Layer_VolumeConfiguration)


