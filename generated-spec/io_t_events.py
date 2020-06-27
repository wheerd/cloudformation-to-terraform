from . import *

class AWS_IoTEvents_DetectorModel_SetTimer(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "set_timer"

  props = {
    "Seconds": (BasicValueConverter(), "seconds"),
    "TimerName": (StringValueConverter(), "timer_name"),
    "DurationExpression": (StringValueConverter(), "duration_expression"),
  }

class AWS_IoTEvents_DetectorModel_ResetTimer(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "reset_timer"

  props = {
    "TimerName": (StringValueConverter(), "timer_name"),
  }

class AWS_IoTEvents_DetectorModel_AssetPropertyTimestamp(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "asset_property_timestamp"

  props = {
    "TimeInSeconds": (StringValueConverter(), "time_in_seconds"),
    "OffsetInNanos": (StringValueConverter(), "offset_in_nanos"),
  }

class AWS_IoTEvents_DetectorModel_AssetPropertyVariant(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "asset_property_variant"

  props = {
    "DoubleValue": (StringValueConverter(), "double_value"),
    "IntegerValue": (StringValueConverter(), "integer_value"),
    "BooleanValue": (StringValueConverter(), "boolean_value"),
    "StringValue": (StringValueConverter(), "string_value"),
  }

class AWS_IoTEvents_DetectorModel_SetVariable(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "set_variable"

  props = {
    "VariableName": (StringValueConverter(), "variable_name"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_IoTEvents_DetectorModel_Payload(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "payload"

  props = {
    "ContentExpression": (StringValueConverter(), "content_expression"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_IoTEvents_DetectorModel_ClearTimer(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "clear_timer"

  props = {
    "TimerName": (StringValueConverter(), "timer_name"),
  }

class AWS_IoTEvents_DetectorModel_AssetPropertyValue(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "asset_property_value"

  props = {
    "Quality": (StringValueConverter(), "quality"),
    "Value": (AWS_IoTEvents_DetectorModel_AssetPropertyVariant, "value"),
    "Timestamp": (AWS_IoTEvents_DetectorModel_AssetPropertyTimestamp, "timestamp"),
  }

class AWS_IoTEvents_Input_Attribute(CloudFormationProperty):
  entity = "AWS::IoTEvents::Input"
  tf_block_type = "attribute"

  props = {
    "JsonPath": (StringValueConverter(), "json_path"),
  }

class AWS_IoTEvents_DetectorModel_Sns(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "sns"

  props = {
    "TargetArn": (StringValueConverter(), "target_arn"),
    "Payload": (AWS_IoTEvents_DetectorModel_Payload, "payload"),
  }

class AWS_IoTEvents_DetectorModel_Sqs(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "sqs"

  props = {
    "UseBase64": (BasicValueConverter(), "use_base64"),
    "Payload": (AWS_IoTEvents_DetectorModel_Payload, "payload"),
    "QueueUrl": (StringValueConverter(), "queue_url"),
  }

class AWS_IoTEvents_DetectorModel_IotTopicPublish(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "iot_topic_publish"

  props = {
    "MqttTopic": (StringValueConverter(), "mqtt_topic"),
    "Payload": (AWS_IoTEvents_DetectorModel_Payload, "payload"),
  }

class AWS_IoTEvents_Input_InputDefinition(CloudFormationProperty):
  entity = "AWS::IoTEvents::Input"
  tf_block_type = "input_definition"

  props = {
    "Attributes": (BlockValueConverter(AWS_IoTEvents_Input_Attribute), None),
  }

class AWS_IoTEvents_DetectorModel_Lambda(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "lambda"

  props = {
    "FunctionArn": (StringValueConverter(), "function_arn"),
    "Payload": (AWS_IoTEvents_DetectorModel_Payload, "payload"),
  }

class AWS_IoTEvents_Input(CloudFormationResource):
  terraform_resource = "aws_io_t_events_input"

  resource_type = "AWS::IoTEvents::Input"

  props = {
    "InputDefinition": (AWS_IoTEvents_Input_InputDefinition, "input_definition"),
    "InputName": (StringValueConverter(), "input_name"),
    "InputDescription": (StringValueConverter(), "input_description"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_IoTEvents_DetectorModel_IotEvents(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "iot_events"

  props = {
    "InputName": (StringValueConverter(), "input_name"),
    "Payload": (AWS_IoTEvents_DetectorModel_Payload, "payload"),
  }

class AWS_IoTEvents_DetectorModel_DynamoDBv2(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "dynamo_d_bv2"

  props = {
    "TableName": (StringValueConverter(), "table_name"),
    "Payload": (AWS_IoTEvents_DetectorModel_Payload, "payload"),
  }

class AWS_IoTEvents_DetectorModel_IotSiteWise(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "iot_site_wise"

  props = {
    "EntryId": (StringValueConverter(), "entry_id"),
    "PropertyAlias": (StringValueConverter(), "property_alias"),
    "PropertyValue": (AWS_IoTEvents_DetectorModel_AssetPropertyValue, "property_value"),
    "AssetId": (StringValueConverter(), "asset_id"),
    "PropertyId": (StringValueConverter(), "property_id"),
  }

class AWS_IoTEvents_DetectorModel_DynamoDB(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "dynamo_db"

  props = {
    "TableName": (StringValueConverter(), "table_name"),
    "PayloadField": (StringValueConverter(), "payload_field"),
    "RangeKeyField": (StringValueConverter(), "range_key_field"),
    "HashKeyField": (StringValueConverter(), "hash_key_field"),
    "RangeKeyValue": (StringValueConverter(), "range_key_value"),
    "RangeKeyType": (StringValueConverter(), "range_key_type"),
    "HashKeyType": (StringValueConverter(), "hash_key_type"),
    "HashKeyValue": (StringValueConverter(), "hash_key_value"),
    "Payload": (AWS_IoTEvents_DetectorModel_Payload, "payload"),
    "Operation": (StringValueConverter(), "operation"),
  }

class AWS_IoTEvents_DetectorModel_Firehose(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "firehose"

  props = {
    "DeliveryStreamName": (StringValueConverter(), "delivery_stream_name"),
    "Payload": (AWS_IoTEvents_DetectorModel_Payload, "payload"),
    "Separator": (StringValueConverter(), "separator"),
  }

class AWS_IoTEvents_DetectorModel_Action(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "action"

  props = {
    "IotEvents": (AWS_IoTEvents_DetectorModel_IotEvents, "iot_events"),
    "Firehose": (AWS_IoTEvents_DetectorModel_Firehose, "firehose"),
    "IotTopicPublish": (AWS_IoTEvents_DetectorModel_IotTopicPublish, "iot_topic_publish"),
    "DynamoDB": (AWS_IoTEvents_DetectorModel_DynamoDB, "dynamo_db"),
    "DynamoDBv2": (AWS_IoTEvents_DetectorModel_DynamoDBv2, "dynamo_d_bv2"),
    "IotSiteWise": (AWS_IoTEvents_DetectorModel_IotSiteWise, "iot_site_wise"),
    "ResetTimer": (AWS_IoTEvents_DetectorModel_ResetTimer, "reset_timer"),
    "Sqs": (AWS_IoTEvents_DetectorModel_Sqs, "sqs"),
    "Sns": (AWS_IoTEvents_DetectorModel_Sns, "sns"),
    "SetTimer": (AWS_IoTEvents_DetectorModel_SetTimer, "set_timer"),
    "ClearTimer": (AWS_IoTEvents_DetectorModel_ClearTimer, "clear_timer"),
    "Lambda": (AWS_IoTEvents_DetectorModel_Lambda, "lambda"),
    "SetVariable": (AWS_IoTEvents_DetectorModel_SetVariable, "set_variable"),
  }

class AWS_IoTEvents_DetectorModel_TransitionEvent(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "transition_event"

  props = {
    "Condition": (StringValueConverter(), "condition"),
    "Actions": (BlockValueConverter(AWS_IoTEvents_DetectorModel_Action), None),
    "NextState": (StringValueConverter(), "next_state"),
    "EventName": (StringValueConverter(), "event_name"),
  }

class AWS_IoTEvents_DetectorModel_Event(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "event"

  props = {
    "Condition": (StringValueConverter(), "condition"),
    "Actions": (BlockValueConverter(AWS_IoTEvents_DetectorModel_Action), None),
    "EventName": (StringValueConverter(), "event_name"),
  }

class AWS_IoTEvents_DetectorModel_OnExit(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "on_exit"

  props = {
    "Events": (BlockValueConverter(AWS_IoTEvents_DetectorModel_Event), None),
  }

class AWS_IoTEvents_DetectorModel_OnInput(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "on_input"

  props = {
    "Events": (BlockValueConverter(AWS_IoTEvents_DetectorModel_Event), None),
    "TransitionEvents": (BlockValueConverter(AWS_IoTEvents_DetectorModel_TransitionEvent), None),
  }

class AWS_IoTEvents_DetectorModel_OnEnter(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "on_enter"

  props = {
    "Events": (BlockValueConverter(AWS_IoTEvents_DetectorModel_Event), None),
  }

class AWS_IoTEvents_DetectorModel_State(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "state"

  props = {
    "OnInput": (AWS_IoTEvents_DetectorModel_OnInput, "on_input"),
    "OnExit": (AWS_IoTEvents_DetectorModel_OnExit, "on_exit"),
    "StateName": (StringValueConverter(), "state_name"),
    "OnEnter": (AWS_IoTEvents_DetectorModel_OnEnter, "on_enter"),
  }

class AWS_IoTEvents_DetectorModel_DetectorModelDefinition(CloudFormationProperty):
  entity = "AWS::IoTEvents::DetectorModel"
  tf_block_type = "detector_model_definition"

  props = {
    "States": (BlockValueConverter(AWS_IoTEvents_DetectorModel_State), None),
    "InitialStateName": (StringValueConverter(), "initial_state_name"),
  }

class AWS_IoTEvents_DetectorModel(CloudFormationResource):
  terraform_resource = "aws_io_t_events_detector_model"

  resource_type = "AWS::IoTEvents::DetectorModel"

  props = {
    "DetectorModelDefinition": (AWS_IoTEvents_DetectorModel_DetectorModelDefinition, "detector_model_definition"),
    "EvaluationMethod": (StringValueConverter(), "evaluation_method"),
    "DetectorModelName": (StringValueConverter(), "detector_model_name"),
    "DetectorModelDescription": (StringValueConverter(), "detector_model_description"),
    "Key": (StringValueConverter(), "key"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

