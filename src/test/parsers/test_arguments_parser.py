import sys
import unittest
from src.engine.parsers.ArgumentsParser import ArgumentsParser


class ArgumentsParserTestCase(unittest.TestCase):
    def setUp(self):
        self.argument_parser = ArgumentsParser()
        sys.argv.append("file1")
        sys.argv.append("file2")

    def test_using_parse_returns_two_items(self):
        self.assertEqual(2, len(self.argument_parser.parse()))


if __name__ == '__main__':
    unittest.main()
