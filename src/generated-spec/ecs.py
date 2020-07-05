from . import *

class AWS_ECS_TaskSet_LoadBalancer(CloudFormationProperty):
  def write(self, w):
    with w.block("load_balancer"):
      self.property(w, "ContainerName", "container_name", StringValueConverter())
      self.property(w, "ContainerPort", "container_port", BasicValueConverter())
      self.property(w, "LoadBalancerName", "load_balancer_name", StringValueConverter())
      self.property(w, "TargetGroupArn", "target_group_arn", StringValueConverter())


class AWS_ECS_Service_LoadBalancer(CloudFormationProperty):
  def write(self, w):
    with w.block("load_balancer"):
      self.property(w, "ContainerName", "container_name", StringValueConverter())
      self.property(w, "ContainerPort", "container_port", BasicValueConverter())
      self.property(w, "LoadBalancerName", "load_balancer_name", StringValueConverter())
      self.property(w, "TargetGroupArn", "target_group_arn", StringValueConverter())


class AWS_ECS_TaskDefinition_FirelensConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("firelens_configuration"):
      self.property(w, "Options", "options", MapValueConverter(StringValueConverter()))
      self.property(w, "Type", "type", StringValueConverter())


class AWS_ECS_TaskDefinition_Device(CloudFormationProperty):
  def write(self, w):
    with w.block("device"):
      self.property(w, "ContainerPath", "container_path", StringValueConverter())
      self.property(w, "HostPath", "host_path", StringValueConverter())
      self.property(w, "Permissions", "permissions", ListValueConverter(StringValueConverter()))


class AWS_ECS_TaskDefinition_InferenceAccelerator(CloudFormationProperty):
  def write(self, w):
    with w.block("inference_accelerator"):
      self.property(w, "DeviceName", "device_name", StringValueConverter())
      self.property(w, "DeviceType", "device_type", StringValueConverter())


class AWS_ECS_TaskDefinition_Secret(CloudFormationProperty):
  def write(self, w):
    with w.block("secret"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "ValueFrom", "value_from", StringValueConverter())


