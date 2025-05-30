import unittest
from htmlnode import *

class TestHtmlNode(unittest.TestCase):

    #========== testing HTMLNode class ==========
    def test_eq(self):
        node1 = HTMLNode('p', "test text", None, None)
        node2 = HTMLNode('p', "test text", None, None)
        self.assertEqual(node1, node2)

    def test_neq1(self):
        node1 = HTMLNode('p', "test text", None, None)
        node2 = HTMLNode('p', "another text", None, None)
        self.assertNotEqual(node1, node2)

    def test_neq2(self):
        node1 = HTMLNode('p', "test text", None, None)
        node2 = HTMLNode('a', "test text", None, None)
        self.assertNotEqual(node1, node2)


    #========== testing LeafNode class ==========
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_no_value_tag(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()


    #========== testing ParentNode class ==========
    def test_to_html_with_no_children(self):
        parent_nod = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_nod.to_html()
    
    def test_to_html_with_children_with_no_value(self):
        child_nod = LeafNode(None, None)
        parent_nod = ParentNode("div", [child_nod])
        with self.assertRaises(ValueError) as m:
            parent_nod.to_html()
        self.assertEqual(str(m.exception), "invalid HTML: no value for a leaf node")
    
    def test_to_html_with_children(self):
        child_nod = LeafNode("span", "child")
        parent_nod = ParentNode("div", [child_nod])
        self.assertEqual(parent_nod.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_nod = LeafNode("b", "grandchild")
        child_nod = ParentNode("span", [grandchild_nod])
        parent_nod = ParentNode("div", [child_nod])
        self.assertEqual(
            parent_nod.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "BOLD text"),
                LeafNode(None, "TEXT text"),
                LeafNode("i", "ITALIC text"),
                LeafNode(None, "TEXT text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>BOLD text</b>TEXT text<i>ITALIC text</i>TEXT text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "BOLD text"),
                LeafNode(None, "TEXT text"),
                LeafNode("i", "ITALIC text"),
                LeafNode(None, "TEXT text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>BOLD text</b>TEXT text<i>ITALIC text</i>TEXT text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
