from . import *

class AWS_Cloud9_EnvironmentEC2_Repository(CloudFormationProperty):
  entity = "AWS::Cloud9::EnvironmentEC2"
  tf_block_type = "repository"

  props = {
    "PathComponent": (StringValueConverter(), "path_component"),
    "RepositoryUrl": (StringValueConverter(), "repository_url"),
  }

class AWS_Cloud9_EnvironmentEC2(CloudFormationResource):
  terraform_resource = "aws_cloud9_environment_ec2"

  resource_type = "AWS::Cloud9::EnvironmentEC2"

  props = {
    "Repositories": (BlockValueConverter(AWS_Cloud9_EnvironmentEC2_Repository), None),
    "OwnerArn": (StringValueConverter(), "owner_arn"),
    "Description": (StringValueConverter(), "description"),
    "ConnectionType": (StringValueConverter(), "connection_type"),
    "AutomaticStopTimeMinutes": (BasicValueConverter(), "automatic_stop_time_minutes"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

