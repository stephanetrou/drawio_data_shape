from approvaltests import verify_xml

from drawio_data_shape.library_models import AWSThemes, DatasourceTemplate
from drawio_data_shape.mx.mxmodels import MxCell, MxGeometry, MxGraphModel, MxRectangle, UserObject
from drawio_data_shape.mx.mxstyle import StyleBuilder
from drawio_data_shape.mx.xml_visitor import XMLVisitor
from drawio_data_shape.shape.color import COLOR
from drawio_data_shape.shape.datasource_container import DatasourceContainer


def test_mx_cell_empty():
    visitor = XMLVisitor()
    visitor.visitMxCell(MxCell(0))

    pretty_xml = visitor.xml_str()
    verify_xml(pretty_xml)


def test_mx_cell_parent():
    visitor = XMLVisitor()
    visitor.visitMxCell(MxCell(1, parent=0))

    pretty_xml = visitor.xml_str()
    verify_xml(pretty_xml)


def test_mx_geometry():
    visitor = XMLVisitor()
    visitor.visitMxGeometry(MxGeometry(height=12, width=15))

    pretty_xml = visitor.xml_str()
    verify_xml(pretty_xml)


def test_mx_rectangle():
    visitor = XMLVisitor()
    visitor.visitMxRectangle(MxRectangle(x=10, y=11, width=12, height=13))

    pretty_xml = visitor.xml_str()
    verify_xml(pretty_xml)


def test_mx_cell_with_geometry():
    visitor = XMLVisitor()
    visitor.visitMxCell(MxCell(2, geometry=MxGeometry(height=12, width=15)))

    pretty_xml = visitor.xml_str()
    verify_xml(pretty_xml)


def test_mx_cell_with_geometry_and_alternate_bounds():
    visitor = XMLVisitor()
    visitor.visitMxCell(MxCell(2, geometry=MxGeometry(height=12, width=15, alternateBounds=MxRectangle(x=10, y=11))))

    pretty_xml = visitor.xml_str()
    verify_xml(pretty_xml)


def test_user_object():
    visitor = XMLVisitor()
    visitor.visitUserModel(UserObject(id=1, label="Hello"))

    pretty_xml = visitor.xml_str()
    verify_xml(pretty_xml)


def test_user_object_with_mx_cell():
    visitor = XMLVisitor()
    visitor.visitUserModel(UserObject(id=1, label="Hello", cell=MxCell(2)))

    pretty_xml = visitor.xml_str()
    verify_xml(pretty_xml)


def test_simple_shape():
    graph_model = MxGraphModel()

    graph_model.append(MxCell(0))

    graph_model.append(MxCell(1, parent=0))

    style = (
        StyleBuilder()
        .rounded("1")
        .white_space("wrap")
        .html("1")
        .font_family("Verdana")
        .font_size("9")
        .stroke_color(None)
        .fill_color("#535C71")
        .font_color("#FFFFFF")
        .build()
    )

    geometry = MxGeometry(height=12, width=26)

    graph_model.append(MxCell(2, value="Hi !!", geometry=geometry, style=style, vertex=True, parent=1))

    xml_visitor = XMLVisitor()
    xml_visitor.visitMxGraphModel(graph_model)
    pretty_xml = xml_visitor.xml_str()

    verify_xml(pretty_xml)


def test_datasource_shape():
    template_detail = DatasourceTemplate("source S3", COLOR.SOURCE, "Source S3", AWSThemes.S3, "S3")

    container = DatasourceContainer()
    graph_model = container.build(template_detail)

    xml_visitor = XMLVisitor()
    xml_visitor.visitMxGraphModel(graph_model)
    pretty_xml = xml_visitor.xml_str()

    verify_xml(pretty_xml)
