'''
'   htmlnode.py:
'   Node in HTML document tree, outputs HTML
'''

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # tag name
        self.tag = tag
        # value of tag
        self.value = value
        # list of node children 
        self.children = children
        # key-value pairs of tag attributes
        self.props = props

    '''
    Render as HTML
    '''
    def to_html(self):
        raise NotImplementedError("Child classes will override this method to render themselves as HTML.")
        
    '''
    Returns formatted string representing node 
    html attributes
    '''
    def props_to_html(self) -> str:
        result = ""
        if self.props:
            for key, value in self.props.items():
                result += f' {key}="{value}"'
        return result
    
    '''
    Returns string representation of node properties
    '''
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
'''
HTML tag node with no children
'''
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value)
        self.props = props
    
    def to_html(self) -> str:
        if not self.value:
            raise ValueError("No value for child found. All leaf nodes must have a value.")
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        super().__repr__(self)
        return f'LeafNode({self.tag}, {self.value}, {self.props})'