import unittest

from textnode import TextNode, TextType
from md_to_text import split_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_images, split_nodes_links
from text_to_html import text_node_to_html_node

class TestMDToText(unittest.TestCase):
  def test_sd(self):
    node = TextNode("This is a text node with **bold** markdown", TextType.NORMAL)
    node1 = TextNode("This is a text node with *italic* markdown", TextType.NORMAL)
    node2 = TextNode("This is a text node with `code block` markdown", TextType.NORMAL)
    new_text = split_delimiter([node, node1, node2], "**", TextType.BOLD)
    self.assertEqual(len(new_text), 5)
    new_text = split_delimiter(new_text, "*", TextType.ITALIC)
    self.assertEqual(len(new_text), 7)
    new_text = split_delimiter(new_text, "`", TextType.CODE)
    self.assertEqual(len(new_text), 9)

  def test_regex(self):
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    images = extract_markdown_images(text)
    self.assertEqual(len(images), 2)
    text = "Here is a [link to somewhere](https://example.com) in a sentence"
    links = extract_markdown_links(text)
    self.assertEqual(len(links), 1)

  def test_image_extract(self):
    node = TextNode("This is text with an image ![alt](link)", TextType.NORMAL)
    node1 = TextNode("Start ![alt1](link1) middle ![alt2](link2) end", TextType.NORMAL)
    node2 = TextNode("This is text with no images at all.", TextType.NORMAL)
    node3 = TextNode("![alt](link)", TextType.NORMAL)
    node4 = TextNode("![alt1](link1)![alt2](link2)![alt3](link3)", TextType.NORMAL)
    node5 = TextNode("![img1](link1)text![img2](link2)![img3](link3)", TextType.NORMAL)
    old_nodes = [node, node1, node2, node3, node4, node5]
    new_nodes = split_nodes_images(old_nodes)

  def test_link_extract(self):
    node = TextNode("Here is a [link to Boot.dev](https://www.boot.dev) in the text.", TextType.NORMAL)
    node1 = TextNode("Start with a [link1](https://link1.com), then [link2](https://link2.com), and end.", TextType.NORMAL)
    node2 = TextNode("This text contains no links, it's just plain.", TextType.NORMAL)
    node3 = TextNode("[Boot.dev](https://www.boot.dev) is a great resource for programming.", TextType.NORMAL)
    node4 = TextNode("Find more information at [Boot.dev](https://www.boot.dev).", TextType.NORMAL)
    node5 = TextNode("[link1](https://link1.com)[link2](https://link2.com)[link3](https://link3.com)", TextType.NORMAL)
    old_nodes = [node, node1, node2, node3, node4, node5]
    new_nodes = split_nodes_links(old_nodes)
