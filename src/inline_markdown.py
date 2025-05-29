from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type.normal:
            new_nodes.append(node)
        else:
            splitted_node_text = node.text.split(delimiter)
            if len(splitted_node_text) % 2 == 0:
                raise Exception("Invalid MD Syntax: openning delimiter without closing it")
            for i in range(0,len(splitted_node_text)):
                if splitted_node_text[i] == "":
                    continue
                if i%2==0:
                    new_nodes.append(text_node(splitted_node_text[i], text_type.normal))
                else:
                    new_nodes.append(text_node(splitted_node_text[i], text_type))

    return new_nodes



