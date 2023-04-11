import unittest
from markdown_to_html import markdown_to_html, convert_bold, convert_italic


class TestMarkdownToHTML(unittest.TestCase):
    def test_heading_conversion(self):
        self.assertEqual(markdown_to_html("# Heading 1"), "<h1>Heading 1</h1>")
        self.assertEqual(
            markdown_to_html("## Heading 2"), "<h2>Heading 2</h2>"
        )
        self.assertEqual(
            markdown_to_html("### Heading 3"), "<h3>Heading 3</h3>"
        )

    def test_bold_conversion(self):
        self.assertEqual(markdown_to_html("**bold text**"), "<b>bold text</b>")

    def test_italic_conversion(self):
        self.assertEqual(
            markdown_to_html("*italic text*"), "<i>italic text</i>"
        )

    def test_list_conversion(self):
        self.assertEqual(
            markdown_to_html("- List item 1"),
            "<ul>\n<li>List item 1</li>\n</ul>",
        )

    def test_link_conversion(self):
        self.assertEqual(
            markdown_to_html("[Google](https://www.google.com)"),
            '<a href="https://www.google.com">Google</a>',
        )

    def test_multiple_headings(self):
        input_md = "# Heading 1\n## Heading 2\n### Heading 3"
        expected_html = (
            "<h1>Heading 1</h1>\n<h2>Heading 2</h2>\n<h3>Heading 3</h3>"
        )
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_mixed_formatting(self):
        input_md = "This is a **bold and *italic* mix**."
        expected_html = "This is a <b>bold and <i>italic</i> mix</b>."
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_list_with_multiple_items(self):
        input_md = "- Item 1\n- Item 2\n- Item 3"
        expected_html = (
            "<ul>\n<li>Item 1</li>\n<li>Item 2</li>\n<li>Item 3</li>\n</ul>"
        )
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_no_conversion(self):
        input_md = "This is plain text."
        expected_html = "This is plain text."
        self.assertEqual(markdown_to_html(input_md), expected_html)

    def test_empty_input(self):
        self.assertEqual(markdown_to_html(""), "")

    def test_convert_bold_trailing_space(self):
        self.assertEqual(
            convert_bold("This is **bold text**and more."),
            "This is <b>bold text</b>and more.",
        )

    def test_convert_italic_trailing_space(self):
        self.assertEqual(
            convert_italic("This is *italic text*and more."),
            "This is <i>italic text</i>and more.",
        )


if __name__ == "__main__":
    unittest.main()
