from . import *

class AWS_SES_ReceiptRule_BounceAction(CloudFormationProperty):
  entity = "AWS::SES::ReceiptRule"
  tf_block_type = "bounce_action"

  props = {
    "Sender": (StringValueConverter(), "sender"),
    "SmtpReplyCode": (StringValueConverter(), "smtp_reply_code"),
    "Message": (StringValueConverter(), "message"),
    "TopicArn": (StringValueConverter(), "topic_arn"),
    "StatusCode": (StringValueConverter(), "status_code"),
  }

class AWS_SES_Template_Template(CloudFormationProperty):
  entity = "AWS::SES::Template"
  tf_block_type = "template"

  props = {
    "HtmlPart": (StringValueConverter(), "html_part"),
    "TextPart": (StringValueConverter(), "text_part"),
    "TemplateName": (StringValueConverter(), "template_name"),
    "SubjectPart": (StringValueConverter(), "subject_part"),
  }

class AWS_SES_ReceiptRule_S3Action(CloudFormationProperty):
  entity = "AWS::SES::ReceiptRule"
  tf_block_type = "s3_action"

  props = {
    "BucketName": (StringValueConverter(), "bucket_name"),
    "KmsKeyArn": (StringValueConverter(), "kms_key_arn"),
    "TopicArn": (StringValueConverter(), "topic_arn"),
    "ObjectKeyPrefix": (StringValueConverter(), "object_key_prefix"),
  }

class AWS_SES_ConfigurationSetEventDestination_DimensionConfiguration(CloudFormationProperty):
  entity = "AWS::SES::ConfigurationSetEventDestination"
  tf_block_type = "dimension_configuration"

  props = {
    "DimensionValueSource": (StringValueConverter(), "dimension_value_source"),
    "DefaultDimensionValue": (StringValueConverter(), "default_dimension_value"),
    "DimensionName": (StringValueConverter(), "dimension_name"),
  }

class AWS_SES_ReceiptRule_WorkmailAction(CloudFormationProperty):
  entity = "AWS::SES::ReceiptRule"
  tf_block_type = "workmail_action"

  props = {
    "TopicArn": (StringValueConverter(), "topic_arn"),
    "OrganizationArn": (StringValueConverter(), "organization_arn"),
  }

class AWS_SES_ReceiptRule_StopAction(CloudFormationProperty):
  entity = "AWS::SES::ReceiptRule"
  tf_block_type = "stop_action"

  props = {
    "Scope": (StringValueConverter(), "scope"),
    "TopicArn": (StringValueConverter(), "topic_arn"),
  }

class AWS_SES_ReceiptRule_SNSAction(CloudFormationProperty):
  entity = "AWS::SES::ReceiptRule"
  tf_block_type = "sns_action"

  props = {
    "TopicArn": (StringValueConverter(), "topic_arn"),
    "Encoding": (StringValueConverter(), "encoding"),
  }

class AWS_SES_ConfigurationSetEventDestination_CloudWatchDestination(CloudFormationProperty):
  entity = "AWS::SES::ConfigurationSetEventDestination"
  tf_block_type = "cloud_watch_destination"

  props = {
    "DimensionConfigurations": (BlockValueConverter(AWS_SES_ConfigurationSetEventDestination_DimensionConfiguration), None),
  }

class AWS_SES_ReceiptRule_LambdaAction(CloudFormationProperty):
  entity = "AWS::SES::ReceiptRule"
  tf_block_type = "lambda_action"

  props = {
    "FunctionArn": (StringValueConverter(), "function_arn"),
    "TopicArn": (StringValueConverter(), "topic_arn"),
    "InvocationType": (StringValueConverter(), "invocation_type"),
  }

class AWS_SES_ConfigurationSetEventDestination_KinesisFirehoseDestination(CloudFormationProperty):
  entity = "AWS::SES::ConfigurationSetEventDestination"
  tf_block_type = "kinesis_firehose_destination"

  props = {
    "IAMRoleARN": (StringValueConverter(), "iam_role_arn"),
    "DeliveryStreamARN": (StringValueConverter(), "delivery_stream_arn"),
  }

class AWS_SES_ReceiptRule_AddHeaderAction(CloudFormationProperty):
  entity = "AWS::SES::ReceiptRule"
  tf_block_type = "add_header_action"

  props = {
    "HeaderValue": (StringValueConverter(), "header_value"),
    "HeaderName": (StringValueConverter(), "header_name"),
  }

