from functools import reduce

class HTMLNode():
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def __eq__(self, other):
    return (self.tag, self.value, self.children, self.props) == (other.tag, other.value, other.children, other.props)

  def __repr__(self):
    n = 0
    if self.children:
      n = len(self.children)
    return (
    f"""
======================
HTML NODE:
======================;
| Tag: {self.tag} 
----------------------
| Value: {self.value}
----------------------
| Children: {n}
----------------------
| Properties: {self.props}
======================"""
    )

  def to_html(self):
    raise NotImplementedError()
  
  def props_to_html(self):
    if not self.props:
      return ""
    props_html = []
    for key, value in self.props.items():
      props_html.append(f' {key}="{value}"')
    return "".join(props_html)
  

class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag=tag, value=value, props=props)

  def to_html(self):
    if not self.value:
      raise ValueError("leaf must have value")
    if not self.tag:
      return self.value
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, children=children, props=props)

  def to_html(self):
    if not self.tag:
      raise ValueError("parent must have tag")
    if not self.children:
      raise ValueError("parent must have child")
    sub_html = []
    for child in self.children:
      sub_html.append(child.to_html())
    return f"<{self.tag}{self.props_to_html()}>{"".join(sub_html)}</{self.tag}>"