from tkinter.filedialog import *


class Controller:
    def __init__(self):
        self.text_file_path = None

    def open_file(self):
        file_path = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        self.text_file_path = file_path
        return file_path

    def get_path_for_audio_file(self):
        f = asksaveasfilename(title="Select file", filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
        return f
