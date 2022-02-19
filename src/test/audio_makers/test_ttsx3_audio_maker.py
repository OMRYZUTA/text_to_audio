import unittest
from src.engine.audio_makers.pyttsx3_audio_maker import TTSX3AudioMaker
import os
from pathlib import Path

AUDIO_FILE_NAME = "unit_test_audio_file.mp3"
AUDIO_FILE_PATH = Path(__file__).parent.resolve().joinpath(AUDIO_FILE_NAME)

class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

class TestTtsx3AudioMaker(TestCaseBase):
    def tearDown(self) -> None:
        file_path = AUDIO_FILE_PATH
        os.remove(file_path)

    # @unittest.skip("problem in suites")
    def test_creating_file(self):
        TTSX3AudioMaker().create_audio_file_from_text("test from unit test", AUDIO_FILE_NAME)
        self.assertTrue(Path(AUDIO_FILE_PATH).exists())


if __name__ == '__main__':
    unittest.main()