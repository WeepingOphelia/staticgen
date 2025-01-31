import unittest

from markdown_to_blocks import markdown_to_blocks, block_to_block_type



class TestMDToBlocks(unittest.TestCase):
  def test_md_to_blocks(self):
    text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    self.assertEqual(markdown_to_blocks(text), ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"])

  def test_block_to_block_type(self):
    text = """
# This is a heading

> This is a quote

```python\nprint('Hello, World!')\n```

* This is a list item

1. This is a numbered list item

This is a paragraph

    """
    blocks = markdown_to_blocks(text)
    self.assertEqual(block_to_block_type(blocks[0]), "heading")
    self.assertEqual(block_to_block_type("# This is a heading"), "heading")
    self.assertEqual(block_to_block_type("> This is a quote"), "quote")
    self.assertEqual(block_to_block_type("```python\nprint('Hello, World!')\n```"), "code")
    self.assertEqual(block_to_block_type("* This is a list item"), "unordered_list")
    self.assertEqual(block_to_block_type("1. This is a numbered list item"), "ordered_list")
    self.assertEqual(block_to_block_type("This is a paragraph"), "paragraph")