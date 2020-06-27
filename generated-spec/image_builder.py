from . import *

class AWS_ImageBuilder_ImagePipeline_ImageTestsConfiguration(CloudFormationProperty):
  entity = "AWS::ImageBuilder::ImagePipeline"
  tf_block_type = "image_tests_configuration"

  props = {
    "ImageTestsEnabled": (BasicValueConverter(), "image_tests_enabled"),
    "TimeoutMinutes": (BasicValueConverter(), "timeout_minutes"),
  }

class AWS_ImageBuilder_DistributionConfiguration_Distribution(CloudFormationProperty):
  entity = "AWS::ImageBuilder::DistributionConfiguration"
  tf_block_type = "distribution"

  props = {
    "Region": (StringValueConverter(), "region"),
    "AmiDistributionConfiguration": (StringValueConverter(), "ami_distribution_configuration"),
    "LicenseConfigurationArns": (ListValueConverter(StringValueConverter()), "license_configuration_arns"),
  }

class AWS_ImageBuilder_ImagePipeline_Schedule(CloudFormationProperty):
  entity = "AWS::ImageBuilder::ImagePipeline"
  tf_block_type = "schedule"

  props = {
    "ScheduleExpression": (StringValueConverter(), "schedule_expression"),
    "PipelineExecutionStartCondition": (StringValueConverter(), "pipeline_execution_start_condition"),
  }

class AWS_ImageBuilder_Image_ImageTestsConfiguration(CloudFormationProperty):
  entity = "AWS::ImageBuilder::Image"
  tf_block_type = "image_tests_configuration"

  props = {
    "ImageTestsEnabled": (BasicValueConverter(), "image_tests_enabled"),
    "TimeoutMinutes": (BasicValueConverter(), "timeout_minutes"),
  }

class AWS_ImageBuilder_InfrastructureConfiguration_S3Logs(CloudFormationProperty):
  entity = "AWS::ImageBuilder::InfrastructureConfiguration"
  tf_block_type = "s3_logs"

  props = {
    "S3BucketName": (StringValueConverter(), "s3_bucket_name"),
    "S3KeyPrefix": (StringValueConverter(), "s3_key_prefix"),
  }

class AWS_ImageBuilder_InfrastructureConfiguration_Logging(CloudFormationProperty):
  entity = "AWS::ImageBuilder::InfrastructureConfiguration"
  tf_block_type = "logging"

  props = {
    "S3Logs": (AWS_ImageBuilder_InfrastructureConfiguration_S3Logs, "s3_logs"),
  }

class AWS_ImageBuilder_ImageRecipe_ComponentConfiguration(CloudFormationProperty):
  entity = "AWS::ImageBuilder::ImageRecipe"
  tf_block_type = "component_configuration"

  props = {
    "ComponentArn": (StringValueConverter(), "component_arn"),
  }

