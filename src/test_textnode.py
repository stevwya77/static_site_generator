import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_types(self):
        node = TextNode("This is a text node", TextType.TEXT)
        test = 'TextNode(This is a text node, text, None)'
        self.assertEqual(str(node), test)

        node2 = TextNode("This is a bold node", TextType.BOLD)
        test2 = 'TextNode(This is a bold node, bold, None)'
        self.assertEqual(str(node2), test2)

        node3 = TextNode("This is a italic node", TextType.ITALIC)
        test3 = 'TextNode(This is a italic node, italic, None)'
        self.assertEqual(str(node3), test3)
        
        node4 = TextNode("This is a code node", TextType.CODE)
        test4 = 'TextNode(This is a code node, code, None)'
        self.assertEqual(str(node4), test4)

        node5 = TextNode("This is a link node", TextType.LINK)
        test5 = 'TextNode(This is a link node, link, None)'
        self.assertEqual(str(node5), test5)

        node6 = TextNode("This is a image node", TextType.IMAGE)
        test6 = 'TextNode(This is a image node, image, None)'
        self.assertEqual(str(node6), test6)

    def test_url_none(self):
        node = TextNode("Testing url as none", TextType.LINK, "None")
        node2 = TextNode("Testing url as none", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_type_different(self):
        node = TextNode("Testing text type different", TextType.LINK)
        node2 = TextNode("Testing text type different", TextType.BOLD)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()