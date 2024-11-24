from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field, fields


@dataclass
class MxRectangle:
    x: None | float = None
    y: None | float = None
    width: None | float = None
    height: None | float = None

    def accept(self, visitor: Visitor, **kwargs):
        visitor.visitMxRectangle(self, **kwargs)


@dataclass
class MxGeometry:
    x: None | float = None
    y: None | float = None
    width: None | float = None
    height: None | float = None
    alternateBounds: None | MxRectangle = None

    def accept(self, visitor: Visitor, **kwargs):
        visitor.visitMxGeometry(self, **kwargs)


@dataclass
class UserObject:
    id: None | int = None
    cell: MxCell = None
    label: None | str = None
    tooltip: None | str = None
    link: None | str = None
    linkTarget: None | str = None

    def accept(self, visitor: Visitor, **kwargs):
        visitor.visitUserModel(self, **kwargs)


@dataclass
class MxCell:
    id: None | int = None
    value: None | str | UserObject = None
    geometry: None | MxGeometry = None
    style: None | dict[str, str | None] = None
    vertex: None | bool = False
    edge: None | bool = False
    connectable: None | bool = True
    visible: None | bool = True
    collapsed: None | bool = False
    parent: None | int = None
    source: None | int = None
    target: None | int = None
    children: None | list[int] = None
    edges: None | list[int] = None

    def accept(self, visitor: Visitor, **kwargs):
        visitor.visitMxCell(self, **kwargs)


@dataclass
class MxObject:
    id: int
    cell: None | MxCell = None
    label: None | str = None
    value: None | str = None
    tooltip: None | str = None

    def accept(self, visitor: Visitor):
        visitor.visitMxObject(self)


@dataclass
class MxGraphModel:
    root: list[MxCell | MxObject | UserObject] = field(default_factory=list)

    def append(self, item: MxCell | MxObject | UserObject):
        self.root.append(item)

    def accept(self, visitor: Visitor, **kwargs):
        visitor.visitMxGraphModel(self, **kwargs)


def has_default_value(instance, field_name):
    field_info = next(f for f in fields(instance) if f.name == field_name)
    default_value = field_info.default
    current_value = getattr(instance, field_name)
    return current_value == default_value


class Visitor(ABC):
    @abstractmethod
    def visitMxGraphModel(self, mx_graph_model: MxGraphModel, **kwargs) -> None:
        pass

    @abstractmethod
    def visitMxCell(self, mx_cell: MxCell, **kwargs) -> None:
        pass

    @abstractmethod
    def visitMxGeometry(self, mx_geometry: MxGeometry, **kwargs) -> None:
        pass

    @abstractmethod
    def visitUserModel(self, user_object: UserObject, **kwargs) -> None:
        pass

    @abstractmethod
    def visitMxRectangle(self, mx_rectangle: MxRectangle, **kwargs) -> None:
        pass

    @abstractmethod
    def visitMxObject(self, mx_object: MxObject, **kwargs) -> None:
        pass
