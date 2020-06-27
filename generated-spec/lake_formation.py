from . import *

class AWS_LakeFormation_Permissions_DataLocationResource(CloudFormationProperty):
  def write(self, w):
    with w.block("data_location_resource"):
      self.property(w, "S3Resource", "s3_resource", StringValueConverter())


class AWS_LakeFormation_DataLakeSettings_DataLakePrincipal(CloudFormationProperty):
  def write(self, w):
    with w.block("data_lake_principal"):
      self.property(w, "DataLakePrincipalIdentifier", "data_lake_principal_identifier", StringValueConverter())


class AWS_LakeFormation_Permissions_ColumnWildcard(CloudFormationProperty):
  def write(self, w):
    with w.block("column_wildcard"):
      self.property(w, "ExcludedColumnNames", "excluded_column_names", ListValueConverter(StringValueConverter()))


class AWS_LakeFormation_Permissions_DatabaseResource(CloudFormationProperty):
  def write(self, w):
    with w.block("database_resource"):
      self.property(w, "Name", "name", StringValueConverter())


class AWS_LakeFormation_Permissions_DataLakePrincipal(CloudFormationProperty):
  def write(self, w):
    with w.block("data_lake_principal"):
      self.property(w, "DataLakePrincipalIdentifier", "data_lake_principal_identifier", StringValueConverter())


class AWS_LakeFormation_Permissions_TableResource(CloudFormationProperty):
  def write(self, w):
    with w.block("table_resource"):
      self.property(w, "DatabaseName", "database_name", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_LakeFormation_Permissions_TableWithColumnsResource(CloudFormationProperty):
  def write(self, w):
    with w.block("table_with_columns_resource"):
      self.property(w, "ColumnNames", "column_names", ListValueConverter(StringValueConverter()))
      self.property(w, "DatabaseName", "database_name", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "ColumnWildcard", AWS_LakeFormation_Permissions_ColumnWildcard)


class AWS_LakeFormation_Permissions_Resource(CloudFormationProperty):
  def write(self, w):
    with w.block("resource"):
      self.block(w, "TableResource", AWS_LakeFormation_Permissions_TableResource)
      self.block(w, "DatabaseResource", AWS_LakeFormation_Permissions_DatabaseResource)
      self.block(w, "DataLocationResource", AWS_LakeFormation_Permissions_DataLocationResource)
      self.block(w, "TableWithColumnsResource", AWS_LakeFormation_Permissions_TableWithColumnsResource)


class AWS_LakeFormation_DataLakeSettings_Admins(CloudFormationProperty):
  def write(self, w):
    with w.block("admins"):
      pass


class AWS_LakeFormation_Resource(CloudFormationResource):
  cfn_type = "AWS::LakeFormation::Resource"
  tf_type = "aws_lake_formation_resource"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ResourceArn", "resource_arn", StringValueConverter())
      self.property(w, "UseServiceLinkedRole", "use_service_linked_role", BasicValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_LakeFormation_Permissions(CloudFormationResource):
  cfn_type = "AWS::LakeFormation::Permissions"
  tf_type = "aws_lake_formation_permissions"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "DataLakePrincipal", AWS_LakeFormation_Permissions_DataLakePrincipal)
      self.block(w, "Resource", AWS_LakeFormation_Permissions_Resource)
      self.property(w, "Permissions", "permissions", ListValueConverter(StringValueConverter()))
      self.property(w, "PermissionsWithGrantOption", "permissions_with_grant_option", ListValueConverter(StringValueConverter()))


class AWS_LakeFormation_DataLakeSettings(CloudFormationResource):
  cfn_type = "AWS::LakeFormation::DataLakeSettings"
  tf_type = "aws_lake_formation_data_lake_settings"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "Admins", AWS_LakeFormation_DataLakeSettings_Admins)


