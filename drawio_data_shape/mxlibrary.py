import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict

from drawio_data_shape.library_models import (
    DATASOURCES,
    MEDALLIONS,
)
from drawio_data_shape.mx.xml_visitor import XMLVisitor
from drawio_data_shape.shape.datasource_container import DatasourceContainer
from drawio_data_shape.shape.medallion import Medallion


def map_to_library_entry(template, genarator) -> Dict[str, Any]:
    entry: Dict[str, Any] = {}

    graph_model = genarator.build(template)

    xml_visitor = XMLVisitor()
    xml_visitor.visitMxGraphModel(graph_model)
    pretty_xml = xml_visitor.xml_str()

    entry["title"] = template.title
    entry["h"] = template.height
    entry["w"] = template.width
    entry["aspect"] = template.aspect
    entry["xml"] = re.sub(r"[\t\n]", "", pretty_xml)

    return entry


def create_library() -> None:
    library = [map_to_library_entry(model, DatasourceContainer()) for model in DATASOURCES]
    library += [map_to_library_entry(model, Medallion()) for model in MEDALLIONS]

    res = json.dumps(library, indent=4)
    root = ET.Element("mxlibrary")
    root.text = res
    tree = ET.ElementTree(root)

    path = Path(__file__).parent.resolve() / "pydrawio_data_library.xml"
    tree.write(path)


if __name__ == "__main__":
    create_library()
