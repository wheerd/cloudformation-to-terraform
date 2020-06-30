from . import *

class AWS_IoT_TopicRule_AssetPropertyVariant(CloudFormationProperty):
  def write(self, w):
    with w.block("asset_property_variant"):
      self.property(w, "BooleanValue", "boolean_value", StringValueConverter())
      self.property(w, "DoubleValue", "double_value", StringValueConverter())
      self.property(w, "IntegerValue", "integer_value", StringValueConverter())
      self.property(w, "StringValue", "string_value", StringValueConverter())


class AWS_IoT_TopicRule_S3Action(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_action"):
      self.property(w, "BucketName", "bucket_name", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_IoT_TopicRule_SigV4Authorization(CloudFormationProperty):
  def write(self, w):
    with w.block("sig_v4_authorization"):
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "ServiceName", "service_name", StringValueConverter())
      self.property(w, "SigningRegion", "signing_region", StringValueConverter())


class AWS_IoT_TopicRule_SqsAction(CloudFormationProperty):
  def write(self, w):
    with w.block("sqs_action"):
      self.property(w, "QueueUrl", "queue_url", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "UseBase64", "use_base64", BasicValueConverter())


class AWS_IoT_TopicRule_PutItemInput(CloudFormationProperty):
  def write(self, w):
    with w.block("put_item_input"):
      self.property(w, "TableName", "table_name", StringValueConverter())


class AWS_IoT_TopicRule_SnsAction(CloudFormationProperty):
  def write(self, w):
    with w.block("sns_action"):
      self.property(w, "MessageFormat", "message_format", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "TargetArn", "target_arn", StringValueConverter())


class AWS_IoT_TopicRule_FirehoseAction(CloudFormationProperty):
  def write(self, w):
    with w.block("firehose_action"):
      self.property(w, "DeliveryStreamName", "delivery_stream_name", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "Separator", "separator", StringValueConverter())


class AWS_IoT_TopicRule_LambdaAction(CloudFormationProperty):
  def write(self, w):
    with w.block("lambda_action"):
      self.property(w, "FunctionArn", "function_arn", StringValueConverter())


class AWS_IoT_TopicRule_AssetPropertyTimestamp(CloudFormationProperty):
  def write(self, w):
    with w.block("asset_property_timestamp"):
      self.property(w, "OffsetInNanos", "offset_in_nanos", StringValueConverter())
      self.property(w, "TimeInSeconds", "time_in_seconds", StringValueConverter())


class AWS_IoT_TopicRule_AssetPropertyValue(CloudFormationProperty):
  def write(self, w):
    with w.block("asset_property_value"):
      self.property(w, "Quality", "quality", StringValueConverter())
      self.block(w, "Timestamp", AWS_IoT_TopicRule_AssetPropertyTimestamp)
      self.block(w, "Value", AWS_IoT_TopicRule_AssetPropertyVariant)


class AWS_IoT_TopicRule_ElasticsearchAction(CloudFormationProperty):
  def write(self, w):
    with w.block("elasticsearch_action"):
      self.property(w, "Endpoint", "endpoint", StringValueConverter())
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Index", "index", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_IoT_TopicRule_DynamoDBAction(CloudFormationProperty):
  def write(self, w):
    with w.block("dynamo_db_action"):
      self.property(w, "HashKeyField", "hash_key_field", StringValueConverter())
      self.property(w, "HashKeyType", "hash_key_type", StringValueConverter())
      self.property(w, "HashKeyValue", "hash_key_value", StringValueConverter())
      self.property(w, "PayloadField", "payload_field", StringValueConverter())
      self.property(w, "RangeKeyField", "range_key_field", StringValueConverter())
      self.property(w, "RangeKeyType", "range_key_type", StringValueConverter())
      self.property(w, "RangeKeyValue", "range_key_value", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "TableName", "table_name", StringValueConverter())


class AWS_IoT_TopicRule_KinesisAction(CloudFormationProperty):
  def write(self, w):
    with w.block("kinesis_action"):
      self.property(w, "PartitionKey", "partition_key", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "StreamName", "stream_name", StringValueConverter())


class AWS_IoT_TopicRule_HttpAuthorization(CloudFormationProperty):
  def write(self, w):
    with w.block("http_authorization"):
      self.block(w, "Sigv4", AWS_IoT_TopicRule_SigV4Authorization)


class AWS_IoT_TopicRule_IotAnalyticsAction(CloudFormationProperty):
  def write(self, w):
    with w.block("iot_analytics_action"):
      self.property(w, "ChannelName", "channel_name", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_IoT_TopicRule_IotEventsAction(CloudFormationProperty):
  def write(self, w):
    with w.block("iot_events_action"):
      self.property(w, "InputName", "input_name", StringValueConverter())
      self.property(w, "MessageId", "message_id", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_IoT_TopicRule_HttpActionHeader(CloudFormationProperty):
  def write(self, w):
    with w.block("http_action_header"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_IoT_TopicRule_RepublishAction(CloudFormationProperty):
  def write(self, w):
    with w.block("republish_action"):
      self.property(w, "Qos", "qos", BasicValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "Topic", "topic", StringValueConverter())


class AWS_IoT_TopicRule_StepFunctionsAction(CloudFormationProperty):
  def write(self, w):
    with w.block("step_functions_action"):
      self.property(w, "ExecutionNamePrefix", "execution_name_prefix", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "StateMachineName", "state_machine_name", StringValueConverter())


class AWS_IoT_ProvisioningTemplate_ProvisioningHook(CloudFormationProperty):
  def write(self, w):
    with w.block("provisioning_hook"):
      self.property(w, "TargetArn", "target_arn", StringValueConverter())
      self.property(w, "PayloadVersion", "payload_version", StringValueConverter())


class AWS_IoT_TopicRule_DynamoDBv2Action(CloudFormationProperty):
  def write(self, w):
    with w.block("dynamo_d_bv2_action"):
      self.block(w, "PutItem", AWS_IoT_TopicRule_PutItemInput)
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_IoT_TopicRule_CloudwatchAlarmAction(CloudFormationProperty):
  def write(self, w):
    with w.block("cloudwatch_alarm_action"):
      self.property(w, "AlarmName", "alarm_name", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "StateReason", "state_reason", StringValueConverter())
      self.property(w, "StateValue", "state_value", StringValueConverter())


class AWS_IoT_Thing_AttributePayload(CloudFormationProperty):
  def write(self, w):
    with w.block("attribute_payload"):
      self.property(w, "Attributes", "attributes", MapValueConverter(StringValueConverter()))


class AWS_IoT_TopicRule_CloudwatchMetricAction(CloudFormationProperty):
  def write(self, w):
    with w.block("cloudwatch_metric_action"):
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.property(w, "MetricNamespace", "metric_namespace", StringValueConverter())
      self.property(w, "MetricTimestamp", "metric_timestamp", StringValueConverter())
      self.property(w, "MetricUnit", "metric_unit", StringValueConverter())
      self.property(w, "MetricValue", "metric_value", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_IoT_ProvisioningTemplate(CloudFormationResource):
  cfn_type = "AWS::IoT::ProvisioningTemplate"
  tf_type = "aws_iot_provisioning_template" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "TemplateName", "template_name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "ProvisioningRoleArn", "provisioning_role_arn", StringValueConverter())
      self.property(w, "TemplateBody", "template_body", StringValueConverter())
      self.block(w, "PreProvisioningHook", AWS_IoT_ProvisioningTemplate_ProvisioningHook)
      self.property(w, "Tags", "tags", ListValueConverter("json"))


class AWS_IoT_Thing(CloudFormationResource):
  cfn_type = "AWS::IoT::Thing"
  tf_type = "aws_iot_thing"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "AttributePayload", AWS_IoT_Thing_AttributePayload) # TODO: Probably not the correct mapping
      self.property(w, "ThingName", "name", StringValueConverter())


class AWS_IoT_Policy(CloudFormationResource):
  cfn_type = "AWS::IoT::Policy"
  tf_type = "aws_iot_policy_attachment"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PolicyDocument", "policy", JsonValueConverter())
      self.property(w, "PolicyName", "policy_name", StringValueConverter()) # TODO: Probably not the correct mapping


class AWS_IoT_PolicyPrincipalAttachment(CloudFormationResource):
  cfn_type = "AWS::IoT::PolicyPrincipalAttachment"
  tf_type = "aws_iot_policy"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PolicyName", "name", StringValueConverter())
      self.property(w, "Principal", "principal", StringValueConverter()) # TODO: Probably not the correct mapping


class AWS_IoT_ThingPrincipalAttachment(CloudFormationResource):
  cfn_type = "AWS::IoT::ThingPrincipalAttachment"
  tf_type = "aws_iot_thing_principal_attachment"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Principal", "principal", StringValueConverter())
      self.property(w, "ThingName", "thing", StringValueConverter())


class AWS_IoT_Certificate(CloudFormationResource):
  cfn_type = "AWS::IoT::Certificate"
  tf_type = "aws_iot_certificate"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CertificateSigningRequest", "certificate_signing_request", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Status", "status", StringValueConverter()) # TODO: Probably not the correct mapping


class AWS_IoT_TopicRule_HttpAction(CloudFormationProperty):
  def write(self, w):
    with w.block("http_action"):
      self.block(w, "Auth", AWS_IoT_TopicRule_HttpAuthorization)
      self.property(w, "ConfirmationUrl", "confirmation_url", StringValueConverter())
      self.repeated_block(w, "Headers", AWS_IoT_TopicRule_HttpActionHeader)
      self.property(w, "Url", "url", StringValueConverter())


class AWS_IoT_TopicRule_PutAssetPropertyValueEntry(CloudFormationProperty):
  def write(self, w):
    with w.block("put_asset_property_value_entry"):
      self.property(w, "AssetId", "asset_id", StringValueConverter())
      self.property(w, "EntryId", "entry_id", StringValueConverter())
      self.property(w, "PropertyAlias", "property_alias", StringValueConverter())
      self.property(w, "PropertyId", "property_id", StringValueConverter())
      self.repeated_block(w, "PropertyValues", AWS_IoT_TopicRule_AssetPropertyValue)


class AWS_IoT_TopicRule_IotSiteWiseAction(CloudFormationProperty):
  def write(self, w):
    with w.block("iot_site_wise_action"):
      self.repeated_block(w, "PutAssetPropertyValueEntries", AWS_IoT_TopicRule_PutAssetPropertyValueEntry)
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_IoT_TopicRule_Action(CloudFormationProperty):
  def write(self, w):
    with w.block("action"):
      self.block(w, "CloudwatchAlarm", AWS_IoT_TopicRule_CloudwatchAlarmAction)
      self.block(w, "CloudwatchMetric", AWS_IoT_TopicRule_CloudwatchMetricAction)
      self.block(w, "DynamoDB", AWS_IoT_TopicRule_DynamoDBAction)
      self.block(w, "DynamoDBv2", AWS_IoT_TopicRule_DynamoDBv2Action)
      self.block(w, "Elasticsearch", AWS_IoT_TopicRule_ElasticsearchAction)
      self.block(w, "Firehose", AWS_IoT_TopicRule_FirehoseAction)
      self.block(w, "Http", AWS_IoT_TopicRule_HttpAction)
      self.block(w, "IotAnalytics", AWS_IoT_TopicRule_IotAnalyticsAction)
      self.block(w, "IotEvents", AWS_IoT_TopicRule_IotEventsAction)
      self.block(w, "IotSiteWise", AWS_IoT_TopicRule_IotSiteWiseAction)
      self.block(w, "Kinesis", AWS_IoT_TopicRule_KinesisAction)
      self.block(w, "Lambda", AWS_IoT_TopicRule_LambdaAction)
      self.block(w, "Republish", AWS_IoT_TopicRule_RepublishAction)
      self.block(w, "S3", AWS_IoT_TopicRule_S3Action)
      self.block(w, "Sns", AWS_IoT_TopicRule_SnsAction)
      self.block(w, "Sqs", AWS_IoT_TopicRule_SqsAction)
      self.block(w, "StepFunctions", AWS_IoT_TopicRule_StepFunctionsAction)


class AWS_IoT_TopicRule_TopicRulePayload(CloudFormationProperty):
  def write(self, w):
    with w.block("topic_rule_payload"):
      self.repeated_block(w, "Actions", AWS_IoT_TopicRule_Action)
      self.property(w, "AwsIotSqlVersion", "aws_iot_sql_version", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "ErrorAction", AWS_IoT_TopicRule_Action)
      self.property(w, "RuleDisabled", "rule_disabled", BasicValueConverter())
      self.property(w, "Sql", "sql", StringValueConverter())


class AWS_IoT_TopicRule(CloudFormationResource):
  cfn_type = "AWS::IoT::TopicRule"
  tf_type = "aws_iot_topic_rule"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "RuleName", "name", StringValueConverter())
      self.block(w, "TopicRulePayload", AWS_IoT_TopicRule_TopicRulePayload) # TODO: Probably not the correct mapping


