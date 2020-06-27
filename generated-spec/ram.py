from . import *

class AWS_RAM_ResourceShare(CloudFormationResource):
  cfn_type = "AWS::RAM::ResourceShare"
  tf_type = "aws_ram_resource_share"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Principals", "principals", ListValueConverter(StringValueConverter()))
      self.property(w, "AllowExternalPrincipals", "allow_external_principals", BasicValueConverter())
      self.property(w, "ResourceArns", "resource_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


