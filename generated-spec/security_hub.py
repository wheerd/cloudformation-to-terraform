from . import *

class AWS_SecurityHub_Hub(CloudFormationResource):
  cfn_type = "AWS::SecurityHub::Hub"
  tf_type = "aws_security_hub_hub" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Tags", "tags", JsonValueConverter())


