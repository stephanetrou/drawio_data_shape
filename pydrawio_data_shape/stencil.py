from dataclasses import dataclass

from pydrawio_data_shape.deflate_tools import encode
from pydrawio_data_shape.templating import ENVIRONMENT


@dataclass(frozen=True)
class Stencil:
    width: int
    height: int


def generate_stencil(stencil: Stencil) -> str:
    template = ENVIRONMENT.get_template("stencil.jinja2")
    content = template.render(stencil=stencil)

    encoded = encode(content)
    return encoded
