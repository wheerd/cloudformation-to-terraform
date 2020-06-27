from . import *

class AWS_DirectoryService_MicrosoftAD_VpcSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("vpc_settings"):
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "VpcId", "vpc_id", StringValueConverter())


class AWS_DirectoryService_SimpleAD_VpcSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("vpc_settings"):
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "VpcId", "vpc_id", StringValueConverter())


class AWS_DirectoryService_MicrosoftAD(CloudFormationResource):
  cfn_type = "AWS::DirectoryService::MicrosoftAD"
  tf_type = "aws_directory_service_microsoft_ad"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CreateAlias", "create_alias", BasicValueConverter())
      self.property(w, "Edition", "edition", StringValueConverter())
      self.property(w, "EnableSso", "enable_sso", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Password", "password", StringValueConverter())
      self.property(w, "ShortName", "short_name", StringValueConverter())
      self.block(w, "VpcSettings", AWS_DirectoryService_MicrosoftAD_VpcSettings)


class AWS_DirectoryService_SimpleAD(CloudFormationResource):
  cfn_type = "AWS::DirectoryService::SimpleAD"
  tf_type = "aws_directory_service_simple_ad"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CreateAlias", "create_alias", BasicValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "EnableSso", "enable_sso", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Password", "password", StringValueConverter())
      self.property(w, "ShortName", "short_name", StringValueConverter())
      self.property(w, "Size", "size", StringValueConverter())
      self.block(w, "VpcSettings", AWS_DirectoryService_SimpleAD_VpcSettings)