class AWS_ImageBuilder_ImageRecipe_EbsInstanceBlockDeviceSpecification(CloudFormationProperty):
  entity = "AWS::ImageBuilder::ImageRecipe"
  tf_block_type = "ebs_instance_block_device_specification"

  props = {
    "Encrypted": (BasicValueConverter(), "encrypted"),
    "DeleteOnTermination": (BasicValueConverter(), "delete_on_termination"),
    "Iops": (BasicValueConverter(), "iops"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "SnapshotId": (StringValueConverter(), "snapshot_id"),
    "VolumeSize": (BasicValueConverter(), "volume_size"),
    "VolumeType": (StringValueConverter(), "volume_type"),
  }

class AWS_ImageBuilder_Component(CloudFormationResource):
  terraform_resource = "aws_image_builder_component"

  resource_type = "AWS::ImageBuilder::Component"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Version": (StringValueConverter(), "version"),
    "Description": (StringValueConverter(), "description"),
    "ChangeDescription": (StringValueConverter(), "change_description"),
    "Platform": (StringValueConverter(), "platform"),
    "Data": (StringValueConverter(), "data"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "Tags": (MapValueConverter(StringValueConverter()), "tags"),
    "Uri": (StringValueConverter(), "uri"),
  }

class AWS_ImageBuilder_InfrastructureConfiguration(CloudFormationResource):
  terraform_resource = "aws_image_builder_infrastructure_configuration"

  resource_type = "AWS::ImageBuilder::InfrastructureConfiguration"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Description": (StringValueConverter(), "description"),
    "InstanceTypes": (ListValueConverter(StringValueConverter()), "instance_types"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "Logging": (StringValueConverter(), "logging"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
    "KeyPair": (StringValueConverter(), "key_pair"),
    "TerminateInstanceOnFailure": (BasicValueConverter(), "terminate_instance_on_failure"),
    "InstanceProfileName": (StringValueConverter(), "instance_profile_name"),
    "SnsTopicArn": (StringValueConverter(), "sns_topic_arn"),
    "Tags": (MapValueConverter(StringValueConverter()), "tags"),
  }

class AWS_ImageBuilder_ImagePipeline(CloudFormationResource):
  terraform_resource = "aws_image_builder_image_pipeline"

  resource_type = "AWS::ImageBuilder::ImagePipeline"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Description": (StringValueConverter(), "description"),
    "ImageTestsConfiguration": (AWS_ImageBuilder_ImagePipeline_ImageTestsConfiguration, "image_tests_configuration"),
    "Status": (StringValueConverter(), "status"),
    "Schedule": (AWS_ImageBuilder_ImagePipeline_Schedule, "schedule"),
    "ImageRecipeArn": (StringValueConverter(), "image_recipe_arn"),
    "DistributionConfigurationArn": (StringValueConverter(), "distribution_configuration_arn"),
    "InfrastructureConfigurationArn": (StringValueConverter(), "infrastructure_configuration_arn"),
    "Tags": (MapValueConverter(StringValueConverter()), "tags"),
  }

class AWS_ImageBuilder_DistributionConfiguration(CloudFormationResource):
  terraform_resource = "aws_image_builder_distribution_configuration"

  resource_type = "AWS::ImageBuilder::DistributionConfiguration"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Description": (StringValueConverter(), "description"),
    "Distributions": (BlockValueConverter(AWS_ImageBuilder_DistributionConfiguration_Distribution), None),
    "Tags": (MapValueConverter(StringValueConverter()), "tags"),
  }

class AWS_ImageBuilder_Image(CloudFormationResource):
  terraform_resource = "aws_image_builder_image"

  resource_type = "AWS::ImageBuilder::Image"

  props = {
    "ImageTestsConfiguration": (AWS_ImageBuilder_Image_ImageTestsConfiguration, "image_tests_configuration"),
    "ImageRecipeArn": (StringValueConverter(), "image_recipe_arn"),
    "DistributionConfigurationArn": (StringValueConverter(), "distribution_configuration_arn"),
    "InfrastructureConfigurationArn": (StringValueConverter(), "infrastructure_configuration_arn"),
    "Tags": (MapValueConverter(StringValueConverter()), "tags"),
  }

class AWS_ImageBuilder_ImageRecipe_InstanceBlockDeviceMapping(CloudFormationProperty):
  entity = "AWS::ImageBuilder::ImageRecipe"
  tf_block_type = "instance_block_device_mapping"

  props = {
    "DeviceName": (StringValueConverter(), "device_name"),
    "VirtualName": (StringValueConverter(), "virtual_name"),
    "NoDevice": (StringValueConverter(), "no_device"),
    "Ebs": (AWS_ImageBuilder_ImageRecipe_EbsInstanceBlockDeviceSpecification, "ebs"),
  }

class AWS_ImageBuilder_ImageRecipe(CloudFormationResource):
  terraform_resource = "aws_image_builder_image_recipe"

  resource_type = "AWS::ImageBuilder::ImageRecipe"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Description": (StringValueConverter(), "description"),
    "Version": (StringValueConverter(), "version"),
    "Components": (BlockValueConverter(AWS_ImageBuilder_ImageRecipe_ComponentConfiguration), None),
    "BlockDeviceMappings": (BlockValueConverter(AWS_ImageBuilder_ImageRecipe_InstanceBlockDeviceMapping), None),
    "ParentImage": (StringValueConverter(), "parent_image"),
    "Tags": (MapValueConverter(StringValueConverter()), "tags"),
  }

