from . import *

class AWS_CloudWatch_AnomalyDetector_Range(CloudFormationProperty):
  entity = "AWS::CloudWatch::AnomalyDetector"
  tf_block_type = "range"

  props = {
    "EndTime": (StringValueConverter(), "end_time"),
    "StartTime": (StringValueConverter(), "start_time"),
  }

class AWS_CloudWatch_InsightRule_Tags(CloudFormationProperty):
  entity = "AWS::CloudWatch::InsightRule"
  tf_block_type = "tags"

class AWS_CloudWatch_AnomalyDetector_Dimension(CloudFormationProperty):
  entity = "AWS::CloudWatch::AnomalyDetector"
  tf_block_type = "dimension"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_CloudWatch_Alarm_Dimension(CloudFormationProperty):
  entity = "AWS::CloudWatch::Alarm"
  tf_block_type = "dimension"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_CloudWatch_Alarm_Metric(CloudFormationProperty):
  entity = "AWS::CloudWatch::Alarm"
  tf_block_type = "metric"

  props = {
    "Dimensions": (BlockValueConverter(AWS_CloudWatch_Alarm_Dimension), None),
    "MetricName": (StringValueConverter(), "metric_name"),
    "Namespace": (StringValueConverter(), "namespace"),
  }

class AWS_CloudWatch_AnomalyDetector_Configuration(CloudFormationProperty):
  entity = "AWS::CloudWatch::AnomalyDetector"
  tf_block_type = "configuration"

  props = {
    "MetricTimeZone": (StringValueConverter(), "metric_time_zone"),
    "ExcludedTimeRanges": (BlockValueConverter(AWS_CloudWatch_AnomalyDetector_Range), None),
  }

class AWS_CloudWatch_Dashboard(CloudFormationResource):
  terraform_resource = "aws_cloud_watch_dashboard"

  resource_type = "AWS::CloudWatch::Dashboard"

  props = {
    "DashboardName": (StringValueConverter(), "dashboard_name"),
    "DashboardBody": (StringValueConverter(), "dashboard_body"),
  }

class AWS_CloudWatch_AnomalyDetector(CloudFormationResource):
  terraform_resource = "aws_cloud_watch_anomaly_detector"

  resource_type = "AWS::CloudWatch::AnomalyDetector"

  props = {
    "MetricName": (StringValueConverter(), "metric_name"),
    "Stat": (StringValueConverter(), "stat"),
    "Configuration": (AWS_CloudWatch_AnomalyDetector_Configuration, "configuration"),
    "Dimensions": (BlockValueConverter(AWS_CloudWatch_AnomalyDetector_Dimension), None),
    "Namespace": (StringValueConverter(), "namespace"),
  }

class AWS_CloudWatch_CompositeAlarm(CloudFormationResource):
  terraform_resource = "aws_cloud_watch_composite_alarm"

  resource_type = "AWS::CloudWatch::CompositeAlarm"

  props = {
    "AlarmName": (StringValueConverter(), "alarm_name"),
    "AlarmRule": (StringValueConverter(), "alarm_rule"),
    "AlarmDescription": (StringValueConverter(), "alarm_description"),
    "ActionsEnabled": (BasicValueConverter(), "actions_enabled"),
    "OKActions": (ListValueConverter(StringValueConverter()), "ok_actions"),
    "AlarmActions": (ListValueConverter(StringValueConverter()), "alarm_actions"),
    "InsufficientDataActions": (ListValueConverter(StringValueConverter()), "insufficient_data_actions"),
  }

class AWS_CloudWatch_InsightRule(CloudFormationResource):
  terraform_resource = "aws_cloud_watch_insight_rule"

  resource_type = "AWS::CloudWatch::InsightRule"

  props = {
    "RuleState": (StringValueConverter(), "rule_state"),
    "RuleBody": (StringValueConverter(), "rule_body"),
    "RuleName": (StringValueConverter(), "rule_name"),
    "Tags": (AWS_CloudWatch_InsightRule_Tags, "tags"),
  }

class AWS_CloudWatch_Alarm_MetricStat(CloudFormationProperty):
  entity = "AWS::CloudWatch::Alarm"
  tf_block_type = "metric_stat"

  props = {
    "Metric": (AWS_CloudWatch_Alarm_Metric, "metric"),
    "Period": (BasicValueConverter(), "period"),
    "Stat": (StringValueConverter(), "stat"),
    "Unit": (StringValueConverter(), "unit"),
  }

class AWS_CloudWatch_Alarm_MetricDataQuery(CloudFormationProperty):
  entity = "AWS::CloudWatch::Alarm"
  tf_block_type = "metric_data_query"

  props = {
    "Expression": (StringValueConverter(), "expression"),
    "Id": (StringValueConverter(), "id"),
    "Label": (StringValueConverter(), "label"),
    "MetricStat": (AWS_CloudWatch_Alarm_MetricStat, "metric_stat"),
    "Period": (BasicValueConverter(), "period"),
    "ReturnData": (BasicValueConverter(), "return_data"),
  }

class AWS_CloudWatch_Alarm(CloudFormationResource):
  terraform_resource = "aws_cloud_watch_alarm"

  resource_type = "AWS::CloudWatch::Alarm"

  props = {
    "ActionsEnabled": (BasicValueConverter(), "actions_enabled"),
    "AlarmActions": (ListValueConverter(StringValueConverter()), "alarm_actions"),
    "AlarmDescription": (StringValueConverter(), "alarm_description"),
    "AlarmName": (StringValueConverter(), "alarm_name"),
    "ComparisonOperator": (StringValueConverter(), "comparison_operator"),
    "DatapointsToAlarm": (BasicValueConverter(), "datapoints_to_alarm"),
    "Dimensions": (BlockValueConverter(AWS_CloudWatch_Alarm_Dimension), None),
    "EvaluateLowSampleCountPercentile": (StringValueConverter(), "evaluate_low_sample_count_percentile"),
    "EvaluationPeriods": (BasicValueConverter(), "evaluation_periods"),
    "ExtendedStatistic": (StringValueConverter(), "extended_statistic"),
    "InsufficientDataActions": (ListValueConverter(StringValueConverter()), "insufficient_data_actions"),
    "MetricName": (StringValueConverter(), "metric_name"),
    "Metrics": (BlockValueConverter(AWS_CloudWatch_Alarm_MetricDataQuery), None),
    "Namespace": (StringValueConverter(), "namespace"),
    "OKActions": (ListValueConverter(StringValueConverter()), "ok_actions"),
    "Period": (BasicValueConverter(), "period"),
    "Statistic": (StringValueConverter(), "statistic"),
    "Threshold": (BasicValueConverter(), "threshold"),
    "ThresholdMetricId": (StringValueConverter(), "threshold_metric_id"),
    "TreatMissingData": (StringValueConverter(), "treat_missing_data"),
    "Unit": (StringValueConverter(), "unit"),
  }

