from . import *

class AWS_SDB_Domain(CloudFormationResource):
  cfn_type = "AWS::SDB::Domain"
  tf_type = "aws_swf_domain"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, name

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())


