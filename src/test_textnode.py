import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_noneurl(self):
        node = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertEqual(None, node.url)

    def test_diftype(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)
    
    def test_difurl(self):
        node = TextNode("This is a text node", TextType.LINK, "www.google.com")
        node2 = TextNode("This is a text node", TextType.LINK, "tl.net")
        self.assertNotEqual(node, node2)

    def test_diftext(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is also a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()