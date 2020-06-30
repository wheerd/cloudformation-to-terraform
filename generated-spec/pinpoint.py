from . import *

class AWS_Pinpoint_Campaign_MetricDimension(CloudFormationProperty):
  def write(self, w):
    with w.block("metric_dimension"):
      self.property(w, "ComparisonOperator", "comparison_operator", StringValueConverter())
      self.property(w, "Value", "value", BasicValueConverter())


class AWS_Pinpoint_Segment_Coordinates(CloudFormationProperty):
  def write(self, w):
    with w.block("coordinates"):
      self.property(w, "Latitude", "latitude", BasicValueConverter())
      self.property(w, "Longitude", "longitude", BasicValueConverter())


class AWS_Pinpoint_Campaign_SetDimension(CloudFormationProperty):
  def write(self, w):
    with w.block("set_dimension"):
      self.property(w, "DimensionType", "dimension_type", StringValueConverter())
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_Pinpoint_PushTemplate_AndroidPushNotificationTemplate(CloudFormationProperty):
  def write(self, w):
    with w.block("android_push_notification_template"):
      self.property(w, "Action", "action", StringValueConverter())
      self.property(w, "ImageUrl", "image_url", StringValueConverter())
      self.property(w, "SmallImageIconUrl", "small_image_icon_url", StringValueConverter())
      self.property(w, "Title", "title", StringValueConverter())
      self.property(w, "ImageIconUrl", "image_icon_url", StringValueConverter())
      self.property(w, "Sound", "sound", StringValueConverter())
      self.property(w, "Body", "body", StringValueConverter())
      self.property(w, "Url", "url", StringValueConverter())


class AWS_Pinpoint_Campaign_EventDimensions(CloudFormationProperty):
  def write(self, w):
    with w.block("event_dimensions"):
      self.property(w, "Metrics", "metrics", JsonValueConverter())
      self.block(w, "EventType", AWS_Pinpoint_Campaign_SetDimension)
      self.property(w, "Attributes", "attributes", JsonValueConverter())


class AWS_Pinpoint_Segment_SourceSegments(CloudFormationProperty):
  def write(self, w):
    with w.block("source_segments"):
      self.property(w, "Version", "version", BasicValueConverter())
      self.property(w, "Id", "id", StringValueConverter())


class AWS_Pinpoint_Segment_AttributeDimension(CloudFormationProperty):
  def write(self, w):
    with w.block("attribute_dimension"):
      self.property(w, "AttributeType", "attribute_type", StringValueConverter())
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_Pinpoint_Segment_GPSPoint(CloudFormationProperty):
  def write(self, w):
    with w.block("gps_point"):
      self.property(w, "RangeInKilometers", "range_in_kilometers", BasicValueConverter())
      self.block(w, "Coordinates", AWS_Pinpoint_Segment_Coordinates)


class AWS_Pinpoint_Segment_Recency(CloudFormationProperty):
  def write(self, w):
    with w.block("recency"):
      self.property(w, "Duration", "duration", StringValueConverter())
      self.property(w, "RecencyType", "recency_type", StringValueConverter())


class AWS_Pinpoint_ApplicationSettings_Limits(CloudFormationProperty):
  def write(self, w):
    with w.block("limits"):
      self.property(w, "Daily", "daily", BasicValueConverter())
      self.property(w, "MaximumDuration", "maximum_duration", BasicValueConverter())
      self.property(w, "Total", "total", BasicValueConverter())
      self.property(w, "MessagesPerSecond", "messages_per_second", BasicValueConverter())


class AWS_Pinpoint_Campaign_Limits(CloudFormationProperty):
  def write(self, w):
    with w.block("limits"):
      self.property(w, "Daily", "daily", BasicValueConverter())
      self.property(w, "MaximumDuration", "maximum_duration", BasicValueConverter())
      self.property(w, "Total", "total", BasicValueConverter())
      self.property(w, "MessagesPerSecond", "messages_per_second", BasicValueConverter())


class AWS_Pinpoint_Segment_SetDimension(CloudFormationProperty):
  def write(self, w):
    with w.block("set_dimension"):
      self.property(w, "DimensionType", "dimension_type", StringValueConverter())
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_Pinpoint_Campaign_AttributeDimension(CloudFormationProperty):
  def write(self, w):
    with w.block("attribute_dimension"):
      self.property(w, "AttributeType", "attribute_type", StringValueConverter())
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_Pinpoint_Campaign_QuietTime(CloudFormationProperty):
  def write(self, w):
    with w.block("quiet_time"):
      self.property(w, "Start", "start", StringValueConverter())
      self.property(w, "End", "end", StringValueConverter())


