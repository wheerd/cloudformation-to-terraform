from . import *

class AWS_RAM_ResourceShare(CloudFormationResource):
  cfn_type = "AWS::RAM::ResourceShare"
  tf_type = "aws_ram_resource_share"
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Principals", "principals", ListValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping
      self.property(w, "AllowExternalPrincipals", "allow_external_principals", BasicValueConverter())
      self.property(w, "ResourceArns", "arn", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


