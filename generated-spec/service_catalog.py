from . import *

class AWS_ServiceCatalog_CloudFormationProvisionedProduct_ProvisioningParameter(CloudFormationProperty):
  def write(self, w):
    with w.block("provisioning_parameter"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_ServiceCatalog_CloudFormationProduct_ProvisioningArtifactProperties(CloudFormationProperty):
  def write(self, w):
    with w.block("provisioning_artifact_properties"):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DisableTemplateValidation", "disable_template_validation", BasicValueConverter())
      self.property(w, "Info", "info", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_ServiceCatalog_CloudFormationProvisionedProduct_ProvisioningPreferences(CloudFormationProperty):
  def write(self, w):
    with w.block("provisioning_preferences"):
      self.property(w, "StackSetAccounts", "stack_set_accounts", ListValueConverter(StringValueConverter()))
      self.property(w, "StackSetFailureToleranceCount", "stack_set_failure_tolerance_count", BasicValueConverter())
      self.property(w, "StackSetMaxConcurrencyPercentage", "stack_set_max_concurrency_percentage", BasicValueConverter())
      self.property(w, "StackSetMaxConcurrencyCount", "stack_set_max_concurrency_count", BasicValueConverter())
      self.property(w, "StackSetRegions", "stack_set_regions", ListValueConverter(StringValueConverter()))
      self.property(w, "StackSetOperationType", "stack_set_operation_type", StringValueConverter())
      self.property(w, "StackSetFailureTolerancePercentage", "stack_set_failure_tolerance_percentage", BasicValueConverter())


class AWS_ServiceCatalog_PortfolioShare(CloudFormationResource):
  cfn_type = "AWS::ServiceCatalog::PortfolioShare"
  tf_type = "aws_service_catalog_portfolio_share"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AccountId", "account_id", StringValueConverter())
      self.property(w, "AcceptLanguage", "accept_language", StringValueConverter())
      self.property(w, "PortfolioId", "portfolio_id", StringValueConverter())


class AWS_ServiceCatalog_ResourceUpdateConstraint(CloudFormationResource):
  cfn_type = "AWS::ServiceCatalog::ResourceUpdateConstraint"
  tf_type = "aws_service_catalog_resource_update_constraint"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "AcceptLanguage", "accept_language", StringValueConverter())
      self.property(w, "TagUpdateOnProvisionedProduct", "tag_update_on_provisioned_product", StringValueConverter())
      self.property(w, "PortfolioId", "portfolio_id", StringValueConverter())
      self.property(w, "ProductId", "product_id", StringValueConverter())


class AWS_ServiceCatalog_TagOption(CloudFormationResource):
  cfn_type = "AWS::ServiceCatalog::TagOption"
  tf_type = "aws_service_catalog_tag_option"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Active", "active", BasicValueConverter())
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_ServiceCatalog_CloudFormationProduct(CloudFormationResource):
  cfn_type = "AWS::ServiceCatalog::CloudFormationProduct"
  tf_type = "aws_service_catalog_cloud_formation_product"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ReplaceProvisioningArtifacts", "replace_provisioning_artifacts", BasicValueConverter())
      self.property(w, "Owner", "owner", StringValueConverter())
      self.property(w, "SupportDescription", "support_description", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Distributor", "distributor", StringValueConverter())
      self.property(w, "SupportEmail", "support_email", StringValueConverter())
      self.property(w, "AcceptLanguage", "accept_language", StringValueConverter())
      self.property(w, "SupportUrl", "support_url", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())
      self.repeated_block(w, "ProvisioningArtifactParameters", AWS_ServiceCatalog_CloudFormationProduct_ProvisioningArtifactProperties)


class AWS_ServiceCatalog_PortfolioProductAssociation(CloudFormationResource):
  cfn_type = "AWS::ServiceCatalog::PortfolioProductAssociation"
  tf_type = "aws_service_catalog_portfolio_product_association"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "SourcePortfolioId", "source_portfolio_id", StringValueConverter())
      self.property(w, "AcceptLanguage", "accept_language", StringValueConverter())
      self.property(w, "PortfolioId", "portfolio_id", StringValueConverter())
      self.property(w, "ProductId", "product_id", StringValueConverter())


class AWS_ServiceCatalog_AcceptedPortfolioShare(CloudFormationResource):
  cfn_type = "AWS::ServiceCatalog::AcceptedPortfolioShare"
  tf_type = "aws_service_catalog_accepted_portfolio_share"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AcceptLanguage", "accept_language", StringValueConverter())
      self.property(w, "PortfolioId", "portfolio_id", StringValueConverter())


class AWS_ServiceCatalog_StackSetConstraint(CloudFormationResource):
  cfn_type = "AWS::ServiceCatalog::StackSetConstraint"
  tf_type = "aws_service_catalog_stack_set_constraint"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "StackInstanceControl", "stack_instance_control", StringValueConverter())
      self.property(w, "AcceptLanguage", "accept_language", StringValueConverter())
      self.property(w, "PortfolioId", "portfolio_id", StringValueConverter())
      self.property(w, "ProductId", "product_id", StringValueConverter())
      self.property(w, "RegionList", "region_list", ListValueConverter(StringValueConverter()))
      self.property(w, "AdminRole", "admin_role", StringValueConverter())
      self.property(w, "AccountList", "account_list", ListValueConverter(StringValueConverter()))
      self.property(w, "ExecutionRole", "execution_role", StringValueConverter())


