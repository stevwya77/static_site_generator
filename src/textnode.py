'''
'   textnode.py:
'   Intermediate to parsing Markdown and output to HTML
'''
from enum import Enum


'''
Types of text nodes
'''
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

'''
Main class for text node creation
'''
class TextNode:
    def __init__(self, text, text_type, url=None):
        # txt content of node
        self.text = text
        # type of txt node contains
        self.text_type = text_type
        # url of link or image if txt is link
        self.url = url

    '''
    Compares current node to another node, return true
    if all properties are equal.
    '''
    def __eq__(self, other) -> bool:
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    '''
    Returns string representation of node
    '''
    def __repr__(self) -> str:
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'