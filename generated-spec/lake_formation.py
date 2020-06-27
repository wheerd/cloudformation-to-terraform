from . import *

class AWS_LakeFormation_Permissions_DataLocationResource(CloudFormationProperty):
  entity = "AWS::LakeFormation::Permissions"
  tf_block_type = "data_location_resource"

  props = {
    "S3Resource": (StringValueConverter(), "s3_resource"),
  }

class AWS_LakeFormation_DataLakeSettings_DataLakePrincipal(CloudFormationProperty):
  entity = "AWS::LakeFormation::DataLakeSettings"
  tf_block_type = "data_lake_principal"

  props = {
    "DataLakePrincipalIdentifier": (StringValueConverter(), "data_lake_principal_identifier"),
  }

class AWS_LakeFormation_Permissions_ColumnWildcard(CloudFormationProperty):
  entity = "AWS::LakeFormation::Permissions"
  tf_block_type = "column_wildcard"

  props = {
    "ExcludedColumnNames": (ListValueConverter(StringValueConverter()), "excluded_column_names"),
  }

class AWS_LakeFormation_Permissions_DatabaseResource(CloudFormationProperty):
  entity = "AWS::LakeFormation::Permissions"
  tf_block_type = "database_resource"

  props = {
    "Name": (StringValueConverter(), "name"),
  }

class AWS_LakeFormation_Permissions_DataLakePrincipal(CloudFormationProperty):
  entity = "AWS::LakeFormation::Permissions"
  tf_block_type = "data_lake_principal"

  props = {
    "DataLakePrincipalIdentifier": (StringValueConverter(), "data_lake_principal_identifier"),
  }

class AWS_LakeFormation_Permissions_TableResource(CloudFormationProperty):
  entity = "AWS::LakeFormation::Permissions"
  tf_block_type = "table_resource"

  props = {
    "DatabaseName": (StringValueConverter(), "database_name"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_LakeFormation_Permissions_TableWithColumnsResource(CloudFormationProperty):
  entity = "AWS::LakeFormation::Permissions"
  tf_block_type = "table_with_columns_resource"

  props = {
    "ColumnNames": (ListValueConverter(StringValueConverter()), "column_names"),
    "DatabaseName": (StringValueConverter(), "database_name"),
    "Name": (StringValueConverter(), "name"),
    "ColumnWildcard": (AWS_LakeFormation_Permissions_ColumnWildcard, "column_wildcard"),
  }

class AWS_LakeFormation_Permissions_Resource(CloudFormationProperty):
  entity = "AWS::LakeFormation::Permissions"
  tf_block_type = "resource"

  props = {
    "TableResource": (AWS_LakeFormation_Permissions_TableResource, "table_resource"),
    "DatabaseResource": (AWS_LakeFormation_Permissions_DatabaseResource, "database_resource"),
    "DataLocationResource": (AWS_LakeFormation_Permissions_DataLocationResource, "data_location_resource"),
    "TableWithColumnsResource": (AWS_LakeFormation_Permissions_TableWithColumnsResource, "table_with_columns_resource"),
  }

class AWS_LakeFormation_DataLakeSettings_Admins(CloudFormationProperty):
  entity = "AWS::LakeFormation::DataLakeSettings"
  tf_block_type = "admins"

class AWS_LakeFormation_Resource(CloudFormationResource):
  terraform_resource = "aws_lake_formation_resource"

  resource_type = "AWS::LakeFormation::Resource"

  props = {
    "ResourceArn": (StringValueConverter(), "resource_arn"),
    "UseServiceLinkedRole": (BasicValueConverter(), "use_service_linked_role"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_LakeFormation_Permissions(CloudFormationResource):
  terraform_resource = "aws_lake_formation_permissions"

  resource_type = "AWS::LakeFormation::Permissions"

  props = {
    "DataLakePrincipal": (AWS_LakeFormation_Permissions_DataLakePrincipal, "data_lake_principal"),
    "Resource": (AWS_LakeFormation_Permissions_Resource, "resource"),
    "Permissions": (ListValueConverter(StringValueConverter()), "permissions"),
    "PermissionsWithGrantOption": (ListValueConverter(StringValueConverter()), "permissions_with_grant_option"),
  }

class AWS_LakeFormation_DataLakeSettings(CloudFormationResource):
  terraform_resource = "aws_lake_formation_data_lake_settings"

  resource_type = "AWS::LakeFormation::DataLakeSettings"

  props = {
    "Admins": (AWS_LakeFormation_DataLakeSettings_Admins, "admins"),
  }

