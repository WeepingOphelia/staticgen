import unittest
from markdown_to_htmlnodes import markdown_to_html_node


class TestMDToHTML(unittest.TestCase):
  def test_md_to_html(self):
    print("Hello")
    text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    # self.assertEqual(markdown_to_html_node(text), "<h1>This is a heading</h1>\n<p>This is a paragraph of text. It has some <strong>bold</strong> and <em>italic</em> words inside of it.</p>\n<ul>\n<li>This is the first list item in a list block</li>\n<li>This is a list item</li>\n<li>This is another list item</li>\n</ul>")
    markdown_text = """# My Heading

This is a **bold** paragraph with some *italic* text.

## Second Heading

* List item 1
* List item 2
* List item **3**

1. First ordered item
2. Second ordered item
3. Third *ordered* item

> This is a blockquote
> with multiple lines

```python
def hello():
    print("world")```
"""
    for child in markdown_to_html_node(markdown_text).children:
        print(child.children)