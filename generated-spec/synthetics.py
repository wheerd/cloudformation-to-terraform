from . import *

class AWS_Synthetics_Canary_Code(CloudFormationProperty):
  def write(self, w):
    with w.block("code"):
      self.property(w, "S3Bucket", "s3_bucket", StringValueConverter())
      self.property(w, "S3Key", "s3_key", StringValueConverter())
      self.property(w, "S3ObjectVersion", "s3_object_version", StringValueConverter())
      self.property(w, "Script", "script", StringValueConverter())
      self.property(w, "Handler", "handler", StringValueConverter())


class AWS_Synthetics_Canary_VPCConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("vpc_config"):
      self.property(w, "VpcId", "vpc_id", StringValueConverter())
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))


class AWS_Synthetics_Canary_RunConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("run_config"):
      self.property(w, "TimeoutInSeconds", "timeout_in_seconds", BasicValueConverter())


class AWS_Synthetics_Canary_Schedule(CloudFormationProperty):
  def write(self, w):
    with w.block("schedule"):
      self.property(w, "Expression", "expression", StringValueConverter())
      self.property(w, "DurationInSeconds", "duration_in_seconds", StringValueConverter())


class AWS_Synthetics_Canary(CloudFormationResource):
  cfn_type = "AWS::Synthetics::Canary"
  tf_type = "aws_synthetics_canary"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "Code", AWS_Synthetics_Canary_Code)
      self.property(w, "ArtifactS3Location", "artifact_s3_location", StringValueConverter())
      self.block(w, "Schedule", AWS_Synthetics_Canary_Schedule)
      self.property(w, "ExecutionRoleArn", "execution_role_arn", StringValueConverter())
      self.property(w, "RuntimeVersion", "runtime_version", StringValueConverter())
      self.property(w, "SuccessRetentionPeriod", "success_retention_period", BasicValueConverter())
      self.property(w, "FailureRetentionPeriod", "failure_retention_period", BasicValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.block(w, "VPCConfig", AWS_Synthetics_Canary_VPCConfig)
      self.block(w, "RunConfig", AWS_Synthetics_Canary_RunConfig)
      self.property(w, "StartCanaryAfterCreation", "start_canary_after_creation", BasicValueConverter())


