from textnode import TextNode, TextType

def main():
  dummy = TextNode("One woe doth tread upon another's heel, so fast they'll follow.", TextType.ITALIC, "https://shakespeare.mit.edu/hamlet/full.html")
  print(dummy)

main()