import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_html import text_node_to_html_node

class TestTextToHTML(unittest.TestCase):
  def test_text_node_to_html_node(self):
      text_node = TextNode("Hello, world!", TextType.NORMAL)
      html_node = text_node_to_html_node(text_node)
      assert html_node.tag == None
      assert html_node.value == "Hello, world!"
      print("test complete")