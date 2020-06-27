from . import *

class AWS_RAM_ResourceShare(CloudFormationResource):
  terraform_resource = "aws_ram_resource_share"

  resource_type = "AWS::RAM::ResourceShare"

  props = {
    "Principals": (ListValueConverter(StringValueConverter()), "principals"),
    "AllowExternalPrincipals": (BasicValueConverter(), "allow_external_principals"),
    "ResourceArns": (ListValueConverter(StringValueConverter()), "resource_arns"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

