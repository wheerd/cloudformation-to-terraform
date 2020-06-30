from . import *

class AWS_CodePipeline_Pipeline_InputArtifact(CloudFormationProperty):
  def write(self, w):
    with w.block("input_artifact"):
      self.property(w, "Name", "name", StringValueConverter())


class AWS_CodePipeline_Pipeline_BlockerDeclaration(CloudFormationProperty):
  def write(self, w):
    with w.block("blocker_declaration"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_CodePipeline_CustomActionType_ArtifactDetails(CloudFormationProperty):
  def write(self, w):
    with w.block("artifact_details"):
      self.property(w, "MaximumCount", "maximum_count", BasicValueConverter())
      self.property(w, "MinimumCount", "minimum_count", BasicValueConverter())


class AWS_CodePipeline_Webhook_WebhookFilterRule(CloudFormationProperty):
  def write(self, w):
    with w.block("webhook_filter_rule"):
      self.property(w, "JsonPath", "json_path", StringValueConverter())
      self.property(w, "MatchEquals", "match_equals", StringValueConverter())


class AWS_CodePipeline_Pipeline_OutputArtifact(CloudFormationProperty):
  def write(self, w):
    with w.block("output_artifact"):
      self.property(w, "Name", "name", StringValueConverter())


class AWS_CodePipeline_CustomActionType_ConfigurationProperties(CloudFormationProperty):
  def write(self, w):
    with w.block("configuration_properties"):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Key", "key", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Queryable", "queryable", BasicValueConverter())
      self.property(w, "Required", "required", BasicValueConverter())
      self.property(w, "Secret", "secret", BasicValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_CodePipeline_Pipeline_EncryptionKey(CloudFormationProperty):
  def write(self, w):
    with w.block("encryption_key"):
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_CodePipeline_CustomActionType_Settings(CloudFormationProperty):
  def write(self, w):
    with w.block("settings"):
      self.property(w, "EntityUrlTemplate", "entity_url_template", StringValueConverter())
      self.property(w, "ExecutionUrlTemplate", "execution_url_template", StringValueConverter())
      self.property(w, "RevisionUrlTemplate", "revision_url_template", StringValueConverter())
      self.property(w, "ThirdPartyConfigurationUrl", "third_party_configuration_url", StringValueConverter())


class AWS_CodePipeline_Pipeline_StageTransition(CloudFormationProperty):
  def write(self, w):
    with w.block("stage_transition"):
      self.property(w, "Reason", "reason", StringValueConverter())
      self.property(w, "StageName", "stage_name", StringValueConverter())


class AWS_CodePipeline_Pipeline_ArtifactStore(CloudFormationProperty):
  def write(self, w):
    with w.block("artifact_store"):
      self.block(w, "EncryptionKey", AWS_CodePipeline_Pipeline_EncryptionKey)
      self.property(w, "Location", "location", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_CodePipeline_Pipeline_ActionTypeId(CloudFormationProperty):
  def write(self, w):
    with w.block("action_type_id"):
      self.property(w, "Category", "category", StringValueConverter())
      self.property(w, "Owner", "owner", StringValueConverter())
      self.property(w, "Provider", "provider", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())


class AWS_CodePipeline_Webhook_WebhookAuthConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("webhook_auth_configuration"):
      self.property(w, "AllowedIPRange", "allowed_ip_range", StringValueConverter())
      self.property(w, "SecretToken", "secret_token", StringValueConverter())


class AWS_CodePipeline_CustomActionType(CloudFormationResource):
  cfn_type = "AWS::CodePipeline::CustomActionType"
  tf_type = "aws_codepipeline"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Category", "category", StringValueConverter()) # TODO: Probably not the correct mapping
      self.repeated_block(w, "ConfigurationProperties", AWS_CodePipeline_CustomActionType_ConfigurationProperties) # TODO: Probably not the correct mapping
      self.block(w, "InputArtifactDetails", AWS_CodePipeline_CustomActionType_ArtifactDetails) # TODO: Probably not the correct mapping
      self.block(w, "OutputArtifactDetails", AWS_CodePipeline_CustomActionType_ArtifactDetails) # TODO: Probably not the correct mapping
      self.property(w, "Provider", "id", StringValueConverter())
      self.block(w, "Settings", AWS_CodePipeline_CustomActionType_Settings) # TODO: Probably not the correct mapping
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Version", "version", StringValueConverter()) # TODO: Probably not the correct mapping


class AWS_CodePipeline_Webhook(CloudFormationResource):
  cfn_type = "AWS::CodePipeline::Webhook"
  tf_type = "aws_codepipeline_webhook"
  ref = "id"
  attrs = {
    "Url": "url",
  }

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "AuthenticationConfiguration", AWS_CodePipeline_Webhook_WebhookAuthConfiguration)
      self.repeated_block(w, "Filters", AWS_CodePipeline_Webhook_WebhookFilterRule)
      self.property(w, "Authentication", "authentication", StringValueConverter())
      self.property(w, "TargetPipeline", "target_pipeline", StringValueConverter())
      self.property(w, "TargetAction", "target_action", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "TargetPipelineVersion", "target_pipeline_version", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "RegisterWithThirdParty", "register_with_third_party", BasicValueConverter()) # TODO: Probably not the correct mapping


class AWS_CodePipeline_Pipeline_ArtifactStoreMap(CloudFormationProperty):
  def write(self, w):
    with w.block("artifact_store_map"):
      self.block(w, "ArtifactStore", AWS_CodePipeline_Pipeline_ArtifactStore)
      self.property(w, "Region", "region", StringValueConverter())


class AWS_CodePipeline_Pipeline_ActionDeclaration(CloudFormationProperty):
  def write(self, w):
    with w.block("action_declaration"):
      self.block(w, "ActionTypeId", AWS_CodePipeline_Pipeline_ActionTypeId)
      self.property(w, "Configuration", "configuration", JsonValueConverter())
      self.repeated_block(w, "InputArtifacts", AWS_CodePipeline_Pipeline_InputArtifact)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Namespace", "namespace", StringValueConverter())
      self.repeated_block(w, "OutputArtifacts", AWS_CodePipeline_Pipeline_OutputArtifact)
      self.property(w, "Region", "region", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "RunOrder", "run_order", BasicValueConverter())


class AWS_CodePipeline_Pipeline_StageDeclaration(CloudFormationProperty):
  def write(self, w):
    with w.block("stage_declaration"):
      self.repeated_block(w, "Actions", AWS_CodePipeline_Pipeline_ActionDeclaration)
      self.repeated_block(w, "Blockers", AWS_CodePipeline_Pipeline_BlockerDeclaration)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_CodePipeline_Pipeline(CloudFormationResource):
  cfn_type = "AWS::CodePipeline::Pipeline"
  tf_type = "aws_code_pipeline_pipeline" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "Version": "version",
  }

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "ArtifactStore", AWS_CodePipeline_Pipeline_ArtifactStore)
      self.repeated_block(w, "ArtifactStores", AWS_CodePipeline_Pipeline_ArtifactStoreMap)
      self.repeated_block(w, "DisableInboundStageTransitions", AWS_CodePipeline_Pipeline_StageTransition)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "RestartExecutionOnUpdate", "restart_execution_on_update", BasicValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.repeated_block(w, "Stages", AWS_CodePipeline_Pipeline_StageDeclaration)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


