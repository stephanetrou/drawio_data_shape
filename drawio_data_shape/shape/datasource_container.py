from drawio_data_shape.library_models import DatasourceTemplate, IconDatasource, ImageDatasource
from drawio_data_shape.models.shape import ShapeInformation, generate_encoded_shape
from drawio_data_shape.mx.mxmodels import MxCell, MxGeometry, MxGraphModel, MxObject, MxRectangle, UserObject
from drawio_data_shape.mx.mxstyle import StyleBuilder


class DatasourceContainer:
    def __init__(self):
        self.next_id = -1

    def _get_next_id(self):
        self.next_id += 1
        return self.next_id

    def build(self, template_detail: DatasourceTemplate) -> MxGraphModel:
        mx_graph_model = MxGraphModel()

        cell_0 = MxCell(self._get_next_id())
        mx_graph_model.append(cell_0)

        cell_1 = MxCell(self._get_next_id())
        cell_1.parent = cell_0.id
        mx_graph_model.append(cell_1)

        box = self._generate_box(template_detail)
        box.cell.parent = cell_1.id
        mx_graph_model.append(box)

        icons_container = self._generate_icons_container()
        icons_container.parent = box.id
        mx_graph_model.append(icons_container)

        link = self._generate_documentation()
        link.cell.parent = icons_container.id
        mx_graph_model.append(link)

        squad = self._generate_squad()
        squad.cell.parent = icons_container.id
        mx_graph_model.append(squad)

        git = self._generate_git_repository()
        git.cell.parent = icons_container.id
        mx_graph_model.append(git)

        label = self._generate_label(template_detail.placeholder)
        label.parent = box.id
        mx_graph_model.append(label)

        icon_datasource = self._generate_icon_datasource(template_detail.style)
        icon_datasource.parent = box.id
        mx_graph_model.append(icon_datasource)

        return mx_graph_model

    def _generate_icons_container(self) -> MxCell:
        geometry = MxGeometry(x=9, y=43.25, width=195, height=20)
        style = (
            StyleBuilder()
            .container("1")
            .collapsible("0")
            .movable("0")
            .connectable("0")
            .allow_arrows("0")
            .stroke_color("none")
            .fill_color("#FAFAFA")
            .expand("0")
            .resizable("0")
            .build()
        )

        cell = MxCell(id=self._get_next_id(), value="", style=style, geometry=geometry, vertex=True)

        return cell

    def _generate_box(self, template_detail: DatasourceTemplate) -> MxObject:
        shape_information = ShapeInformation("datasource", template_detail.height, template_detail.width)
        shape = generate_encoded_shape(shape_information)

        style = (
            StyleBuilder()
            .html("1")
            .aspect("fixed")
            .shadow("1")
            .container("1")
            .collapsible("0")
            .connectable("1")
            .fill_opacity("100")
            .fill_color(template_detail.shape_color)
            .shape(f"stencil({shape})")
            .build()
        )

        mx_object = MxObject(id=self._get_next_id(), label="", tooltip="")

        mx_object.cell = MxCell(
            style=style,
            vertex=True,
            geometry=MxGeometry(
                width=template_detail.width,
                height=template_detail.height,
                alternateBounds=MxRectangle(width=template_detail.width, height=template_detail.height),
            ),
        )

        return mx_object

    def _generate_documentation(self) -> UserObject:
        user_object = UserObject(
            id=self._get_next_id(), link="modify link", linkTarget="_blank", tooltip="Documentation", label=""
        )

        style = (
            StyleBuilder()
            .shape("image")
            .editable_css_rules(".*")
            .vertical_label_position("bottom")
            .label_background_color("default")
            .vertical_align("top")
            .aspect("fixed")
            .image_aspect("0")
            .image(
                "data:image/svg+xml,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0wLjUgLTAuNSAyNy45NDcgMjgiIGhlaWdodD0iMjgiIHdpZHRoPSIyNy45NDciPiYjeGE7CSAgPHN0eWxlIHR5cGU9InRleHQvY3NzIj4uc3QwIHsgc3RvcC1jb2xvcjogcmdiKDkxLCAxMTUsIDEzOSk7IH0gLnN0MSB7IHN0b3AtY29sb3I6IHJnYigzNCwgNTMsIDcyKTsgfSA8L3N0eWxlPiYjeGE7CTxkZWZzPiYjeGE7CQk8bGluZWFyR3JhZGllbnQgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHkyPSIyNS4yNjkiIHgyPSIyMy40NSIgeTE9IjMuNDc0IiB4MT0iMi4wMzQiIGlkPSJBIj4mI3hhOwkJCTxzdG9wIGNsYXNzPSJzdDAiLz4mI3hhOwkJCTxzdG9wIGNsYXNzPSJzdDEiIG9mZnNldD0iMSIvPiYjeGE7CQk8L2xpbmVhckdyYWRpZW50PiYjeGE7CTwvZGVmcz4mI3hhOwk8cGF0aCBmaWxsPSJ1cmwoI0EpIiBkPSJNMTIuMTg5IDIwLjk5MmMuMTQzLS4xNDQuMzEzLS4yNTcuNTAyLS4zMzJzLjM5LS4xMTEuNTkyLS4xMDVjLjQzOCAwIC43NjcuMjAxLjk4NS42MDIuMjkuMjkyLjQzOC42MzkuNDM4IDEuMDRzLS4xNDcuNzQ3LS40MzcgMS4wNGwtMi4wODEgMi4wMjNjLS43MTMuNzE4LTEuNTcgMS4yNzctMi41MTUgMS42NGE2Ljg0IDYuODQgMCAwIDEtMi43OS42MDJjLS45NjItLjAwMy0xLjkxMi0uMjA4LTIuNzktLjYwMi0uODc1LS4zNjQtMS42NzYtLjkxLTIuNDA2LTEuNjQtLjcwOS0uNjk5LTEuMjY3LTEuNTM3LTEuNjQtMi40NmE3LjQ1IDcuNDUgMCAwIDEtLjU0OC0yLjc5YzAtLjk0OC4xODItMS44NzguNTQ4LTIuNzg5cy45MS0xLjczMyAxLjY0LTIuNDYxbDQuMTU2LTQuMTAyYy43My0uNzMgMS41NS0xLjI3NyAyLjQ2LTEuNjQxYTcuMjUgNy4yNSAwIDAgMSAyLjg0NC0uNmMuOTQ4IDAgMS44NzguMiAyLjc5LjYuOTEyLjM2NiAxLjcxNS45MTIgMi40MDYgMS42NDFhMS40MiAxLjQyIDAgMCAxIC40MzggMS4wNGMwIC40MDEtLjE0NS43NDctLjQzNyAxLjAzOGExLjQyIDEuNDIgMCAwIDEtMS4wMzkuNDM4IDEuNDIgMS40MiAwIDAgMS0xLjAzOC0uNDM3Yy0uODQtLjkxLTEuODYtMS4zNjUtMy4wNjItMS4zNjVzLTIuMjQ0LjQ1NS0zLjExOCAxLjM2NWwtNC4xNTMgNC4xMDJjLS45MS44NC0xLjM2NSAxLjg2LTEuMzY1IDMuMDYzcy40NTUgMi4yNjEgMS4zNjUgMy4xNzNjLjg0Ljg3NSAxLjg2IDEuMzEzIDMuMDYzIDEuMzEzczIuMjQ0LS40MzcgMy4xMTktMS4zMTJsMi4wNzQtMi4wODF6bTEzLjAxNy0xOS4yNWMuNzI4LjY5MyAxLjI3NiAxLjQ5NSAxLjY0IDIuNDA2YTYuODQgNi44NCAwIDAgMSAuNjAyIDIuNzljMCAuOTQ5LS4yMDEgMS44NzgtLjYwMiAyLjc5LS4zNjQuODc1LS45MSAxLjY3Ny0xLjY0IDIuNDA2bC00LjEwMiA0LjFjLS43NjcuNzY3LTEuNjA1IDEuMzMtMi41MTcgMS42OTgtLjkwNC4zNjMtMS44NjguNTQ4LTIuODQyLjU0NmE3LjQ1IDcuNDUgMCAwIDEtMi43OS0uNTQ4Yy0uOTAxLS4zODMtMS43MDQtLjk2Mi0yLjM1Mi0xLjY5NmExLjM2IDEuMzYgMCAwIDEtLjQzNy0uOTgzYzAtLjQwMi4xNDUtLjc0Ny40MzgtMS4wNGExLjM2IDEuMzYgMCAwIDEgLjk4NS0uNDM3IDEuNDIgMS40MiAwIDAgMSAxLjAzOC40MzggMy44NSAzLjg1IDAgMCAwIDEuNDIzLjk4NSA0LjM5IDQuMzkgMCAwIDAgMy4zMzYgMGMuNTQ4LS4yMTkgMS4wNC0uNTQ4IDEuNDc3LS45ODVsNC4xNTYtNC4xNTZjLjg3NS0uODM4IDEuMzEzLTEuODU5IDEuMzEzLTMuMDYzcy0uNDM3LTIuMjU5LTEuMzEyLTMuMTcxYy0uODQtLjg3NS0xLjg2LTEuMzEyLTMuMDYyLTEuMzEycy0yLjI2MS40MzgtMy4xNzMgMS4zMTNsLTIuMDc1IDIuMDc3YTEuNDIgMS40MiAwIDAgMS0xLjAzOS40MzggMS40MiAxLjQyIDAgMCAxLTEuMDQtLjQzNyAxLjQyIDEuNDIgMCAwIDEtLjQzNy0xLjA0IDEuNDIgMS40MiAwIDAgMSAuNDM4LTEuMDM4bDIuMDc5LTIuMDgxYy43MjgtLjcyOCAxLjU0OS0xLjI3NiAyLjQ2LTEuNjRhNy4yNSA3LjI1IDAgMCAxIDIuODQyLS42Yy45NDggMCAxLjg3OC4yMDEgMi43OS42MDIuOTEuMzY0IDEuNzEzLjkxIDIuNDA2IDEuNjR6Ii8+JiN4YTs8L3N2Zz4=;"
            )
            .editable("1")
            .movable("1")
            .resizable("0")
            .rotatable("1")
            .deletable("1")
            .locked("0")
            .connectable("0")
            .allow_arrows("0")
            .expand("0")
            .meta_edit("0")
            .container("0")
            .build()
        )

        cell = MxCell(
            style=style,
            vertex=True,
            geometry=MxGeometry(x=7, y=5, width=10, height=10),
        )

        user_object.cell = cell

        return user_object

    def _generate_squad(self) -> UserObject:
        user_object = UserObject(id=self._get_next_id(), tooltip="Squad", label="")

        style = (
            StyleBuilder()
            .fill_color("#535C71")
            .stroke_color(None)
            .pointer_events("1")
            .align("center")
            .aspect("fixed")
            .connectable("0")
            .container("0")
            .allow_arrows("0")
            .resizable("0")
            .shape("mxgraph.cisco_safe.people_places_things_icons.icon9")
            .build()
        )

        cell = MxCell(
            style=style,
            vertex=True,
            geometry=MxGeometry(x=22.46, y=3.25, width=15, height=13.5),
        )

        user_object.cell = cell

        return user_object

    def _generate_git_repository(self) -> UserObject:
        user_object = UserObject(id=self._get_next_id(), link="Git link", linkTarget="_blank", tooltip="Git", label="")

        style = (
            StyleBuilder()
            .fill_color("#535C71")
            .stroke_color(None)
            .pointer_events("1")
            .align("center")
            .aspect("fixed")
            .connectable("0")
            .container("0")
            .allow_arrows("0")
            .resizable("0")
            .shape("mxgraph.azure.git_repository")
            .build()
        )

        cell = MxCell(
            style=style,
            vertex=True,
            geometry=MxGeometry(x=42, y=3.25, width=15, height=15),
        )

        user_object.cell = cell

        return user_object

    def _generate_label(self, placeholder) -> MxCell:
        style = (
            StyleBuilder()
            .html("1")
            .align("left")
            .vertical_align("middle")
            .white_space("wrap")
            .rounded("0")
            .font_style("0")
            .font_family("Tahoma")
            .font_size("12")
            .font_color("#535C71")
            .stroke_color("none")
            .movable("0")
            .connectable("0")
            .allow_arrows("0")
            .expand("0")
            .resizable("0")
            .build()
        )

        geometry = MxGeometry(x=40, y=6, width=164, height=20)

        cell = MxCell(id=self._get_next_id(), value=placeholder, style=style, geometry=geometry, vertex=True)
        return cell

    def _generate_icon_datasource(self, style_icon) -> MxCell:
        style = self._generate_style_icon(style_icon)
        geometry = MxGeometry(x=15, y=5, width=style_icon.width, height=style_icon.height)

        cell = MxCell(id=self._get_next_id(), value="", style=style.build(), geometry=geometry, vertex=True)
        return cell

    def _generate_style_icon(self, style_icon) -> StyleBuilder:
        if isinstance(style_icon, IconDatasource):
            return (
                StyleBuilder()
                .align("center")
                .allow_arrows("0")
                .aspect("fixed")
                .connectable("0")
                .expand("0")
                .fill_color(style_icon.shape_icon_color)
                .font_color("#232F3E")
                .font_size("12")
                .font_style("0")
                .html("1")
                .outline_connect("0")
                .recursive_resize("0")
                .res_icon(style_icon.shape_icon)
                .resizable("0")
                .shape(style_icon.shape_group_icon)
                .sketch("0")
                .stroke_color("#FFFFFF")
                .vertical_align("top")
                .vertical_label_position("bottom")
            )
        elif isinstance(style_icon, ImageDatasource):
            return (
                StyleBuilder()
                .align("center")
                .image_align("center")
                .allow_arrows("0")
                .aspect("fixed")
                .connectable("0")
                .expand("0")
                .font_size("12")
                .font_style("0")
                .html("1")
                .image(style_icon.image)
                .stroke_color("none")
                .outline_connect("0")
                .recursive_resize("0")
                .resizable("0")
            )
