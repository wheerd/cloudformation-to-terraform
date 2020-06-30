from . import *

class AWS_OpsWorksCM_Server_EngineAttribute(CloudFormationProperty):
  def write(self, w):
    with w.block("engine_attribute"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_OpsWorksCM_Server(CloudFormationResource):
  cfn_type = "AWS::OpsWorksCM::Server"
  tf_type = "aws_ops_works_cm_server" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "KeyPair", "key_pair", StringValueConverter())
      self.property(w, "EngineVersion", "engine_version", StringValueConverter())
      self.property(w, "ServiceRoleArn", "service_role_arn", StringValueConverter())
      self.property(w, "DisableAutomatedBackup", "disable_automated_backup", BasicValueConverter())
      self.property(w, "BackupId", "backup_id", StringValueConverter())
      self.property(w, "EngineModel", "engine_model", StringValueConverter())
      self.property(w, "PreferredMaintenanceWindow", "preferred_maintenance_window", StringValueConverter())
      self.property(w, "AssociatePublicIpAddress", "associate_public_ip_address", BasicValueConverter())
      self.property(w, "InstanceProfileArn", "instance_profile_arn", StringValueConverter())
      self.property(w, "CustomCertificate", "custom_certificate", StringValueConverter())
      self.property(w, "PreferredBackupWindow", "preferred_backup_window", StringValueConverter())
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "CustomDomain", "custom_domain", StringValueConverter())
      self.property(w, "CustomPrivateKey", "custom_private_key", StringValueConverter())
      self.property(w, "ServerName", "server_name", StringValueConverter())
      self.repeated_block(w, "EngineAttributes", AWS_OpsWorksCM_Server_EngineAttribute)
      self.property(w, "BackupRetentionCount", "backup_retention_count", BasicValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Engine", "engine", StringValueConverter())


