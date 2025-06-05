import re
from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, TextType):
    new_nodes = []
    for node in old_nodes:
        if node.TextType != TextType.TEXT:
            new_nodes.append(node)
        else:
            splitted_node_text = node.text.split(delimiter)
            if len(splitted_node_text) % 2 == 0:
                print(splitted_node_text)
                raise Exception("Invalid MD Syntax: openning delimiter without closing it")
            for i in range(0,len(splitted_node_text)):
                if splitted_node_text[i] == "":
                    continue
                if i%2==0:
                    new_nodes.append(TextNode(splitted_node_text[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(splitted_node_text[i], TextType))
    return new_nodes



def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]+)\]\(([^\)\)]+)\)" ,text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]+)\]\(([^\)\)]+)\)" ,text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.TextType != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        images = extract_markdown_images(text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown: image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.TextType != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown: link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

