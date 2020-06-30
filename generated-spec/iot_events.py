from . import *

class AWS_IoTEvents_DetectorModel_SetTimer(CloudFormationProperty):
  def write(self, w):
    with w.block("set_timer"):
      self.property(w, "Seconds", "seconds", BasicValueConverter())
      self.property(w, "TimerName", "timer_name", StringValueConverter())
      self.property(w, "DurationExpression", "duration_expression", StringValueConverter())


class AWS_IoTEvents_DetectorModel_ResetTimer(CloudFormationProperty):
  def write(self, w):
    with w.block("reset_timer"):
      self.property(w, "TimerName", "timer_name", StringValueConverter())


class AWS_IoTEvents_DetectorModel_AssetPropertyTimestamp(CloudFormationProperty):
  def write(self, w):
    with w.block("asset_property_timestamp"):
      self.property(w, "TimeInSeconds", "time_in_seconds", StringValueConverter())
      self.property(w, "OffsetInNanos", "offset_in_nanos", StringValueConverter())


class AWS_IoTEvents_DetectorModel_AssetPropertyVariant(CloudFormationProperty):
  def write(self, w):
    with w.block("asset_property_variant"):
      self.property(w, "DoubleValue", "double_value", StringValueConverter())
      self.property(w, "IntegerValue", "integer_value", StringValueConverter())
      self.property(w, "BooleanValue", "boolean_value", StringValueConverter())
      self.property(w, "StringValue", "string_value", StringValueConverter())


