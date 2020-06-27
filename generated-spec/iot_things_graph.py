from . import *

class AWS_IoTThingsGraph_FlowTemplate_DefinitionDocument(CloudFormationProperty):
  def write(self, w):
    with w.block("definition_document"):
      self.property(w, "Language", "language", StringValueConverter())
      self.property(w, "Text", "text", StringValueConverter())


class AWS_IoTThingsGraph_FlowTemplate(CloudFormationResource):
  cfn_type = "AWS::IoTThingsGraph::FlowTemplate"
  tf_type = "aws_iot_things_graph_flow_template"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CompatibleNamespaceVersion", "compatible_namespace_version", BasicValueConverter())
      self.block(w, "Definition", AWS_IoTThingsGraph_FlowTemplate_DefinitionDocument)


