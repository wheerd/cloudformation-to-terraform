from . import *

class AWS_CodeCommit_Repository_S3(CloudFormationProperty):
  entity = "AWS::CodeCommit::Repository"
  tf_block_type = "s3"

  props = {
    "ObjectVersion": (StringValueConverter(), "object_version"),
    "Bucket": (StringValueConverter(), "bucket"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_CodeCommit_Repository_RepositoryTrigger(CloudFormationProperty):
  entity = "AWS::CodeCommit::Repository"
  tf_block_type = "repository_trigger"

  props = {
    "Events": (ListValueConverter(StringValueConverter()), "events"),
    "Branches": (ListValueConverter(StringValueConverter()), "branches"),
    "CustomData": (StringValueConverter(), "custom_data"),
    "DestinationArn": (StringValueConverter(), "destination_arn"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_CodeCommit_Repository_Code(CloudFormationProperty):
  entity = "AWS::CodeCommit::Repository"
  tf_block_type = "code"

  props = {
    "S3": (AWS_CodeCommit_Repository_S3, "s3"),
  }

class AWS_CodeCommit_Repository(CloudFormationResource):
  terraform_resource = "aws_code_commit_repository"

  resource_type = "AWS::CodeCommit::Repository"

  props = {
    "RepositoryName": (StringValueConverter(), "repository_name"),
    "Triggers": (BlockValueConverter(AWS_CodeCommit_Repository_RepositoryTrigger), None),
    "Code": (AWS_CodeCommit_Repository_Code, "code"),
    "RepositoryDescription": (StringValueConverter(), "repository_description"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

