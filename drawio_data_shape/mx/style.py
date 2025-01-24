from __future__ import annotations

from enum import StrEnum


class StyleName(StrEnum):
    # Alignment and Positioning
    ALIGN = "align"
    IMAGE_ALIGN = "imageAlign"
    VERTICAL_ALIGN = "verticalAlign"
    VERTICAL_LABEL_POSITION = "verticalLabelPosition"

    # Appearance
    ASPECT = "aspect"
    FILL_COLOR = "fillColor"
    FILL_OPACITY = "fillOpacity"
    IMAGE = "image"
    IMAGE_ASPECT = "imageAspect"
    LABEL_BACKGROUND_COLOR = "labelBackgroundColor"
    SKETCH = "sketch"
    STROKE_COLOR = "strokeColor"

    # Behavior
    ALLOW_ARROWS = "allowArrows"
    COLLAPSIBLE = "collapsible"
    CONNECTABLE = "connectable"
    CONTAINER = "container"
    DELETABLE = "deletable"
    EDITABLE = "editable"
    EDITABLE_CSS_RULES = "editableCssRules"
    EXPAND = "expand"
    LOCKED = "locked"
    META_EDIT = "metaEdit"
    MOVABLE = "movable"
    POINTER_EVENTS = "pointerEvents"
    RESIZABLE = "resizable"
    ROTATABLE = "rotatable"

    # Miscellaneous
    HTML = "html"
    ROUNDED = "rounded"
    SHAPE = "shape"
    WHITE_SPACE = "whiteSpace"
    TEXT = "text"
    FONT_STYLE = "fontStyle"
    FONT_FAMILY = "fontFamily"
    FONT_SIZE = "fontSize"
    FONT_COLOR = "fontColor"
    MOVABLE_LABEL = "movableLabel"
    NO_LABEL = "noLabel"
    OVERFLOW = "overflow"
    TEXT_SHADOW = "textShadow"
    SHADOW = "shadow"
    ROTATION = "rotation"
    TREE_FOLDING = "treeFolding"
    TREE_MOVING = "treeMoving"
    ENUMERATE = "enumerate"
    COMIC = "comic"
    OUTLINE_CONNECT = "outlineConnect"
    RECURSIVE_RESIZE = "recursiveResize"
    RES_ICON = "resIcon"


class StyleBuilder:
    def __init__(self):
        self.styles = {}

    def set_style(self, name: StyleName, value: None | str) -> StyleBuilder:
        self.styles[name.value] = value
        return self

    def build(self) -> dict[str, None | str]:
        return self.styles

    def align(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.ALIGN, value)

    def image_align(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.IMAGE_ALIGN, value)

    def vertical_align(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.VERTICAL_ALIGN, value)

    def vertical_label_position(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.VERTICAL_LABEL_POSITION, value)

    def aspect(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.ASPECT, value)

    def editable(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.EDITABLE, value)

    def fill_color(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.FILL_COLOR, value)

    def fill_opacity(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.FILL_OPACITY, value)

    def image(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.IMAGE, value)

    def image_aspect(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.IMAGE_ASPECT, value)

    def label_background_color(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.LABEL_BACKGROUND_COLOR, value)

    def sketch(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.SKETCH, value)

    def stroke_color(self, value: None | str) -> StyleBuilder:
        return self.set_style(StyleName.STROKE_COLOR, value)

    def allow_arrows(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.ALLOW_ARROWS, value)

    def collapsible(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.COLLAPSIBLE, value)

    def connectable(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.CONNECTABLE, value)

    def container(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.CONTAINER, value)

    def deletable(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.DELETABLE, value)

    def editable_css_rules(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.EDITABLE_CSS_RULES, value)

    def expand(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.EXPAND, value)

    def locked(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.LOCKED, value)

    def meta_edit(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.META_EDIT, value)

    def movable(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.MOVABLE, value)

    def pointer_events(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.POINTER_EVENTS, value)

    def resizable(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.RESIZABLE, value)

    def rotatable(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.ROTATABLE, value)

    def html(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.HTML, value)

    def rounded(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.ROUNDED, value)

    def shape(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.SHAPE, value)

    def white_space(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.WHITE_SPACE, value)

    def text(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.TEXT, value)

    def font_style(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.FONT_STYLE, value)

    def font_family(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.FONT_FAMILY, value)

    def font_size(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.FONT_SIZE, value)

    def font_color(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.FONT_COLOR, value)

    def movable_label(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.MOVABLE_LABEL, value)

    def no_label(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.NO_LABEL, value)

    def overflow(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.OVERFLOW, value)

    def text_shadow(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.TEXT_SHADOW, value)

    def shadow(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.SHADOW, value)

    def rotation(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.ROTATION, value)

    def tree_folding(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.TREE_FOLDING, value)

    def tree_moving(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.TREE_MOVING, value)

    def enumerate(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.ENUMERATE, value)

    def comic(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.COMIC, value)

    def outline_connect(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.OUTLINE_CONNECT, value)

    def recursive_resize(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.RECURSIVE_RESIZE, value)

    def res_icon(self, value: str) -> StyleBuilder:
        return self.set_style(StyleName.RES_ICON, value)