class AWS_Pinpoint_Segment_Behavior(CloudFormationProperty):
  def write(self, w):
    with w.block("behavior"):
      self.block(w, "Recency", AWS_Pinpoint_Segment_Recency)


class AWS_Pinpoint_Campaign_CampaignHook(CloudFormationProperty):
  def write(self, w):
    with w.block("campaign_hook"):
      self.property(w, "Mode", "mode", StringValueConverter())
      self.property(w, "WebUrl", "web_url", StringValueConverter())
      self.property(w, "LambdaFunctionName", "lambda_function_name", StringValueConverter())


class AWS_Pinpoint_Segment_Location(CloudFormationProperty):
  def write(self, w):
    with w.block("location"):
      self.block(w, "GPSPoint", AWS_Pinpoint_Segment_GPSPoint)
      self.block(w, "Country", AWS_Pinpoint_Segment_SetDimension)


class AWS_Pinpoint_ApplicationSettings_CampaignHook(CloudFormationProperty):
  def write(self, w):
    with w.block("campaign_hook"):
      self.property(w, "Mode", "mode", StringValueConverter())
      self.property(w, "WebUrl", "web_url", StringValueConverter())
      self.property(w, "LambdaFunctionName", "lambda_function_name", StringValueConverter())


class AWS_Pinpoint_PushTemplate_DefaultPushNotificationTemplate(CloudFormationProperty):
  def write(self, w):
    with w.block("default_push_notification_template"):
      self.property(w, "Action", "action", StringValueConverter())
      self.property(w, "Title", "title", StringValueConverter())
      self.property(w, "Sound", "sound", StringValueConverter())
      self.property(w, "Body", "body", StringValueConverter())
      self.property(w, "Url", "url", StringValueConverter())


class AWS_Pinpoint_PushTemplate_APNSPushNotificationTemplate(CloudFormationProperty):
  def write(self, w):
    with w.block("apns_push_notification_template"):
      self.property(w, "Action", "action", StringValueConverter())
      self.property(w, "MediaUrl", "media_url", StringValueConverter())
      self.property(w, "Title", "title", StringValueConverter())
      self.property(w, "Sound", "sound", StringValueConverter())
      self.property(w, "Body", "body", StringValueConverter())
      self.property(w, "Url", "url", StringValueConverter())


class AWS_Pinpoint_Campaign_Message(CloudFormationProperty):
  def write(self, w):
    with w.block("message"):
      self.property(w, "JsonBody", "json_body", StringValueConverter())
      self.property(w, "Action", "action", StringValueConverter())
      self.property(w, "MediaUrl", "media_url", StringValueConverter())
      self.property(w, "TimeToLive", "time_to_live", BasicValueConverter())
      self.property(w, "ImageSmallIconUrl", "image_small_icon_url", StringValueConverter())
      self.property(w, "ImageUrl", "image_url", StringValueConverter())
      self.property(w, "Title", "title", StringValueConverter())
      self.property(w, "ImageIconUrl", "image_icon_url", StringValueConverter())
      self.property(w, "SilentPush", "silent_push", BasicValueConverter())
      self.property(w, "Body", "body", StringValueConverter())
      self.property(w, "RawContent", "raw_content", StringValueConverter())
      self.property(w, "Url", "url", StringValueConverter())


class AWS_Pinpoint_Campaign_CampaignEventFilter(CloudFormationProperty):
  def write(self, w):
    with w.block("campaign_event_filter"):
      self.property(w, "FilterType", "filter_type", StringValueConverter())
      self.block(w, "Dimensions", AWS_Pinpoint_Campaign_EventDimensions)


class AWS_Pinpoint_Campaign_CampaignSmsMessage(CloudFormationProperty):
  def write(self, w):
    with w.block("campaign_sms_message"):
      self.property(w, "SenderId", "sender_id", StringValueConverter())
      self.property(w, "Body", "body", StringValueConverter())
      self.property(w, "MessageType", "message_type", StringValueConverter())


class AWS_Pinpoint_Campaign_CampaignEmailMessage(CloudFormationProperty):
  def write(self, w):
    with w.block("campaign_email_message"):
      self.property(w, "FromAddress", "from_address", StringValueConverter())
      self.property(w, "HtmlBody", "html_body", StringValueConverter())
      self.property(w, "Title", "title", StringValueConverter())
      self.property(w, "Body", "body", StringValueConverter())


