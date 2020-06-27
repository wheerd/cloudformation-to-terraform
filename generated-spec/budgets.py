from . import *

class AWS_Budgets_Budget_CostTypes(CloudFormationProperty):
  def write(self, w):
    with w.block("cost_types"):
      self.property(w, "IncludeSupport", "include_support", BasicValueConverter())
      self.property(w, "IncludeOtherSubscription", "include_other_subscription", BasicValueConverter())
      self.property(w, "IncludeTax", "include_tax", BasicValueConverter())
      self.property(w, "IncludeSubscription", "include_subscription", BasicValueConverter())
      self.property(w, "UseBlended", "use_blended", BasicValueConverter())
      self.property(w, "IncludeUpfront", "include_upfront", BasicValueConverter())
      self.property(w, "IncludeDiscount", "include_discount", BasicValueConverter())
      self.property(w, "IncludeCredit", "include_credit", BasicValueConverter())
      self.property(w, "IncludeRecurring", "include_recurring", BasicValueConverter())
      self.property(w, "UseAmortized", "use_amortized", BasicValueConverter())
      self.property(w, "IncludeRefund", "include_refund", BasicValueConverter())


class AWS_Budgets_Budget_Subscriber(CloudFormationProperty):
  def write(self, w):
    with w.block("subscriber"):
      self.property(w, "SubscriptionType", "subscription_type", StringValueConverter())
      self.property(w, "Address", "address", StringValueConverter())


class AWS_Budgets_Budget_Notification(CloudFormationProperty):
  def write(self, w):
    with w.block("notification"):
      self.property(w, "ComparisonOperator", "comparison_operator", StringValueConverter())
      self.property(w, "NotificationType", "notification_type", StringValueConverter())
      self.property(w, "Threshold", "threshold", BasicValueConverter())
      self.property(w, "ThresholdType", "threshold_type", StringValueConverter())


class AWS_Budgets_Budget_TimePeriod(CloudFormationProperty):
  def write(self, w):
    with w.block("time_period"):
      self.property(w, "Start", "start", StringValueConverter())
      self.property(w, "End", "end", StringValueConverter())


class AWS_Budgets_Budget_Spend(CloudFormationProperty):
  def write(self, w):
    with w.block("spend"):
      self.property(w, "Amount", "amount", BasicValueConverter())
      self.property(w, "Unit", "unit", StringValueConverter())


class AWS_Budgets_Budget_BudgetData(CloudFormationProperty):
  def write(self, w):
    with w.block("budget_data"):
      self.block(w, "BudgetLimit", AWS_Budgets_Budget_Spend)
      self.block(w, "TimePeriod", AWS_Budgets_Budget_TimePeriod)
      self.property(w, "TimeUnit", "time_unit", StringValueConverter())
      self.property(w, "PlannedBudgetLimits", "planned_budget_limits", StringValueConverter())
      self.property(w, "CostFilters", "cost_filters", StringValueConverter())
      self.property(w, "BudgetName", "budget_name", StringValueConverter())
      self.block(w, "CostTypes", AWS_Budgets_Budget_CostTypes)
      self.property(w, "BudgetType", "budget_type", StringValueConverter())


class AWS_Budgets_Budget_NotificationWithSubscribers(CloudFormationProperty):
  def write(self, w):
    with w.block("notification_with_subscribers"):
      self.repeated_block(w, "Subscribers", AWS_Budgets_Budget_Subscriber)
      self.block(w, "Notification", AWS_Budgets_Budget_Notification)


class AWS_Budgets_Budget(CloudFormationResource):
  cfn_type = "AWS::Budgets::Budget"
  tf_type = "aws_budgets_budget"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "NotificationsWithSubscribers", AWS_Budgets_Budget_NotificationWithSubscribers)
      self.block(w, "Budget", AWS_Budgets_Budget_BudgetData)


