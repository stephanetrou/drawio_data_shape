from dataclasses import dataclass

from drawio_data_shape.templates.configuration import ENVIRONMENT
from drawio_data_shape.tools.deflate_tools import encode


@dataclass(frozen=True)
class Stencil:
    width: int
    height: int


def generate_stencil(stencil: Stencil) -> str:
    template = ENVIRONMENT.get_template("datasource.jinja2")
    content = template.render(stencil=stencil)

    encoded = encode(content)
    return encoded
