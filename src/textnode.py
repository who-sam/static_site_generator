from enum import Enum
from htmlnode import *


class TextType(Enum):
    TEXT = "TEXT"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    IMAGE = "IMAGE"


class TextNode:
    def __init__(self, text, TextType, url=None):
        self.text = text
        self.TextType = TextType
        self.url = url

    def __eq__(self,node):
        if (self.text == node.text) and (self.TextType == node.TextType) and (self.url == node.url):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.TextType.value}, {self.url})"






def TextNode_to_HTMLNode(TextNode):
    match TextNode.TextType:
        case TextType.TEXT:
            return LeafNode(None, TextNode.text)
        case TextType.BOLD:
            return LeafNode("b", TextNode.text)
        case TextType.ITALIC:
            return LeafNode("i", TextNode.text)
        case TextType.CODE:
            return LeafNode("code", TextNode.text)
        case TextType.LINK:
            return LeafNode("a", TextNode.text, {"href":TextNode.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src":TextNode.url , "alt":TextNode.text})

        case _:
            raise ValueError("ValueError: invalid text node type")
