from . import *

class AWS_IoT_TopicRule_AssetPropertyVariant(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "asset_property_variant"

  props = {
    "BooleanValue": (StringValueConverter(), "boolean_value"),
    "DoubleValue": (StringValueConverter(), "double_value"),
    "IntegerValue": (StringValueConverter(), "integer_value"),
    "StringValue": (StringValueConverter(), "string_value"),
  }

class AWS_IoT_TopicRule_S3Action(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "s3_action"

  props = {
    "BucketName": (StringValueConverter(), "bucket_name"),
    "Key": (StringValueConverter(), "key"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_IoT_TopicRule_SigV4Authorization(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "sig_v4_authorization"

  props = {
    "RoleArn": (StringValueConverter(), "role_arn"),
    "ServiceName": (StringValueConverter(), "service_name"),
    "SigningRegion": (StringValueConverter(), "signing_region"),
  }

class AWS_IoT_TopicRule_SqsAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "sqs_action"

  props = {
    "QueueUrl": (StringValueConverter(), "queue_url"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "UseBase64": (BasicValueConverter(), "use_base64"),
  }

class AWS_IoT_TopicRule_PutItemInput(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "put_item_input"

  props = {
    "TableName": (StringValueConverter(), "table_name"),
  }

class AWS_IoT_TopicRule_SnsAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "sns_action"

  props = {
    "MessageFormat": (StringValueConverter(), "message_format"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "TargetArn": (StringValueConverter(), "target_arn"),
  }

class AWS_IoT_TopicRule_FirehoseAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "firehose_action"

  props = {
    "DeliveryStreamName": (StringValueConverter(), "delivery_stream_name"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "Separator": (StringValueConverter(), "separator"),
  }

class AWS_IoT_TopicRule_LambdaAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "lambda_action"

  props = {
    "FunctionArn": (StringValueConverter(), "function_arn"),
  }

class AWS_IoT_TopicRule_AssetPropertyTimestamp(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "asset_property_timestamp"

  props = {
    "OffsetInNanos": (StringValueConverter(), "offset_in_nanos"),
    "TimeInSeconds": (StringValueConverter(), "time_in_seconds"),
  }

class AWS_IoT_TopicRule_AssetPropertyValue(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "asset_property_value"

  props = {
    "Quality": (StringValueConverter(), "quality"),
    "Timestamp": (AWS_IoT_TopicRule_AssetPropertyTimestamp, "timestamp"),
    "Value": (AWS_IoT_TopicRule_AssetPropertyVariant, "value"),
  }

class AWS_IoT_TopicRule_ElasticsearchAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "elasticsearch_action"

  props = {
    "Endpoint": (StringValueConverter(), "endpoint"),
    "Id": (StringValueConverter(), "id"),
    "Index": (StringValueConverter(), "index"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_IoT_TopicRule_DynamoDBAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "dynamo_db_action"

  props = {
    "HashKeyField": (StringValueConverter(), "hash_key_field"),
    "HashKeyType": (StringValueConverter(), "hash_key_type"),
    "HashKeyValue": (StringValueConverter(), "hash_key_value"),
    "PayloadField": (StringValueConverter(), "payload_field"),
    "RangeKeyField": (StringValueConverter(), "range_key_field"),
    "RangeKeyType": (StringValueConverter(), "range_key_type"),
    "RangeKeyValue": (StringValueConverter(), "range_key_value"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "TableName": (StringValueConverter(), "table_name"),
  }

class AWS_IoT_TopicRule_KinesisAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "kinesis_action"

  props = {
    "PartitionKey": (StringValueConverter(), "partition_key"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "StreamName": (StringValueConverter(), "stream_name"),
  }

class AWS_IoT_TopicRule_HttpAuthorization(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "http_authorization"

  props = {
    "Sigv4": (AWS_IoT_TopicRule_SigV4Authorization, "sigv4"),
  }

class AWS_IoT_TopicRule_IotAnalyticsAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "iot_analytics_action"

  props = {
    "ChannelName": (StringValueConverter(), "channel_name"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_IoT_TopicRule_IotEventsAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "iot_events_action"

  props = {
    "InputName": (StringValueConverter(), "input_name"),
    "MessageId": (StringValueConverter(), "message_id"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_IoT_TopicRule_HttpActionHeader(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "http_action_header"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_IoT_TopicRule_RepublishAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "republish_action"

  props = {
    "Qos": (BasicValueConverter(), "qos"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "Topic": (StringValueConverter(), "topic"),
  }

class AWS_IoT_TopicRule_StepFunctionsAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "step_functions_action"

  props = {
    "ExecutionNamePrefix": (StringValueConverter(), "execution_name_prefix"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "StateMachineName": (StringValueConverter(), "state_machine_name"),
  }

class AWS_IoT_ProvisioningTemplate_ProvisioningHook(CloudFormationProperty):
  entity = "AWS::IoT::ProvisioningTemplate"
  tf_block_type = "provisioning_hook"

  props = {
    "TargetArn": (StringValueConverter(), "target_arn"),
    "PayloadVersion": (StringValueConverter(), "payload_version"),
  }

class AWS_IoT_TopicRule_DynamoDBv2Action(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "dynamo_d_bv2_action"

  props = {
    "PutItem": (AWS_IoT_TopicRule_PutItemInput, "put_item"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_IoT_TopicRule_CloudwatchAlarmAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "cloudwatch_alarm_action"

  props = {
    "AlarmName": (StringValueConverter(), "alarm_name"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "StateReason": (StringValueConverter(), "state_reason"),
    "StateValue": (StringValueConverter(), "state_value"),
  }

class AWS_IoT_Thing_AttributePayload(CloudFormationProperty):
  entity = "AWS::IoT::Thing"
  tf_block_type = "attribute_payload"

  props = {
    "Attributes": (MapValueConverter(StringValueConverter()), "attributes"),
  }

class AWS_IoT_TopicRule_CloudwatchMetricAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "cloudwatch_metric_action"

  props = {
    "MetricName": (StringValueConverter(), "metric_name"),
    "MetricNamespace": (StringValueConverter(), "metric_namespace"),
    "MetricTimestamp": (StringValueConverter(), "metric_timestamp"),
    "MetricUnit": (StringValueConverter(), "metric_unit"),
    "MetricValue": (StringValueConverter(), "metric_value"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_IoT_ProvisioningTemplate(CloudFormationResource):
  terraform_resource = "aws_io_t_provisioning_template"

  resource_type = "AWS::IoT::ProvisioningTemplate"

  props = {
    "TemplateName": (StringValueConverter(), "template_name"),
    "Description": (StringValueConverter(), "description"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "ProvisioningRoleArn": (StringValueConverter(), "provisioning_role_arn"),
    "TemplateBody": (StringValueConverter(), "template_body"),
    "PreProvisioningHook": (AWS_IoT_ProvisioningTemplate_ProvisioningHook, "pre_provisioning_hook"),
    "Tags": (ListValueConverter("json"), "tags"),
  }

class AWS_IoT_Thing(CloudFormationResource):
  terraform_resource = "aws_io_t_thing"

  resource_type = "AWS::IoT::Thing"

  props = {
    "AttributePayload": (AWS_IoT_Thing_AttributePayload, "attribute_payload"),
    "ThingName": (StringValueConverter(), "thing_name"),
  }

class AWS_IoT_Policy(CloudFormationResource):
  terraform_resource = "aws_io_t_policy"

  resource_type = "AWS::IoT::Policy"

  props = {
    "PolicyDocument": (StringValueConverter(), "policy_document"),
    "PolicyName": (StringValueConverter(), "policy_name"),
  }

class AWS_IoT_PolicyPrincipalAttachment(CloudFormationResource):
  terraform_resource = "aws_io_t_policy_principal_attachment"

  resource_type = "AWS::IoT::PolicyPrincipalAttachment"

  props = {
    "PolicyName": (StringValueConverter(), "policy_name"),
    "Principal": (StringValueConverter(), "principal"),
  }

class AWS_IoT_ThingPrincipalAttachment(CloudFormationResource):
  terraform_resource = "aws_io_t_thing_principal_attachment"

  resource_type = "AWS::IoT::ThingPrincipalAttachment"

  props = {
    "Principal": (StringValueConverter(), "principal"),
    "ThingName": (StringValueConverter(), "thing_name"),
  }

class AWS_IoT_Certificate(CloudFormationResource):
  terraform_resource = "aws_io_t_certificate"

  resource_type = "AWS::IoT::Certificate"

  props = {
    "CertificateSigningRequest": (StringValueConverter(), "certificate_signing_request"),
    "Status": (StringValueConverter(), "status"),
  }

class AWS_IoT_TopicRule_HttpAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "http_action"

  props = {
    "Auth": (AWS_IoT_TopicRule_HttpAuthorization, "auth"),
    "ConfirmationUrl": (StringValueConverter(), "confirmation_url"),
    "Headers": (BlockValueConverter(AWS_IoT_TopicRule_HttpActionHeader), None),
    "Url": (StringValueConverter(), "url"),
  }

class AWS_IoT_TopicRule_PutAssetPropertyValueEntry(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "put_asset_property_value_entry"

  props = {
    "AssetId": (StringValueConverter(), "asset_id"),
    "EntryId": (StringValueConverter(), "entry_id"),
    "PropertyAlias": (StringValueConverter(), "property_alias"),
    "PropertyId": (StringValueConverter(), "property_id"),
    "PropertyValues": (BlockValueConverter(AWS_IoT_TopicRule_AssetPropertyValue), None),
  }

class AWS_IoT_TopicRule_IotSiteWiseAction(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "iot_site_wise_action"

  props = {
    "PutAssetPropertyValueEntries": (BlockValueConverter(AWS_IoT_TopicRule_PutAssetPropertyValueEntry), None),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_IoT_TopicRule_Action(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "action"

  props = {
    "CloudwatchAlarm": (AWS_IoT_TopicRule_CloudwatchAlarmAction, "cloudwatch_alarm"),
    "CloudwatchMetric": (AWS_IoT_TopicRule_CloudwatchMetricAction, "cloudwatch_metric"),
    "DynamoDB": (AWS_IoT_TopicRule_DynamoDBAction, "dynamo_db"),
    "DynamoDBv2": (AWS_IoT_TopicRule_DynamoDBv2Action, "dynamo_d_bv2"),
    "Elasticsearch": (AWS_IoT_TopicRule_ElasticsearchAction, "elasticsearch"),
    "Firehose": (AWS_IoT_TopicRule_FirehoseAction, "firehose"),
    "Http": (AWS_IoT_TopicRule_HttpAction, "http"),
    "IotAnalytics": (AWS_IoT_TopicRule_IotAnalyticsAction, "iot_analytics"),
    "IotEvents": (AWS_IoT_TopicRule_IotEventsAction, "iot_events"),
    "IotSiteWise": (AWS_IoT_TopicRule_IotSiteWiseAction, "iot_site_wise"),
    "Kinesis": (AWS_IoT_TopicRule_KinesisAction, "kinesis"),
    "Lambda": (AWS_IoT_TopicRule_LambdaAction, "lambda"),
    "Republish": (AWS_IoT_TopicRule_RepublishAction, "republish"),
    "S3": (AWS_IoT_TopicRule_S3Action, "s3"),
    "Sns": (AWS_IoT_TopicRule_SnsAction, "sns"),
    "Sqs": (AWS_IoT_TopicRule_SqsAction, "sqs"),
    "StepFunctions": (AWS_IoT_TopicRule_StepFunctionsAction, "step_functions"),
  }

class AWS_IoT_TopicRule_TopicRulePayload(CloudFormationProperty):
  entity = "AWS::IoT::TopicRule"
  tf_block_type = "topic_rule_payload"

  props = {
    "Actions": (BlockValueConverter(AWS_IoT_TopicRule_Action), None),
    "AwsIotSqlVersion": (StringValueConverter(), "aws_iot_sql_version"),
    "Description": (StringValueConverter(), "description"),
    "ErrorAction": (AWS_IoT_TopicRule_Action, "error_action"),
    "RuleDisabled": (BasicValueConverter(), "rule_disabled"),
    "Sql": (StringValueConverter(), "sql"),
  }

class AWS_IoT_TopicRule(CloudFormationResource):
  terraform_resource = "aws_io_t_topic_rule"

  resource_type = "AWS::IoT::TopicRule"

  props = {
    "RuleName": (StringValueConverter(), "rule_name"),
    "TopicRulePayload": (AWS_IoT_TopicRule_TopicRulePayload, "topic_rule_payload"),
  }

