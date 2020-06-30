from . import *

class AWS_SES_ReceiptRule_BounceAction(CloudFormationProperty):
  def write(self, w):
    with w.block("bounce_action"):
      self.property(w, "Sender", "sender", StringValueConverter())
      self.property(w, "SmtpReplyCode", "smtp_reply_code", StringValueConverter())
      self.property(w, "Message", "message", StringValueConverter())
      self.property(w, "TopicArn", "topic_arn", StringValueConverter())
      self.property(w, "StatusCode", "status_code", StringValueConverter())


class AWS_SES_Template_Template(CloudFormationProperty):
  def write(self, w):
    with w.block("template"):
      self.property(w, "HtmlPart", "html_part", StringValueConverter())
      self.property(w, "TextPart", "text_part", StringValueConverter())
      self.property(w, "TemplateName", "template_name", StringValueConverter())
      self.property(w, "SubjectPart", "subject_part", StringValueConverter())


class AWS_SES_ReceiptRule_S3Action(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_action"):
      self.property(w, "BucketName", "bucket_name", StringValueConverter())
      self.property(w, "KmsKeyArn", "kms_key_arn", StringValueConverter())
      self.property(w, "TopicArn", "topic_arn", StringValueConverter())
      self.property(w, "ObjectKeyPrefix", "object_key_prefix", StringValueConverter())


class AWS_SES_ConfigurationSetEventDestination_DimensionConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("dimension_configuration"):
      self.property(w, "DimensionValueSource", "dimension_value_source", StringValueConverter())
      self.property(w, "DefaultDimensionValue", "default_dimension_value", StringValueConverter())
      self.property(w, "DimensionName", "dimension_name", StringValueConverter())


class AWS_SES_ReceiptRule_WorkmailAction(CloudFormationProperty):
  def write(self, w):
    with w.block("workmail_action"):
      self.property(w, "TopicArn", "topic_arn", StringValueConverter())
      self.property(w, "OrganizationArn", "organization_arn", StringValueConverter())


class AWS_SES_ReceiptRule_StopAction(CloudFormationProperty):
  def write(self, w):
    with w.block("stop_action"):
      self.property(w, "Scope", "scope", StringValueConverter())
      self.property(w, "TopicArn", "topic_arn", StringValueConverter())


class AWS_SES_ReceiptRule_SNSAction(CloudFormationProperty):
  def write(self, w):
    with w.block("sns_action"):
      self.property(w, "TopicArn", "topic_arn", StringValueConverter())
      self.property(w, "Encoding", "encoding", StringValueConverter())


class AWS_SES_ConfigurationSetEventDestination_CloudWatchDestination(CloudFormationProperty):
  def write(self, w):
    with w.block("cloud_watch_destination"):
      self.repeated_block(w, "DimensionConfigurations", AWS_SES_ConfigurationSetEventDestination_DimensionConfiguration)


class AWS_SES_ReceiptRule_LambdaAction(CloudFormationProperty):
  def write(self, w):
    with w.block("lambda_action"):
      self.property(w, "FunctionArn", "function_arn", StringValueConverter())
      self.property(w, "TopicArn", "topic_arn", StringValueConverter())
      self.property(w, "InvocationType", "invocation_type", StringValueConverter())


class AWS_SES_ConfigurationSetEventDestination_KinesisFirehoseDestination(CloudFormationProperty):
  def write(self, w):
    with w.block("kinesis_firehose_destination"):
      self.property(w, "IAMRoleARN", "iam_role_arn", StringValueConverter())
      self.property(w, "DeliveryStreamARN", "delivery_stream_arn", StringValueConverter())


class AWS_SES_ReceiptRule_AddHeaderAction(CloudFormationProperty):
  def write(self, w):
    with w.block("add_header_action"):
      self.property(w, "HeaderValue", "header_value", StringValueConverter())
      self.property(w, "HeaderName", "header_name", StringValueConverter())


class AWS_SES_ReceiptFilter_IpFilter(CloudFormationProperty):
  def write(self, w):
    with w.block("ip_filter"):
      self.property(w, "Policy", "policy", StringValueConverter())
      self.property(w, "Cidr", "cidr", StringValueConverter())


class AWS_SES_Template(CloudFormationResource):
  cfn_type = "AWS::SES::Template"
  tf_type = "aws_ses_template"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "Template", AWS_SES_Template_Template) # TODO: Probably not the correct mapping


