from . import *

class AWS_SecurityHub_Hub(CloudFormationResource):
  terraform_resource = "aws_security_hub_hub"

  resource_type = "AWS::SecurityHub::Hub"

  props = {
    "Tags": (StringValueConverter(), "tags"),
  }

