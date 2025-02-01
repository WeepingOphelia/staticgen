import re
from textnode import TextNode, TextType

def split_delimiter(old_nodes, delimiter, text_type):
  delimiter_dict = {"**": TextType.BOLD, "*": TextType.ITALIC, "`": TextType.CODE}
  if delimiter not in delimiter_dict:
    raise Exception("invalid delimiter")
  if delimiter_dict[delimiter] != text_type:
    raise Exception("invalid delimiter/text_type pair")
  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.NORMAL:
      new_nodes.append(node)
    else:
      new_text = []
      start = node.text.find(delimiter)
      if start != -1:
        end = node.text.find(delimiter, start + 1)
        if end == -1:
          raise Exception("invalid markdown syntax")
        i = len(delimiter)
        new_text = [node.text[:start], node.text[start + i:end], node.text[end + i:]]
        new_text_nodes = filter(lambda x: x.text, [TextNode(new_text[0], TextType.NORMAL), TextNode(new_text[1], text_type), TextNode(new_text[2], TextType.NORMAL)]) 
        new_nodes.extend(new_text_nodes)
      else:
        new_nodes.append(node)
  return new_nodes


def extract_markdown_images(text):
  # hits = re.findall(r"!\[.*?\]\(.*?\)", text)
  return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
  return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_images(old_nodes):
  new_nodes = []
  for node in old_nodes:
    images = extract_markdown_images(node.text)
    if len(images) == 0:
      new_nodes.append(node)
    elif len(images) == 1:
      text = node.text.split(f"![{images[0][0]}]({images[0][1]})", 1)
      if text[0] != "":
        new_nodes.append(TextNode(text[0], TextType.NORMAL))
      new_nodes.append(TextNode(images[0][0], TextType.IMAGE, images[0][1]))
      if text[1] != "":
        new_nodes.append(TextNode(text[1], TextType.NORMAL))
    else:
      text = node.text.split(f"![{images[0][0]}]({images[0][1]})")
      if text[0] != "":
        new_nodes.append(TextNode(text[0], TextType.NORMAL))
      new_nodes.append(TextNode(images[0][0], TextType.IMAGE, images[0][1]))
      new_nodes += split_nodes_images([TextNode(text[1], TextType.NORMAL)])
  return new_nodes

def split_nodes_links(old_nodes):
  new_nodes = []
  for node in old_nodes:
    links = extract_markdown_links(node.text)
    if len(links) == 0:
      new_nodes.append(node)
    elif len(links) == 1:
      text = node.text.split(f"[{links[0][0]}]({links[0][1]})", 1)
      if text[0] != "":
        new_nodes.append(TextNode(text[0], TextType.NORMAL))
      new_nodes.append(TextNode(links[0][0], TextType.LINK, links[0][1]))
      if text[1] != "":
        new_nodes.append(TextNode(text[1], TextType.NORMAL))
    else:
      text = node.text.split(f"[{links[0][0]}]({links[0][1]})")
      if text[0] != "":
        new_nodes.append(TextNode(text[0], TextType.NORMAL))
      new_nodes.append(TextNode(links[0][0], TextType.LINK, links[0][1]))
      new_nodes += split_nodes_links([TextNode(text[1], TextType.NORMAL)])
  return new_nodes
      