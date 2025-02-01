import unittest
from markdown_to_html import markdown_to_html_node


class TestMDToHTML(unittest.TestCase):
  def test_md_to_html(self):
    text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    self.assertIn("<h1>This is a heading</h1>", markdown_to_html_node(text).to_html())
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
    assert "<div>" in markdown_to_html_node(markdown_text).to_html()
    assert "<h1>" in markdown_to_html_node(markdown_text).to_html()
    assert "<h2>" in markdown_to_html_node(markdown_text).to_html()
    assert "<ul>" in markdown_to_html_node(markdown_text).to_html()
    assert "<ol>" in markdown_to_html_node(markdown_text).to_html()
    assert "<blockquote>" in markdown_to_html_node(markdown_text).to_html()
    assert "<pre>" in markdown_to_html_node(markdown_text).to_html()
    assert "<code>" in markdown_to_html_node(markdown_text).to_html()

    markdown_text = "> This is a **bold *italic* text** in a quote"

    self.assertEqual(markdown_to_html_node(markdown_text).to_html(), '<div><blockquote>This is a <b>bold *italic* text</b> in a quote</blockquote></div>')

    markdown_text = """> First paragraph
>
> Second paragraph"""

    self.assertEqual(markdown_to_html_node(markdown_text).to_html(), '<div><blockquote>First paragraph\n\nSecond paragraph</blockquote></div>')

    markdown_text = """* Normal item
* Item with **bold**
* Item with `code`"""

    self.assertEqual(markdown_to_html_node(markdown_text).to_html(), '<div><ul><li>Normal item</li><li>Item with <b>bold</b></li><li>Item with <code>code</code></li></ul></div>')