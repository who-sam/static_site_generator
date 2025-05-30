import unittest
from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq_type(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node1, node2, msg="passed different type")

    def test_neq_text(self):
        node1 = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("this is different text", TextType.CODE)
        self.assertNotEqual(node1, node2, msg="passed different text")


#=============================================================
class TestTextToHtmlNode(unittest.TestCase):
    def test_TEXT(self):
        node = TextNode("This is a text node", TextType.TEXT)
        HTMLNode = TextNode_to_HTMLNode(node)
        self.assertEqual(HTMLNode.tag, None)
        self.assertEqual(HTMLNode.value, "This is a text node")

    def test_BOLD(self):
        node = TextNode("This is a BOLD text node", TextType.BOLD)
        HTMLNode = TextNode_to_HTMLNode(node)
        self.assertEqual(HTMLNode.tag, "b")
        self.assertEqual(HTMLNode.value, "This is a BOLD text node")

    def test_ITALIC(self):
        node = TextNode("This is a ITALIC text node", TextType.ITALIC)
        HTMLNode = TextNode_to_HTMLNode(node)
        self.assertEqual(HTMLNode.tag, "i")
        self.assertEqual(HTMLNode.value, "This is a ITALIC text node")

    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        HTMLNode = TextNode_to_HTMLNode(node)
        self.assertEqual(HTMLNode.tag, "code")
        self.assertEqual(HTMLNode.value, "This is a code text node")

    def test_LINK(self):
        node = TextNode("This is a LINK text node", TextType.LINK, "https://www.boot.dev")
        HTMLNode = TextNode_to_HTMLNode(node)
        self.assertEqual(HTMLNode.tag, "a")
        self.assertEqual(HTMLNode.value, "This is a LINK text node")
        self.assertEqual(HTMLNode.props, {"href":"https://www.boot.dev"})

    def test_IMAGE(self):
        node = TextNode("this an IMAGE", TextType.IMAGE, "https://www.boot.dev")
        HTMLNode = TextNode_to_HTMLNode(node)
        self.assertEqual(HTMLNode.tag, "img")
        self.assertEqual(HTMLNode.value, "")
        self.assertEqual(
            HTMLNode.props,
            {"src":"https://www.boot.dev", "alt":"this an IMAGE"}
        )

if __name__ == "__main__":
    unittest.main()

