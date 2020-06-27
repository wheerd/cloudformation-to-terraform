from . import *

class AWS_ECR_Repository_LifecyclePolicy(CloudFormationProperty):
  entity = "AWS::ECR::Repository"
  tf_block_type = "lifecycle_policy"

  props = {
    "LifecyclePolicyText": (StringValueConverter(), "lifecycle_policy_text"),
    "RegistryId": (StringValueConverter(), "registry_id"),
  }

class AWS_ECR_Repository(CloudFormationResource):
  terraform_resource = "aws_ecr_repository"

  resource_type = "AWS::ECR::Repository"

  props = {
    "LifecyclePolicy": (AWS_ECR_Repository_LifecyclePolicy, "lifecycle_policy"),
    "RepositoryName": (StringValueConverter(), "repository_name"),
    "RepositoryPolicyText": (StringValueConverter(), "repository_policy_text"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

