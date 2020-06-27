from . import *

class AWS_MediaLive_Channel_MediaPackageOutputDestinationSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("media_package_output_destination_settings"):
      self.property(w, "ChannelId", "channel_id", StringValueConverter())


class AWS_MediaLive_InputSecurityGroup_InputWhitelistRuleCidr(CloudFormationProperty):
  def write(self, w):
    with w.block("input_whitelist_rule_cidr"):
      self.property(w, "Cidr", "cidr", StringValueConverter())


class AWS_MediaLive_Channel_HlsInputSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("hls_input_settings"):
      self.property(w, "BufferSegments", "buffer_segments", BasicValueConverter())
      self.property(w, "Retries", "retries", BasicValueConverter())
      self.property(w, "Bandwidth", "bandwidth", BasicValueConverter())
      self.property(w, "RetryInterval", "retry_interval", BasicValueConverter())


class AWS_MediaLive_Channel_VideoSelectorProgramId(CloudFormationProperty):
  def write(self, w):
    with w.block("video_selector_program_id"):
      self.property(w, "ProgramId", "program_id", BasicValueConverter())


class AWS_MediaLive_Channel_MultiplexProgramChannelDestinationSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("multiplex_program_channel_destination_settings"):
      self.property(w, "MultiplexId", "multiplex_id", StringValueConverter())
      self.property(w, "ProgramName", "program_name", StringValueConverter())


class AWS_MediaLive_Channel_EmbeddedSourceSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("embedded_source_settings"):
      self.property(w, "Source608ChannelNumber", "source608_channel_number", BasicValueConverter())
      self.property(w, "Scte20Detection", "scte20_detection", StringValueConverter())
      self.property(w, "Source608TrackNumber", "source608_track_number", BasicValueConverter())
      self.property(w, "Convert608To708", "convert608_to708", StringValueConverter())


class AWS_MediaLive_Channel_InputSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("input_specification"):
      self.property(w, "Codec", "codec", StringValueConverter())
      self.property(w, "MaximumBitrate", "maximum_bitrate", StringValueConverter())
      self.property(w, "Resolution", "resolution", StringValueConverter())


class AWS_MediaLive_Channel_Scte27SourceSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("scte27_source_settings"):
      self.property(w, "Pid", "pid", BasicValueConverter())


class AWS_MediaLive_Channel_VideoSelectorPid(CloudFormationProperty):
  def write(self, w):
    with w.block("video_selector_pid"):
      self.property(w, "Pid", "pid", BasicValueConverter())


class AWS_MediaLive_Input_InputVpcRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("input_vpc_request"):
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))


class AWS_MediaLive_Channel_AudioLanguageSelection(CloudFormationProperty):
  def write(self, w):
    with w.block("audio_language_selection"):
      self.property(w, "LanguageCode", "language_code", StringValueConverter())
      self.property(w, "LanguageSelectionPolicy", "language_selection_policy", StringValueConverter())


class AWS_MediaLive_Channel_AribSourceSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("arib_source_settings"):
      pass


class AWS_MediaLive_Channel_AudioPidSelection(CloudFormationProperty):
  def write(self, w):
    with w.block("audio_pid_selection"):
      self.property(w, "Pid", "pid", BasicValueConverter())


class AWS_MediaLive_Channel_DvbSubSourceSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("dvb_sub_source_settings"):
      self.property(w, "Pid", "pid", BasicValueConverter())


class AWS_MediaLive_Input_InputSourceRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("input_source_request"):
      self.property(w, "Username", "username", StringValueConverter())
      self.property(w, "PasswordParam", "password_param", StringValueConverter())
      self.property(w, "Url", "url", StringValueConverter())


class AWS_MediaLive_Channel_VideoSelectorSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("video_selector_settings"):
      self.block(w, "VideoSelectorProgramId", AWS_MediaLive_Channel_VideoSelectorProgramId)
      self.block(w, "VideoSelectorPid", AWS_MediaLive_Channel_VideoSelectorPid)


class AWS_MediaLive_Channel_TeletextSourceSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("teletext_source_settings"):
      self.property(w, "PageNumber", "page_number", StringValueConverter())


class AWS_MediaLive_Input_InputDestinationRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("input_destination_request"):
      self.property(w, "StreamName", "stream_name", StringValueConverter())


class AWS_MediaLive_Channel_NetworkInputSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("network_input_settings"):
      self.property(w, "ServerValidation", "server_validation", StringValueConverter())
      self.block(w, "HlsInputSettings", AWS_MediaLive_Channel_HlsInputSettings)


class AWS_MediaLive_Input_MediaConnectFlowRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("media_connect_flow_request"):
      self.property(w, "FlowArn", "flow_arn", StringValueConverter())


class AWS_MediaLive_Channel_Scte20SourceSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("scte20_source_settings"):
      self.property(w, "Source608ChannelNumber", "source608_channel_number", BasicValueConverter())
      self.property(w, "Convert608To708", "convert608_to708", StringValueConverter())


class AWS_MediaLive_Channel_AudioSelectorSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("audio_selector_settings"):
      self.block(w, "AudioPidSelection", AWS_MediaLive_Channel_AudioPidSelection)
      self.block(w, "AudioLanguageSelection", AWS_MediaLive_Channel_AudioLanguageSelection)


