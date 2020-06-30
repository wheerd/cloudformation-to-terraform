from . import *

class AWS_Backup_BackupPlan_LifecycleResourceType(CloudFormationProperty):
  def write(self, w):
    with w.block("lifecycle_resource_type"):
      self.property(w, "DeleteAfterDays", "delete_after_days", BasicValueConverter())
      self.property(w, "MoveToColdStorageAfterDays", "move_to_cold_storage_after_days", BasicValueConverter())


class AWS_Backup_BackupSelection_ConditionResourceType(CloudFormationProperty):
  def write(self, w):
    with w.block("condition_resource_type"):
      self.property(w, "ConditionValue", "condition_value", StringValueConverter())
      self.property(w, "ConditionKey", "condition_key", StringValueConverter())
      self.property(w, "ConditionType", "condition_type", StringValueConverter())


class AWS_Backup_BackupVault_NotificationObjectType(CloudFormationProperty):
  def write(self, w):
    with w.block("notification_object_type"):
      self.property(w, "SNSTopicArn", "sns_topic_arn", StringValueConverter())
      self.property(w, "BackupVaultEvents", "backup_vault_events", ListValueConverter(StringValueConverter()))


class AWS_Backup_BackupVault(CloudFormationResource):
  cfn_type = "AWS::Backup::BackupVault"
  tf_type = "aws_backup_backup_vault" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "BackupVaultTags", "backup_vault_tags", JsonValueConverter())
      self.property(w, "BackupVaultName", "backup_vault_name", StringValueConverter())
      self.property(w, "EncryptionKeyArn", "encryption_key_arn", StringValueConverter())
      self.block(w, "Notifications", AWS_Backup_BackupVault_NotificationObjectType)
      self.property(w, "AccessPolicy", "access_policy", JsonValueConverter())


class AWS_Backup_BackupPlan_CopyActionResourceType(CloudFormationProperty):
  def write(self, w):
    with w.block("copy_action_resource_type"):
      self.block(w, "Lifecycle", AWS_Backup_BackupPlan_LifecycleResourceType)
      self.property(w, "DestinationBackupVaultArn", "destination_backup_vault_arn", StringValueConverter())


class AWS_Backup_BackupSelection_BackupSelectionResourceType(CloudFormationProperty):
  def write(self, w):
    with w.block("backup_selection_resource_type"):
      self.repeated_block(w, "ListOfTags", AWS_Backup_BackupSelection_ConditionResourceType)
      self.property(w, "SelectionName", "selection_name", StringValueConverter())
      self.property(w, "IamRoleArn", "iam_role_arn", StringValueConverter())
      self.property(w, "Resources", "resources", ListValueConverter(StringValueConverter()))


class AWS_Backup_BackupPlan_BackupRuleResourceType(CloudFormationProperty):
  def write(self, w):
    with w.block("backup_rule_resource_type"):
      self.property(w, "CompletionWindowMinutes", "completion_window_minutes", BasicValueConverter())
      self.property(w, "ScheduleExpression", "schedule_expression", StringValueConverter())
      self.property(w, "RecoveryPointTags", "recovery_point_tags", JsonValueConverter())
      self.repeated_block(w, "CopyActions", AWS_Backup_BackupPlan_CopyActionResourceType)
      self.block(w, "Lifecycle", AWS_Backup_BackupPlan_LifecycleResourceType)
      self.property(w, "TargetBackupVault", "target_backup_vault", StringValueConverter())
      self.property(w, "StartWindowMinutes", "start_window_minutes", BasicValueConverter())
      self.property(w, "RuleName", "rule_name", StringValueConverter())


class AWS_Backup_BackupPlan_BackupPlanResourceType(CloudFormationProperty):
  def write(self, w):
    with w.block("backup_plan_resource_type"):
      self.property(w, "BackupPlanName", "backup_plan_name", StringValueConverter())
      self.repeated_block(w, "BackupPlanRule", AWS_Backup_BackupPlan_BackupRuleResourceType)


class AWS_Backup_BackupPlan(CloudFormationResource):
  cfn_type = "AWS::Backup::BackupPlan"
  tf_type = "aws_backup_backup_plan" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "BackupPlan", AWS_Backup_BackupPlan_BackupPlanResourceType)
      self.property(w, "BackupPlanTags", "backup_plan_tags", JsonValueConverter())


class AWS_Backup_BackupSelection(CloudFormationResource):
  cfn_type = "AWS::Backup::BackupSelection"
  tf_type = "aws_backup_selection"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "BackupSelection", AWS_Backup_BackupSelection_BackupSelectionResourceType) # TODO: Probably not the correct mapping
      self.property(w, "BackupPlanId", "id", StringValueConverter())


