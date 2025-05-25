from enum import Enum


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

