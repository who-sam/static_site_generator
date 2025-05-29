import unittest
from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = text_node("This is a text node", text_type.bold)
        node2 = text_node("This is a text node", text_type.bold)
        self.assertEqual(node, node2)

    def test_neq_type(self):
        node1 = text_node("This is a text node", text_type.bold)
        node2 = text_node("This is a text node", text_type.code)
        self.assertNotEqual(node1, node2, msg="passed different type")

    def test_neq_text(self):
        node1 = text_node("This is a text node", text_type.code)
        node2 = text_node("this is different text", text_type.code)
        self.assertNotEqual(node1, node2, msg="passed different text")


#=============================================================
class TestTextToHtmlNode(unittest.TestCase):
    def test_normal(self):
        node = text_node("This is a text node", text_type.normal)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = text_node("This is a bold text node", text_type.bold)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = text_node("This is a italic text node", text_type.italic)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic text node")

    def test_code(self):
        node = text_node("This is a code text node", text_type.code)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_link(self):
        node = text_node("This is a link text node", text_type.link, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, {"href":"https://www.boot.dev"})

    def test_image(self):
        node = text_node("this an image", text_type.image, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src":"https://www.boot.dev", "alt":"this an image"}
        )

if __name__ == "__main__":
    unittest.main()

