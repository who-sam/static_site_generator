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

    def __repr__(self):
        return f"tag = {self.tag}\nvalue = {self.value}\nchildren = {self.children}\nprops = {props_to_html(self)}"

    def __eq__(self,node):
        if (self.tag == node.tag) and (self.value == node.value) and (self.children == node.children) and (self.props == node.props):
            return True
        return False



class leaf_node(html_node):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class 
