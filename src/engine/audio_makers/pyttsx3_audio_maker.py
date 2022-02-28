import pyttsx3

class TTSX3AudioMaker:
    def __init__(self):
        self.engine = pyttsx3.init(driverName='nsss')

    def create_audio_file_from_text(self, txt, result_file_name):
        self.engine.setProperty('rate', 150)
        self.engine.save_to_file(txt, result_file_name)
        self.engine.runAndWait()

