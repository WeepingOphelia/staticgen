
from htmlnode import LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from text_to_html import text_node_to_html_node
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown):
    nodes = []
    blocks = markdown_to_blocks(markdown)

    def text_to_children(text):
        text_nodes = text_to_textnodes(text)
        return [text_node_to_html_node(node) for node in text_nodes]

    for block in blocks:
        match block_to_block_type(block):
            case "heading":
                tag = f"h{len(block.split()[0])}"
                text = block.lstrip("#").strip()
                nodes.append(ParentNode(tag=tag, children = text_to_children(text)))
            case "quote":
                tag = "blockquote"
                text = block.lstrip(">").strip()

                nodes.append(ParentNode(tag=tag, children = text_to_children(text)))
            case "code":
                tag = "pre"
                tag1 = "code"
                text = block.strip("```").strip()
                nodes.append(ParentNode(tag=tag, children = [LeafNode(tag=tag1, value=text)]))
            case "unordered_list":
                tag = "ul"
                children = [ParentNode(tag="li", children = text_to_children(line.lstrip("*-").strip())) for line in block.split("\n") if line.lstrip("*-")]
                nodes.append(ParentNode(tag=tag, children=children))
            case "ordered_list":
                tag = "ol"
                children = [ParentNode(tag="li", children = text_to_children(line.lstrip("1234567890.").strip())) for line in block.split("\n")]
                nodes.append(ParentNode(tag=tag, children=children))
            case "paragraph":
                nodes.append(ParentNode(tag="p", children = text_to_children(block)))
    
    return ParentNode(tag="div", children=nodes)