class AWS_ServiceCatalog_TagOptionAssociation(CloudFormationResource):
  cfn_type = "AWS::ServiceCatalog::TagOptionAssociation"
  tf_type = "aws_service_catalog_tag_option_association"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "TagOptionId", "tag_option_id", StringValueConverter())
      self.property(w, "ResourceId", "resource_id", StringValueConverter())


class AWS_ServiceCatalog_LaunchTemplateConstraint(CloudFormationResource):
  cfn_type = "AWS::ServiceCatalog::LaunchTemplateConstraint"
  tf_type = "aws_service_catalog_launch_template_constraint"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "AcceptLanguage", "accept_language", StringValueConverter())
      self.property(w, "PortfolioId", "portfolio_id", StringValueConverter())
      self.property(w, "ProductId", "product_id", StringValueConverter())
      self.property(w, "Rules", "rules", StringValueConverter())


class AWS_ServiceCatalog_PortfolioPrincipalAssociation(CloudFormationResource):
  cfn_type = "AWS::ServiceCatalog::PortfolioPrincipalAssociation"
  tf_type = "aws_service_catalog_portfolio_principal_association"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PrincipalARN", "principal_arn", StringValueConverter())
      self.property(w, "AcceptLanguage", "accept_language", StringValueConverter())
      self.property(w, "PortfolioId", "portfolio_id", StringValueConverter())
      self.property(w, "PrincipalType", "principal_type", StringValueConverter())


class AWS_ServiceCatalog_CloudFormationProvisionedProduct(CloudFormationResource):
  cfn_type = "AWS::ServiceCatalog::CloudFormationProvisionedProduct"
  tf_type = "aws_service_catalog_cloud_formation_provisioned_product"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PathId", "path_id", StringValueConverter())
      self.repeated_block(w, "ProvisioningParameters", AWS_ServiceCatalog_CloudFormationProvisionedProduct_ProvisioningParameter)
      self.block(w, "ProvisioningPreferences", AWS_ServiceCatalog_CloudFormationProvisionedProduct_ProvisioningPreferences)
      self.property(w, "ProductName", "product_name", StringValueConverter())
      self.property(w, "ProvisioningArtifactName", "provisioning_artifact_name", StringValueConverter())
      self.property(w, "NotificationArns", "notification_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "AcceptLanguage", "accept_language", StringValueConverter())
      self.property(w, "ProductId", "product_id", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "ProvisionedProductName", "provisioned_product_name", StringValueConverter())
      self.property(w, "ProvisioningArtifactId", "provisioning_artifact_id", StringValueConverter())


class AWS_ServiceCatalog_LaunchRoleConstraint(CloudFormationResource):
  cfn_type = "AWS::ServiceCatalog::LaunchRoleConstraint"
  tf_type = "aws_service_catalog_launch_role_constraint"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "LocalRoleName", "local_role_name", StringValueConverter())
      self.property(w, "AcceptLanguage", "accept_language", StringValueConverter())
      self.property(w, "PortfolioId", "portfolio_id", StringValueConverter())
      self.property(w, "ProductId", "product_id", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_ServiceCatalog_Portfolio(CloudFormationResource):
  cfn_type = "AWS::ServiceCatalog::Portfolio"
  tf_type = "aws_service_catalog_portfolio"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ProviderName", "provider_name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DisplayName", "display_name", StringValueConverter())
      self.property(w, "AcceptLanguage", "accept_language", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_ServiceCatalog_LaunchNotificationConstraint(CloudFormationResource):
  cfn_type = "AWS::ServiceCatalog::LaunchNotificationConstraint"
  tf_type = "aws_service_catalog_launch_notification_constraint"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "NotificationArns", "notification_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "AcceptLanguage", "accept_language", StringValueConverter())
      self.property(w, "PortfolioId", "portfolio_id", StringValueConverter())
      self.property(w, "ProductId", "product_id", StringValueConverter())


