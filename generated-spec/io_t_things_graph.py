from . import *

class AWS_IoTThingsGraph_FlowTemplate_DefinitionDocument(CloudFormationProperty):
  entity = "AWS::IoTThingsGraph::FlowTemplate"
  tf_block_type = "definition_document"

  props = {
    "Language": (StringValueConverter(), "language"),
    "Text": (StringValueConverter(), "text"),
  }

class AWS_IoTThingsGraph_FlowTemplate(CloudFormationResource):
  terraform_resource = "aws_io_t_things_graph_flow_template"

  resource_type = "AWS::IoTThingsGraph::FlowTemplate"

  props = {
    "CompatibleNamespaceVersion": (BasicValueConverter(), "compatible_namespace_version"),
    "Definition": (AWS_IoTThingsGraph_FlowTemplate_DefinitionDocument, "definition"),
  }

