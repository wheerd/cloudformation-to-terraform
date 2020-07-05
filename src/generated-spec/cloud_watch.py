from . import *

class AWS_CloudWatch_AnomalyDetector_Range(CloudFormationProperty):
  def write(self, w):
    with w.block("range"):
      self.property(w, "EndTime", "end_time", StringValueConverter())
      self.property(w, "StartTime", "start_time", StringValueConverter())


class AWS_CloudWatch_InsightRule_Tags(CloudFormationProperty):
  def write(self, w):
    with w.block("tags"):
      pass


class AWS_CloudWatch_AnomalyDetector_Dimension(CloudFormationProperty):
  def write(self, w):
    with w.block("dimension"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_CloudWatch_Alarm_Dimension(CloudFormationProperty):
  def write(self, w):
    with w.block("dimension"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_CloudWatch_Alarm_Metric(CloudFormationProperty):
  def write(self, w):
    with w.block("metric"):
      self.repeated_block(w, "Dimensions", AWS_CloudWatch_Alarm_Dimension)
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.property(w, "Namespace", "namespace", StringValueConverter())


class AWS_CloudWatch_AnomalyDetector_Configuration(CloudFormationProperty):
  def write(self, w):
    with w.block("configuration"):
      self.property(w, "MetricTimeZone", "metric_time_zone", StringValueConverter())
      self.repeated_block(w, "ExcludedTimeRanges", AWS_CloudWatch_AnomalyDetector_Range)


class AWS_CloudWatch_Dashboard(CloudFormationResource):
  cfn_type = "AWS::CloudWatch::Dashboard"
  tf_type = "aws_cloudwatch_dashboard"
  ref = "id"
  attrs = {} # Additional TF attributes: dashboard_arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DashboardName", "dashboard_name", StringValueConverter())
      self.property(w, "DashboardBody", "dashboard_body", StringValueConverter())


class AWS_CloudWatch_AnomalyDetector(CloudFormationResource):
  cfn_type = "AWS::CloudWatch::AnomalyDetector"
  tf_type = "aws_cloud_watch_anomaly_detector" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.property(w, "Stat", "stat", StringValueConverter())
      self.block(w, "Configuration", AWS_CloudWatch_AnomalyDetector_Configuration)
      self.repeated_block(w, "Dimensions", AWS_CloudWatch_AnomalyDetector_Dimension)
      self.property(w, "Namespace", "namespace", StringValueConverter())


class AWS_CloudWatch_CompositeAlarm(CloudFormationResource):
  cfn_type = "AWS::CloudWatch::CompositeAlarm"
  tf_type = "aws_cloud_watch_composite_alarm" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AlarmName", "alarm_name", StringValueConverter())
      self.property(w, "AlarmRule", "alarm_rule", StringValueConverter())
      self.property(w, "AlarmDescription", "alarm_description", StringValueConverter())
      self.property(w, "ActionsEnabled", "actions_enabled", BasicValueConverter())
      self.property(w, "OKActions", "ok_actions", ListValueConverter(StringValueConverter()))
      self.property(w, "AlarmActions", "alarm_actions", ListValueConverter(StringValueConverter()))
      self.property(w, "InsufficientDataActions", "insufficient_data_actions", ListValueConverter(StringValueConverter()))


class AWS_CloudWatch_InsightRule(CloudFormationResource):
  cfn_type = "AWS::CloudWatch::InsightRule"
  tf_type = "aws_cloud_watch_insight_rule" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "Arn": "arn",
    "RuleName": "rule_name",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "RuleState", "rule_state", StringValueConverter())
      self.property(w, "RuleBody", "rule_body", StringValueConverter())
      self.property(w, "RuleName", "rule_name", StringValueConverter())
      self.block(w, "Tags", AWS_CloudWatch_InsightRule_Tags)


class AWS_CloudWatch_Alarm_MetricStat(CloudFormationProperty):
  def write(self, w):
    with w.block("metric_stat"):
      self.block(w, "Metric", AWS_CloudWatch_Alarm_Metric)
      self.property(w, "Period", "period", BasicValueConverter())
      self.property(w, "Stat", "stat", StringValueConverter())
      self.property(w, "Unit", "unit", StringValueConverter())


class AWS_CloudWatch_Alarm_MetricDataQuery(CloudFormationProperty):
  def write(self, w):
    with w.block("metric_data_query"):
      self.property(w, "Expression", "expression", StringValueConverter())
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Label", "label", StringValueConverter())
      self.block(w, "MetricStat", AWS_CloudWatch_Alarm_MetricStat)
      self.property(w, "Period", "period", BasicValueConverter())
      self.property(w, "ReturnData", "return_data", BasicValueConverter())


class AWS_CloudWatch_Alarm(CloudFormationResource):
  cfn_type = "AWS::CloudWatch::Alarm"
  tf_type = "aws_cloud_watch_alarm" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ActionsEnabled", "actions_enabled", BasicValueConverter())
      self.property(w, "AlarmActions", "alarm_actions", ListValueConverter(StringValueConverter()))
      self.property(w, "AlarmDescription", "alarm_description", StringValueConverter())
      self.property(w, "AlarmName", "alarm_name", StringValueConverter())
      self.property(w, "ComparisonOperator", "comparison_operator", StringValueConverter())
      self.property(w, "DatapointsToAlarm", "datapoints_to_alarm", BasicValueConverter())
      self.repeated_block(w, "Dimensions", AWS_CloudWatch_Alarm_Dimension)
      self.property(w, "EvaluateLowSampleCountPercentile", "evaluate_low_sample_count_percentile", StringValueConverter())
      self.property(w, "EvaluationPeriods", "evaluation_periods", BasicValueConverter())
      self.property(w, "ExtendedStatistic", "extended_statistic", StringValueConverter())
      self.property(w, "InsufficientDataActions", "insufficient_data_actions", ListValueConverter(StringValueConverter()))
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.repeated_block(w, "Metrics", AWS_CloudWatch_Alarm_MetricDataQuery)
      self.property(w, "Namespace", "namespace", StringValueConverter())
      self.property(w, "OKActions", "ok_actions", ListValueConverter(StringValueConverter()))
      self.property(w, "Period", "period", BasicValueConverter())
      self.property(w, "Statistic", "statistic", StringValueConverter())
      self.property(w, "Threshold", "threshold", BasicValueConverter())
      self.property(w, "ThresholdMetricId", "threshold_metric_id", StringValueConverter())
      self.property(w, "TreatMissingData", "treat_missing_data", StringValueConverter())
      self.property(w, "Unit", "unit", StringValueConverter())


