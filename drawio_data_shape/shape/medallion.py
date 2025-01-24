from drawio_data_shape.library_models import MedallionTemplate
from drawio_data_shape.models.shape import ShapeInformation, generate_encoded_shape
from drawio_data_shape.mx.mxmodels import MxCell, MxGeometry, MxGraphModel, MxObject, MxRectangle
from drawio_data_shape.mx.mxstyle import StyleBuilder


class Medallion:
    def __init__(self):
        self.next_id = -1

    def _get_next_id(self):
        self.next_id += 1
        return self.next_id

    def build(self, template: MedallionTemplate) -> MxGraphModel:
        mx_graph_model = MxGraphModel()

        cell_0 = MxCell(self._get_next_id())
        mx_graph_model.append(cell_0)

        cell_1 = MxCell(self._get_next_id())
        cell_1.parent = cell_0.id
        mx_graph_model.append(cell_1)

        medallion = self._generate_medallion(template)
        medallion.cell.parent = cell_1.id
        mx_graph_model.append(medallion)

        return mx_graph_model

    def _generate_medallion(self, template: MedallionTemplate) -> MxObject:
        shape_information = ShapeInformation("medallion", template.height, template.width)
        shape = generate_encoded_shape(shape_information)

        style = (
            StyleBuilder()
            .html("1")
            .aspect("fixed")
            .collapsible("0")
            .connectable("0")
            .container("0")
            .allow_arrows("0")
            .resizable("0")
            .fill_color(template.shape_color)
            .shape(f"stencil({shape})")
            .build()
        )

        mx_object = MxObject(id=self._get_next_id(), label="", tooltip=template.title)

        mx_object.cell = MxCell(
            style=style,
            vertex=True,
            geometry=MxGeometry(
                width=template.width,
                height=template.height,
                alternateBounds=MxRectangle(width=template.width, height=template.height),
            ),
        )

        return mx_object
