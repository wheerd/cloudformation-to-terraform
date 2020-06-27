from . import *

class AWS_Synthetics_Canary_Code(CloudFormationProperty):
  entity = "AWS::Synthetics::Canary"
  tf_block_type = "code"

  props = {
    "S3Bucket": (StringValueConverter(), "s3_bucket"),
    "S3Key": (StringValueConverter(), "s3_key"),
    "S3ObjectVersion": (StringValueConverter(), "s3_object_version"),
    "Script": (StringValueConverter(), "script"),
    "Handler": (StringValueConverter(), "handler"),
  }

class AWS_Synthetics_Canary_VPCConfig(CloudFormationProperty):
  entity = "AWS::Synthetics::Canary"
  tf_block_type = "vpc_config"

  props = {
    "VpcId": (StringValueConverter(), "vpc_id"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
  }

class AWS_Synthetics_Canary_RunConfig(CloudFormationProperty):
  entity = "AWS::Synthetics::Canary"
  tf_block_type = "run_config"

  props = {
    "TimeoutInSeconds": (BasicValueConverter(), "timeout_in_seconds"),
  }

class AWS_Synthetics_Canary_Schedule(CloudFormationProperty):
  entity = "AWS::Synthetics::Canary"
  tf_block_type = "schedule"

  props = {
    "Expression": (StringValueConverter(), "expression"),
    "DurationInSeconds": (StringValueConverter(), "duration_in_seconds"),
  }

class AWS_Synthetics_Canary(CloudFormationResource):
  terraform_resource = "aws_synthetics_canary"

  resource_type = "AWS::Synthetics::Canary"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Code": (AWS_Synthetics_Canary_Code, "code"),
    "ArtifactS3Location": (StringValueConverter(), "artifact_s3_location"),
    "Schedule": (AWS_Synthetics_Canary_Schedule, "schedule"),
    "ExecutionRoleArn": (StringValueConverter(), "execution_role_arn"),
    "RuntimeVersion": (StringValueConverter(), "runtime_version"),
    "SuccessRetentionPeriod": (BasicValueConverter(), "success_retention_period"),
    "FailureRetentionPeriod": (BasicValueConverter(), "failure_retention_period"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "VPCConfig": (AWS_Synthetics_Canary_VPCConfig, "vpc_config"),
    "RunConfig": (AWS_Synthetics_Canary_RunConfig, "run_config"),
    "StartCanaryAfterCreation": (BasicValueConverter(), "start_canary_after_creation"),
  }

