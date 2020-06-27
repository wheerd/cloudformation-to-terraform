from . import *

class AWS_CodeStar_GitHubRepository_S3(CloudFormationProperty):
  entity = "AWS::CodeStar::GitHubRepository"
  tf_block_type = "s3"

  props = {
    "ObjectVersion": (StringValueConverter(), "object_version"),
    "Bucket": (StringValueConverter(), "bucket"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_CodeStar_GitHubRepository_Code(CloudFormationProperty):
  entity = "AWS::CodeStar::GitHubRepository"
  tf_block_type = "code"

  props = {
    "S3": (AWS_CodeStar_GitHubRepository_S3, "s3"),
  }

class AWS_CodeStar_GitHubRepository(CloudFormationResource):
  terraform_resource = "aws_code_star_git_hub_repository"

  resource_type = "AWS::CodeStar::GitHubRepository"

  props = {
    "EnableIssues": (BasicValueConverter(), "enable_issues"),
    "RepositoryName": (StringValueConverter(), "repository_name"),
    "RepositoryAccessToken": (StringValueConverter(), "repository_access_token"),
    "RepositoryOwner": (StringValueConverter(), "repository_owner"),
    "IsPrivate": (BasicValueConverter(), "is_private"),
    "Code": (AWS_CodeStar_GitHubRepository_Code, "code"),
    "RepositoryDescription": (StringValueConverter(), "repository_description"),
  }

