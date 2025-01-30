import unittest

from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
  def test_text_to_text_nodes(self):
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(text_to_textnodes(text))