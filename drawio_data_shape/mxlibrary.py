import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, List

from drawio_data_shape.datasource_container import DatasourceContainer
from drawio_data_shape.model import MX_GRAPH_MODELS, Datasource, IconDatasource, ImageDatasource, TemplateDetails
from drawio_data_shape.mx.xml_visitor import XMLVisitor
from drawio_data_shape.templating import ENVIRONMENT


def get_template(style: Datasource) -> str:
    if isinstance(style, IconDatasource):
        return "aws_graph_model.jinja2"
    if isinstance(style, ImageDatasource):
        return "image_graph_model.jinja2"

    raise ValueError(f"Unknown style {style.__class__}")


def render_template(model: TemplateDetails, stencil_content: str) -> str:
    template_name = get_template(model.style)
    template = ENVIRONMENT.get_template(template_name)

    rendered = template.render(model=model, stencil=stencil_content)
    return rendered


def create_library(models: List[TemplateDetails]) -> None:
    library: List[Dict[str, Any]] = []

    for model in models:
        entry: Dict[str, Any] = {}

        container = DatasourceContainer()
        graph_model = container.build(model)

        xml_visitor = XMLVisitor()
        xml_visitor.visitMxGraphModel(graph_model)
        pretty_xml = xml_visitor.xml_str()

        entry["title"] = model.title
        entry["h"] = model.height
        entry["w"] = model.width
        entry["aspect"] = model.aspect
        entry["xml"] = re.sub(r"[\t\n]", "", pretty_xml)

        library.append(entry)

    res = json.dumps(library, indent=4)
    root = ET.Element("mxlibrary")
    root.text = res
    tree = ET.ElementTree(root)

    path = Path(__file__).parent.resolve() / "data_library.xml"
    tree.write(path)


if __name__ == "__main__":
    create_library(MX_GRAPH_MODELS)
