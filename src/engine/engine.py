from src.engine.fetchers.text_fetcher import TextFetcher
from src.engine.audio_makers.gtts_audio_maker import GttsAudioMaker
from src.engine.audio_makers.pyttsx3_audio_maker import TTSX3AudioMaker

class Engine:
    def __init__(self):
        self.text_fetcher = TextFetcher()
        self.audio_maker = GttsAudioMaker()

    def fetch_text_from_path(self, path):
        return self.text_fetcher.fetch_from_path(path)

    def create_audio_file_from_text(self, text, path):
        self.audio_maker.create_audio_file_from_text(text, path)
