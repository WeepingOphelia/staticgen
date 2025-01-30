import unittest

from markdown_to_blocks import markdown_to_blocks



class TestMDToBlocks(unittest.TestCase):
  def test_md_to_blocks(self):
    text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    print(markdown_to_blocks(text))
    