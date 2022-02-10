from gtts import gTTS


class AudioMaker:
    def __init__(self):
        self.lang = 'en'
        self.tld = 'ca'

    def create_audio_file_from_text(self, txt, result_file_name):
        tts = gTTS(txt, lang=self.lang, tld=self.tld)
        tts.save(result_file_name)
