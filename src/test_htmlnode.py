import unittest
from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node1 = html_node('p', "test text", None, None)
        node2 = html_node('p', "test text", None, None)
        self.assertEqual(node1, node2)