class AWS_IoTEvents_DetectorModel_SetVariable(CloudFormationProperty):
  def write(self, w):
    with w.block("set_variable"):
      self.property(w, "VariableName", "variable_name", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_IoTEvents_DetectorModel_Payload(CloudFormationProperty):
  def write(self, w):
    with w.block("payload"):
      self.property(w, "ContentExpression", "content_expression", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_IoTEvents_DetectorModel_ClearTimer(CloudFormationProperty):
  def write(self, w):
    with w.block("clear_timer"):
      self.property(w, "TimerName", "timer_name", StringValueConverter())


class AWS_IoTEvents_DetectorModel_AssetPropertyValue(CloudFormationProperty):
  def write(self, w):
    with w.block("asset_property_value"):
      self.property(w, "Quality", "quality", StringValueConverter())
      self.block(w, "Value", AWS_IoTEvents_DetectorModel_AssetPropertyVariant)
      self.block(w, "Timestamp", AWS_IoTEvents_DetectorModel_AssetPropertyTimestamp)


class AWS_IoTEvents_Input_Attribute(CloudFormationProperty):
  def write(self, w):
    with w.block("attribute"):
      self.property(w, "JsonPath", "json_path", StringValueConverter())


class AWS_IoTEvents_DetectorModel_Sns(CloudFormationProperty):
  def write(self, w):
    with w.block("sns"):
      self.property(w, "TargetArn", "target_arn", StringValueConverter())
      self.block(w, "Payload", AWS_IoTEvents_DetectorModel_Payload)


class AWS_IoTEvents_DetectorModel_Sqs(CloudFormationProperty):
  def write(self, w):
    with w.block("sqs"):
      self.property(w, "UseBase64", "use_base64", BasicValueConverter())
      self.block(w, "Payload", AWS_IoTEvents_DetectorModel_Payload)
      self.property(w, "QueueUrl", "queue_url", StringValueConverter())


class AWS_IoTEvents_DetectorModel_IotTopicPublish(CloudFormationProperty):
  def write(self, w):
    with w.block("iot_topic_publish"):
      self.property(w, "MqttTopic", "mqtt_topic", StringValueConverter())
      self.block(w, "Payload", AWS_IoTEvents_DetectorModel_Payload)


class AWS_IoTEvents_Input_InputDefinition(CloudFormationProperty):
  def write(self, w):
    with w.block("input_definition"):
      self.repeated_block(w, "Attributes", AWS_IoTEvents_Input_Attribute)


class AWS_IoTEvents_DetectorModel_Lambda(CloudFormationProperty):
  def write(self, w):
    with w.block("lambda"):
      self.property(w, "FunctionArn", "function_arn", StringValueConverter())
      self.block(w, "Payload", AWS_IoTEvents_DetectorModel_Payload)


class AWS_IoTEvents_Input(CloudFormationResource):
  cfn_type = "AWS::IoTEvents::Input"
  tf_type = "aws_iot_events_input" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "InputDefinition", AWS_IoTEvents_Input_InputDefinition)
      self.property(w, "InputName", "input_name", StringValueConverter())
      self.property(w, "InputDescription", "input_description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_IoTEvents_DetectorModel_IotEvents(CloudFormationProperty):
  def write(self, w):
    with w.block("iot_events"):
      self.property(w, "InputName", "input_name", StringValueConverter())
      self.block(w, "Payload", AWS_IoTEvents_DetectorModel_Payload)


class AWS_IoTEvents_DetectorModel_DynamoDBv2(CloudFormationProperty):
  def write(self, w):
    with w.block("dynamo_d_bv2"):
      self.property(w, "TableName", "table_name", StringValueConverter())
      self.block(w, "Payload", AWS_IoTEvents_DetectorModel_Payload)


class AWS_IoTEvents_DetectorModel_IotSiteWise(CloudFormationProperty):
  def write(self, w):
    with w.block("iot_site_wise"):
      self.property(w, "EntryId", "entry_id", StringValueConverter())
      self.property(w, "PropertyAlias", "property_alias", StringValueConverter())
      self.block(w, "PropertyValue", AWS_IoTEvents_DetectorModel_AssetPropertyValue)
      self.property(w, "AssetId", "asset_id", StringValueConverter())
      self.property(w, "PropertyId", "property_id", StringValueConverter())


class AWS_IoTEvents_DetectorModel_DynamoDB(CloudFormationProperty):
  def write(self, w):
    with w.block("dynamo_db"):
      self.property(w, "TableName", "table_name", StringValueConverter())
      self.property(w, "PayloadField", "payload_field", StringValueConverter())
      self.property(w, "RangeKeyField", "range_key_field", StringValueConverter())
      self.property(w, "HashKeyField", "hash_key_field", StringValueConverter())
      self.property(w, "RangeKeyValue", "range_key_value", StringValueConverter())
      self.property(w, "RangeKeyType", "range_key_type", StringValueConverter())
      self.property(w, "HashKeyType", "hash_key_type", StringValueConverter())
      self.property(w, "HashKeyValue", "hash_key_value", StringValueConverter())
      self.block(w, "Payload", AWS_IoTEvents_DetectorModel_Payload)
      self.property(w, "Operation", "operation", StringValueConverter())


class AWS_IoTEvents_DetectorModel_Firehose(CloudFormationProperty):
  def write(self, w):
    with w.block("firehose"):
      self.property(w, "DeliveryStreamName", "delivery_stream_name", StringValueConverter())
      self.block(w, "Payload", AWS_IoTEvents_DetectorModel_Payload)
      self.property(w, "Separator", "separator", StringValueConverter())


class AWS_IoTEvents_DetectorModel_Action(CloudFormationProperty):
  def write(self, w):
    with w.block("action"):
      self.block(w, "IotEvents", AWS_IoTEvents_DetectorModel_IotEvents)
      self.block(w, "Firehose", AWS_IoTEvents_DetectorModel_Firehose)
      self.block(w, "IotTopicPublish", AWS_IoTEvents_DetectorModel_IotTopicPublish)
      self.block(w, "DynamoDB", AWS_IoTEvents_DetectorModel_DynamoDB)
      self.block(w, "DynamoDBv2", AWS_IoTEvents_DetectorModel_DynamoDBv2)
      self.block(w, "IotSiteWise", AWS_IoTEvents_DetectorModel_IotSiteWise)
      self.block(w, "ResetTimer", AWS_IoTEvents_DetectorModel_ResetTimer)
      self.block(w, "Sqs", AWS_IoTEvents_DetectorModel_Sqs)
      self.block(w, "Sns", AWS_IoTEvents_DetectorModel_Sns)
      self.block(w, "SetTimer", AWS_IoTEvents_DetectorModel_SetTimer)
      self.block(w, "ClearTimer", AWS_IoTEvents_DetectorModel_ClearTimer)
      self.block(w, "Lambda", AWS_IoTEvents_DetectorModel_Lambda)
      self.block(w, "SetVariable", AWS_IoTEvents_DetectorModel_SetVariable)


class AWS_IoTEvents_DetectorModel_TransitionEvent(CloudFormationProperty):
  def write(self, w):
    with w.block("transition_event"):
      self.property(w, "Condition", "condition", StringValueConverter())
      self.repeated_block(w, "Actions", AWS_IoTEvents_DetectorModel_Action)
      self.property(w, "NextState", "next_state", StringValueConverter())
      self.property(w, "EventName", "event_name", StringValueConverter())


class AWS_IoTEvents_DetectorModel_Event(CloudFormationProperty):
  def write(self, w):
    with w.block("event"):
      self.property(w, "Condition", "condition", StringValueConverter())
      self.repeated_block(w, "Actions", AWS_IoTEvents_DetectorModel_Action)
      self.property(w, "EventName", "event_name", StringValueConverter())


class AWS_IoTEvents_DetectorModel_OnExit(CloudFormationProperty):
  def write(self, w):
    with w.block("on_exit"):
      self.repeated_block(w, "Events", AWS_IoTEvents_DetectorModel_Event)


class AWS_IoTEvents_DetectorModel_OnInput(CloudFormationProperty):
  def write(self, w):
    with w.block("on_input"):
      self.repeated_block(w, "Events", AWS_IoTEvents_DetectorModel_Event)
      self.repeated_block(w, "TransitionEvents", AWS_IoTEvents_DetectorModel_TransitionEvent)


class AWS_IoTEvents_DetectorModel_OnEnter(CloudFormationProperty):
  def write(self, w):
    with w.block("on_enter"):
      self.repeated_block(w, "Events", AWS_IoTEvents_DetectorModel_Event)


class AWS_IoTEvents_DetectorModel_State(CloudFormationProperty):
  def write(self, w):
    with w.block("state"):
      self.block(w, "OnInput", AWS_IoTEvents_DetectorModel_OnInput)
      self.block(w, "OnExit", AWS_IoTEvents_DetectorModel_OnExit)
      self.property(w, "StateName", "state_name", StringValueConverter())
      self.block(w, "OnEnter", AWS_IoTEvents_DetectorModel_OnEnter)


class AWS_IoTEvents_DetectorModel_DetectorModelDefinition(CloudFormationProperty):
  def write(self, w):
    with w.block("detector_model_definition"):
      self.repeated_block(w, "States", AWS_IoTEvents_DetectorModel_State)
      self.property(w, "InitialStateName", "initial_state_name", StringValueConverter())


class AWS_IoTEvents_DetectorModel(CloudFormationResource):
  cfn_type = "AWS::IoTEvents::DetectorModel"
  tf_type = "aws_iot_events_detector_model" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "DetectorModelDefinition", AWS_IoTEvents_DetectorModel_DetectorModelDefinition)
      self.property(w, "EvaluationMethod", "evaluation_method", StringValueConverter())
      self.property(w, "DetectorModelName", "detector_model_name", StringValueConverter())
      self.property(w, "DetectorModelDescription", "detector_model_description", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


