from . import *

class AWS_CodeStarNotifications_NotificationRule_Target(CloudFormationProperty):
  entity = "AWS::CodeStarNotifications::NotificationRule"
  tf_block_type = "target"

  props = {
    "TargetType": (StringValueConverter(), "target_type"),
    "TargetAddress": (StringValueConverter(), "target_address"),
  }

class AWS_CodeStarNotifications_NotificationRule(CloudFormationResource):
  terraform_resource = "aws_code_star_notifications_notification_rule"

  resource_type = "AWS::CodeStarNotifications::NotificationRule"

  props = {
    "EventTypeIds": (ListValueConverter(StringValueConverter()), "event_type_ids"),
    "Status": (StringValueConverter(), "status"),
    "DetailType": (StringValueConverter(), "detail_type"),
    "Resource": (StringValueConverter(), "resource"),
    "Targets": (BlockValueConverter(AWS_CodeStarNotifications_NotificationRule_Target), None),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

