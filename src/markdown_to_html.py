from markdown_blocks import *
from htmlnode import *
from textnode import *
from inline_markdown import *


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        if block_to_block_type(block) == BlockType.PARAGRAPH:
            nodes.append(paragraph_to_html(block))
        if block_to_block_type(block) == BlockType.HEADING:
            nodes.append(heading_to_html(block))
        if block_to_block_type(block) == BlockType.CODE:
            nodes.append(code_to_html(block))
        if block_to_block_type(block) == BlockType.QUOTE:
            nodes.append(quotes_to_html(block))
        if block_to_block_type(block) == BlockType.ULIST:
            nodes.append(ulist_to_markdown(block))
        if block_to_block_type(block) == BlockType.OLIST:
            nodes.append(olist_to_markdown(block))
    return ParentNode("div", nodes)


















#==================== implemented ====================
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = list(map(TextNode_to_HTMLNode, text_nodes))
    return children
   

def paragraph_to_html(block):
    formatted = " ".join(block.split("\n"))
    child_nodes = text_to_children(formatted)
    return ParentNode("p", child_nodes)


def heading_to_html(block):
    block_text = block.split("# ")[-1]
    child_nodes = text_to_children(block_text)
    if block.startswith("# "):
        tag = "h1"
    elif block.startswith("## "):
        tag = "h2"
    elif block.startswith("### "):
        tag = "h3"
    elif block.startswith("#### "):
        tag = "h4"
    elif block.startswith("##### "):
        tag = "h5"
    elif block.startswith("###### "):
        tag = "h6"
    else:
        raise ValueError("invalid heading")
    return ParentNode(tag, child_nodes)


def ulist_to_markdown(block):
    lines = block.split("\n")
    text_lines = list(map(lambda x: x[2:], lines))
    item_nodes = []
    for line in text_lines:
        line_childs = text_to_children(line)
        item_nodes.append(ParentNode("li", line_childs))
    return ParentNode("ul", item_nodes)


def olist_to_markdown(block):
    lines = block.split("\n")
    text_lines = list(map(lambda x: x[3:], lines))
    item_nodes = []
    for line in text_lines:
        line_childs = text_to_children(line)
        item_nodes.append(ParentNode("li", line_childs))
    return ParentNode("ol", item_nodes)


def quotes_to_html(block):
    lines = block.split("\n")
    text_lines = list(map(lambda line: line.lstrip(">").strip(), lines))
    # childs = []
    # for line in text_lines:
    #     line_childs = text_to_children(line)
    content = " ".join(text_lines)
    childs = text_to_children(content)   #     item_nodes.extend(childs)
    return ParentNode("blockquote", childs)


def code_to_html(block):
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = TextNode_to_HTMLNode(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

