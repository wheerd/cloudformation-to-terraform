from . import *

class AWS_QLDB_Ledger(CloudFormationResource):
  cfn_type = "AWS::QLDB::Ledger"
  tf_type = "aws_qldb_ledger"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PermissionsMode", "permissions_mode", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "DeletionProtection", "deletion_protection", BasicValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


