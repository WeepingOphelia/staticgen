
def block_to_block_type(block):
  if block.startswith("#") and len(block) - len(block.lstrip("#")) <= 6 and block.lstrip("#")[0] == " ":
    return "heading"
  elif block.startswith(">"):
    return "quote" if all(line.startswith(">") for line in block.split("\n")) else "paragraph"
  elif block.startswith("```") and block.endswith("```"):
    return "code"
  elif block.startswith("* ") or block.startswith("- "):
    return "unordered_list" if all(line.startswith("* ") or line.startswith("- ") for line in block.split("\n")) else "paragraph"
  elif block.startswith("1. "):
    i = 1
    for line in block.split("\n"):
      if line.startswith(f"{i}. "):
        i += 1
      else:
        return "paragraph"
    return "ordered_list"
  else:
    return "paragraph"

def markdown_to_blocks(markdown):
  return [block.strip() for block in markdown.split("\n\n") if block.strip()]

def markdown_to_blocks_legacy(markdown):
  blocks = markdown.split("\n\n")
  for i in range(len(blocks)):
    blocks[i] = blocks[i].strip()
  return list(filter(lambda x: x != "", blocks))