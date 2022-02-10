import unittest
from src.engine.audio_makers.audio_maker import AudioMaker
import os
import pathlib
AUDIO_FILE_NAME ="unit_test_audio_file.mp3"
AUDIO_FILE_PATH = pathlib.Path(__file__).parent.resolve().joinpath(AUDIO_FILE_NAME)


class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not pathlib.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))


class TestAudioMaker(TestCaseBase):

    def tearDown(self) -> None:
        file_path = AUDIO_FILE_PATH
        os.remove(file_path)

    def test_creating_file(self):
        AudioMaker().create_audio_file_from_text("test from unit test", AUDIO_FILE_NAME)
        self.assertIsFile(AUDIO_FILE_PATH)


if __name__ == '__main__':
    unittest.main()
