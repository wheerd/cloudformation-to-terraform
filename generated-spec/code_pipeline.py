from . import *

class AWS_CodePipeline_Pipeline_InputArtifact(CloudFormationProperty):
  entity = "AWS::CodePipeline::Pipeline"
  tf_block_type = "input_artifact"

  props = {
    "Name": (StringValueConverter(), "name"),
  }

class AWS_CodePipeline_Pipeline_BlockerDeclaration(CloudFormationProperty):
  entity = "AWS::CodePipeline::Pipeline"
  tf_block_type = "blocker_declaration"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_CodePipeline_CustomActionType_ArtifactDetails(CloudFormationProperty):
  entity = "AWS::CodePipeline::CustomActionType"
  tf_block_type = "artifact_details"

  props = {
    "MaximumCount": (BasicValueConverter(), "maximum_count"),
    "MinimumCount": (BasicValueConverter(), "minimum_count"),
  }

class AWS_CodePipeline_Webhook_WebhookFilterRule(CloudFormationProperty):
  entity = "AWS::CodePipeline::Webhook"
  tf_block_type = "webhook_filter_rule"

  props = {
    "JsonPath": (StringValueConverter(), "json_path"),
    "MatchEquals": (StringValueConverter(), "match_equals"),
  }

class AWS_CodePipeline_Pipeline_OutputArtifact(CloudFormationProperty):
  entity = "AWS::CodePipeline::Pipeline"
  tf_block_type = "output_artifact"

  props = {
    "Name": (StringValueConverter(), "name"),
  }

