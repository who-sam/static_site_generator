import unittest
from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node1 = html_node('p', "test text", None, None)
        node2 = html_node('p', "test text", None, None)
        self.assertEqual(node1, node2)

    def test_neq1(self):
        node1 = html_node('p', "test text", None, None)
        node2 = html_node('p', "another text", None, None)
        self.assertNotEqual(node1, node2)

    def test_neq2(self):
        node1 = html_node('p', "test text", None, None)
        node2 = html_node('a', "test text", None, None)
        self.assertNotEqual(node1, node2)

    def test_leaf_to_html_p(self):
        node = leaf_node("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p(self):
        node = leaf_node("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_no_tag(self):
        node = leaf_node(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_no_value(self):
        node = leaf_node("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_no_value_tag(self):
        node = leaf_node(None, None)
        with self.assertRaises(ValueError):
            node.to_html()




if __name__ == "__main__":
    unittest.main()
