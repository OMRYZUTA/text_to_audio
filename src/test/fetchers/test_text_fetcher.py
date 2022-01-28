import unittest
from src.engine.fetchers.text_fetcher import TextFetcher


class ArgumentsParserTestCase(unittest.TestCase):
    def setUp(self):
        self.text_fetcher = TextFetcher()

    def test_using_path_fetch_text(self):
        self.assertTrue(isinstance(self.text_fetcher.fetch_from_path("temp_input/test.txt"), str))


if __name__ == '__main__':
    unittest.main()
