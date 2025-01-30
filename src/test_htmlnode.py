import unittest
import sys

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
  def test_eq(self):
    node = HTMLNode()
    node2 = HTMLNode()
    self.assertEqual(node, node2)
    self.assertEqual(node2.props, None)
    self.assertEqual(node.children, None)
  
  def test_repr(self):
    testchild = HTMLNode()
    testchild2 = HTMLNode()
    testchild3 = HTMLNode()
    testchild4 = HTMLNode()
    node = HTMLNode("p", "this is a paragraph", [testchild, testchild2, testchild3, testchild4], {"george": "is_curious", "grail":"not_found"})
    self.assertEqual(len(node.children), 4)

  def test_random(self):
    node = HTMLNode("p")
    node2 = HTMLNode(None , "what do you mean?")
    self.assertNotEqual(node, node2)

  def test_leaf(self):
    node = LeafNode("p", "look at this paragraph", {"laugh": "every_time"})
    self.assertIn("</p>", node.to_html())

  def test_parent(self):
    testchild = LeafNode("i", "italicized text")
    testchild2 = LeafNode("p", "a paragraph")
    testchild3 = LeafNode("a", "an image", {'href':'www.someimage.com'})
    testchild4 = LeafNode("b", "bolded text")
    node = ParentNode("h1", [testchild, testchild2, testchild3, testchild4], {"george": "is_curious", "grail":"not_found"})
    self.assertIn("</p><a", node.to_html())
