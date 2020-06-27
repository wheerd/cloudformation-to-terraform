from . import *

class AWS_GameLift_GameSessionQueue_Destination(CloudFormationProperty):
  entity = "AWS::GameLift::GameSessionQueue"
  tf_block_type = "destination"

  props = {
    "DestinationArn": (StringValueConverter(), "destination_arn"),
  }

class AWS_GameLift_Fleet_IpPermission(CloudFormationProperty):
  entity = "AWS::GameLift::Fleet"
  tf_block_type = "ip_permission"

  props = {
    "FromPort": (BasicValueConverter(), "from_port"),
    "IpRange": (StringValueConverter(), "ip_range"),
    "Protocol": (StringValueConverter(), "protocol"),
    "ToPort": (BasicValueConverter(), "to_port"),
  }

class AWS_GameLift_Fleet_ServerProcess(CloudFormationProperty):
  entity = "AWS::GameLift::Fleet"
  tf_block_type = "server_process"

  props = {
    "ConcurrentExecutions": (BasicValueConverter(), "concurrent_executions"),
    "LaunchPath": (StringValueConverter(), "launch_path"),
    "Parameters": (StringValueConverter(), "parameters"),
  }

class AWS_GameLift_Fleet_ResourceCreationLimitPolicy(CloudFormationProperty):
  entity = "AWS::GameLift::Fleet"
  tf_block_type = "resource_creation_limit_policy"

  props = {
    "NewGameSessionsPerCreator": (BasicValueConverter(), "new_game_sessions_per_creator"),
    "PolicyPeriodInMinutes": (BasicValueConverter(), "policy_period_in_minutes"),
  }

