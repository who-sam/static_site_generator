from enum import Enum
from htmlnode import *


class text_type(Enum):
    normal = "normal"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"


class text_node:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,node):
        if (self.text == node.text) and (self.text_type == node.text_type) and (self.url == node.url):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"






def text_node_to_html_node(text_node):
    match text_node.text_type:
        case text_type.normal:
            return leaf_node(None, text_node.text)
        case text_type.bold:
            return leaf_node("b", text_node.text)
        case text_type.italic:
            return leaf_node("i", text_node.text)
        case text_type.code:
            return leaf_node("code", text_node.text)
        case text_type.link:
            return leaf_node("a", text_node.text, {"href":text_node.url})
        case text_type.image:
            return leaf_node("img", "", {"src":text_node.url , "alt":text_node.text})

        case _:
            raise ValueError("ValueError: invalid text node type")
