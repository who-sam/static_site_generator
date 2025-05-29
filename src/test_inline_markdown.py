import unittest
from inline_markdown import *

from textnode import text_node, text_type


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = text_node("This is text with a **bolded** word", text_type.normal)
        new_nodes = split_nodes_delimiter([node], "**", text_type.bold)
        self.assertListEqual(
            [
                text_node("This is text with a ", text_type.normal),
                text_node("bolded", text_type.bold),
                text_node(" word", text_type.normal),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = text_node(
            "This is text with a **bolded** word and **another**", text_type.normal
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type.bold)
        self.assertListEqual(
            [
                text_node("This is text with a ", text_type.normal),
                text_node("bolded", text_type.bold),
                text_node(" word and ", text_type.normal),
                text_node("another", text_type.bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = text_node(
            "This is text with a **bolded word** and **another**", text_type.normal
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type.bold)
        self.assertListEqual(
            [
                text_node("This is text with a ", text_type.normal),
                text_node("bolded word", text_type.bold),
                text_node(" and ", text_type.normal),
                text_node("another", text_type.bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = text_node("This is text with an _italic_ word", text_type.normal)
        new_nodes = split_nodes_delimiter([node], "_", text_type.italic)
        self.assertListEqual(
            [
                text_node("This is text with an ", text_type.normal),
                text_node("italic", text_type.italic),
                text_node(" word", text_type.normal),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = text_node("**bold** and _italic_", text_type.normal)
        new_nodes = split_nodes_delimiter([node], "**", text_type.bold)
        new_nodes = split_nodes_delimiter(new_nodes, "_", text_type.italic)
        self.assertListEqual(
            [
                text_node("bold", text_type.bold),
                text_node(" and ", text_type.normal),
                text_node("italic", text_type.italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = text_node("This is text with a `code block` word", text_type.normal)
        new_nodes = split_nodes_delimiter([node], "`", text_type.code)
        self.assertListEqual(
            [
                text_node("This is text with a ", text_type.normal),
                text_node("code block", text_type.code),
                text_node(" word", text_type.normal),
            ],
            new_nodes,
        )

    #===============================================================
    def test_extract_markdown_images_1(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_2(self):
        matches = extract_markdown_images(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_link_1(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link_2(self):
        matches = extract_markdown_links(
            "This is text with an ![link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()