class AWS_SES_ConfigurationSet(CloudFormationResource):
  cfn_type = "AWS::SES::ConfigurationSet"
  tf_type = "aws_ses_configuration_set"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())


class AWS_SES_ReceiptRuleSet(CloudFormationResource):
  cfn_type = "AWS::SES::ReceiptRuleSet"
  tf_type = "aws_ses_receipt_rule_set"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "RuleSetName", "rule_set_name", StringValueConverter())


class AWS_SES_ReceiptRule_Action(CloudFormationProperty):
  def write(self, w):
    with w.block("action"):
      self.block(w, "BounceAction", AWS_SES_ReceiptRule_BounceAction)
      self.block(w, "S3Action", AWS_SES_ReceiptRule_S3Action)
      self.block(w, "StopAction", AWS_SES_ReceiptRule_StopAction)
      self.block(w, "SNSAction", AWS_SES_ReceiptRule_SNSAction)
      self.block(w, "WorkmailAction", AWS_SES_ReceiptRule_WorkmailAction)
      self.block(w, "AddHeaderAction", AWS_SES_ReceiptRule_AddHeaderAction)
      self.block(w, "LambdaAction", AWS_SES_ReceiptRule_LambdaAction)


class AWS_SES_ReceiptFilter_Filter(CloudFormationProperty):
  def write(self, w):
    with w.block("filter"):
      self.block(w, "IpFilter", AWS_SES_ReceiptFilter_IpFilter)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_SES_ConfigurationSetEventDestination_EventDestination(CloudFormationProperty):
  def write(self, w):
    with w.block("event_destination"):
      self.block(w, "CloudWatchDestination", AWS_SES_ConfigurationSetEventDestination_CloudWatchDestination)
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "MatchingEventTypes", "matching_event_types", ListValueConverter(StringValueConverter()))
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "KinesisFirehoseDestination", AWS_SES_ConfigurationSetEventDestination_KinesisFirehoseDestination)


class AWS_SES_ReceiptRule_Rule(CloudFormationProperty):
  def write(self, w):
    with w.block("rule"):
      self.property(w, "ScanEnabled", "scan_enabled", BasicValueConverter())
      self.property(w, "Recipients", "recipients", ListValueConverter(StringValueConverter()))
      self.repeated_block(w, "Actions", AWS_SES_ReceiptRule_Action)
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "TlsPolicy", "tls_policy", StringValueConverter())


class AWS_SES_ReceiptFilter(CloudFormationResource):
  cfn_type = "AWS::SES::ReceiptFilter"
  tf_type = "aws_ses_receipt_filter"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "Filter", AWS_SES_ReceiptFilter_Filter) # TODO: Probably not the correct mapping


class AWS_SES_ConfigurationSetEventDestination(CloudFormationResource):
  cfn_type = "AWS::SES::ConfigurationSetEventDestination"
  tf_type = "aws_ses_configuration_set_event_destination" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ConfigurationSetName", "configuration_set_name", StringValueConverter())
      self.block(w, "EventDestination", AWS_SES_ConfigurationSetEventDestination_EventDestination)


class AWS_SES_ReceiptRule(CloudFormationResource):
  cfn_type = "AWS::SES::ReceiptRule"
  tf_type = "aws_ses_receipt_rule"
  ref = "id"
  attrs = {} # Additional TF attributes: enabled, scan_enabled, tls_policy

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "After", "after", StringValueConverter())
      self.block(w, "Rule", AWS_SES_ReceiptRule_Rule)
      self.property(w, "RuleSetName", "name", StringValueConverter())


