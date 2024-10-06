import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, List

from pydrawio_data_shape.model import MX_GRAPH_MODELS, AWSStyle, ImageStyle, MxGraphModel, Style
from pydrawio_data_shape.stencil import Stencil, generate_stencil
from pydrawio_data_shape.templating import ENVIRONMENT


def get_template(style: Style) -> str:
    if isinstance(style, AWSStyle):
        return "aws_graph_model.jinja2"
    if isinstance(style, ImageStyle):
        return "image_graph_model.jinja2"

    raise ValueError(f"Unknown style {style.__class__}")


def render_template(model: MxGraphModel, stencil_content: str) -> str:
    template_name = get_template(model.style)
    template = ENVIRONMENT.get_template(template_name)

    rendered = template.render(model=model, stencil=stencil_content)
    return rendered


def create_library(models: List[MxGraphModel]) -> None:
    library: List[Dict[str, Any]] = []

    for model in models:
        entry: Dict[str, Any] = {}

        stencil = generate_stencil(Stencil(model.width, model.height))
        rendered = render_template(model, stencil)

        entry["title"] = model.title
        entry["h"] = model.height
        entry["w"] = model.width
        entry["aspect"] = model.aspect
        entry["xml"] = re.sub(r"[\t\n]", "", rendered)

        library.append(entry)

    res = json.dumps(library, indent=4)
    root = ET.Element("mxlibrary")
    root.text = res
    tree = ET.ElementTree(root)

    path = Path(__file__).parent.resolve() / "data_library.xml"
    tree.write(path)


if __name__ == "__main__":
    create_library(MX_GRAPH_MODELS)