class AWS_MediaLive_Channel_VideoSelector(CloudFormationProperty):
  def write(self, w):
    with w.block("video_selector"):
      self.block(w, "SelectorSettings", AWS_MediaLive_Channel_VideoSelectorSettings)
      self.property(w, "ColorSpace", "color_space", StringValueConverter())
      self.property(w, "ColorSpaceUsage", "color_space_usage", StringValueConverter())


class AWS_MediaLive_Channel_OutputDestinationSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("output_destination_settings"):
      self.property(w, "StreamName", "stream_name", StringValueConverter())
      self.property(w, "Username", "username", StringValueConverter())
      self.property(w, "PasswordParam", "password_param", StringValueConverter())
      self.property(w, "Url", "url", StringValueConverter())


class AWS_MediaLive_Channel_OutputDestination(CloudFormationProperty):
  def write(self, w):
    with w.block("output_destination"):
      self.block(w, "MultiplexSettings", AWS_MediaLive_Channel_MultiplexProgramChannelDestinationSettings)
      self.property(w, "Id", "id", StringValueConverter())
      self.repeated_block(w, "Settings", AWS_MediaLive_Channel_OutputDestinationSettings)
      self.repeated_block(w, "MediaPackageSettings", AWS_MediaLive_Channel_MediaPackageOutputDestinationSettings)


class AWS_MediaLive_Input(CloudFormationResource):
  cfn_type = "AWS::MediaLive::Input"
  tf_type = "aws_media_live_input"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Type", "type", StringValueConverter())
      self.repeated_block(w, "Destinations", AWS_MediaLive_Input_InputDestinationRequest)
      self.block(w, "Vpc", AWS_MediaLive_Input_InputVpcRequest)
      self.repeated_block(w, "MediaConnectFlows", AWS_MediaLive_Input_MediaConnectFlowRequest)
      self.property(w, "InputSecurityGroups", "input_security_groups", ListValueConverter(StringValueConverter()))
      self.repeated_block(w, "Sources", AWS_MediaLive_Input_InputSourceRequest)
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_MediaLive_InputSecurityGroup(CloudFormationResource):
  cfn_type = "AWS::MediaLive::InputSecurityGroup"
  tf_type = "aws_media_live_input_security_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "WhitelistRules", AWS_MediaLive_InputSecurityGroup_InputWhitelistRuleCidr)
      self.property(w, "Tags", "tags", JsonValueConverter())


class AWS_MediaLive_Channel_AudioSelector(CloudFormationProperty):
  def write(self, w):
    with w.block("audio_selector"):
      self.block(w, "SelectorSettings", AWS_MediaLive_Channel_AudioSelectorSettings)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_MediaLive_Channel_CaptionSelectorSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("caption_selector_settings"):
      self.block(w, "DvbSubSourceSettings", AWS_MediaLive_Channel_DvbSubSourceSettings)
      self.block(w, "Scte27SourceSettings", AWS_MediaLive_Channel_Scte27SourceSettings)
      self.block(w, "AribSourceSettings", AWS_MediaLive_Channel_AribSourceSettings)
      self.block(w, "EmbeddedSourceSettings", AWS_MediaLive_Channel_EmbeddedSourceSettings)
      self.block(w, "Scte20SourceSettings", AWS_MediaLive_Channel_Scte20SourceSettings)
      self.block(w, "TeletextSourceSettings", AWS_MediaLive_Channel_TeletextSourceSettings)


class AWS_MediaLive_Channel_CaptionSelector(CloudFormationProperty):
  def write(self, w):
    with w.block("caption_selector"):
      self.property(w, "LanguageCode", "language_code", StringValueConverter())
      self.block(w, "SelectorSettings", AWS_MediaLive_Channel_CaptionSelectorSettings)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_MediaLive_Channel_InputSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("input_settings"):
      self.property(w, "DeblockFilter", "deblock_filter", StringValueConverter())
      self.property(w, "FilterStrength", "filter_strength", BasicValueConverter())
      self.property(w, "InputFilter", "input_filter", StringValueConverter())
      self.property(w, "SourceEndBehavior", "source_end_behavior", StringValueConverter())
      self.block(w, "VideoSelector", AWS_MediaLive_Channel_VideoSelector)
      self.repeated_block(w, "AudioSelectors", AWS_MediaLive_Channel_AudioSelector)
      self.repeated_block(w, "CaptionSelectors", AWS_MediaLive_Channel_CaptionSelector)
      self.property(w, "DenoiseFilter", "denoise_filter", StringValueConverter())
      self.block(w, "NetworkInputSettings", AWS_MediaLive_Channel_NetworkInputSettings)


class AWS_MediaLive_Channel_InputAttachment(CloudFormationProperty):
  def write(self, w):
    with w.block("input_attachment"):
      self.property(w, "InputAttachmentName", "input_attachment_name", StringValueConverter())
      self.property(w, "InputId", "input_id", StringValueConverter())
      self.block(w, "InputSettings", AWS_MediaLive_Channel_InputSettings)


class AWS_MediaLive_Channel(CloudFormationResource):
  cfn_type = "AWS::MediaLive::Channel"
  tf_type = "aws_media_live_channel"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "InputAttachments", AWS_MediaLive_Channel_InputAttachment)
      self.block(w, "InputSpecification", AWS_MediaLive_Channel_InputSpecification)
      self.property(w, "ChannelClass", "channel_class", StringValueConverter())
      self.property(w, "EncoderSettings", "encoder_settings", JsonValueConverter())
      self.repeated_block(w, "Destinations", AWS_MediaLive_Channel_OutputDestination)
      self.property(w, "LogLevel", "log_level", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


