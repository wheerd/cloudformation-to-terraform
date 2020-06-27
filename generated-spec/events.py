from . import *

class AWS_Events_Rule_RunCommandTarget(CloudFormationProperty):
  entity = "AWS::Events::Rule"
  tf_block_type = "run_command_target"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_Events_Rule_InputTransformer(CloudFormationProperty):
  entity = "AWS::Events::Rule"
  tf_block_type = "input_transformer"

  props = {
    "InputPathsMap": (MapValueConverter(StringValueConverter()), "input_paths_map"),
    "InputTemplate": (StringValueConverter(), "input_template"),
  }

class AWS_Events_Rule_BatchRetryStrategy(CloudFormationProperty):
  entity = "AWS::Events::Rule"
  tf_block_type = "batch_retry_strategy"

  props = {
    "Attempts": (BasicValueConverter(), "attempts"),
  }

class AWS_Events_Rule_SqsParameters(CloudFormationProperty):
  entity = "AWS::Events::Rule"
  tf_block_type = "sqs_parameters"

  props = {
    "MessageGroupId": (StringValueConverter(), "message_group_id"),
  }

class AWS_Events_Rule_HttpParameters(CloudFormationProperty):
  entity = "AWS::Events::Rule"
  tf_block_type = "http_parameters"

  props = {
    "HeaderParameters": (MapValueConverter(StringValueConverter()), "header_parameters"),
    "PathParameterValues": (ListValueConverter(StringValueConverter()), "path_parameter_values"),
    "QueryStringParameters": (MapValueConverter(StringValueConverter()), "query_string_parameters"),
  }

class AWS_Events_EventBusPolicy_Condition(CloudFormationProperty):
  entity = "AWS::Events::EventBusPolicy"
  tf_block_type = "condition"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_Events_Rule_KinesisParameters(CloudFormationProperty):
  entity = "AWS::Events::Rule"
  tf_block_type = "kinesis_parameters"

  props = {
    "PartitionKeyPath": (StringValueConverter(), "partition_key_path"),
  }

class AWS_Events_Rule_BatchArrayProperties(CloudFormationProperty):
  entity = "AWS::Events::Rule"
  tf_block_type = "batch_array_properties"

  props = {
    "Size": (BasicValueConverter(), "size"),
  }

class AWS_Events_Rule_AwsVpcConfiguration(CloudFormationProperty):
  entity = "AWS::Events::Rule"
  tf_block_type = "aws_vpc_configuration"

  props = {
    "AssignPublicIp": (StringValueConverter(), "assign_public_ip"),
    "SecurityGroups": (ListValueConverter(StringValueConverter()), "security_groups"),
    "Subnets": (ListValueConverter(StringValueConverter()), "subnets"),
  }

class AWS_Events_Rule_BatchParameters(CloudFormationProperty):
  entity = "AWS::Events::Rule"
  tf_block_type = "batch_parameters"

  props = {
    "ArrayProperties": (AWS_Events_Rule_BatchArrayProperties, "array_properties"),
    "JobDefinition": (StringValueConverter(), "job_definition"),
    "JobName": (StringValueConverter(), "job_name"),
    "RetryStrategy": (AWS_Events_Rule_BatchRetryStrategy, "retry_strategy"),
  }

class AWS_Events_EventBusPolicy(CloudFormationResource):
  terraform_resource = "aws_events_event_bus_policy"

  resource_type = "AWS::Events::EventBusPolicy"

  props = {
    "EventBusName": (StringValueConverter(), "event_bus_name"),
    "Condition": (AWS_Events_EventBusPolicy_Condition, "condition"),
    "Action": (StringValueConverter(), "action"),
    "StatementId": (StringValueConverter(), "statement_id"),
    "Principal": (StringValueConverter(), "principal"),
  }

class AWS_Events_EventBus(CloudFormationResource):
  terraform_resource = "aws_events_event_bus"

  resource_type = "AWS::Events::EventBus"

  props = {
    "EventSourceName": (StringValueConverter(), "event_source_name"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Events_Rule_RunCommandParameters(CloudFormationProperty):
  entity = "AWS::Events::Rule"
  tf_block_type = "run_command_parameters"

  props = {
    "RunCommandTargets": (BlockValueConverter(AWS_Events_Rule_RunCommandTarget), None),
  }

class AWS_Events_Rule_NetworkConfiguration(CloudFormationProperty):
  entity = "AWS::Events::Rule"
  tf_block_type = "network_configuration"

  props = {
    "AwsVpcConfiguration": (AWS_Events_Rule_AwsVpcConfiguration, "aws_vpc_configuration"),
  }

class AWS_Events_Rule_EcsParameters(CloudFormationProperty):
  entity = "AWS::Events::Rule"
  tf_block_type = "ecs_parameters"

  props = {
    "Group": (StringValueConverter(), "group"),
    "LaunchType": (StringValueConverter(), "launch_type"),
    "NetworkConfiguration": (AWS_Events_Rule_NetworkConfiguration, "network_configuration"),
    "PlatformVersion": (StringValueConverter(), "platform_version"),
    "TaskCount": (BasicValueConverter(), "task_count"),
    "TaskDefinitionArn": (StringValueConverter(), "task_definition_arn"),
  }

class AWS_Events_Rule_Target(CloudFormationProperty):
  entity = "AWS::Events::Rule"
  tf_block_type = "target"

  props = {
    "Arn": (StringValueConverter(), "arn"),
    "BatchParameters": (AWS_Events_Rule_BatchParameters, "batch_parameters"),
    "EcsParameters": (AWS_Events_Rule_EcsParameters, "ecs_parameters"),
    "HttpParameters": (AWS_Events_Rule_HttpParameters, "http_parameters"),
    "Id": (StringValueConverter(), "id"),
    "Input": (StringValueConverter(), "input"),
    "InputPath": (StringValueConverter(), "input_path"),
    "InputTransformer": (AWS_Events_Rule_InputTransformer, "input_transformer"),
    "KinesisParameters": (AWS_Events_Rule_KinesisParameters, "kinesis_parameters"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "RunCommandParameters": (AWS_Events_Rule_RunCommandParameters, "run_command_parameters"),
    "SqsParameters": (AWS_Events_Rule_SqsParameters, "sqs_parameters"),
  }

class AWS_Events_Rule(CloudFormationResource):
  terraform_resource = "aws_events_rule"

  resource_type = "AWS::Events::Rule"

  props = {
    "Description": (StringValueConverter(), "description"),
    "EventBusName": (StringValueConverter(), "event_bus_name"),
    "EventPattern": (StringValueConverter(), "event_pattern"),
    "Name": (StringValueConverter(), "name"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "ScheduleExpression": (StringValueConverter(), "schedule_expression"),
    "State": (StringValueConverter(), "state"),
    "Targets": (BlockValueConverter(AWS_Events_Rule_Target), None),
  }

