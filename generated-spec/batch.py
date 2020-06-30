from . import *

class AWS_Batch_ComputeEnvironment_LaunchTemplateSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("launch_template_specification"):
      self.property(w, "LaunchTemplateName", "launch_template_name", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())
      self.property(w, "LaunchTemplateId", "launch_template_id", StringValueConverter())


class AWS_Batch_ComputeEnvironment_ComputeResources(CloudFormationProperty):
  def write(self, w):
    with w.block("compute_resources"):
      self.property(w, "SpotIamFleetRole", "spot_iam_fleet_role", StringValueConverter())
      self.property(w, "MaxvCpus", "maxv_cpus", BasicValueConverter())
      self.property(w, "BidPercentage", "bid_percentage", BasicValueConverter())
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "Subnets", "subnets", ListValueConverter(StringValueConverter()))
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "AllocationStrategy", "allocation_strategy", StringValueConverter())
      self.property(w, "MinvCpus", "minv_cpus", BasicValueConverter())
      self.block(w, "LaunchTemplate", AWS_Batch_ComputeEnvironment_LaunchTemplateSpecification)
      self.property(w, "ImageId", "image_id", StringValueConverter())
      self.property(w, "InstanceRole", "instance_role", StringValueConverter())
      self.property(w, "InstanceTypes", "instance_types", ListValueConverter(StringValueConverter()))
      self.property(w, "Ec2KeyPair", "ec2_key_pair", StringValueConverter())
      self.property(w, "PlacementGroup", "placement_group", StringValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "DesiredvCpus", "desiredv_cpus", BasicValueConverter())


