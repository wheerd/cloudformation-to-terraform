from . import *

class AWS_Cloud9_EnvironmentEC2_Repository(CloudFormationProperty):
  def write(self, w):
    with w.block("repository"):
      self.property(w, "PathComponent", "path_component", StringValueConverter())
      self.property(w, "RepositoryUrl", "repository_url", StringValueConverter())


class AWS_Cloud9_EnvironmentEC2(CloudFormationResource):
  cfn_type = "AWS::Cloud9::EnvironmentEC2"
  tf_type = "aws_cloud9_environment_ec2"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "Repositories", AWS_Cloud9_EnvironmentEC2_Repository) # TODO: Probably not the correct mapping
      self.property(w, "OwnerArn", "owner_arn", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ConnectionType", "type", StringValueConverter())
      self.property(w, "AutomaticStopTimeMinutes", "automatic_stop_time_minutes", BasicValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