class AWS_CodePipeline_CustomActionType_ConfigurationProperties(CloudFormationProperty):
  entity = "AWS::CodePipeline::CustomActionType"
  tf_block_type = "configuration_properties"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Key": (BasicValueConverter(), "key"),
    "Name": (StringValueConverter(), "name"),
    "Queryable": (BasicValueConverter(), "queryable"),
    "Required": (BasicValueConverter(), "required"),
    "Secret": (BasicValueConverter(), "secret"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_CodePipeline_Pipeline_EncryptionKey(CloudFormationProperty):
  entity = "AWS::CodePipeline::Pipeline"
  tf_block_type = "encryption_key"

  props = {
    "Id": (StringValueConverter(), "id"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_CodePipeline_CustomActionType_Settings(CloudFormationProperty):
  entity = "AWS::CodePipeline::CustomActionType"
  tf_block_type = "settings"

  props = {
    "EntityUrlTemplate": (StringValueConverter(), "entity_url_template"),
    "ExecutionUrlTemplate": (StringValueConverter(), "execution_url_template"),
    "RevisionUrlTemplate": (StringValueConverter(), "revision_url_template"),
    "ThirdPartyConfigurationUrl": (StringValueConverter(), "third_party_configuration_url"),
  }

class AWS_CodePipeline_Pipeline_StageTransition(CloudFormationProperty):
  entity = "AWS::CodePipeline::Pipeline"
  tf_block_type = "stage_transition"

  props = {
    "Reason": (StringValueConverter(), "reason"),
    "StageName": (StringValueConverter(), "stage_name"),
  }

class AWS_CodePipeline_Pipeline_ArtifactStore(CloudFormationProperty):
  entity = "AWS::CodePipeline::Pipeline"
  tf_block_type = "artifact_store"

  props = {
    "EncryptionKey": (AWS_CodePipeline_Pipeline_EncryptionKey, "encryption_key"),
    "Location": (StringValueConverter(), "location"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_CodePipeline_Pipeline_ActionTypeId(CloudFormationProperty):
  entity = "AWS::CodePipeline::Pipeline"
  tf_block_type = "action_type_id"

  props = {
    "Category": (StringValueConverter(), "category"),
    "Owner": (StringValueConverter(), "owner"),
    "Provider": (StringValueConverter(), "provider"),
    "Version": (StringValueConverter(), "version"),
  }

class AWS_CodePipeline_Webhook_WebhookAuthConfiguration(CloudFormationProperty):
  entity = "AWS::CodePipeline::Webhook"
  tf_block_type = "webhook_auth_configuration"

  props = {
    "AllowedIPRange": (StringValueConverter(), "allowed_ip_range"),
    "SecretToken": (StringValueConverter(), "secret_token"),
  }

class AWS_CodePipeline_CustomActionType(CloudFormationResource):
  terraform_resource = "aws_code_pipeline_custom_action_type"

  resource_type = "AWS::CodePipeline::CustomActionType"

  props = {
    "Category": (StringValueConverter(), "category"),
    "ConfigurationProperties": (BlockValueConverter(AWS_CodePipeline_CustomActionType_ConfigurationProperties), None),
    "InputArtifactDetails": (AWS_CodePipeline_CustomActionType_ArtifactDetails, "input_artifact_details"),
    "OutputArtifactDetails": (AWS_CodePipeline_CustomActionType_ArtifactDetails, "output_artifact_details"),
    "Provider": (StringValueConverter(), "provider"),
    "Settings": (AWS_CodePipeline_CustomActionType_Settings, "settings"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Version": (StringValueConverter(), "version"),
  }

class AWS_CodePipeline_Webhook(CloudFormationResource):
  terraform_resource = "aws_code_pipeline_webhook"

  resource_type = "AWS::CodePipeline::Webhook"

  props = {
    "AuthenticationConfiguration": (AWS_CodePipeline_Webhook_WebhookAuthConfiguration, "authentication_configuration"),
    "Filters": (BlockValueConverter(AWS_CodePipeline_Webhook_WebhookFilterRule), None),
    "Authentication": (StringValueConverter(), "authentication"),
    "TargetPipeline": (StringValueConverter(), "target_pipeline"),
    "TargetAction": (StringValueConverter(), "target_action"),
    "Name": (StringValueConverter(), "name"),
    "TargetPipelineVersion": (BasicValueConverter(), "target_pipeline_version"),
    "RegisterWithThirdParty": (BasicValueConverter(), "register_with_third_party"),
  }

class AWS_CodePipeline_Pipeline_ArtifactStoreMap(CloudFormationProperty):
  entity = "AWS::CodePipeline::Pipeline"
  tf_block_type = "artifact_store_map"

  props = {
    "ArtifactStore": (AWS_CodePipeline_Pipeline_ArtifactStore, "artifact_store"),
    "Region": (StringValueConverter(), "region"),
  }

class AWS_CodePipeline_Pipeline_ActionDeclaration(CloudFormationProperty):
  entity = "AWS::CodePipeline::Pipeline"
  tf_block_type = "action_declaration"

  props = {
    "ActionTypeId": (AWS_CodePipeline_Pipeline_ActionTypeId, "action_type_id"),
    "Configuration": (StringValueConverter(), "configuration"),
    "InputArtifacts": (BlockValueConverter(AWS_CodePipeline_Pipeline_InputArtifact), None),
    "Name": (StringValueConverter(), "name"),
    "Namespace": (StringValueConverter(), "namespace"),
    "OutputArtifacts": (BlockValueConverter(AWS_CodePipeline_Pipeline_OutputArtifact), None),
    "Region": (StringValueConverter(), "region"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "RunOrder": (BasicValueConverter(), "run_order"),
  }

class AWS_CodePipeline_Pipeline_StageDeclaration(CloudFormationProperty):
  entity = "AWS::CodePipeline::Pipeline"
  tf_block_type = "stage_declaration"

  props = {
    "Actions": (BlockValueConverter(AWS_CodePipeline_Pipeline_ActionDeclaration), None),
    "Blockers": (BlockValueConverter(AWS_CodePipeline_Pipeline_BlockerDeclaration), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_CodePipeline_Pipeline(CloudFormationResource):
  terraform_resource = "aws_code_pipeline_pipeline"

  resource_type = "AWS::CodePipeline::Pipeline"

  props = {
    "ArtifactStore": (AWS_CodePipeline_Pipeline_ArtifactStore, "artifact_store"),
    "ArtifactStores": (BlockValueConverter(AWS_CodePipeline_Pipeline_ArtifactStoreMap), None),
    "DisableInboundStageTransitions": (BlockValueConverter(AWS_CodePipeline_Pipeline_StageTransition), None),
    "Name": (StringValueConverter(), "name"),
    "RestartExecutionOnUpdate": (BasicValueConverter(), "restart_execution_on_update"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "Stages": (BlockValueConverter(AWS_CodePipeline_Pipeline_StageDeclaration), None),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