class AWS_SES_ReceiptFilter_IpFilter(CloudFormationProperty):
  entity = "AWS::SES::ReceiptFilter"
  tf_block_type = "ip_filter"

  props = {
    "Policy": (StringValueConverter(), "policy"),
    "Cidr": (StringValueConverter(), "cidr"),
  }

class AWS_SES_Template(CloudFormationResource):
  terraform_resource = "aws_ses_template"

  resource_type = "AWS::SES::Template"

  props = {
    "Template": (AWS_SES_Template_Template, "template"),
  }

class AWS_SES_ConfigurationSet(CloudFormationResource):
  terraform_resource = "aws_ses_configuration_set"

  resource_type = "AWS::SES::ConfigurationSet"

  props = {
    "Name": (StringValueConverter(), "name"),
  }

class AWS_SES_ReceiptRuleSet(CloudFormationResource):
  terraform_resource = "aws_ses_receipt_rule_set"

  resource_type = "AWS::SES::ReceiptRuleSet"

  props = {
    "RuleSetName": (StringValueConverter(), "rule_set_name"),
  }

class AWS_SES_ReceiptRule_Action(CloudFormationProperty):
  entity = "AWS::SES::ReceiptRule"
  tf_block_type = "action"

  props = {
    "BounceAction": (AWS_SES_ReceiptRule_BounceAction, "bounce_action"),
    "S3Action": (AWS_SES_ReceiptRule_S3Action, "s3_action"),
    "StopAction": (AWS_SES_ReceiptRule_StopAction, "stop_action"),
    "SNSAction": (AWS_SES_ReceiptRule_SNSAction, "sns_action"),
    "WorkmailAction": (AWS_SES_ReceiptRule_WorkmailAction, "workmail_action"),
    "AddHeaderAction": (AWS_SES_ReceiptRule_AddHeaderAction, "add_header_action"),
    "LambdaAction": (AWS_SES_ReceiptRule_LambdaAction, "lambda_action"),
  }

class AWS_SES_ReceiptFilter_Filter(CloudFormationProperty):
  entity = "AWS::SES::ReceiptFilter"
  tf_block_type = "filter"

  props = {
    "IpFilter": (AWS_SES_ReceiptFilter_IpFilter, "ip_filter"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_SES_ConfigurationSetEventDestination_EventDestination(CloudFormationProperty):
  entity = "AWS::SES::ConfigurationSetEventDestination"
  tf_block_type = "event_destination"

  props = {
    "CloudWatchDestination": (AWS_SES_ConfigurationSetEventDestination_CloudWatchDestination, "cloud_watch_destination"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "MatchingEventTypes": (ListValueConverter(StringValueConverter()), "matching_event_types"),
    "Name": (StringValueConverter(), "name"),
    "KinesisFirehoseDestination": (AWS_SES_ConfigurationSetEventDestination_KinesisFirehoseDestination, "kinesis_firehose_destination"),
  }

class AWS_SES_ReceiptRule_Rule(CloudFormationProperty):
  entity = "AWS::SES::ReceiptRule"
  tf_block_type = "rule"

  props = {
    "ScanEnabled": (BasicValueConverter(), "scan_enabled"),
    "Recipients": (ListValueConverter(StringValueConverter()), "recipients"),
    "Actions": (BlockValueConverter(AWS_SES_ReceiptRule_Action), None),
    "Enabled": (BasicValueConverter(), "enabled"),
    "Name": (StringValueConverter(), "name"),
    "TlsPolicy": (StringValueConverter(), "tls_policy"),
  }

class AWS_SES_ReceiptFilter(CloudFormationResource):
  terraform_resource = "aws_ses_receipt_filter"

  resource_type = "AWS::SES::ReceiptFilter"

  props = {
    "Filter": (AWS_SES_ReceiptFilter_Filter, "filter"),
  }

class AWS_SES_ConfigurationSetEventDestination(CloudFormationResource):
  terraform_resource = "aws_ses_configuration_set_event_destination"

  resource_type = "AWS::SES::ConfigurationSetEventDestination"

  props = {
    "ConfigurationSetName": (StringValueConverter(), "configuration_set_name"),
    "EventDestination": (AWS_SES_ConfigurationSetEventDestination_EventDestination, "event_destination"),
  }

class AWS_SES_ReceiptRule(CloudFormationResource):
  terraform_resource = "aws_ses_receipt_rule"

  resource_type = "AWS::SES::ReceiptRule"

  props = {
    "After": (StringValueConverter(), "after"),
    "Rule": (AWS_SES_ReceiptRule_Rule, "rule"),
    "RuleSetName": (StringValueConverter(), "rule_set_name"),
  }