class AWS_ECS_Service_PlacementStrategy(CloudFormationProperty):
  def write(self, w):
    with w.block("placement_strategy"):
      self.property(w, "Field", "field", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_ECS_TaskSet_AwsVpcConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("aws_vpc_configuration"):
      self.property(w, "AssignPublicIp", "assign_public_ip", StringValueConverter())
      self.property(w, "SecurityGroups", "security_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "Subnets", "subnets", ListValueConverter(StringValueConverter()))


class AWS_ECS_TaskDefinition_VolumeFrom(CloudFormationProperty):
  def write(self, w):
    with w.block("volume_from"):
      self.property(w, "ReadOnly", "read_only", BasicValueConverter())
      self.property(w, "SourceContainer", "source_container", StringValueConverter())


class AWS_ECS_TaskDefinition_HostEntry(CloudFormationProperty):
  def write(self, w):
    with w.block("host_entry"):
      self.property(w, "Hostname", "hostname", StringValueConverter())
      self.property(w, "IpAddress", "ip_address", StringValueConverter())


class AWS_ECS_TaskDefinition_TaskDefinitionPlacementConstraint(CloudFormationProperty):
  def write(self, w):
    with w.block("task_definition_placement_constraint"):
      self.property(w, "Expression", "expression", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_ECS_Service_DeploymentConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("deployment_configuration"):
      self.property(w, "MaximumPercent", "maximum_percent", BasicValueConverter())
      self.property(w, "MinimumHealthyPercent", "minimum_healthy_percent", BasicValueConverter())


class AWS_ECS_Service_DeploymentController(CloudFormationProperty):
  def write(self, w):
    with w.block("deployment_controller"):
      self.property(w, "Type", "type", StringValueConverter())


class AWS_ECS_TaskDefinition_SystemControl(CloudFormationProperty):
  def write(self, w):
    with w.block("system_control"):
      self.property(w, "Namespace", "namespace", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_ECS_TaskSet_NetworkConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("network_configuration"):
      self.block(w, "AwsVpcConfiguration", AWS_ECS_TaskSet_AwsVpcConfiguration)


class AWS_ECS_Cluster_ClusterSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("cluster_settings"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_ECS_Service_PlacementConstraint(CloudFormationProperty):
  def write(self, w):
    with w.block("placement_constraint"):
      self.property(w, "Expression", "expression", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_ECS_TaskSet_ServiceRegistry(CloudFormationProperty):
  def write(self, w):
    with w.block("service_registry"):
      self.property(w, "ContainerName", "container_name", StringValueConverter())
      self.property(w, "ContainerPort", "container_port", BasicValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "RegistryArn", "registry_arn", StringValueConverter())


class AWS_ECS_CapacityProvider_ManagedScaling(CloudFormationProperty):
  def write(self, w):
    with w.block("managed_scaling"):
      self.property(w, "MinimumScalingStepSize", "minimum_scaling_step_size", BasicValueConverter())
      self.property(w, "MaximumScalingStepSize", "maximum_scaling_step_size", BasicValueConverter())
      self.property(w, "Status", "status", StringValueConverter())
      self.property(w, "TargetCapacity", "target_capacity", BasicValueConverter())


class AWS_ECS_Service_AwsVpcConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("aws_vpc_configuration"):
      self.property(w, "AssignPublicIp", "assign_public_ip", StringValueConverter())
      self.property(w, "SecurityGroups", "security_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "Subnets", "subnets", ListValueConverter(StringValueConverter()))


class AWS_ECS_Service_NetworkConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("network_configuration"):
      self.block(w, "AwsvpcConfiguration", AWS_ECS_Service_AwsVpcConfiguration)


class AWS_ECS_TaskDefinition_Tmpfs(CloudFormationProperty):
  def write(self, w):
    with w.block("tmpfs"):
      self.property(w, "ContainerPath", "container_path", StringValueConverter())
      self.property(w, "MountOptions", "mount_options", ListValueConverter(StringValueConverter()))
      self.property(w, "Size", "size", BasicValueConverter())


class AWS_ECS_TaskDefinition_ResourceRequirement(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_requirement"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_ECS_TaskDefinition_DockerVolumeConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("docker_volume_configuration"):
      self.property(w, "Autoprovision", "autoprovision", BasicValueConverter())
      self.property(w, "Driver", "driver", StringValueConverter())
      self.property(w, "DriverOpts", "driver_opts", MapValueConverter(StringValueConverter()))
      self.property(w, "Labels", "labels", MapValueConverter(StringValueConverter()))
      self.property(w, "Scope", "scope", StringValueConverter())


class AWS_ECS_TaskDefinition_KeyValuePair(CloudFormationProperty):
  def write(self, w):
    with w.block("key_value_pair"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_ECS_TaskDefinition_MountPoint(CloudFormationProperty):
  def write(self, w):
    with w.block("mount_point"):
      self.property(w, "ContainerPath", "container_path", StringValueConverter())
      self.property(w, "ReadOnly", "read_only", BasicValueConverter())
      self.property(w, "SourceVolume", "source_volume", StringValueConverter())


class AWS_ECS_Service_ServiceRegistry(CloudFormationProperty):
  def write(self, w):
    with w.block("service_registry"):
      self.property(w, "ContainerName", "container_name", StringValueConverter())
      self.property(w, "ContainerPort", "container_port", BasicValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "RegistryArn", "registry_arn", StringValueConverter())


class AWS_ECS_TaskDefinition_KernelCapabilities(CloudFormationProperty):
  def write(self, w):
    with w.block("kernel_capabilities"):
      self.property(w, "Add", "add", ListValueConverter(StringValueConverter()))
      self.property(w, "Drop", "drop", ListValueConverter(StringValueConverter()))


class AWS_ECS_CapacityProvider_AutoScalingGroupProvider(CloudFormationProperty):
  def write(self, w):
    with w.block("auto_scaling_group_provider"):
      self.property(w, "AutoScalingGroupArn", "auto_scaling_group_arn", StringValueConverter())
      self.block(w, "ManagedScaling", AWS_ECS_CapacityProvider_ManagedScaling)
      self.property(w, "ManagedTerminationProtection", "managed_termination_protection", StringValueConverter())


class AWS_ECS_TaskDefinition_HealthCheck(CloudFormationProperty):
  def write(self, w):
    with w.block("health_check"):
      self.property(w, "Command", "command", ListValueConverter(StringValueConverter()))
      self.property(w, "Interval", "interval", BasicValueConverter())
      self.property(w, "Retries", "retries", BasicValueConverter())
      self.property(w, "StartPeriod", "start_period", BasicValueConverter())
      self.property(w, "Timeout", "timeout", BasicValueConverter())


class AWS_ECS_TaskDefinition_PortMapping(CloudFormationProperty):
  def write(self, w):
    with w.block("port_mapping"):
      self.property(w, "ContainerPort", "container_port", BasicValueConverter())
      self.property(w, "HostPort", "host_port", BasicValueConverter())
      self.property(w, "Protocol", "protocol", StringValueConverter())


class AWS_ECS_TaskDefinition_Ulimit(CloudFormationProperty):
  def write(self, w):
    with w.block("ulimit"):
      self.property(w, "HardLimit", "hard_limit", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "SoftLimit", "soft_limit", BasicValueConverter())


class AWS_ECS_TaskDefinition_LinuxParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("linux_parameters"):
      self.block(w, "Capabilities", AWS_ECS_TaskDefinition_KernelCapabilities)
      self.repeated_block(w, "Devices", AWS_ECS_TaskDefinition_Device)
      self.property(w, "InitProcessEnabled", "init_process_enabled", BasicValueConverter())
      self.property(w, "MaxSwap", "max_swap", BasicValueConverter())
      self.property(w, "SharedMemorySize", "shared_memory_size", BasicValueConverter())
      self.property(w, "Swappiness", "swappiness", BasicValueConverter())
      self.repeated_block(w, "Tmpfs", AWS_ECS_TaskDefinition_Tmpfs)


class AWS_ECS_TaskDefinition_ContainerDependency(CloudFormationProperty):
  def write(self, w):
    with w.block("container_dependency"):
      self.property(w, "Condition", "condition", StringValueConverter())
      self.property(w, "ContainerName", "container_name", StringValueConverter())


class AWS_ECS_TaskDefinition_ProxyConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("proxy_configuration"):
      self.property(w, "ContainerName", "container_name", StringValueConverter())
      self.repeated_block(w, "ProxyConfigurationProperties", AWS_ECS_TaskDefinition_KeyValuePair)
      self.property(w, "Type", "type", StringValueConverter())


class AWS_ECS_TaskSet_Scale(CloudFormationProperty):
  def write(self, w):
    with w.block("scale"):
      self.property(w, "Unit", "unit", StringValueConverter())
      self.property(w, "Value", "value", BasicValueConverter())


class AWS_ECS_TaskDefinition_HostVolumeProperties(CloudFormationProperty):
  def write(self, w):
    with w.block("host_volume_properties"):
      self.property(w, "SourcePath", "source_path", StringValueConverter())


class AWS_ECS_Cluster_CapacityProviderStrategyItem(CloudFormationProperty):
  def write(self, w):
    with w.block("capacity_provider_strategy_item"):
      self.property(w, "CapacityProvider", "capacity_provider", StringValueConverter())
      self.property(w, "Weight", "weight", BasicValueConverter())
      self.property(w, "Base", "base", BasicValueConverter())


class AWS_ECS_TaskDefinition_RepositoryCredentials(CloudFormationProperty):
  def write(self, w):
    with w.block("repository_credentials"):
      self.property(w, "CredentialsParameter", "credentials_parameter", StringValueConverter())


class AWS_ECS_Cluster(CloudFormationResource):
  cfn_type = "AWS::ECS::Cluster"
  tf_type = "aws_ecs_cluster"
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "ClusterName", "name", StringValueConverter())
      self.repeated_block(w, "ClusterSettings", AWS_ECS_Cluster_ClusterSettings)
      self.property(w, "CapacityProviders", "capacity_providers", ListValueConverter(StringValueConverter()))
      self.repeated_block(w, "DefaultCapacityProviderStrategy", AWS_ECS_Cluster_CapacityProviderStrategyItem)


class AWS_ECS_CapacityProvider(CloudFormationResource):
  cfn_type = "AWS::ECS::CapacityProvider"
  tf_type = "aws_ecs_capacity_provider"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "AutoScalingGroupProvider", AWS_ECS_CapacityProvider_AutoScalingGroupProvider)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_ECS_PrimaryTaskSet(CloudFormationResource):
  cfn_type = "AWS::ECS::PrimaryTaskSet"
  tf_type = "aws_ecs_primary_task_set" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Cluster", "cluster", StringValueConverter())
      self.property(w, "TaskSetId", "task_set_id", StringValueConverter())
      self.property(w, "Service", "service", StringValueConverter())


class AWS_ECS_Service(CloudFormationResource):
  cfn_type = "AWS::ECS::Service"
  tf_type = "aws_ecs_service"
  ref = "id"
  attrs = {
    "Name": "name", # TODO: Probably not the correct mapping
    # Additional TF attributes: cluster, iam_role, launch_type, platform_version
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Cluster", "cluster", StringValueConverter())
      self.block(w, "DeploymentConfiguration", AWS_ECS_Service_DeploymentConfiguration) # TODO: Probably not the correct mapping
      self.block(w, "DeploymentController", AWS_ECS_Service_DeploymentController)
      self.property(w, "DesiredCount", "desired_count", BasicValueConverter())
      self.property(w, "EnableECSManagedTags", "enable_ecs_managed_tags", BasicValueConverter())
      self.property(w, "HealthCheckGracePeriodSeconds", "health_check_grace_period_seconds", BasicValueConverter())
      self.property(w, "LaunchType", "launch_type", StringValueConverter())
      self.repeated_block(w, "LoadBalancers", AWS_ECS_Service_LoadBalancer)
      self.block(w, "NetworkConfiguration", AWS_ECS_Service_NetworkConfiguration)
      self.repeated_block(w, "PlacementConstraints", AWS_ECS_Service_PlacementConstraint)
      self.repeated_block(w, "PlacementStrategies", AWS_ECS_Service_PlacementStrategy) # TODO: Probably not the correct mapping
      self.property(w, "PlatformVersion", "platform_version", StringValueConverter())
      self.property(w, "PropagateTags", "propagate_tags", StringValueConverter())
      self.property(w, "Role", "iam_role", StringValueConverter())
      self.property(w, "SchedulingStrategy", "scheduling_strategy", StringValueConverter())
      self.property(w, "ServiceName", "name", StringValueConverter())
      self.repeated_block(w, "ServiceRegistries", AWS_ECS_Service_ServiceRegistry)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "TaskDefinition", "task_definition", StringValueConverter())


class AWS_ECS_TaskSet(CloudFormationResource):
  cfn_type = "AWS::ECS::TaskSet"
  tf_type = "aws_ecs_task_set" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "Id": "id",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Cluster", "cluster", StringValueConverter())
      self.property(w, "ExternalId", "external_id", StringValueConverter())
      self.property(w, "LaunchType", "launch_type", StringValueConverter())
      self.repeated_block(w, "LoadBalancers", AWS_ECS_TaskSet_LoadBalancer)
      self.block(w, "NetworkConfiguration", AWS_ECS_TaskSet_NetworkConfiguration)
      self.property(w, "PlatformVersion", "platform_version", StringValueConverter())
      self.block(w, "Scale", AWS_ECS_TaskSet_Scale)
      self.property(w, "Service", "service", StringValueConverter())
      self.repeated_block(w, "ServiceRegistries", AWS_ECS_TaskSet_ServiceRegistry)
      self.property(w, "TaskDefinition", "task_definition", StringValueConverter())


class AWS_ECS_TaskDefinition_LogConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("log_configuration"):
      self.property(w, "LogDriver", "log_driver", StringValueConverter())
      self.property(w, "Options", "options", MapValueConverter(StringValueConverter()))
      self.repeated_block(w, "SecretOptions", AWS_ECS_TaskDefinition_Secret)


class AWS_ECS_TaskDefinition_Volume(CloudFormationProperty):
  def write(self, w):
    with w.block("volume"):
      self.block(w, "DockerVolumeConfiguration", AWS_ECS_TaskDefinition_DockerVolumeConfiguration)
      self.block(w, "Host", AWS_ECS_TaskDefinition_HostVolumeProperties)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_ECS_TaskDefinition_ContainerDefinition(CloudFormationProperty):
  def write(self, w):
    with w.block("container_definition"):
      self.property(w, "Command", "command", ListValueConverter(StringValueConverter()))
      self.property(w, "Cpu", "cpu", BasicValueConverter())
      self.repeated_block(w, "DependsOn", AWS_ECS_TaskDefinition_ContainerDependency)
      self.property(w, "DisableNetworking", "disable_networking", BasicValueConverter())
      self.property(w, "DnsSearchDomains", "dns_search_domains", ListValueConverter(StringValueConverter()))
      self.property(w, "DnsServers", "dns_servers", ListValueConverter(StringValueConverter()))
      self.property(w, "DockerLabels", "docker_labels", MapValueConverter(StringValueConverter()))
      self.property(w, "DockerSecurityOptions", "docker_security_options", ListValueConverter(StringValueConverter()))
      self.property(w, "EntryPoint", "entry_point", ListValueConverter(StringValueConverter()))
      self.repeated_block(w, "Environment", AWS_ECS_TaskDefinition_KeyValuePair)
      self.property(w, "Essential", "essential", BasicValueConverter())
      self.repeated_block(w, "ExtraHosts", AWS_ECS_TaskDefinition_HostEntry)
      self.block(w, "FirelensConfiguration", AWS_ECS_TaskDefinition_FirelensConfiguration)
      self.block(w, "HealthCheck", AWS_ECS_TaskDefinition_HealthCheck)
      self.property(w, "Hostname", "hostname", StringValueConverter())
      self.property(w, "Image", "image", StringValueConverter())
      self.property(w, "Interactive", "interactive", BasicValueConverter())
      self.property(w, "Links", "links", ListValueConverter(StringValueConverter()))
      self.block(w, "LinuxParameters", AWS_ECS_TaskDefinition_LinuxParameters)
      self.block(w, "LogConfiguration", AWS_ECS_TaskDefinition_LogConfiguration)
      self.property(w, "Memory", "memory", BasicValueConverter())
      self.property(w, "MemoryReservation", "memory_reservation", BasicValueConverter())
      self.repeated_block(w, "MountPoints", AWS_ECS_TaskDefinition_MountPoint)
      self.property(w, "Name", "name", StringValueConverter())
      self.repeated_block(w, "PortMappings", AWS_ECS_TaskDefinition_PortMapping)
      self.property(w, "Privileged", "privileged", BasicValueConverter())
      self.property(w, "PseudoTerminal", "pseudo_terminal", BasicValueConverter())
      self.property(w, "ReadonlyRootFilesystem", "readonly_root_filesystem", BasicValueConverter())
      self.block(w, "RepositoryCredentials", AWS_ECS_TaskDefinition_RepositoryCredentials)
      self.repeated_block(w, "ResourceRequirements", AWS_ECS_TaskDefinition_ResourceRequirement)
      self.repeated_block(w, "Secrets", AWS_ECS_TaskDefinition_Secret)
      self.property(w, "StartTimeout", "start_timeout", BasicValueConverter())
      self.property(w, "StopTimeout", "stop_timeout", BasicValueConverter())
      self.repeated_block(w, "SystemControls", AWS_ECS_TaskDefinition_SystemControl)
      self.repeated_block(w, "Ulimits", AWS_ECS_TaskDefinition_Ulimit)
      self.property(w, "User", "user", StringValueConverter())
      self.repeated_block(w, "VolumesFrom", AWS_ECS_TaskDefinition_VolumeFrom)
      self.property(w, "WorkingDirectory", "working_directory", StringValueConverter())


class AWS_ECS_TaskDefinition(CloudFormationResource):
  cfn_type = "AWS::ECS::TaskDefinition"
  tf_type = "aws_ecs_task_definition"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, network_mode, revision

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "ContainerDefinitions", AWS_ECS_TaskDefinition_ContainerDefinition)
      self.property(w, "Cpu", "cpu", StringValueConverter())
      self.property(w, "ExecutionRoleArn", "execution_role_arn", StringValueConverter())
      self.property(w, "Family", "family", StringValueConverter())
      self.repeated_block(w, "InferenceAccelerators", AWS_ECS_TaskDefinition_InferenceAccelerator)
      self.property(w, "IpcMode", "ipc_mode", StringValueConverter())
      self.property(w, "Memory", "memory", StringValueConverter())
      self.property(w, "NetworkMode", "network_mode", StringValueConverter())
      self.property(w, "PidMode", "pid_mode", StringValueConverter())
      self.repeated_block(w, "PlacementConstraints", AWS_ECS_TaskDefinition_TaskDefinitionPlacementConstraint)
      self.block(w, "ProxyConfiguration", AWS_ECS_TaskDefinition_ProxyConfiguration)
      self.property(w, "RequiresCompatibilities", "requires_compatibilities", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "TaskRoleArn", "task_role_arn", StringValueConverter())
      self.repeated_block(w, "Volumes", AWS_ECS_TaskDefinition_Volume)


