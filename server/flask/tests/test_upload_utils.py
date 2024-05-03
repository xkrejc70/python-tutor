import unittest
from app.uploads.upload_utils import to_camel_case

class TestToCamelCase(unittest.TestCase):
    def test_basic_conversion(self):
        self.assertEqual(to_camel_case("hello_world"), "helloWorld")

    def test_multiple_underscores(self):
        self.assertEqual(to_camel_case("hello__world"), "helloWorld")

    def test_capital_letters(self):
        self.assertEqual(to_camel_case("Hello World"), "helloWorld")

    def test_special_characters(self):
        self.assertEqual(to_camel_case("!hello@world#"), "helloWorld")

    def test_empty_string(self):
        self.assertEqual(to_camel_case(""), "")

    def test_single_word(self):
        self.assertEqual(to_camel_case("hello"), "hello")

    def test_whitespace(self):
        self.assertEqual(to_camel_case("  hello  world  "), "helloWorld")

if __name__ == '__main__':
    unittest.main()
