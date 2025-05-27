import unittest
from htmlnode import *

class TestHtmlNode(unittest.TestCase):

    #========== testing html_node class ==========
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


    #========== testing leaf_node class ==========
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


    #========== testing parent_node class ==========
    def test_to_html_with_no_children(self):
        parent_nod = parent_node("div", None)
        with self.assertRaises(ValueError):
            parent_nod.to_html()
    
    def test_to_html_with_children_with_no_value(self):
        child_nod = leaf_node(None, None)
        parent_nod = parent_node("div", [child_nod])
        with self.assertRaises(ValueError) as m:
            parent_nod.to_html()
        self.assertEqual(str(m.exception), "invalid HTML: no value for a leaf node")
    
    def test_to_html_with_children(self):
        child_nod = leaf_node("span", "child")
        parent_nod = parent_node("div", [child_nod])
        self.assertEqual(parent_nod.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_nod = leaf_node("b", "grandchild")
        child_nod = parent_node("span", [grandchild_nod])
        parent_nod = parent_node("div", [child_nod])
        self.assertEqual(
            parent_nod.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_many_children(self):
        node = parent_node(
            "p",
            [
                leaf_node("b", "Bold text"),
                leaf_node(None, "Normal text"),
                leaf_node("i", "italic text"),
                leaf_node(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = parent_node(
            "h2",
            [
                leaf_node("b", "Bold text"),
                leaf_node(None, "Normal text"),
                leaf_node("i", "italic text"),
                leaf_node(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
