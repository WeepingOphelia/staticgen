import os
import shutil

from textnode import TextNode, TextType
from markdown_to_html import markdown_to_html_node

def main():
  dummy = TextNode("One woe doth tread upon another's heel, so fast they'll follow.", TextType.ITALIC, "https://shakespeare.mit.edu/hamlet/full.html")
  print(dummy)
  copy_directory("static", "public")
  generate_pages_recursive("content", "template.html", "public")

def copy_directory(source, destination):
  if os.path.exists(destination):
    shutil.rmtree(destination)
  os.mkdir(destination)
  for item in os.listdir(source):
    print(f"Copying {item}. . .")
    full_path = os.path.join(source, item)
    if os.path.isfile(full_path):
      shutil.copy(full_path, destination)
    else:
      copy_directory(full_path, os.path.join(destination, item))
    print(f"{item} copied.")

def extract_title(markdown):
  for line in markdown.split("\n"):
    if line.startswith("# "):
      return line.lstrip("#").strip()
    else:
      raise Exception("header not found!")
    
def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} using {template_path} to {dest_path} . . .")
  from_file = open(from_path)
  markdown = from_file.read()
  template_file = open(template_path)
  template = template_file.read()
  from_file.close()
  template_file.close()
  content = markdown_to_html_node(markdown).to_html()
  title = extract_title(markdown)
  template = template.replace("{{ Title }}", title)
  template = template.replace("{{ Content }}", content)
  if not os.path.exists(os.path.dirname(dest_path)):
    os.makedirs(os.path.dirname(dest_path))
  file = open(dest_path, "x")
  file.write(template)
  file.close()
  print("Page generated.")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  for item in os.listdir(dir_path_content):
    if len(item.split(".")) == 2 and item.split(".")[1] == "md":
      generate_page(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item.split(".")[0] + ".html"))
    elif os.path.isdir(os.path.join(dir_path_content, item)):
      generate_pages_recursive(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item))



main()