class AWS_GameLift_Build_S3Location(CloudFormationProperty):
  entity = "AWS::GameLift::Build"
  tf_block_type = "s3_location"

  props = {
    "Bucket": (StringValueConverter(), "bucket"),
    "Key": (StringValueConverter(), "key"),
    "ObjectVersion": (StringValueConverter(), "object_version"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_GameLift_Alias_RoutingStrategy(CloudFormationProperty):
  entity = "AWS::GameLift::Alias"
  tf_block_type = "routing_strategy"

  props = {
    "FleetId": (StringValueConverter(), "fleet_id"),
    "Message": (StringValueConverter(), "message"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_GameLift_Fleet_CertificateConfiguration(CloudFormationProperty):
  entity = "AWS::GameLift::Fleet"
  tf_block_type = "certificate_configuration"

  props = {
    "CertificateType": (StringValueConverter(), "certificate_type"),
  }

class AWS_GameLift_Fleet_RuntimeConfiguration(CloudFormationProperty):
  entity = "AWS::GameLift::Fleet"
  tf_block_type = "runtime_configuration"

  props = {
    "GameSessionActivationTimeoutSeconds": (BasicValueConverter(), "game_session_activation_timeout_seconds"),
    "MaxConcurrentGameSessionActivations": (BasicValueConverter(), "max_concurrent_game_session_activations"),
    "ServerProcesses": (BlockValueConverter(AWS_GameLift_Fleet_ServerProcess), None),
  }

class AWS_GameLift_Script_S3Location(CloudFormationProperty):
  entity = "AWS::GameLift::Script"
  tf_block_type = "s3_location"

  props = {
    "ObjectVersion": (StringValueConverter(), "object_version"),
    "Bucket": (StringValueConverter(), "bucket"),
    "Key": (StringValueConverter(), "key"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_GameLift_MatchmakingConfiguration_GameProperty(CloudFormationProperty):
  entity = "AWS::GameLift::MatchmakingConfiguration"
  tf_block_type = "game_property"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_GameLift_GameSessionQueue_PlayerLatencyPolicy(CloudFormationProperty):
  entity = "AWS::GameLift::GameSessionQueue"
  tf_block_type = "player_latency_policy"

  props = {
    "PolicyDurationSeconds": (BasicValueConverter(), "policy_duration_seconds"),
    "MaximumIndividualPlayerLatencyMilliseconds": (BasicValueConverter(), "maximum_individual_player_latency_milliseconds"),
  }

class AWS_GameLift_Fleet(CloudFormationResource):
  terraform_resource = "aws_game_lift_fleet"

  resource_type = "AWS::GameLift::Fleet"

  props = {
    "BuildId": (StringValueConverter(), "build_id"),
    "CertificateConfiguration": (AWS_GameLift_Fleet_CertificateConfiguration, "certificate_configuration"),
    "Description": (StringValueConverter(), "description"),
    "DesiredEC2Instances": (BasicValueConverter(), "desired_ec2_instances"),
    "EC2InboundPermissions": (BlockValueConverter(AWS_GameLift_Fleet_IpPermission), None),
    "EC2InstanceType": (StringValueConverter(), "ec2_instance_type"),
    "FleetType": (StringValueConverter(), "fleet_type"),
    "InstanceRoleARN": (StringValueConverter(), "instance_role_arn"),
    "LogPaths": (ListValueConverter(StringValueConverter()), "log_paths"),
    "MaxSize": (BasicValueConverter(), "max_size"),
    "MetricGroups": (ListValueConverter(StringValueConverter()), "metric_groups"),
    "MinSize": (BasicValueConverter(), "min_size"),
    "Name": (StringValueConverter(), "name"),
    "NewGameSessionProtectionPolicy": (StringValueConverter(), "new_game_session_protection_policy"),
    "PeerVpcAwsAccountId": (StringValueConverter(), "peer_vpc_aws_account_id"),
    "PeerVpcId": (StringValueConverter(), "peer_vpc_id"),
    "ResourceCreationLimitPolicy": (AWS_GameLift_Fleet_ResourceCreationLimitPolicy, "resource_creation_limit_policy"),
    "RuntimeConfiguration": (AWS_GameLift_Fleet_RuntimeConfiguration, "runtime_configuration"),
    "ScriptId": (StringValueConverter(), "script_id"),
    "ServerLaunchParameters": (StringValueConverter(), "server_launch_parameters"),
    "ServerLaunchPath": (StringValueConverter(), "server_launch_path"),
  }

class AWS_GameLift_MatchmakingConfiguration(CloudFormationResource):
  terraform_resource = "aws_game_lift_matchmaking_configuration"

  resource_type = "AWS::GameLift::MatchmakingConfiguration"

  props = {
    "GameProperties": (BlockValueConverter(AWS_GameLift_MatchmakingConfiguration_GameProperty), None),
    "GameSessionData": (StringValueConverter(), "game_session_data"),
    "Description": (StringValueConverter(), "description"),
    "AcceptanceTimeoutSeconds": (BasicValueConverter(), "acceptance_timeout_seconds"),
    "NotificationTarget": (StringValueConverter(), "notification_target"),
    "CustomEventData": (StringValueConverter(), "custom_event_data"),
    "Name": (StringValueConverter(), "name"),
    "AdditionalPlayerCount": (BasicValueConverter(), "additional_player_count"),
    "BackfillMode": (StringValueConverter(), "backfill_mode"),
    "RequestTimeoutSeconds": (BasicValueConverter(), "request_timeout_seconds"),
    "AcceptanceRequired": (BasicValueConverter(), "acceptance_required"),
    "RuleSetName": (StringValueConverter(), "rule_set_name"),
    "GameSessionQueueArns": (ListValueConverter(StringValueConverter()), "game_session_queue_arns"),
  }

class AWS_GameLift_Alias(CloudFormationResource):
  terraform_resource = "aws_game_lift_alias"

  resource_type = "AWS::GameLift::Alias"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Name": (StringValueConverter(), "name"),
    "RoutingStrategy": (AWS_GameLift_Alias_RoutingStrategy, "routing_strategy"),
  }

class AWS_GameLift_Build(CloudFormationResource):
  terraform_resource = "aws_game_lift_build"

  resource_type = "AWS::GameLift::Build"

  props = {
    "Name": (StringValueConverter(), "name"),
    "OperatingSystem": (StringValueConverter(), "operating_system"),
    "StorageLocation": (AWS_GameLift_Build_S3Location, "storage_location"),
    "Version": (StringValueConverter(), "version"),
  }

class AWS_GameLift_MatchmakingRuleSet(CloudFormationResource):
  terraform_resource = "aws_game_lift_matchmaking_rule_set"

  resource_type = "AWS::GameLift::MatchmakingRuleSet"

  props = {
    "RuleSetBody": (StringValueConverter(), "rule_set_body"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_GameLift_GameSessionQueue(CloudFormationResource):
  terraform_resource = "aws_game_lift_game_session_queue"

  resource_type = "AWS::GameLift::GameSessionQueue"

  props = {
    "TimeoutInSeconds": (BasicValueConverter(), "timeout_in_seconds"),
    "PlayerLatencyPolicies": (BlockValueConverter(AWS_GameLift_GameSessionQueue_PlayerLatencyPolicy), None),
    "Destinations": (BlockValueConverter(AWS_GameLift_GameSessionQueue_Destination), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_GameLift_Script(CloudFormationResource):
  terraform_resource = "aws_game_lift_script"

  resource_type = "AWS::GameLift::Script"

  props = {
    "Version": (StringValueConverter(), "version"),
    "StorageLocation": (AWS_GameLift_Script_S3Location, "storage_location"),
    "Name": (StringValueConverter(), "name"),
  }

