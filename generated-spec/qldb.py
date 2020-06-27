from . import *

class AWS_QLDB_Ledger(CloudFormationResource):
  terraform_resource = "aws_qldb_ledger"

  resource_type = "AWS::QLDB::Ledger"

  props = {
    "PermissionsMode": (StringValueConverter(), "permissions_mode"),
    "DeletionProtection": (BasicValueConverter(), "deletion_protection"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

