from . import *

class AWS_CE_CostCategory(CloudFormationResource):
  cfn_type = "AWS::CE::CostCategory"
  tf_type = "aws_ce_cost_category" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "Arn": "arn",
    "EffectiveStart": "effective_start",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "RuleVersion", "rule_version", StringValueConverter())
      self.property(w, "Rules", "rules", StringValueConverter())


