from dataclasses import dataclass

from drawio_data_shape.templates.configuration import ENVIRONMENT
from drawio_data_shape.tools.deflate_tools import encode


@dataclass(frozen=True)
class ShapeInformation:
    name: str
    height: int
    width: int


def generate_encoded_shape(shape_information: ShapeInformation) -> str:
    template = ENVIRONMENT.get_template(f"shapes/{shape_information.name}.jinja2")
    content = template.render(shape=shape_information)

    encoded = encode(content)
    return encoded
