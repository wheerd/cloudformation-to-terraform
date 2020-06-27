from . import *

class AWS_CE_CostCategory(CloudFormationResource):
  terraform_resource = "aws_ce_cost_category"

  resource_type = "AWS::CE::CostCategory"

  props = {
    "Name": (StringValueConverter(), "name"),
    "RuleVersion": (StringValueConverter(), "rule_version"),
    "Rules": (StringValueConverter(), "rules"),
  }

