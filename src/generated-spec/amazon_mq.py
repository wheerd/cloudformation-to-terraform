from . import *

class AWS_AmazonMQ_Broker_EncryptionOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("encryption_options"):
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "UseAwsOwnedKey", "use_aws_owned_key", BasicValueConverter())


class AWS_AmazonMQ_Broker_MaintenanceWindow(CloudFormationProperty):
  def write(self, w):
    with w.block("maintenance_window"):
      self.property(w, "DayOfWeek", "day_of_week", StringValueConverter())
      self.property(w, "TimeOfDay", "time_of_day", StringValueConverter())
      self.property(w, "TimeZone", "time_zone", StringValueConverter())


class AWS_AmazonMQ_Broker_LogList(CloudFormationProperty):
  def write(self, w):
    with w.block("log_list"):
      self.property(w, "Audit", "audit", BasicValueConverter())
      self.property(w, "General", "general", BasicValueConverter())


class AWS_AmazonMQ_Broker_TagsEntry(CloudFormationProperty):
  def write(self, w):
    with w.block("tags_entry"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_AmazonMQ_Broker_User(CloudFormationProperty):
  def write(self, w):
    with w.block("user"):
      self.property(w, "Username", "username", StringValueConverter())
      self.property(w, "Groups", "groups", ListValueConverter(StringValueConverter()))
      self.property(w, "ConsoleAccess", "console_access", BasicValueConverter())
      self.property(w, "Password", "password", StringValueConverter())


class AWS_AmazonMQ_Configuration_TagsEntry(CloudFormationProperty):
  def write(self, w):
    with w.block("tags_entry"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_AmazonMQ_Broker_ConfigurationId(CloudFormationProperty):
  def write(self, w):
    with w.block("configuration_id"):
      self.property(w, "Revision", "revision", BasicValueConverter())
      self.property(w, "Id", "id", StringValueConverter())


class AWS_AmazonMQ_ConfigurationAssociation_ConfigurationId(CloudFormationProperty):
  def write(self, w):
    with w.block("configuration_id"):
      self.property(w, "Revision", "revision", BasicValueConverter())
      self.property(w, "Id", "id", StringValueConverter())


class AWS_AmazonMQ_ConfigurationAssociation(CloudFormationResource):
  cfn_type = "AWS::AmazonMQ::ConfigurationAssociation"
  tf_type = "aws_amazon_mq_configuration_association" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Broker", "broker", StringValueConverter())
      self.block(w, "Configuration", AWS_AmazonMQ_ConfigurationAssociation_ConfigurationId)


class AWS_AmazonMQ_Configuration(CloudFormationResource):
  cfn_type = "AWS::AmazonMQ::Configuration"
  tf_type = "aws_mq_configuration"
  ref = None # TODO: Could not determine the ref automatically
  attrs = {
    "Revision": "latest_revision",
    "Id": "id",
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "EngineVersion", "engine_version", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "EngineType", "engine_type", StringValueConverter())
      self.property(w, "Data", "data", StringValueConverter())
      self.repeated_block(w, "Tags", AWS_AmazonMQ_Configuration_TagsEntry)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_AmazonMQ_Broker(CloudFormationResource):
  cfn_type = "AWS::AmazonMQ::Broker"
  tf_type = "aws_amazon_mq_broker" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "IpAddresses": "ip_addresses",
    "OpenWireEndpoints": "open_wire_endpoints",
    "ConfigurationRevision": "configuration_revision",
    "StompEndpoints": "stomp_endpoints",
    "MqttEndpoints": "mqtt_endpoints",
    "AmqpEndpoints": "amqp_endpoints",
    "Arn": "arn",
    "ConfigurationId": "configuration_id",
    "WssEndpoints": "wss_endpoints",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "SecurityGroups", "security_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "StorageType", "storage_type", StringValueConverter())
      self.property(w, "EngineVersion", "engine_version", StringValueConverter())
      self.block(w, "Configuration", AWS_AmazonMQ_Broker_ConfigurationId)
      self.block(w, "MaintenanceWindowStartTime", AWS_AmazonMQ_Broker_MaintenanceWindow)
      self.property(w, "HostInstanceType", "host_instance_type", StringValueConverter())
      self.property(w, "AutoMinorVersionUpgrade", "auto_minor_version_upgrade", BasicValueConverter())
      self.repeated_block(w, "Users", AWS_AmazonMQ_Broker_User)
      self.block(w, "Logs", AWS_AmazonMQ_Broker_LogList)
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "BrokerName", "broker_name", StringValueConverter())
      self.property(w, "DeploymentMode", "deployment_mode", StringValueConverter())
      self.property(w, "EngineType", "engine_type", StringValueConverter())
      self.property(w, "PubliclyAccessible", "publicly_accessible", BasicValueConverter())
      self.block(w, "EncryptionOptions", AWS_AmazonMQ_Broker_EncryptionOptions)
      self.repeated_block(w, "Tags", AWS_AmazonMQ_Broker_TagsEntry)


