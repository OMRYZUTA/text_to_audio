from gtts import *

class AudioCreator:
    def create(file_path, result_file_name):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            txt = ''.join(lines)
            tts = gTTS(txt, lang='en', tld='ca')
            tts.save(result_file_name)