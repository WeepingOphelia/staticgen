

def markdown_to_blocks(markdown):
  blocks = markdown.split("\n\n")
  for i in range(len(blocks)):
    blocks[i] = blocks[i].strip()
    if blocks[i] == "\n" or blocks[i] == "":
      
  return blocks