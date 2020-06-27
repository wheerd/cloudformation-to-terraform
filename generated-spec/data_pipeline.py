from . import *

class AWS_DataPipeline_Pipeline_ParameterAttribute(CloudFormationProperty):
  entity = "AWS::DataPipeline::Pipeline"
  tf_block_type = "parameter_attribute"

  props = {
    "Key": (StringValueConverter(), "key"),
    "StringValue": (StringValueConverter(), "string_value"),
  }

class AWS_DataPipeline_Pipeline_PipelineTag(CloudFormationProperty):
  entity = "AWS::DataPipeline::Pipeline"
  tf_block_type = "pipeline_tag"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_DataPipeline_Pipeline_ParameterObject(CloudFormationProperty):
  entity = "AWS::DataPipeline::Pipeline"
  tf_block_type = "parameter_object"

  props = {
    "Attributes": (BlockValueConverter(AWS_DataPipeline_Pipeline_ParameterAttribute), None),
    "Id": (StringValueConverter(), "id"),
  }

class AWS_DataPipeline_Pipeline_ParameterValue(CloudFormationProperty):
  entity = "AWS::DataPipeline::Pipeline"
  tf_block_type = "parameter_value"

  props = {
    "Id": (StringValueConverter(), "id"),
    "StringValue": (StringValueConverter(), "string_value"),
  }

class AWS_DataPipeline_Pipeline_Field(CloudFormationProperty):
  entity = "AWS::DataPipeline::Pipeline"
  tf_block_type = "field"

  props = {
    "Key": (StringValueConverter(), "key"),
    "RefValue": (StringValueConverter(), "ref_value"),
    "StringValue": (StringValueConverter(), "string_value"),
  }

class AWS_DataPipeline_Pipeline_PipelineObject(CloudFormationProperty):
  entity = "AWS::DataPipeline::Pipeline"
  tf_block_type = "pipeline_object"

  props = {
    "Fields": (BlockValueConverter(AWS_DataPipeline_Pipeline_Field), None),
    "Id": (StringValueConverter(), "id"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_DataPipeline_Pipeline(CloudFormationResource):
  terraform_resource = "aws_data_pipeline_pipeline"

  resource_type = "AWS::DataPipeline::Pipeline"

  props = {
    "Activate": (BasicValueConverter(), "activate"),
    "Description": (StringValueConverter(), "description"),
    "Name": (StringValueConverter(), "name"),
    "ParameterObjects": (BlockValueConverter(AWS_DataPipeline_Pipeline_ParameterObject), None),
    "ParameterValues": (BlockValueConverter(AWS_DataPipeline_Pipeline_ParameterValue), None),
    "PipelineObjects": (BlockValueConverter(AWS_DataPipeline_Pipeline_PipelineObject), None),
    "PipelineTags": (BlockValueConverter(AWS_DataPipeline_Pipeline_PipelineTag), None),
  }

