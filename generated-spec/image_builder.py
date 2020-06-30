from . import *

class AWS_ImageBuilder_ImagePipeline_ImageTestsConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("image_tests_configuration"):
      self.property(w, "ImageTestsEnabled", "image_tests_enabled", BasicValueConverter())
      self.property(w, "TimeoutMinutes", "timeout_minutes", BasicValueConverter())


class AWS_ImageBuilder_DistributionConfiguration_Distribution(CloudFormationProperty):
  def write(self, w):
    with w.block("distribution"):
      self.property(w, "Region", "region", StringValueConverter())
      self.property(w, "AmiDistributionConfiguration", "ami_distribution_configuration", JsonValueConverter())
      self.property(w, "LicenseConfigurationArns", "license_configuration_arns", ListValueConverter(StringValueConverter()))


class AWS_ImageBuilder_ImagePipeline_Schedule(CloudFormationProperty):
  def write(self, w):
    with w.block("schedule"):
      self.property(w, "ScheduleExpression", "schedule_expression", StringValueConverter())
      self.property(w, "PipelineExecutionStartCondition", "pipeline_execution_start_condition", StringValueConverter())


class AWS_ImageBuilder_Image_ImageTestsConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("image_tests_configuration"):
      self.property(w, "ImageTestsEnabled", "image_tests_enabled", BasicValueConverter())
      self.property(w, "TimeoutMinutes", "timeout_minutes", BasicValueConverter())


class AWS_ImageBuilder_InfrastructureConfiguration_S3Logs(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_logs"):
      self.property(w, "S3BucketName", "s3_bucket_name", StringValueConverter())
      self.property(w, "S3KeyPrefix", "s3_key_prefix", StringValueConverter())


class AWS_ImageBuilder_InfrastructureConfiguration_Logging(CloudFormationProperty):
  def write(self, w):
    with w.block("logging"):
      self.block(w, "S3Logs", AWS_ImageBuilder_InfrastructureConfiguration_S3Logs)


class AWS_ImageBuilder_ImageRecipe_ComponentConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("component_configuration"):
      self.property(w, "ComponentArn", "component_arn", StringValueConverter())


class AWS_ImageBuilder_ImageRecipe_EbsInstanceBlockDeviceSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("ebs_instance_block_device_specification"):
      self.property(w, "Encrypted", "encrypted", BasicValueConverter())
      self.property(w, "DeleteOnTermination", "delete_on_termination", BasicValueConverter())
      self.property(w, "Iops", "iops", BasicValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "SnapshotId", "snapshot_id", StringValueConverter())
      self.property(w, "VolumeSize", "volume_size", BasicValueConverter())
      self.property(w, "VolumeType", "volume_type", StringValueConverter())


class AWS_ImageBuilder_Component(CloudFormationResource):
  cfn_type = "AWS::ImageBuilder::Component"
  tf_type = "aws_image_builder_component" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "Arn": "arn",
    "Type": "type",
    "Encrypted": "encrypted",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ChangeDescription", "change_description", StringValueConverter())
      self.property(w, "Platform", "platform", StringValueConverter())
      self.property(w, "Data", "data", StringValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "Tags", "tags", MapValueConverter(StringValueConverter()))
      self.property(w, "Uri", "uri", StringValueConverter())


class AWS_ImageBuilder_InfrastructureConfiguration(CloudFormationResource):
  cfn_type = "AWS::ImageBuilder::InfrastructureConfiguration"
  tf_type = "aws_image_builder_infrastructure_configuration" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "InstanceTypes", "instance_types", ListValueConverter(StringValueConverter()))
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "Logging", "logging", JsonValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())
      self.property(w, "KeyPair", "key_pair", StringValueConverter())
      self.property(w, "TerminateInstanceOnFailure", "terminate_instance_on_failure", BasicValueConverter())
      self.property(w, "InstanceProfileName", "instance_profile_name", StringValueConverter())
      self.property(w, "SnsTopicArn", "sns_topic_arn", StringValueConverter())
      self.property(w, "Tags", "tags", MapValueConverter(StringValueConverter()))


class AWS_ImageBuilder_ImagePipeline(CloudFormationResource):
  cfn_type = "AWS::ImageBuilder::ImagePipeline"
  tf_type = "aws_image_builder_image_pipeline" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "ImageTestsConfiguration", AWS_ImageBuilder_ImagePipeline_ImageTestsConfiguration)
      self.property(w, "Status", "status", StringValueConverter())
      self.block(w, "Schedule", AWS_ImageBuilder_ImagePipeline_Schedule)
      self.property(w, "ImageRecipeArn", "image_recipe_arn", StringValueConverter())
      self.property(w, "DistributionConfigurationArn", "distribution_configuration_arn", StringValueConverter())
      self.property(w, "InfrastructureConfigurationArn", "infrastructure_configuration_arn", StringValueConverter())
      self.property(w, "Tags", "tags", MapValueConverter(StringValueConverter()))


class AWS_ImageBuilder_DistributionConfiguration(CloudFormationResource):
  cfn_type = "AWS::ImageBuilder::DistributionConfiguration"
  tf_type = "aws_image_builder_distribution_configuration" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.repeated_block(w, "Distributions", AWS_ImageBuilder_DistributionConfiguration_Distribution)
      self.property(w, "Tags", "tags", MapValueConverter(StringValueConverter()))


class AWS_ImageBuilder_Image(CloudFormationResource):
  cfn_type = "AWS::ImageBuilder::Image"
  tf_type = "aws_image_builder_image" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "Arn": "arn",
    "ImageId": "image_id",
  }

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "ImageTestsConfiguration", AWS_ImageBuilder_Image_ImageTestsConfiguration)
      self.property(w, "ImageRecipeArn", "image_recipe_arn", StringValueConverter())
      self.property(w, "DistributionConfigurationArn", "distribution_configuration_arn", StringValueConverter())
      self.property(w, "InfrastructureConfigurationArn", "infrastructure_configuration_arn", StringValueConverter())
      self.property(w, "Tags", "tags", MapValueConverter(StringValueConverter()))


class AWS_ImageBuilder_ImageRecipe_InstanceBlockDeviceMapping(CloudFormationProperty):
  def write(self, w):
    with w.block("instance_block_device_mapping"):
      self.property(w, "DeviceName", "device_name", StringValueConverter())
      self.property(w, "VirtualName", "virtual_name", StringValueConverter())
      self.property(w, "NoDevice", "no_device", StringValueConverter())
      self.block(w, "Ebs", AWS_ImageBuilder_ImageRecipe_EbsInstanceBlockDeviceSpecification)


class AWS_ImageBuilder_ImageRecipe(CloudFormationResource):
  cfn_type = "AWS::ImageBuilder::ImageRecipe"
  tf_type = "aws_image_builder_image_recipe" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())
      self.repeated_block(w, "Components", AWS_ImageBuilder_ImageRecipe_ComponentConfiguration)
      self.repeated_block(w, "BlockDeviceMappings", AWS_ImageBuilder_ImageRecipe_InstanceBlockDeviceMapping)
      self.property(w, "ParentImage", "parent_image", StringValueConverter())
      self.property(w, "Tags", "tags", MapValueConverter(StringValueConverter()))


