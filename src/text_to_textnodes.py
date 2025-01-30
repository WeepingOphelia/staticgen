from md_to_text import *
from textnode import TextType, TextNode

def text_to_textnodes(text):
  processed = split_nodes_images([TextNode(text, TextType.NORMAL)])
  processed = split_nodes_links(processed)
  processed = split_delimiter(processed, "**", TextType.BOLD)
  processed = split_delimiter(processed, "*", TextType.ITALIC)
  processed = split_delimiter(processed, "`", TextType.CODE)
  return processed