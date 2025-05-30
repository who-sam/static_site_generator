import unittest
from markdown_blocks import *


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **BOLDed** paragraph

This is another paragraph with _ITALIC_ text and `CODE` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **BOLDed** paragraph",
                "This is another paragraph with _ITALIC_ text and `CODE` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **BOLDed** paragraph




This is another paragraph with _ITALIC_ text and `CODE` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **BOLDed** paragraph",
                "This is another paragraph with _ITALIC_ text and `CODE` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )



class TestBlockToBlockType(unittest.TestCase):
#====================================================================================
    def test_block_to_block_type_paragraph(self):
        block = """
normal paragraph
another line
-hay you
"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
#====================================================================================
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
# #====================================================================================



if __name__ == "__main__":
    unittest.main()

