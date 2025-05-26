# test_static_site_generator.py
import unittest
from static_site_generator import text_to_html_nodes

class TestTextToHtmlNodes(unittest.TestCase):

    def test_single_line(self):
        # Arrange
        input_text = "Hello, world!"
        expected_output = "<p>Hello, world!</p>"

        # Act
        result = text_to_html_nodes(input_text)

        # Assert
        self.assertEqual(result, expected_output)

    def test_multiple_lines(self):
        # Arrange
        input_text = "Line one\nLine two\nLine three"
        expected_output = "<p>Line one</p>\n<p>Line two</p>\n<p>Line three</p>"

        # Act
        result = text_to_html_nodes(input_text)

        # Assert
        self.assertEqual(result, expected_output)

    def test_empty_lines_ignored(self):
        # Arrange
        input_text = "Line one\n\nLine two\n   \nLine three"
        expected_output = "<p>Line one</p>\n<p>Line two</p>\n<p>Line three</p>"

        # Act
        result = text_to_html_nodes(input_text)

        # Assert
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main():
