import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq1(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("And this is not", "bold")
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("And this is not", "bold")
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("Inside the TextNode", text_type_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Inside the TextNode")

    def test_image(self):
        node = TextNode("Image", text_type_image, "https://gnu.org")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://gnu.org", "alt": "Image"},
        )

    def test_bold(self):
        node = TextNode("Bold text", text_type_bold)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")


if __name__ == "__main__":
    unittest.main()
