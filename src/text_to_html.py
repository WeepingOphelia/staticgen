from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def text_node_to_html_node(text_node):
  match text_node.text_type:
    case TextType.NORMAL:
      return LeafNode(None, text_node.text)
    case TextType.BOLD:
      return LeafNode("b", text_node.text)
    case TextType.ITALIC:
      return LeafNode("i", text_node.text)
    case TextType.CODE:
      return LeafNode("code", text_node.text)
    case TextType.LINK:
      return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
    case TextType.IMAGE:
      return LeafNode("img", "poop", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})