class AWS_Batch_JobDefinition_ResourceRequirement(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_requirement"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_Batch_JobDefinition_MountPoints(CloudFormationProperty):
  def write(self, w):
    with w.block("mount_points"):
      self.property(w, "ReadOnly", "read_only", BasicValueConverter())
      self.property(w, "SourceVolume", "source_volume", StringValueConverter())
      self.property(w, "ContainerPath", "container_path", StringValueConverter())


class AWS_Batch_JobDefinition_Environment(CloudFormationProperty):
  def write(self, w):
    with w.block("environment"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Batch_JobDefinition_Ulimit(CloudFormationProperty):
  def write(self, w):
    with w.block("ulimit"):
      self.property(w, "SoftLimit", "soft_limit", BasicValueConverter())
      self.property(w, "HardLimit", "hard_limit", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Batch_JobDefinition_VolumesHost(CloudFormationProperty):
  def write(self, w):
    with w.block("volumes_host"):
      self.property(w, "SourcePath", "source_path", StringValueConverter())


class AWS_Batch_JobQueue_ComputeEnvironmentOrder(CloudFormationProperty):
  def write(self, w):
    with w.block("compute_environment_order"):
      self.property(w, "ComputeEnvironment", "compute_environment", StringValueConverter())
      self.property(w, "Order", "order", BasicValueConverter())


class AWS_Batch_JobDefinition_RetryStrategy(CloudFormationProperty):
  def write(self, w):
    with w.block("retry_strategy"):
      self.property(w, "Attempts", "attempts", BasicValueConverter())


class AWS_Batch_JobDefinition_Timeout(CloudFormationProperty):
  def write(self, w):
    with w.block("timeout"):
      self.property(w, "AttemptDurationSeconds", "attempt_duration_seconds", BasicValueConverter())


class AWS_Batch_JobDefinition_Device(CloudFormationProperty):
  def write(self, w):
    with w.block("device"):
      self.property(w, "HostPath", "host_path", StringValueConverter())
      self.property(w, "Permissions", "permissions", ListValueConverter(StringValueConverter()))
      self.property(w, "ContainerPath", "container_path", StringValueConverter())


class AWS_Batch_JobQueue(CloudFormationResource):
  cfn_type = "AWS::Batch::JobQueue"
  tf_type = "aws_batch_job_queue"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "ComputeEnvironmentOrder", AWS_Batch_JobQueue_ComputeEnvironmentOrder) # TODO: Probably not the correct mapping
      self.property(w, "Priority", "priority", BasicValueConverter())
      self.property(w, "State", "state", StringValueConverter())
      self.property(w, "JobQueueName", "name", StringValueConverter())


class AWS_Batch_ComputeEnvironment(CloudFormationResource):
  cfn_type = "AWS::Batch::ComputeEnvironment"
  tf_type = "aws_batch_compute_environment"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "ServiceRole", "service_role", StringValueConverter())
      self.property(w, "ComputeEnvironmentName", "compute_environment_name", StringValueConverter())
      self.block(w, "ComputeResources", AWS_Batch_ComputeEnvironment_ComputeResources)
      self.property(w, "State", "state", StringValueConverter())


class AWS_Batch_JobDefinition_Volumes(CloudFormationProperty):
  def write(self, w):
    with w.block("volumes"):
      self.block(w, "Host", AWS_Batch_JobDefinition_VolumesHost)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Batch_JobDefinition_LinuxParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("linux_parameters"):
      self.repeated_block(w, "Devices", AWS_Batch_JobDefinition_Device)


class AWS_Batch_JobDefinition_ContainerProperties(CloudFormationProperty):
  def write(self, w):
    with w.block("container_properties"):
      self.property(w, "User", "user", StringValueConverter())
      self.property(w, "Memory", "memory", BasicValueConverter())
      self.property(w, "Privileged", "privileged", BasicValueConverter())
      self.block(w, "LinuxParameters", AWS_Batch_JobDefinition_LinuxParameters)
      self.property(w, "JobRoleArn", "job_role_arn", StringValueConverter())
      self.property(w, "ReadonlyRootFilesystem", "readonly_root_filesystem", BasicValueConverter())
      self.property(w, "Vcpus", "vcpus", BasicValueConverter())
      self.property(w, "Image", "image", StringValueConverter())
      self.repeated_block(w, "ResourceRequirements", AWS_Batch_JobDefinition_ResourceRequirement)
      self.repeated_block(w, "MountPoints", AWS_Batch_JobDefinition_MountPoints)
      self.repeated_block(w, "Volumes", AWS_Batch_JobDefinition_Volumes)
      self.property(w, "Command", "command", ListValueConverter(StringValueConverter()))
      self.repeated_block(w, "Environment", AWS_Batch_JobDefinition_Environment)
      self.repeated_block(w, "Ulimits", AWS_Batch_JobDefinition_Ulimit)
      self.property(w, "InstanceType", "instance_type", StringValueConverter())


class AWS_Batch_JobDefinition_NodeRangeProperty(CloudFormationProperty):
  def write(self, w):
    with w.block("node_range_property"):
      self.block(w, "Container", AWS_Batch_JobDefinition_ContainerProperties)
      self.property(w, "TargetNodes", "target_nodes", StringValueConverter())


class AWS_Batch_JobDefinition_NodeProperties(CloudFormationProperty):
  def write(self, w):
    with w.block("node_properties"):
      self.property(w, "MainNode", "main_node", BasicValueConverter())
      self.repeated_block(w, "NodeRangeProperties", AWS_Batch_JobDefinition_NodeRangeProperty)
      self.property(w, "NumNodes", "num_nodes", BasicValueConverter())


class AWS_Batch_JobDefinition(CloudFormationResource):
  cfn_type = "AWS::Batch::JobDefinition"
  tf_type = "aws_batch_job_definition"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Parameters", "parameters", JsonValueConverter())
      self.block(w, "NodeProperties", AWS_Batch_JobDefinition_NodeProperties) # TODO: Probably not the correct mapping
      self.block(w, "Timeout", AWS_Batch_JobDefinition_Timeout)
      self.block(w, "ContainerProperties", AWS_Batch_JobDefinition_ContainerProperties)
      self.property(w, "JobDefinitionName", "name", StringValueConverter())
      self.block(w, "RetryStrategy", AWS_Batch_JobDefinition_RetryStrategy)