class AWS_Pinpoint_ApplicationSettings_QuietTime(CloudFormationProperty):
  def write(self, w):
    with w.block("quiet_time"):
      self.property(w, "Start", "start", StringValueConverter())
      self.property(w, "End", "end", StringValueConverter())


class AWS_Pinpoint_SMSChannel(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::SMSChannel"
  tf_type = "aws_pinpoint_sms_channel"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ShortCode", "short_code", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "ApplicationId", "application_id", StringValueConverter())
      self.property(w, "SenderId", "sender_id", StringValueConverter())


class AWS_Pinpoint_VoiceChannel(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::VoiceChannel"
  tf_type = "aws_pinpoint_voice_channel" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "ApplicationId", "application_id", StringValueConverter())


class AWS_Pinpoint_EventStream(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::EventStream"
  tf_type = "aws_pinpoint_event_stream"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApplicationId", "application_id", StringValueConverter())
      self.property(w, "DestinationStreamArn", "destination_stream_arn", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_Pinpoint_EmailTemplate(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::EmailTemplate"
  tf_type = "aws_pinpoint_email_template" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "HtmlPart", "html_part", StringValueConverter())
      self.property(w, "TextPart", "text_part", StringValueConverter())
      self.property(w, "TemplateName", "template_name", StringValueConverter())
      self.property(w, "TemplateDescription", "template_description", StringValueConverter())
      self.property(w, "DefaultSubstitutions", "default_substitutions", StringValueConverter())
      self.property(w, "Subject", "subject", StringValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())


class AWS_Pinpoint_BaiduChannel(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::BaiduChannel"
  tf_type = "aws_pinpoint_baidu_channel"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "SecretKey", "secret_key", StringValueConverter())
      self.property(w, "ApiKey", "api_key", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "ApplicationId", "application_id", StringValueConverter())


class AWS_Pinpoint_GCMChannel(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::GCMChannel"
  tf_type = "aws_pinpoint_gcm_channel"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApiKey", "api_key", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "ApplicationId", "application_id", StringValueConverter())


class AWS_Pinpoint_APNSChannel(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::APNSChannel"
  tf_type = "aws_pinpoint_apns_channel"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "BundleId", "bundle_id", StringValueConverter())
      self.property(w, "PrivateKey", "private_key", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "DefaultAuthenticationMethod", "default_authentication_method", StringValueConverter())
      self.property(w, "TokenKey", "token_key", StringValueConverter())
      self.property(w, "ApplicationId", "application_id", StringValueConverter())
      self.property(w, "TeamId", "team_id", StringValueConverter())
      self.property(w, "Certificate", "certificate", StringValueConverter())
      self.property(w, "TokenKeyId", "token_key_id", StringValueConverter())


class AWS_Pinpoint_SmsTemplate(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::SmsTemplate"
  tf_type = "aws_pinpoint_sms_template" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "TemplateName", "template_name", StringValueConverter())
      self.property(w, "TemplateDescription", "template_description", StringValueConverter())
      self.property(w, "DefaultSubstitutions", "default_substitutions", StringValueConverter())
      self.property(w, "Body", "body", StringValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())


class AWS_Pinpoint_APNSSandboxChannel(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::APNSSandboxChannel"
  tf_type = "aws_pinpoint_apns_sandbox_channel"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "BundleId", "bundle_id", StringValueConverter())
      self.property(w, "PrivateKey", "private_key", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "DefaultAuthenticationMethod", "default_authentication_method", StringValueConverter())
      self.property(w, "TokenKey", "token_key", StringValueConverter())
      self.property(w, "ApplicationId", "application_id", StringValueConverter())
      self.property(w, "TeamId", "team_id", StringValueConverter())
      self.property(w, "Certificate", "certificate", StringValueConverter())
      self.property(w, "TokenKeyId", "token_key_id", StringValueConverter())


class AWS_Pinpoint_ADMChannel(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::ADMChannel"
  tf_type = "aws_pinpoint_adm_channel"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ClientSecret", "client_secret", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "ClientId", "client_id", StringValueConverter())
      self.property(w, "ApplicationId", "application_id", StringValueConverter())


class AWS_Pinpoint_ApplicationSettings(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::ApplicationSettings"
  tf_type = "aws_pinpoint_application_settings" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "QuietTime", AWS_Pinpoint_ApplicationSettings_QuietTime)
      self.block(w, "Limits", AWS_Pinpoint_ApplicationSettings_Limits)
      self.property(w, "ApplicationId", "application_id", StringValueConverter())
      self.block(w, "CampaignHook", AWS_Pinpoint_ApplicationSettings_CampaignHook)
      self.property(w, "CloudWatchMetricsEnabled", "cloud_watch_metrics_enabled", BasicValueConverter())


class AWS_Pinpoint_PushTemplate(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::PushTemplate"
  tf_type = "aws_pinpoint_push_template" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "GCM", AWS_Pinpoint_PushTemplate_AndroidPushNotificationTemplate)
      self.block(w, "Baidu", AWS_Pinpoint_PushTemplate_AndroidPushNotificationTemplate)
      self.property(w, "TemplateName", "template_name", StringValueConverter())
      self.block(w, "ADM", AWS_Pinpoint_PushTemplate_AndroidPushNotificationTemplate)
      self.block(w, "APNS", AWS_Pinpoint_PushTemplate_APNSPushNotificationTemplate)
      self.property(w, "TemplateDescription", "template_description", StringValueConverter())
      self.property(w, "DefaultSubstitutions", "default_substitutions", StringValueConverter())
      self.block(w, "Default", AWS_Pinpoint_PushTemplate_DefaultPushNotificationTemplate)
      self.property(w, "Tags", "tags", JsonValueConverter())


class AWS_Pinpoint_APNSVoipSandboxChannel(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::APNSVoipSandboxChannel"
  tf_type = "aws_pinpoint_apns_voip_sandbox_channel"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "BundleId", "bundle_id", StringValueConverter())
      self.property(w, "PrivateKey", "private_key", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "DefaultAuthenticationMethod", "default_authentication_method", StringValueConverter())
      self.property(w, "TokenKey", "token_key", StringValueConverter())
      self.property(w, "ApplicationId", "application_id", StringValueConverter())
      self.property(w, "TeamId", "team_id", StringValueConverter())
      self.property(w, "Certificate", "certificate", StringValueConverter())
      self.property(w, "TokenKeyId", "token_key_id", StringValueConverter())


class AWS_Pinpoint_APNSVoipChannel(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::APNSVoipChannel"
  tf_type = "aws_pinpoint_apns_voip_channel"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "BundleId", "bundle_id", StringValueConverter())
      self.property(w, "PrivateKey", "private_key", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "DefaultAuthenticationMethod", "default_authentication_method", StringValueConverter())
      self.property(w, "TokenKey", "token_key", StringValueConverter())
      self.property(w, "ApplicationId", "application_id", StringValueConverter())
      self.property(w, "TeamId", "team_id", StringValueConverter())
      self.property(w, "Certificate", "certificate", StringValueConverter())
      self.property(w, "TokenKeyId", "token_key_id", StringValueConverter())


class AWS_Pinpoint_EmailChannel(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::EmailChannel"
  tf_type = "aws_pinpoint_email_channel"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ConfigurationSet", "configuration_set", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "FromAddress", "from_address", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "ApplicationId", "application_id", StringValueConverter())
      self.property(w, "Identity", "identity", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_Pinpoint_App(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::App"
  tf_type = "aws_pinpoint_app"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Pinpoint_Segment_Demographic(CloudFormationProperty):
  def write(self, w):
    with w.block("demographic"):
      self.block(w, "AppVersion", AWS_Pinpoint_Segment_SetDimension)
      self.block(w, "DeviceType", AWS_Pinpoint_Segment_SetDimension)
      self.block(w, "Platform", AWS_Pinpoint_Segment_SetDimension)
      self.block(w, "Channel", AWS_Pinpoint_Segment_SetDimension)
      self.block(w, "Model", AWS_Pinpoint_Segment_SetDimension)
      self.block(w, "Make", AWS_Pinpoint_Segment_SetDimension)


class AWS_Pinpoint_Campaign_Schedule(CloudFormationProperty):
  def write(self, w):
    with w.block("schedule"):
      self.property(w, "TimeZone", "time_zone", StringValueConverter())
      self.block(w, "QuietTime", AWS_Pinpoint_Campaign_QuietTime)
      self.property(w, "EndTime", "end_time", StringValueConverter())
      self.property(w, "StartTime", "start_time", StringValueConverter())
      self.property(w, "Frequency", "frequency", StringValueConverter())
      self.block(w, "EventFilter", AWS_Pinpoint_Campaign_CampaignEventFilter)
      self.property(w, "IsLocalTime", "is_local_time", BasicValueConverter())


class AWS_Pinpoint_Campaign_MessageConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("message_configuration"):
      self.block(w, "APNSMessage", AWS_Pinpoint_Campaign_Message)
      self.block(w, "BaiduMessage", AWS_Pinpoint_Campaign_Message)
      self.block(w, "DefaultMessage", AWS_Pinpoint_Campaign_Message)
      self.block(w, "EmailMessage", AWS_Pinpoint_Campaign_CampaignEmailMessage)
      self.block(w, "GCMMessage", AWS_Pinpoint_Campaign_Message)
      self.block(w, "SMSMessage", AWS_Pinpoint_Campaign_CampaignSmsMessage)
      self.block(w, "ADMMessage", AWS_Pinpoint_Campaign_Message)


class AWS_Pinpoint_Campaign_WriteTreatmentResource(CloudFormationProperty):
  def write(self, w):
    with w.block("write_treatment_resource"):
      self.property(w, "TreatmentDescription", "treatment_description", StringValueConverter())
      self.block(w, "MessageConfiguration", AWS_Pinpoint_Campaign_MessageConfiguration)
      self.block(w, "Schedule", AWS_Pinpoint_Campaign_Schedule)
      self.property(w, "SizePercent", "size_percent", BasicValueConverter())
      self.property(w, "TreatmentName", "treatment_name", StringValueConverter())


class AWS_Pinpoint_Campaign(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::Campaign"
  tf_type = "aws_pinpoint_campaign" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "SegmentId", "segment_id", StringValueConverter())
      self.property(w, "IsPaused", "is_paused", BasicValueConverter())
      self.repeated_block(w, "AdditionalTreatments", AWS_Pinpoint_Campaign_WriteTreatmentResource)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "SegmentVersion", "segment_version", BasicValueConverter())
      self.property(w, "TreatmentDescription", "treatment_description", StringValueConverter())
      self.block(w, "MessageConfiguration", AWS_Pinpoint_Campaign_MessageConfiguration)
      self.block(w, "Limits", AWS_Pinpoint_Campaign_Limits)
      self.property(w, "HoldoutPercent", "holdout_percent", BasicValueConverter())
      self.block(w, "Schedule", AWS_Pinpoint_Campaign_Schedule)
      self.property(w, "ApplicationId", "application_id", StringValueConverter())
      self.block(w, "CampaignHook", AWS_Pinpoint_Campaign_CampaignHook)
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "TreatmentName", "treatment_name", StringValueConverter())


class AWS_Pinpoint_Segment_SegmentDimensions(CloudFormationProperty):
  def write(self, w):
    with w.block("segment_dimensions"):
      self.block(w, "Demographic", AWS_Pinpoint_Segment_Demographic)
      self.property(w, "Metrics", "metrics", JsonValueConverter())
      self.property(w, "Attributes", "attributes", JsonValueConverter())
      self.block(w, "Behavior", AWS_Pinpoint_Segment_Behavior)
      self.property(w, "UserAttributes", "user_attributes", JsonValueConverter())
      self.block(w, "Location", AWS_Pinpoint_Segment_Location)


class AWS_Pinpoint_Segment_Groups(CloudFormationProperty):
  def write(self, w):
    with w.block("groups"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "SourceType", "source_type", StringValueConverter())
      self.repeated_block(w, "Dimensions", AWS_Pinpoint_Segment_SegmentDimensions)
      self.repeated_block(w, "SourceSegments", AWS_Pinpoint_Segment_SourceSegments)


class AWS_Pinpoint_Segment_SegmentGroups(CloudFormationProperty):
  def write(self, w):
    with w.block("segment_groups"):
      self.repeated_block(w, "Groups", AWS_Pinpoint_Segment_Groups)
      self.property(w, "Include", "include", StringValueConverter())


class AWS_Pinpoint_Segment(CloudFormationResource):
  cfn_type = "AWS::Pinpoint::Segment"
  tf_type = "aws_pinpoint_segment" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "SegmentGroups", AWS_Pinpoint_Segment_SegmentGroups)
      self.block(w, "Dimensions", AWS_Pinpoint_Segment_SegmentDimensions)
      self.property(w, "ApplicationId", "application_id", StringValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


