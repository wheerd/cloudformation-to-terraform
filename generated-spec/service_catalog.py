from . import *

class AWS_ServiceCatalog_CloudFormationProvisionedProduct_ProvisioningParameter(CloudFormationProperty):
  entity = "AWS::ServiceCatalog::CloudFormationProvisionedProduct"
  tf_block_type = "provisioning_parameter"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_ServiceCatalog_CloudFormationProduct_ProvisioningArtifactProperties(CloudFormationProperty):
  entity = "AWS::ServiceCatalog::CloudFormationProduct"
  tf_block_type = "provisioning_artifact_properties"

  props = {
    "Description": (StringValueConverter(), "description"),
    "DisableTemplateValidation": (BasicValueConverter(), "disable_template_validation"),
    "Info": (StringValueConverter(), "info"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_ServiceCatalog_CloudFormationProvisionedProduct_ProvisioningPreferences(CloudFormationProperty):
  entity = "AWS::ServiceCatalog::CloudFormationProvisionedProduct"
  tf_block_type = "provisioning_preferences"

  props = {
    "StackSetAccounts": (ListValueConverter(StringValueConverter()), "stack_set_accounts"),
    "StackSetFailureToleranceCount": (BasicValueConverter(), "stack_set_failure_tolerance_count"),
    "StackSetMaxConcurrencyPercentage": (BasicValueConverter(), "stack_set_max_concurrency_percentage"),
    "StackSetMaxConcurrencyCount": (BasicValueConverter(), "stack_set_max_concurrency_count"),
    "StackSetRegions": (ListValueConverter(StringValueConverter()), "stack_set_regions"),
    "StackSetOperationType": (StringValueConverter(), "stack_set_operation_type"),
    "StackSetFailureTolerancePercentage": (BasicValueConverter(), "stack_set_failure_tolerance_percentage"),
  }

class AWS_ServiceCatalog_PortfolioShare(CloudFormationResource):
  terraform_resource = "aws_service_catalog_portfolio_share"

  resource_type = "AWS::ServiceCatalog::PortfolioShare"

  props = {
    "AccountId": (StringValueConverter(), "account_id"),
    "AcceptLanguage": (StringValueConverter(), "accept_language"),
    "PortfolioId": (StringValueConverter(), "portfolio_id"),
  }

class AWS_ServiceCatalog_ResourceUpdateConstraint(CloudFormationResource):
  terraform_resource = "aws_service_catalog_resource_update_constraint"

  resource_type = "AWS::ServiceCatalog::ResourceUpdateConstraint"

  props = {
    "Description": (StringValueConverter(), "description"),
    "AcceptLanguage": (StringValueConverter(), "accept_language"),
    "TagUpdateOnProvisionedProduct": (StringValueConverter(), "tag_update_on_provisioned_product"),
    "PortfolioId": (StringValueConverter(), "portfolio_id"),
    "ProductId": (StringValueConverter(), "product_id"),
  }

class AWS_ServiceCatalog_TagOption(CloudFormationResource):
  terraform_resource = "aws_service_catalog_tag_option"

  resource_type = "AWS::ServiceCatalog::TagOption"

  props = {
    "Active": (BasicValueConverter(), "active"),
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_ServiceCatalog_CloudFormationProduct(CloudFormationResource):
  terraform_resource = "aws_service_catalog_cloud_formation_product"

  resource_type = "AWS::ServiceCatalog::CloudFormationProduct"

  props = {
    "ReplaceProvisioningArtifacts": (BasicValueConverter(), "replace_provisioning_artifacts"),
    "Owner": (StringValueConverter(), "owner"),
    "SupportDescription": (StringValueConverter(), "support_description"),
    "Description": (StringValueConverter(), "description"),
    "Distributor": (StringValueConverter(), "distributor"),
    "SupportEmail": (StringValueConverter(), "support_email"),
    "AcceptLanguage": (StringValueConverter(), "accept_language"),
    "SupportUrl": (StringValueConverter(), "support_url"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
    "ProvisioningArtifactParameters": (BlockValueConverter(AWS_ServiceCatalog_CloudFormationProduct_ProvisioningArtifactProperties), None),
  }

class AWS_ServiceCatalog_PortfolioProductAssociation(CloudFormationResource):
  terraform_resource = "aws_service_catalog_portfolio_product_association"

  resource_type = "AWS::ServiceCatalog::PortfolioProductAssociation"

  props = {
    "SourcePortfolioId": (StringValueConverter(), "source_portfolio_id"),
    "AcceptLanguage": (StringValueConverter(), "accept_language"),
    "PortfolioId": (StringValueConverter(), "portfolio_id"),
    "ProductId": (StringValueConverter(), "product_id"),
  }

class AWS_ServiceCatalog_AcceptedPortfolioShare(CloudFormationResource):
  terraform_resource = "aws_service_catalog_accepted_portfolio_share"

  resource_type = "AWS::ServiceCatalog::AcceptedPortfolioShare"

  props = {
    "AcceptLanguage": (StringValueConverter(), "accept_language"),
    "PortfolioId": (StringValueConverter(), "portfolio_id"),
  }

class AWS_ServiceCatalog_StackSetConstraint(CloudFormationResource):
  terraform_resource = "aws_service_catalog_stack_set_constraint"

  resource_type = "AWS::ServiceCatalog::StackSetConstraint"

  props = {
    "Description": (StringValueConverter(), "description"),
    "StackInstanceControl": (StringValueConverter(), "stack_instance_control"),
    "AcceptLanguage": (StringValueConverter(), "accept_language"),
    "PortfolioId": (StringValueConverter(), "portfolio_id"),
    "ProductId": (StringValueConverter(), "product_id"),
    "RegionList": (ListValueConverter(StringValueConverter()), "region_list"),
    "AdminRole": (StringValueConverter(), "admin_role"),
    "AccountList": (ListValueConverter(StringValueConverter()), "account_list"),
    "ExecutionRole": (StringValueConverter(), "execution_role"),
  }

class AWS_ServiceCatalog_TagOptionAssociation(CloudFormationResource):
  terraform_resource = "aws_service_catalog_tag_option_association"

  resource_type = "AWS::ServiceCatalog::TagOptionAssociation"

  props = {
    "TagOptionId": (StringValueConverter(), "tag_option_id"),
    "ResourceId": (StringValueConverter(), "resource_id"),
  }

class AWS_ServiceCatalog_LaunchTemplateConstraint(CloudFormationResource):
  terraform_resource = "aws_service_catalog_launch_template_constraint"

  resource_type = "AWS::ServiceCatalog::LaunchTemplateConstraint"

  props = {
    "Description": (StringValueConverter(), "description"),
    "AcceptLanguage": (StringValueConverter(), "accept_language"),
    "PortfolioId": (StringValueConverter(), "portfolio_id"),
    "ProductId": (StringValueConverter(), "product_id"),
    "Rules": (StringValueConverter(), "rules"),
  }

class AWS_ServiceCatalog_PortfolioPrincipalAssociation(CloudFormationResource):
  terraform_resource = "aws_service_catalog_portfolio_principal_association"

  resource_type = "AWS::ServiceCatalog::PortfolioPrincipalAssociation"

  props = {
    "PrincipalARN": (StringValueConverter(), "principal_arn"),
    "AcceptLanguage": (StringValueConverter(), "accept_language"),
    "PortfolioId": (StringValueConverter(), "portfolio_id"),
    "PrincipalType": (StringValueConverter(), "principal_type"),
  }

class AWS_ServiceCatalog_CloudFormationProvisionedProduct(CloudFormationResource):
  terraform_resource = "aws_service_catalog_cloud_formation_provisioned_product"

  resource_type = "AWS::ServiceCatalog::CloudFormationProvisionedProduct"

  props = {
    "PathId": (StringValueConverter(), "path_id"),
    "ProvisioningParameters": (BlockValueConverter(AWS_ServiceCatalog_CloudFormationProvisionedProduct_ProvisioningParameter), None),
    "ProvisioningPreferences": (AWS_ServiceCatalog_CloudFormationProvisionedProduct_ProvisioningPreferences, "provisioning_preferences"),
    "ProductName": (StringValueConverter(), "product_name"),
    "ProvisioningArtifactName": (StringValueConverter(), "provisioning_artifact_name"),
    "NotificationArns": (ListValueConverter(StringValueConverter()), "notification_arns"),
    "AcceptLanguage": (StringValueConverter(), "accept_language"),
    "ProductId": (StringValueConverter(), "product_id"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "ProvisionedProductName": (StringValueConverter(), "provisioned_product_name"),
    "ProvisioningArtifactId": (StringValueConverter(), "provisioning_artifact_id"),
  }

class AWS_ServiceCatalog_LaunchRoleConstraint(CloudFormationResource):
  terraform_resource = "aws_service_catalog_launch_role_constraint"

  resource_type = "AWS::ServiceCatalog::LaunchRoleConstraint"

  props = {
    "Description": (StringValueConverter(), "description"),
    "LocalRoleName": (StringValueConverter(), "local_role_name"),
    "AcceptLanguage": (StringValueConverter(), "accept_language"),
    "PortfolioId": (StringValueConverter(), "portfolio_id"),
    "ProductId": (StringValueConverter(), "product_id"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_ServiceCatalog_Portfolio(CloudFormationResource):
  terraform_resource = "aws_service_catalog_portfolio"

  resource_type = "AWS::ServiceCatalog::Portfolio"

  props = {
    "ProviderName": (StringValueConverter(), "provider_name"),
    "Description": (StringValueConverter(), "description"),
    "DisplayName": (StringValueConverter(), "display_name"),
    "AcceptLanguage": (StringValueConverter(), "accept_language"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_ServiceCatalog_LaunchNotificationConstraint(CloudFormationResource):
  terraform_resource = "aws_service_catalog_launch_notification_constraint"

  resource_type = "AWS::ServiceCatalog::LaunchNotificationConstraint"

  props = {
    "Description": (StringValueConverter(), "description"),
    "NotificationArns": (ListValueConverter(StringValueConverter()), "notification_arns"),
    "AcceptLanguage": (StringValueConverter(), "accept_language"),
    "PortfolioId": (StringValueConverter(), "portfolio_id"),
    "ProductId": (StringValueConverter(), "product_id"),
  }

