from enum import Enum
from functools import reduce


class html_node:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        return reduce(lambda acc,item: acc+" "+f"{item[0]}=\"{item[1]}\"", self.props.items(), "")

    def __eq__(self,node):
        if (self.tag == node.tag) and (self.value == node.value) and (self.children == node.children) and (self.props == node.props):
            return True
        return False

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"



class leaf_node(html_node):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("invalid HTML: no value for a leaf node")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"



class parent_node(html_node):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("invalid HTML: no tag for a parent node")
        if self.children == None:
            raise ValueError("invalid HTML: no children for a parent node")


        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

        def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
