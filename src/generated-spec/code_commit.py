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
  tf_type = "aws_codecommit_repository"
  ref = "id"
  attrs = {
    "CloneUrlHttp": "clone_url_http",
    "CloneUrlSsh": "clone_url_ssh",
    "Arn": "arn",
    "Name": "name", # TODO: Probably not the correct mapping
    # Additional TF attributes: repository_id
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "RepositoryName", "repository_name", StringValueConverter())
      self.repeated_block(w, "Triggers", AWS_CodeCommit_Repository_RepositoryTrigger) # TODO: Probably not the correct mapping
      self.block(w, "Code", AWS_CodeCommit_Repository_Code) # TODO: Probably not the correct mapping
      self.property(w, "RepositoryDescription", "description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


