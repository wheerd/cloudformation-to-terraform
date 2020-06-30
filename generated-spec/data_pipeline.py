from . import *

class AWS_DataPipeline_Pipeline_ParameterAttribute(CloudFormationProperty):
  def write(self, w):
    with w.block("parameter_attribute"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "StringValue", "string_value", StringValueConverter())


class AWS_DataPipeline_Pipeline_PipelineTag(CloudFormationProperty):
  def write(self, w):
    with w.block("pipeline_tag"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_DataPipeline_Pipeline_ParameterObject(CloudFormationProperty):
  def write(self, w):
    with w.block("parameter_object"):
      self.repeated_block(w, "Attributes", AWS_DataPipeline_Pipeline_ParameterAttribute)
      self.property(w, "Id", "id", StringValueConverter())


class AWS_DataPipeline_Pipeline_ParameterValue(CloudFormationProperty):
  def write(self, w):
    with w.block("parameter_value"):
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "StringValue", "string_value", StringValueConverter())


class AWS_DataPipeline_Pipeline_Field(CloudFormationProperty):
  def write(self, w):
    with w.block("field"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "RefValue", "ref_value", StringValueConverter())
      self.property(w, "StringValue", "string_value", StringValueConverter())


class AWS_DataPipeline_Pipeline_PipelineObject(CloudFormationProperty):
  def write(self, w):
    with w.block("pipeline_object"):
      self.repeated_block(w, "Fields", AWS_DataPipeline_Pipeline_Field)
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_DataPipeline_Pipeline(CloudFormationResource):
  cfn_type = "AWS::DataPipeline::Pipeline"
  tf_type = "aws_datapipeline_pipeline"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Activate", "activate", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.repeated_block(w, "ParameterObjects", AWS_DataPipeline_Pipeline_ParameterObject) # TODO: Probably not the correct mapping
      self.repeated_block(w, "ParameterValues", AWS_DataPipeline_Pipeline_ParameterValue) # TODO: Probably not the correct mapping
      self.repeated_block(w, "PipelineObjects", AWS_DataPipeline_Pipeline_PipelineObject) # TODO: Probably not the correct mapping
      self.repeated_block(w, "PipelineTags", AWS_DataPipeline_Pipeline_PipelineTag)


