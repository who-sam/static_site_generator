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
