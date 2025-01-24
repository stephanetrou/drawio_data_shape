from __future__ import annotations

from dataclasses import asdict
from typing import Any
from xml.etree import ElementTree as ET

from drawio_data_shape.mx.mxmodels import (
    MxCell,
    MxGeometry,
    MxGraphModel,
    MxObject,
    MxRectangle,
    UserObject,
    Visitor,
    has_default_value,
)


class XMLVisitor(Visitor):
    _hierarchy: list[ET.Element]

    def __init__(self):
        self._hierarchy = []

    def _append_hierarchical_element(self, element: ET.Element) -> None:
        """
        Append the element to the hierarchy and set it as the current element
        """
        if self._hierarchy:
            self._hierarchy[-1].append(element)

        self._hierarchy.append(element)

    def _pop_hierarchical_element(self) -> None:
        """
        Remove the current element from the hierarchy
        """
        if len(self._hierarchy) > 1:
            self._hierarchy.pop()

    @staticmethod
    def _create_element(key: str, value=None) -> ET.Element:
        """
        Create an XML element with the given key and value
        """
        element = ET.Element(key)

        if value is not None:
            element.text = str(value)

        return element

    @staticmethod
    def _add_attributes(element: ET.Element, visited: Any) -> None:
        for key, value in asdict(visited).items():
            if has_default_value(visited, key):
                continue

            if isinstance(value, bool):
                element.attrib[key] = "1" if value else "0"
            elif isinstance(value, str | int | float):
                element.attrib[key] = str(value)

    def visitMxGraphModel(self, mx_graph_model: MxGraphModel, **kwargs) -> None:
        xml_graph_model = XMLVisitor._create_element("mxGraphModel")
        self._append_hierarchical_element(xml_graph_model)

        xml_root = XMLVisitor._create_element("root")
        self._append_hierarchical_element(xml_root)

        for item in mx_graph_model.root:
            item.accept(self)

        self._pop_hierarchical_element()
        self._pop_hierarchical_element()

    def visitMxObject(self, mx_object: MxObject, **kwargs) -> None:
        xml_object = XMLVisitor._create_element("object")
        self._append_hierarchical_element(xml_object)

        XMLVisitor._add_attributes(xml_object, mx_object)
        if mx_object.cell is not None:
            mx_object.cell.accept(self)

        self._pop_hierarchical_element()

    def visitMxCell(self, mx_cell: MxCell, **kwargs) -> None:
        xml_cell = XMLVisitor._create_element("mxCell")

        self._append_hierarchical_element(xml_cell)

        XMLVisitor._add_attributes(xml_cell, mx_cell)

        if mx_cell.style is not None:
            styles = [f"{k}={'none' if v is None else v}" for k, v in mx_cell.style.items()]
            xml_cell.attrib["style"] = ";".join(styles)

        if mx_cell.geometry is not None:
            mx_cell.geometry.accept(self, _as="geometry")

        self._pop_hierarchical_element()

    def visitMxGeometry(self, mx_geometry: MxGeometry, **kwargs) -> None:
        xml_geometry = XMLVisitor._create_element("mxGeometry")
        self._append_hierarchical_element(xml_geometry)

        XMLVisitor._add_attributes(xml_geometry, mx_geometry)

        if "_as" in kwargs:
            xml_geometry.attrib["as"] = kwargs["_as"]

        if mx_geometry.alternateBounds is not None:
            mx_geometry.alternateBounds.accept(self, _as="alternateBounds")

        self._pop_hierarchical_element()

    def visitMxRectangle(self, mx_rectangle: MxRectangle, **kwargs) -> None:
        xml_rectangle = XMLVisitor._create_element("mxRectangle")
        self._append_hierarchical_element(xml_rectangle)

        XMLVisitor._add_attributes(xml_rectangle, mx_rectangle)
        if "_as" in kwargs:
            xml_rectangle.attrib["as"] = kwargs["_as"]

        self._pop_hierarchical_element()

    def visitUserModel(self, user_object: UserObject, **kwargs) -> None:
        xml_user_object = XMLVisitor._create_element("UserObject")
        self._append_hierarchical_element(xml_user_object)

        XMLVisitor._add_attributes(xml_user_object, user_object)
        if user_object.cell is not None:
            user_object.cell.accept(self)

        self._pop_hierarchical_element()

    def xml_str(self) -> str:
        return ET.tostring(self._hierarchy[0], encoding="unicode")
