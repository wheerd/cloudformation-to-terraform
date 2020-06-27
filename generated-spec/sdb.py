from . import *

class AWS_SDB_Domain(CloudFormationResource):
  terraform_resource = "aws_sdb_domain"

  resource_type = "AWS::SDB::Domain"

  props = {
    "Description": (StringValueConverter(), "description"),
  }

