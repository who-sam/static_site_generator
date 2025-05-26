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
        node2 = text_node("This is a text node", text_type.code)
        node3 = text_node("this is different text", text_type.code)
        self.assertNotEqual(node3, node2, msg="passed different text")

if __name__ == "__main__":
    unittest.main()
