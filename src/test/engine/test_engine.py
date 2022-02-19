import unittest
from src.engine.engine import Engine
from pathlib import Path


AUDIO_FILE_NAME = "unit_test_audio_file.mp3"
AUDIO_FILE_PATH = Path(__file__).parent.resolve().joinpath(AUDIO_FILE_NAME)


class TestEngine(unittest.TestCase):

    def setUp(self):
        self.engine = Engine()

    def test_using_path_fetch_text(self):
        self.assertTrue(isinstance(
            self.engine.fetch_text_from_path("/Users/omry.zuta/IdeaProjects/text_to_audio/temp_input/test.txt"), str))

    @unittest.skip("problem in suites")
    def test_creating_file(self):
        self.engine.create_audio_file_from_text("test from unit test", AUDIO_FILE_NAME)
        self.assertTrue(Path(AUDIO_FILE_PATH).exists())

if __name__ == '__main__':
    unittest.main()
