from . import *

class AWS_CodeCommit_Repository_S3(CloudFormationProperty):
  def write(self, w):
    with w.block("s3"):
      self.property(w, "ObjectVersion", "object_version", StringValueConverter())
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_CodeCommit_Repository_RepositoryTrigger(CloudFormationProperty):
  def write(self, w):
    with w.block("repository_trigger"):
      self.property(w, "Events", "events", ListValueConverter(StringValueConverter()))
      self.property(w, "Branches", "branches", ListValueConverter(StringValueConverter()))
      self.property(w, "CustomData", "custom_data", StringValueConverter())
      self.property(w, "DestinationArn", "destination_arn", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_CodeCommit_Repository_Code(CloudFormationProperty):
  def write(self, w):
    with w.block("code"):
      self.block(w, "S3", AWS_CodeCommit_Repository_S3)


class AWS_CodeCommit_Repository(CloudFormationResource):
  cfn_type = "AWS::CodeCommit::Repository"
  tf_type = "aws_code_commit_repository"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "RepositoryName", "repository_name", StringValueConverter())
      self.repeated_block(w, "Triggers", AWS_CodeCommit_Repository_RepositoryTrigger)
      self.block(w, "Code", AWS_CodeCommit_Repository_Code)
      self.property(w, "RepositoryDescription", "repository_description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


