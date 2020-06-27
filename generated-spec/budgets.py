from . import *

class AWS_Budgets_Budget_CostTypes(CloudFormationProperty):
  entity = "AWS::Budgets::Budget"
  tf_block_type = "cost_types"

  props = {
    "IncludeSupport": (BasicValueConverter(), "include_support"),
    "IncludeOtherSubscription": (BasicValueConverter(), "include_other_subscription"),
    "IncludeTax": (BasicValueConverter(), "include_tax"),
    "IncludeSubscription": (BasicValueConverter(), "include_subscription"),
    "UseBlended": (BasicValueConverter(), "use_blended"),
    "IncludeUpfront": (BasicValueConverter(), "include_upfront"),
    "IncludeDiscount": (BasicValueConverter(), "include_discount"),
    "IncludeCredit": (BasicValueConverter(), "include_credit"),
    "IncludeRecurring": (BasicValueConverter(), "include_recurring"),
    "UseAmortized": (BasicValueConverter(), "use_amortized"),
    "IncludeRefund": (BasicValueConverter(), "include_refund"),
  }

class AWS_Budgets_Budget_Subscriber(CloudFormationProperty):
  entity = "AWS::Budgets::Budget"
  tf_block_type = "subscriber"

  props = {
    "SubscriptionType": (StringValueConverter(), "subscription_type"),
    "Address": (StringValueConverter(), "address"),
  }

class AWS_Budgets_Budget_Notification(CloudFormationProperty):
  entity = "AWS::Budgets::Budget"
  tf_block_type = "notification"

  props = {
    "ComparisonOperator": (StringValueConverter(), "comparison_operator"),
    "NotificationType": (StringValueConverter(), "notification_type"),
    "Threshold": (BasicValueConverter(), "threshold"),
    "ThresholdType": (StringValueConverter(), "threshold_type"),
  }

class AWS_Budgets_Budget_TimePeriod(CloudFormationProperty):
  entity = "AWS::Budgets::Budget"
  tf_block_type = "time_period"

  props = {
    "Start": (StringValueConverter(), "start"),
    "End": (StringValueConverter(), "end"),
  }

class AWS_Budgets_Budget_Spend(CloudFormationProperty):
  entity = "AWS::Budgets::Budget"
  tf_block_type = "spend"

  props = {
    "Amount": (BasicValueConverter(), "amount"),
    "Unit": (StringValueConverter(), "unit"),
  }

class AWS_Budgets_Budget_BudgetData(CloudFormationProperty):
  entity = "AWS::Budgets::Budget"
  tf_block_type = "budget_data"

  props = {
    "BudgetLimit": (AWS_Budgets_Budget_Spend, "budget_limit"),
    "TimePeriod": (AWS_Budgets_Budget_TimePeriod, "time_period"),
    "TimeUnit": (StringValueConverter(), "time_unit"),
    "PlannedBudgetLimits": (StringValueConverter(), "planned_budget_limits"),
    "CostFilters": (StringValueConverter(), "cost_filters"),
    "BudgetName": (StringValueConverter(), "budget_name"),
    "CostTypes": (AWS_Budgets_Budget_CostTypes, "cost_types"),
    "BudgetType": (StringValueConverter(), "budget_type"),
  }

class AWS_Budgets_Budget_NotificationWithSubscribers(CloudFormationProperty):
  entity = "AWS::Budgets::Budget"
  tf_block_type = "notification_with_subscribers"

  props = {
    "Subscribers": (BlockValueConverter(AWS_Budgets_Budget_Subscriber), None),
    "Notification": (AWS_Budgets_Budget_Notification, "notification"),
  }

class AWS_Budgets_Budget(CloudFormationResource):
  terraform_resource = "aws_budgets_budget"

  resource_type = "AWS::Budgets::Budget"

  props = {
    "NotificationsWithSubscribers": (BlockValueConverter(AWS_Budgets_Budget_NotificationWithSubscribers), None),
    "Budget": (AWS_Budgets_Budget_BudgetData, "budget"),
  }

