from . import *

class AWS_CodeBuild_Project_ProjectSourceVersion(CloudFormationProperty):
  def write(self, w):
    with w.block("project_source_version"):
      self.property(w, "SourceIdentifier", "source_identifier", StringValueConverter())
      self.property(w, "SourceVersion", "source_version", StringValueConverter())


class AWS_CodeBuild_Project_SourceAuth(CloudFormationProperty):
  def write(self, w):
    with w.block("source_auth"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Resource", "resource", StringValueConverter())


class AWS_CodeBuild_Project_GitSubmodulesConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("git_submodules_config"):
      self.property(w, "FetchSubmodules", "fetch_submodules", BasicValueConverter())


class AWS_CodeBuild_Project_VpcConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("vpc_config"):
      self.property(w, "Subnets", "subnets", ListValueConverter(StringValueConverter()))
      self.property(w, "VpcId", "vpc_id", StringValueConverter())
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))


class AWS_CodeBuild_Project_ProjectFileSystemLocation(CloudFormationProperty):
  def write(self, w):
    with w.block("project_file_system_location"):
      self.property(w, "MountPoint", "mount_point", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Identifier", "identifier", StringValueConverter())
      self.property(w, "MountOptions", "mount_options", StringValueConverter())
      self.property(w, "Location", "location", StringValueConverter())


class AWS_CodeBuild_Project_S3LogsConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_logs_config"):
      self.property(w, "Status", "status", StringValueConverter())
      self.property(w, "EncryptionDisabled", "encryption_disabled", BasicValueConverter())
      self.property(w, "Location", "location", StringValueConverter())


class AWS_CodeBuild_Project_WebhookFilter(CloudFormationProperty):
  def write(self, w):
    with w.block("webhook_filter"):
      self.property(w, "Pattern", "pattern", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "ExcludeMatchedPattern", "exclude_matched_pattern", BasicValueConverter())


class AWS_CodeBuild_Project_Artifacts(CloudFormationProperty):
  def write(self, w):
    with w.block("artifacts"):
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "ArtifactIdentifier", "artifact_identifier", StringValueConverter())
      self.property(w, "OverrideArtifactName", "override_artifact_name", BasicValueConverter())
      self.property(w, "Packaging", "packaging", StringValueConverter())
      self.property(w, "EncryptionDisabled", "encryption_disabled", BasicValueConverter())
      self.property(w, "Location", "location", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "NamespaceType", "namespace_type", StringValueConverter())


class AWS_CodeBuild_Project_RegistryCredential(CloudFormationProperty):
  def write(self, w):
    with w.block("registry_credential"):
      self.property(w, "Credential", "credential", StringValueConverter())
      self.property(w, "CredentialProvider", "credential_provider", StringValueConverter())


class AWS_CodeBuild_ReportGroup_S3ReportExportConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_report_export_config"):
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "Packaging", "packaging", StringValueConverter())
      self.property(w, "EncryptionKey", "encryption_key", StringValueConverter())
      self.property(w, "EncryptionDisabled", "encryption_disabled", BasicValueConverter())


class AWS_CodeBuild_Project_CloudWatchLogsConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("cloud_watch_logs_config"):
      self.property(w, "Status", "status", StringValueConverter())
      self.property(w, "GroupName", "group_name", StringValueConverter())
      self.property(w, "StreamName", "stream_name", StringValueConverter())


class AWS_CodeBuild_Project_ProjectCache(CloudFormationProperty):
  def write(self, w):
    with w.block("project_cache"):
      self.property(w, "Modes", "modes", ListValueConverter(StringValueConverter()))
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Location", "location", StringValueConverter())


class AWS_CodeBuild_Project_FilterGroup(CloudFormationProperty):
  def write(self, w):
    with w.block("filter_group"):
      pass


class AWS_CodeBuild_Project_ProjectTriggers(CloudFormationProperty):
  def write(self, w):
    with w.block("project_triggers"):
      self.repeated_block(w, "FilterGroups", AWS_CodeBuild_Project_FilterGroup)
      self.property(w, "Webhook", "webhook", BasicValueConverter())


