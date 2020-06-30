from . import *

class AWS_ECR_Repository_LifecyclePolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("lifecycle_policy"):
      self.property(w, "LifecyclePolicyText", "lifecycle_policy_text", StringValueConverter())
      self.property(w, "RegistryId", "registry_id", StringValueConverter())


class AWS_ECR_Repository(CloudFormationResource):
  cfn_type = "AWS::ECR::Repository"
  tf_type = "aws_ecr_repository"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "LifecyclePolicy", AWS_ECR_Repository_LifecyclePolicy) # TODO: Probably not the correct mapping
      self.property(w, "RepositoryName", "name", StringValueConverter())
      self.property(w, "RepositoryPolicyText", "repository_policy_text", JsonValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


