from . import *

class AWS_Batch_ComputeEnvironment_LaunchTemplateSpecification(CloudFormationProperty):
  entity = "AWS::Batch::ComputeEnvironment"
  tf_block_type = "launch_template_specification"

  props = {
    "LaunchTemplateName": (StringValueConverter(), "launch_template_name"),
    "Version": (StringValueConverter(), "version"),
    "LaunchTemplateId": (StringValueConverter(), "launch_template_id"),
  }

class AWS_Batch_ComputeEnvironment_ComputeResources(CloudFormationProperty):
  entity = "AWS::Batch::ComputeEnvironment"
  tf_block_type = "compute_resources"

  props = {
    "SpotIamFleetRole": (StringValueConverter(), "spot_iam_fleet_role"),
    "MaxvCpus": (BasicValueConverter(), "maxv_cpus"),
    "BidPercentage": (BasicValueConverter(), "bid_percentage"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "Subnets": (ListValueConverter(StringValueConverter()), "subnets"),
    "Type": (StringValueConverter(), "type"),
    "AllocationStrategy": (StringValueConverter(), "allocation_strategy"),
    "MinvCpus": (BasicValueConverter(), "minv_cpus"),
    "LaunchTemplate": (AWS_Batch_ComputeEnvironment_LaunchTemplateSpecification, "launch_template"),
    "ImageId": (StringValueConverter(), "image_id"),
    "InstanceRole": (StringValueConverter(), "instance_role"),
    "InstanceTypes": (ListValueConverter(StringValueConverter()), "instance_types"),
    "Ec2KeyPair": (StringValueConverter(), "ec2_key_pair"),
    "PlacementGroup": (StringValueConverter(), "placement_group"),
    "Tags": (StringValueConverter(), "tags"),
    "DesiredvCpus": (BasicValueConverter(), "desiredv_cpus"),
  }

class AWS_Batch_JobDefinition_ResourceRequirement(CloudFormationProperty):
  entity = "AWS::Batch::JobDefinition"
  tf_block_type = "resource_requirement"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_Batch_JobDefinition_MountPoints(CloudFormationProperty):
  entity = "AWS::Batch::JobDefinition"
  tf_block_type = "mount_points"

  props = {
    "ReadOnly": (BasicValueConverter(), "read_only"),
    "SourceVolume": (StringValueConverter(), "source_volume"),
    "ContainerPath": (StringValueConverter(), "container_path"),
  }

class AWS_Batch_JobDefinition_Environment(CloudFormationProperty):
  entity = "AWS::Batch::JobDefinition"
  tf_block_type = "environment"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Batch_JobDefinition_Ulimit(CloudFormationProperty):
  entity = "AWS::Batch::JobDefinition"
  tf_block_type = "ulimit"

  props = {
    "SoftLimit": (BasicValueConverter(), "soft_limit"),
    "HardLimit": (BasicValueConverter(), "hard_limit"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Batch_JobDefinition_VolumesHost(CloudFormationProperty):
  entity = "AWS::Batch::JobDefinition"
  tf_block_type = "volumes_host"

  props = {
    "SourcePath": (StringValueConverter(), "source_path"),
  }

class AWS_Batch_JobQueue_ComputeEnvironmentOrder(CloudFormationProperty):
  entity = "AWS::Batch::JobQueue"
  tf_block_type = "compute_environment_order"

  props = {
    "ComputeEnvironment": (StringValueConverter(), "compute_environment"),
    "Order": (BasicValueConverter(), "order"),
  }

class AWS_Batch_JobDefinition_RetryStrategy(CloudFormationProperty):
  entity = "AWS::Batch::JobDefinition"
  tf_block_type = "retry_strategy"

  props = {
    "Attempts": (BasicValueConverter(), "attempts"),
  }

class AWS_Batch_JobDefinition_Timeout(CloudFormationProperty):
  entity = "AWS::Batch::JobDefinition"
  tf_block_type = "timeout"

  props = {
    "AttemptDurationSeconds": (BasicValueConverter(), "attempt_duration_seconds"),
  }

class AWS_Batch_JobDefinition_Device(CloudFormationProperty):
  entity = "AWS::Batch::JobDefinition"
  tf_block_type = "device"

  props = {
    "HostPath": (StringValueConverter(), "host_path"),
    "Permissions": (ListValueConverter(StringValueConverter()), "permissions"),
    "ContainerPath": (StringValueConverter(), "container_path"),
  }

class AWS_Batch_JobQueue(CloudFormationResource):
  terraform_resource = "aws_batch_job_queue"

  resource_type = "AWS::Batch::JobQueue"

  props = {
    "ComputeEnvironmentOrder": (BlockValueConverter(AWS_Batch_JobQueue_ComputeEnvironmentOrder), None),
    "Priority": (BasicValueConverter(), "priority"),
    "State": (StringValueConverter(), "state"),
    "JobQueueName": (StringValueConverter(), "job_queue_name"),
  }

class AWS_Batch_ComputeEnvironment(CloudFormationResource):
  terraform_resource = "aws_batch_compute_environment"

  resource_type = "AWS::Batch::ComputeEnvironment"

  props = {
    "Type": (StringValueConverter(), "type"),
    "ServiceRole": (StringValueConverter(), "service_role"),
    "ComputeEnvironmentName": (StringValueConverter(), "compute_environment_name"),
    "ComputeResources": (AWS_Batch_ComputeEnvironment_ComputeResources, "compute_resources"),
    "State": (StringValueConverter(), "state"),
  }

class AWS_Batch_JobDefinition_Volumes(CloudFormationProperty):
  entity = "AWS::Batch::JobDefinition"
  tf_block_type = "volumes"

  props = {
    "Host": (AWS_Batch_JobDefinition_VolumesHost, "host"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Batch_JobDefinition_LinuxParameters(CloudFormationProperty):
  entity = "AWS::Batch::JobDefinition"
  tf_block_type = "linux_parameters"

  props = {
    "Devices": (BlockValueConverter(AWS_Batch_JobDefinition_Device), None),
  }

class AWS_Batch_JobDefinition_ContainerProperties(CloudFormationProperty):
  entity = "AWS::Batch::JobDefinition"
  tf_block_type = "container_properties"

  props = {
    "User": (StringValueConverter(), "user"),
    "Memory": (BasicValueConverter(), "memory"),
    "Privileged": (BasicValueConverter(), "privileged"),
    "LinuxParameters": (AWS_Batch_JobDefinition_LinuxParameters, "linux_parameters"),
    "JobRoleArn": (StringValueConverter(), "job_role_arn"),
    "ReadonlyRootFilesystem": (BasicValueConverter(), "readonly_root_filesystem"),
    "Vcpus": (BasicValueConverter(), "vcpus"),
    "Image": (StringValueConverter(), "image"),
    "ResourceRequirements": (BlockValueConverter(AWS_Batch_JobDefinition_ResourceRequirement), None),
    "MountPoints": (BlockValueConverter(AWS_Batch_JobDefinition_MountPoints), None),
    "Volumes": (BlockValueConverter(AWS_Batch_JobDefinition_Volumes), None),
    "Command": (ListValueConverter(StringValueConverter()), "command"),
    "Environment": (BlockValueConverter(AWS_Batch_JobDefinition_Environment), None),
    "Ulimits": (BlockValueConverter(AWS_Batch_JobDefinition_Ulimit), None),
    "InstanceType": (StringValueConverter(), "instance_type"),
  }

class AWS_Batch_JobDefinition_NodeRangeProperty(CloudFormationProperty):
  entity = "AWS::Batch::JobDefinition"
  tf_block_type = "node_range_property"

  props = {
    "Container": (AWS_Batch_JobDefinition_ContainerProperties, "container"),
    "TargetNodes": (StringValueConverter(), "target_nodes"),
  }

class AWS_Batch_JobDefinition_NodeProperties(CloudFormationProperty):
  entity = "AWS::Batch::JobDefinition"
  tf_block_type = "node_properties"

  props = {
    "MainNode": (BasicValueConverter(), "main_node"),
    "NodeRangeProperties": (BlockValueConverter(AWS_Batch_JobDefinition_NodeRangeProperty), None),
    "NumNodes": (BasicValueConverter(), "num_nodes"),
  }

class AWS_Batch_JobDefinition(CloudFormationResource):
  terraform_resource = "aws_batch_job_definition"

  resource_type = "AWS::Batch::JobDefinition"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Parameters": (StringValueConverter(), "parameters"),
    "NodeProperties": (AWS_Batch_JobDefinition_NodeProperties, "node_properties"),
    "Timeout": (AWS_Batch_JobDefinition_Timeout, "timeout"),
    "ContainerProperties": (AWS_Batch_JobDefinition_ContainerProperties, "container_properties"),
    "JobDefinitionName": (StringValueConverter(), "job_definition_name"),
    "RetryStrategy": (AWS_Batch_JobDefinition_RetryStrategy, "retry_strategy"),
  }