class AWS_CodeBuild_Project_EnvironmentVariable(CloudFormationProperty):
  def write(self, w):
    with w.block("environment_variable"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_CodeBuild_Project_Source(CloudFormationProperty):
  def write(self, w):
    with w.block("source"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "ReportBuildStatus", "report_build_status", BasicValueConverter())
      self.block(w, "Auth", AWS_CodeBuild_Project_SourceAuth)
      self.property(w, "SourceIdentifier", "source_identifier", StringValueConverter())
      self.property(w, "BuildSpec", "build_spec", StringValueConverter())
      self.property(w, "GitCloneDepth", "git_clone_depth", BasicValueConverter())
      self.block(w, "GitSubmodulesConfig", AWS_CodeBuild_Project_GitSubmodulesConfig)
      self.property(w, "InsecureSsl", "insecure_ssl", BasicValueConverter())
      self.property(w, "Location", "location", StringValueConverter())


class AWS_CodeBuild_SourceCredential(CloudFormationResource):
  cfn_type = "AWS::CodeBuild::SourceCredential"
  tf_type = "aws_codebuild_source_credential"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ServerType", "server_type", StringValueConverter())
      self.property(w, "Username", "user_name", StringValueConverter())
      self.property(w, "Token", "token", StringValueConverter())
      self.property(w, "AuthType", "auth_type", StringValueConverter())


class AWS_CodeBuild_Project_LogsConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("logs_config"):
      self.block(w, "CloudWatchLogs", AWS_CodeBuild_Project_CloudWatchLogsConfig)
      self.block(w, "S3Logs", AWS_CodeBuild_Project_S3LogsConfig)


class AWS_CodeBuild_Project_Environment(CloudFormationProperty):
  def write(self, w):
    with w.block("environment"):
      self.property(w, "Type", "type", StringValueConverter())
      self.repeated_block(w, "EnvironmentVariables", AWS_CodeBuild_Project_EnvironmentVariable)
      self.property(w, "PrivilegedMode", "privileged_mode", BasicValueConverter())
      self.property(w, "ImagePullCredentialsType", "image_pull_credentials_type", StringValueConverter())
      self.property(w, "Image", "image", StringValueConverter())
      self.block(w, "RegistryCredential", AWS_CodeBuild_Project_RegistryCredential)
      self.property(w, "ComputeType", "compute_type", StringValueConverter())
      self.property(w, "Certificate", "certificate", StringValueConverter())


class AWS_CodeBuild_ReportGroup_ReportExportConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("report_export_config"):
      self.block(w, "S3Destination", AWS_CodeBuild_ReportGroup_S3ReportExportConfig)
      self.property(w, "ExportConfigType", "export_config_type", StringValueConverter())


class AWS_CodeBuild_Project(CloudFormationResource):
  cfn_type = "AWS::CodeBuild::Project"
  tf_type = "aws_codebuild_project"
  ref = "id"
  attrs = {
    "Arn": "arn",
    # Additional TF attributes: badge_url, description, encryption_key
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "VpcConfig", AWS_CodeBuild_Project_VpcConfig)
      self.repeated_block(w, "SecondarySources", AWS_CodeBuild_Project_Source)
      self.property(w, "EncryptionKey", "encryption_key", StringValueConverter())
      self.property(w, "SourceVersion", "source_version", StringValueConverter())
      self.block(w, "Triggers", AWS_CodeBuild_Project_ProjectTriggers) # TODO: Probably not the correct mapping
      self.repeated_block(w, "SecondaryArtifacts", AWS_CodeBuild_Project_Artifacts)
      self.block(w, "Source", AWS_CodeBuild_Project_Source)
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "Artifacts", AWS_CodeBuild_Project_Artifacts)
      self.property(w, "BadgeEnabled", "badge_enabled", BasicValueConverter())
      self.block(w, "LogsConfig", AWS_CodeBuild_Project_LogsConfig)
      self.property(w, "ServiceRole", "service_role", StringValueConverter())
      self.property(w, "QueuedTimeoutInMinutes", "queued_timeout", BasicValueConverter())
      self.repeated_block(w, "FileSystemLocations", AWS_CodeBuild_Project_ProjectFileSystemLocation) # TODO: Probably not the correct mapping
      self.block(w, "Environment", AWS_CodeBuild_Project_Environment)
      self.repeated_block(w, "SecondarySourceVersions", AWS_CodeBuild_Project_ProjectSourceVersion) # TODO: Probably not the correct mapping
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "TimeoutInMinutes", "timeout_in_minutes", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "Cache", AWS_CodeBuild_Project_ProjectCache)


class AWS_CodeBuild_ReportGroup(CloudFormationResource):
  cfn_type = "AWS::CodeBuild::ReportGroup"
  tf_type = "aws_code_build_report_group" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Type", "type", StringValueConverter())
      self.block(w, "ExportConfig", AWS_CodeBuild_ReportGroup_ReportExportConfig)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


