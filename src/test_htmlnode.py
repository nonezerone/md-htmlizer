import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello from HTMLNode!",
            None,
            {"class": "text", "href": "https://gnu.org"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="text" href="https://gnu.org"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I have no mouth but I must scream",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I have no mouth but I must scream",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "True and Real",
            None,
            {"class": "real"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, True and Real, children: None, {'class': 'real'})",
        )

    def test_leaf_to_html(self):
        node = LeafNode(
                "p",
                "Sample text",
                {"class": "alert", "href": "https://gnu.org"},
        )
        self.assertEqual(
            node.to_html(),
            '<p class="alert" href="https://gnu.org">Sample text</p>',
        )

    def test_leaf_to_html_no_props(self):
        node = LeafNode("div", "Sample text the Sequel")
        self.assertEqual(node.to_html(), "<div>Sample text the Sequel</div>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Sample text again!")
        self.assertEqual(node.to_html(), "Sample text again!")

    def test_leaf_attributes(self):
        node = LeafNode("div", "Just text", {"class": "text"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Just text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"class": "text"})

    def test_leaf_error(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
        node1 = ParentNode(
            "p",
            [],
        )
        self.assertEqual(node1.to_html(), "<p></p>")
        node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"class": "alert"},
        )
        node3 = ParentNode(
            "p",
            [
                node2
            ]
        )
        self.assertEqual(
            node3.to_html(),
            '<p><p class="alert"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>'
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
