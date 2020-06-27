from . import *

class AWS_CodeStar_GitHubRepository_S3(CloudFormationProperty):
  def write(self, w):
    with w.block("s3"):
      self.property(w, "ObjectVersion", "object_version", StringValueConverter())
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_CodeStar_GitHubRepository_Code(CloudFormationProperty):
  def write(self, w):
    with w.block("code"):
      self.block(w, "S3", AWS_CodeStar_GitHubRepository_S3)


class AWS_CodeStar_GitHubRepository(CloudFormationResource):
  cfn_type = "AWS::CodeStar::GitHubRepository"
  tf_type = "aws_code_star_git_hub_repository"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "EnableIssues", "enable_issues", BasicValueConverter())
      self.property(w, "RepositoryName", "repository_name", StringValueConverter())
      self.property(w, "RepositoryAccessToken", "repository_access_token", StringValueConverter())
      self.property(w, "RepositoryOwner", "repository_owner", StringValueConverter())
      self.property(w, "IsPrivate", "is_private", BasicValueConverter())
      self.block(w, "Code", AWS_CodeStar_GitHubRepository_Code)
      self.property(w, "RepositoryDescription", "repository_description", StringValueConverter())


