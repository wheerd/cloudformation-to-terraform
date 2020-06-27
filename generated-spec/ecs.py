from . import *

class AWS_ECS_TaskSet_LoadBalancer(CloudFormationProperty):
  entity = "AWS::ECS::TaskSet"
  tf_block_type = "load_balancer"

  props = {
    "ContainerName": (StringValueConverter(), "container_name"),
    "ContainerPort": (BasicValueConverter(), "container_port"),
    "LoadBalancerName": (StringValueConverter(), "load_balancer_name"),
    "TargetGroupArn": (StringValueConverter(), "target_group_arn"),
  }

class AWS_ECS_Service_LoadBalancer(CloudFormationProperty):
  entity = "AWS::ECS::Service"
  tf_block_type = "load_balancer"

  props = {
    "ContainerName": (StringValueConverter(), "container_name"),
    "ContainerPort": (BasicValueConverter(), "container_port"),
    "LoadBalancerName": (StringValueConverter(), "load_balancer_name"),
    "TargetGroupArn": (StringValueConverter(), "target_group_arn"),
  }

class AWS_ECS_TaskDefinition_FirelensConfiguration(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "firelens_configuration"

  props = {
    "Options": (MapValueConverter(StringValueConverter()), "options"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_ECS_TaskDefinition_Device(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "device"

  props = {
    "ContainerPath": (StringValueConverter(), "container_path"),
    "HostPath": (StringValueConverter(), "host_path"),
    "Permissions": (ListValueConverter(StringValueConverter()), "permissions"),
  }

class AWS_ECS_TaskDefinition_InferenceAccelerator(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "inference_accelerator"

  props = {
    "DeviceName": (StringValueConverter(), "device_name"),
    "DeviceType": (StringValueConverter(), "device_type"),
  }

class AWS_ECS_TaskDefinition_Secret(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "secret"

  props = {
    "Name": (StringValueConverter(), "name"),
    "ValueFrom": (StringValueConverter(), "value_from"),
  }

class AWS_ECS_Service_PlacementStrategy(CloudFormationProperty):
  entity = "AWS::ECS::Service"
  tf_block_type = "placement_strategy"

  props = {
    "Field": (StringValueConverter(), "field"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_ECS_TaskSet_AwsVpcConfiguration(CloudFormationProperty):
  entity = "AWS::ECS::TaskSet"
  tf_block_type = "aws_vpc_configuration"

  props = {
    "AssignPublicIp": (StringValueConverter(), "assign_public_ip"),
    "SecurityGroups": (ListValueConverter(StringValueConverter()), "security_groups"),
    "Subnets": (ListValueConverter(StringValueConverter()), "subnets"),
  }

class AWS_ECS_TaskDefinition_VolumeFrom(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "volume_from"

  props = {
    "ReadOnly": (BasicValueConverter(), "read_only"),
    "SourceContainer": (StringValueConverter(), "source_container"),
  }

class AWS_ECS_TaskDefinition_HostEntry(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "host_entry"

  props = {
    "Hostname": (StringValueConverter(), "hostname"),
    "IpAddress": (StringValueConverter(), "ip_address"),
  }

class AWS_ECS_TaskDefinition_TaskDefinitionPlacementConstraint(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "task_definition_placement_constraint"

  props = {
    "Expression": (StringValueConverter(), "expression"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_ECS_Service_DeploymentConfiguration(CloudFormationProperty):
  entity = "AWS::ECS::Service"
  tf_block_type = "deployment_configuration"

  props = {
    "MaximumPercent": (BasicValueConverter(), "maximum_percent"),
    "MinimumHealthyPercent": (BasicValueConverter(), "minimum_healthy_percent"),
  }

class AWS_ECS_Service_DeploymentController(CloudFormationProperty):
  entity = "AWS::ECS::Service"
  tf_block_type = "deployment_controller"

  props = {
    "Type": (StringValueConverter(), "type"),
  }

class AWS_ECS_TaskDefinition_SystemControl(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "system_control"

  props = {
    "Namespace": (StringValueConverter(), "namespace"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_ECS_TaskSet_NetworkConfiguration(CloudFormationProperty):
  entity = "AWS::ECS::TaskSet"
  tf_block_type = "network_configuration"

  props = {
    "AwsVpcConfiguration": (AWS_ECS_TaskSet_AwsVpcConfiguration, "aws_vpc_configuration"),
  }

class AWS_ECS_Cluster_ClusterSettings(CloudFormationProperty):
  entity = "AWS::ECS::Cluster"
  tf_block_type = "cluster_settings"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_ECS_Service_PlacementConstraint(CloudFormationProperty):
  entity = "AWS::ECS::Service"
  tf_block_type = "placement_constraint"

  props = {
    "Expression": (StringValueConverter(), "expression"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_ECS_TaskSet_ServiceRegistry(CloudFormationProperty):
  entity = "AWS::ECS::TaskSet"
  tf_block_type = "service_registry"

  props = {
    "ContainerName": (StringValueConverter(), "container_name"),
    "ContainerPort": (BasicValueConverter(), "container_port"),
    "Port": (BasicValueConverter(), "port"),
    "RegistryArn": (StringValueConverter(), "registry_arn"),
  }

class AWS_ECS_CapacityProvider_ManagedScaling(CloudFormationProperty):
  entity = "AWS::ECS::CapacityProvider"
  tf_block_type = "managed_scaling"

  props = {
    "MinimumScalingStepSize": (BasicValueConverter(), "minimum_scaling_step_size"),
    "MaximumScalingStepSize": (BasicValueConverter(), "maximum_scaling_step_size"),
    "Status": (StringValueConverter(), "status"),
    "TargetCapacity": (BasicValueConverter(), "target_capacity"),
  }

class AWS_ECS_Service_AwsVpcConfiguration(CloudFormationProperty):
  entity = "AWS::ECS::Service"
  tf_block_type = "aws_vpc_configuration"

  props = {
    "AssignPublicIp": (StringValueConverter(), "assign_public_ip"),
    "SecurityGroups": (ListValueConverter(StringValueConverter()), "security_groups"),
    "Subnets": (ListValueConverter(StringValueConverter()), "subnets"),
  }

class AWS_ECS_Service_NetworkConfiguration(CloudFormationProperty):
  entity = "AWS::ECS::Service"
  tf_block_type = "network_configuration"

  props = {
    "AwsvpcConfiguration": (AWS_ECS_Service_AwsVpcConfiguration, "awsvpc_configuration"),
  }

class AWS_ECS_TaskDefinition_Tmpfs(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "tmpfs"

  props = {
    "ContainerPath": (StringValueConverter(), "container_path"),
    "MountOptions": (ListValueConverter(StringValueConverter()), "mount_options"),
    "Size": (BasicValueConverter(), "size"),
  }

class AWS_ECS_TaskDefinition_ResourceRequirement(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "resource_requirement"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_ECS_TaskDefinition_DockerVolumeConfiguration(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "docker_volume_configuration"

  props = {
    "Autoprovision": (BasicValueConverter(), "autoprovision"),
    "Driver": (StringValueConverter(), "driver"),
    "DriverOpts": (MapValueConverter(StringValueConverter()), "driver_opts"),
    "Labels": (MapValueConverter(StringValueConverter()), "labels"),
    "Scope": (StringValueConverter(), "scope"),
  }

class AWS_ECS_TaskDefinition_KeyValuePair(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "key_value_pair"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_ECS_TaskDefinition_MountPoint(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "mount_point"

  props = {
    "ContainerPath": (StringValueConverter(), "container_path"),
    "ReadOnly": (BasicValueConverter(), "read_only"),
    "SourceVolume": (StringValueConverter(), "source_volume"),
  }

class AWS_ECS_Service_ServiceRegistry(CloudFormationProperty):
  entity = "AWS::ECS::Service"
  tf_block_type = "service_registry"

  props = {
    "ContainerName": (StringValueConverter(), "container_name"),
    "ContainerPort": (BasicValueConverter(), "container_port"),
    "Port": (BasicValueConverter(), "port"),
    "RegistryArn": (StringValueConverter(), "registry_arn"),
  }

class AWS_ECS_TaskDefinition_KernelCapabilities(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "kernel_capabilities"

  props = {
    "Add": (ListValueConverter(StringValueConverter()), "add"),
    "Drop": (ListValueConverter(StringValueConverter()), "drop"),
  }

class AWS_ECS_CapacityProvider_AutoScalingGroupProvider(CloudFormationProperty):
  entity = "AWS::ECS::CapacityProvider"
  tf_block_type = "auto_scaling_group_provider"

  props = {
    "AutoScalingGroupArn": (StringValueConverter(), "auto_scaling_group_arn"),
    "ManagedScaling": (AWS_ECS_CapacityProvider_ManagedScaling, "managed_scaling"),
    "ManagedTerminationProtection": (StringValueConverter(), "managed_termination_protection"),
  }

class AWS_ECS_TaskDefinition_HealthCheck(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "health_check"

  props = {
    "Command": (ListValueConverter(StringValueConverter()), "command"),
    "Interval": (BasicValueConverter(), "interval"),
    "Retries": (BasicValueConverter(), "retries"),
    "StartPeriod": (BasicValueConverter(), "start_period"),
    "Timeout": (BasicValueConverter(), "timeout"),
  }

class AWS_ECS_TaskDefinition_PortMapping(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "port_mapping"

  props = {
    "ContainerPort": (BasicValueConverter(), "container_port"),
    "HostPort": (BasicValueConverter(), "host_port"),
    "Protocol": (StringValueConverter(), "protocol"),
  }

class AWS_ECS_TaskDefinition_Ulimit(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "ulimit"

  props = {
    "HardLimit": (BasicValueConverter(), "hard_limit"),
    "Name": (StringValueConverter(), "name"),
    "SoftLimit": (BasicValueConverter(), "soft_limit"),
  }

class AWS_ECS_TaskDefinition_LinuxParameters(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "linux_parameters"

  props = {
    "Capabilities": (AWS_ECS_TaskDefinition_KernelCapabilities, "capabilities"),
    "Devices": (BlockValueConverter(AWS_ECS_TaskDefinition_Device), None),
    "InitProcessEnabled": (BasicValueConverter(), "init_process_enabled"),
    "MaxSwap": (BasicValueConverter(), "max_swap"),
    "SharedMemorySize": (BasicValueConverter(), "shared_memory_size"),
    "Swappiness": (BasicValueConverter(), "swappiness"),
    "Tmpfs": (BlockValueConverter(AWS_ECS_TaskDefinition_Tmpfs), None),
  }

class AWS_ECS_TaskDefinition_ContainerDependency(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "container_dependency"

  props = {
    "Condition": (StringValueConverter(), "condition"),
    "ContainerName": (StringValueConverter(), "container_name"),
  }

class AWS_ECS_TaskDefinition_ProxyConfiguration(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "proxy_configuration"

  props = {
    "ContainerName": (StringValueConverter(), "container_name"),
    "ProxyConfigurationProperties": (BlockValueConverter(AWS_ECS_TaskDefinition_KeyValuePair), None),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_ECS_TaskSet_Scale(CloudFormationProperty):
  entity = "AWS::ECS::TaskSet"
  tf_block_type = "scale"

  props = {
    "Unit": (StringValueConverter(), "unit"),
    "Value": (BasicValueConverter(), "value"),
  }

class AWS_ECS_TaskDefinition_HostVolumeProperties(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "host_volume_properties"

  props = {
    "SourcePath": (StringValueConverter(), "source_path"),
  }

class AWS_ECS_Cluster_CapacityProviderStrategyItem(CloudFormationProperty):
  entity = "AWS::ECS::Cluster"
  tf_block_type = "capacity_provider_strategy_item"

  props = {
    "CapacityProvider": (StringValueConverter(), "capacity_provider"),
    "Weight": (BasicValueConverter(), "weight"),
    "Base": (BasicValueConverter(), "base"),
  }

class AWS_ECS_TaskDefinition_RepositoryCredentials(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "repository_credentials"

  props = {
    "CredentialsParameter": (StringValueConverter(), "credentials_parameter"),
  }

class AWS_ECS_Cluster(CloudFormationResource):
  terraform_resource = "aws_ecs_cluster"

  resource_type = "AWS::ECS::Cluster"

  props = {
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "ClusterName": (StringValueConverter(), "cluster_name"),
    "ClusterSettings": (BlockValueConverter(AWS_ECS_Cluster_ClusterSettings), None),
    "CapacityProviders": (ListValueConverter(StringValueConverter()), "capacity_providers"),
    "DefaultCapacityProviderStrategy": (BlockValueConverter(AWS_ECS_Cluster_CapacityProviderStrategyItem), None),
  }

class AWS_ECS_CapacityProvider(CloudFormationResource):
  terraform_resource = "aws_ecs_capacity_provider"

  resource_type = "AWS::ECS::CapacityProvider"

  props = {
    "AutoScalingGroupProvider": (AWS_ECS_CapacityProvider_AutoScalingGroupProvider, "auto_scaling_group_provider"),
    "Name": (StringValueConverter(), "name"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_ECS_PrimaryTaskSet(CloudFormationResource):
  terraform_resource = "aws_ecs_primary_task_set"

  resource_type = "AWS::ECS::PrimaryTaskSet"

  props = {
    "Cluster": (StringValueConverter(), "cluster"),
    "TaskSetId": (StringValueConverter(), "task_set_id"),
    "Service": (StringValueConverter(), "service"),
  }

class AWS_ECS_Service(CloudFormationResource):
  terraform_resource = "aws_ecs_service"

  resource_type = "AWS::ECS::Service"

  props = {
    "Cluster": (StringValueConverter(), "cluster"),
    "DeploymentConfiguration": (AWS_ECS_Service_DeploymentConfiguration, "deployment_configuration"),
    "DeploymentController": (AWS_ECS_Service_DeploymentController, "deployment_controller"),
    "DesiredCount": (BasicValueConverter(), "desired_count"),
    "EnableECSManagedTags": (BasicValueConverter(), "enable_ecs_managed_tags"),
    "HealthCheckGracePeriodSeconds": (BasicValueConverter(), "health_check_grace_period_seconds"),
    "LaunchType": (StringValueConverter(), "launch_type"),
    "LoadBalancers": (BlockValueConverter(AWS_ECS_Service_LoadBalancer), None),
    "NetworkConfiguration": (AWS_ECS_Service_NetworkConfiguration, "network_configuration"),
    "PlacementConstraints": (BlockValueConverter(AWS_ECS_Service_PlacementConstraint), None),
    "PlacementStrategies": (BlockValueConverter(AWS_ECS_Service_PlacementStrategy), None),
    "PlatformVersion": (StringValueConverter(), "platform_version"),
    "PropagateTags": (StringValueConverter(), "propagate_tags"),
    "Role": (StringValueConverter(), "role"),
    "SchedulingStrategy": (StringValueConverter(), "scheduling_strategy"),
    "ServiceName": (StringValueConverter(), "service_name"),
    "ServiceRegistries": (BlockValueConverter(AWS_ECS_Service_ServiceRegistry), None),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "TaskDefinition": (StringValueConverter(), "task_definition"),
  }

class AWS_ECS_TaskSet(CloudFormationResource):
  terraform_resource = "aws_ecs_task_set"

  resource_type = "AWS::ECS::TaskSet"

  props = {
    "Cluster": (StringValueConverter(), "cluster"),
    "ExternalId": (StringValueConverter(), "external_id"),
    "LaunchType": (StringValueConverter(), "launch_type"),
    "LoadBalancers": (BlockValueConverter(AWS_ECS_TaskSet_LoadBalancer), None),
    "NetworkConfiguration": (AWS_ECS_TaskSet_NetworkConfiguration, "network_configuration"),
    "PlatformVersion": (StringValueConverter(), "platform_version"),
    "Scale": (AWS_ECS_TaskSet_Scale, "scale"),
    "Service": (StringValueConverter(), "service"),
    "ServiceRegistries": (BlockValueConverter(AWS_ECS_TaskSet_ServiceRegistry), None),
    "TaskDefinition": (StringValueConverter(), "task_definition"),
  }

class AWS_ECS_TaskDefinition_LogConfiguration(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "log_configuration"

  props = {
    "LogDriver": (StringValueConverter(), "log_driver"),
    "Options": (MapValueConverter(StringValueConverter()), "options"),
    "SecretOptions": (BlockValueConverter(AWS_ECS_TaskDefinition_Secret), None),
  }

class AWS_ECS_TaskDefinition_Volume(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "volume"

  props = {
    "DockerVolumeConfiguration": (AWS_ECS_TaskDefinition_DockerVolumeConfiguration, "docker_volume_configuration"),
    "Host": (AWS_ECS_TaskDefinition_HostVolumeProperties, "host"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_ECS_TaskDefinition_ContainerDefinition(CloudFormationProperty):
  entity = "AWS::ECS::TaskDefinition"
  tf_block_type = "container_definition"

  props = {
    "Command": (ListValueConverter(StringValueConverter()), "command"),
    "Cpu": (BasicValueConverter(), "cpu"),
    "DependsOn": (BlockValueConverter(AWS_ECS_TaskDefinition_ContainerDependency), None),
    "DisableNetworking": (BasicValueConverter(), "disable_networking"),
    "DnsSearchDomains": (ListValueConverter(StringValueConverter()), "dns_search_domains"),
    "DnsServers": (ListValueConverter(StringValueConverter()), "dns_servers"),
    "DockerLabels": (MapValueConverter(StringValueConverter()), "docker_labels"),
    "DockerSecurityOptions": (ListValueConverter(StringValueConverter()), "docker_security_options"),
    "EntryPoint": (ListValueConverter(StringValueConverter()), "entry_point"),
    "Environment": (BlockValueConverter(AWS_ECS_TaskDefinition_KeyValuePair), None),
    "Essential": (BasicValueConverter(), "essential"),
    "ExtraHosts": (BlockValueConverter(AWS_ECS_TaskDefinition_HostEntry), None),
    "FirelensConfiguration": (AWS_ECS_TaskDefinition_FirelensConfiguration, "firelens_configuration"),
    "HealthCheck": (AWS_ECS_TaskDefinition_HealthCheck, "health_check"),
    "Hostname": (StringValueConverter(), "hostname"),
    "Image": (StringValueConverter(), "image"),
    "Interactive": (BasicValueConverter(), "interactive"),
    "Links": (ListValueConverter(StringValueConverter()), "links"),
    "LinuxParameters": (AWS_ECS_TaskDefinition_LinuxParameters, "linux_parameters"),
    "LogConfiguration": (AWS_ECS_TaskDefinition_LogConfiguration, "log_configuration"),
    "Memory": (BasicValueConverter(), "memory"),
    "MemoryReservation": (BasicValueConverter(), "memory_reservation"),
    "MountPoints": (BlockValueConverter(AWS_ECS_TaskDefinition_MountPoint), None),
    "Name": (StringValueConverter(), "name"),
    "PortMappings": (BlockValueConverter(AWS_ECS_TaskDefinition_PortMapping), None),
    "Privileged": (BasicValueConverter(), "privileged"),
    "PseudoTerminal": (BasicValueConverter(), "pseudo_terminal"),
    "ReadonlyRootFilesystem": (BasicValueConverter(), "readonly_root_filesystem"),
    "RepositoryCredentials": (AWS_ECS_TaskDefinition_RepositoryCredentials, "repository_credentials"),
    "ResourceRequirements": (BlockValueConverter(AWS_ECS_TaskDefinition_ResourceRequirement), None),
    "Secrets": (BlockValueConverter(AWS_ECS_TaskDefinition_Secret), None),
    "StartTimeout": (BasicValueConverter(), "start_timeout"),
    "StopTimeout": (BasicValueConverter(), "stop_timeout"),
    "SystemControls": (BlockValueConverter(AWS_ECS_TaskDefinition_SystemControl), None),
    "Ulimits": (BlockValueConverter(AWS_ECS_TaskDefinition_Ulimit), None),
    "User": (StringValueConverter(), "user"),
    "VolumesFrom": (BlockValueConverter(AWS_ECS_TaskDefinition_VolumeFrom), None),
    "WorkingDirectory": (StringValueConverter(), "working_directory"),
  }

class AWS_ECS_TaskDefinition(CloudFormationResource):
  terraform_resource = "aws_ecs_task_definition"

  resource_type = "AWS::ECS::TaskDefinition"

  props = {
    "ContainerDefinitions": (BlockValueConverter(AWS_ECS_TaskDefinition_ContainerDefinition), None),
    "Cpu": (StringValueConverter(), "cpu"),
    "ExecutionRoleArn": (StringValueConverter(), "execution_role_arn"),
    "Family": (StringValueConverter(), "family"),
    "InferenceAccelerators": (BlockValueConverter(AWS_ECS_TaskDefinition_InferenceAccelerator), None),
    "IpcMode": (StringValueConverter(), "ipc_mode"),
    "Memory": (StringValueConverter(), "memory"),
    "NetworkMode": (StringValueConverter(), "network_mode"),
    "PidMode": (StringValueConverter(), "pid_mode"),
    "PlacementConstraints": (BlockValueConverter(AWS_ECS_TaskDefinition_TaskDefinitionPlacementConstraint), None),
    "ProxyConfiguration": (AWS_ECS_TaskDefinition_ProxyConfiguration, "proxy_configuration"),
    "RequiresCompatibilities": (ListValueConverter(StringValueConverter()), "requires_compatibilities"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "TaskRoleArn": (StringValueConverter(), "task_role_arn"),
    "Volumes": (BlockValueConverter(AWS_ECS_TaskDefinition_Volume), None),
  }

