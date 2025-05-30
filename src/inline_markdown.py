import re
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



def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]+)\]\(([^\)\)]+)\)" ,text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]+)\]\(([^\)\)]+)\)" ,text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type.normal:
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
                new_nodes.append(text_node(sections[0], text_type.normal))
            new_nodes.append(text_node(image[0], text_type.image, image[1]))
            text = sections[1]
        if text != "":
            new_nodes.append(text_node(text, text_type.normal))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type.normal:
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
                new_nodes.append(text_node(sections[0], text_type.normal))
            new_nodes.append(text_node(link[0], text_type.link, link[1]))
            text = sections[1]
        if text != "":
            new_nodes.append(text_node(text, text_type.normal))
    return new_nodes


def text_to_textnodes(text):
    nodes = [text_node(text, text_type.normal)]
    nodes = split_nodes_delimiter(nodes, "**", text_type.bold)
    nodes = split_nodes_delimiter(nodes, "_", text_type.italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type.code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

# text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
# print(text_to_textnodes(text))
node = text_node(
    "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
    text_type.normal,
)
new_nodes = split_nodes_link([node])
print(new_nodes)
