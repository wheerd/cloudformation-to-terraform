from . import *

class AWS_CodeStarNotifications_NotificationRule_Target(CloudFormationProperty):
  def write(self, w):
    with w.block("target"):
      self.property(w, "TargetType", "target_type", StringValueConverter())
      self.property(w, "TargetAddress", "target_address", StringValueConverter())


class AWS_CodeStarNotifications_NotificationRule(CloudFormationResource):
  cfn_type = "AWS::CodeStarNotifications::NotificationRule"
  tf_type = "aws_codestarnotifications_notification_rule"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "EventTypeIds", "event_type_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "Status", "status", StringValueConverter())
      self.property(w, "DetailType", "detail_type", StringValueConverter())
      self.property(w, "Resource", "resource", StringValueConverter())
      self.repeated_block(w, "Targets", AWS_CodeStarNotifications_NotificationRule_Target)
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


