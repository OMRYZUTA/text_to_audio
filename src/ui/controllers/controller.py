from tkinter import PhotoImage
from tkinter.filedialog import *
import os
import sys


class Controller:
    def __init__(self):
        self.image_names = ["save", "open"]
        self.done_sound_name = 'done_sound.wav'
        self.image_name_per_image_path = self.build_image_dict()
        self.text_file_path = None


    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


    def open_file(self):
        file_path = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        self.text_file_path = file_path
        return file_path

    def get_path_for_audio_file(self):
        f = asksaveasfilename(title="Select file", filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
        return f

    def get_image(self, image_name):
        # return self.image_name_per_image_path[image_name]
        return self.resource_path(image_name + ".png") # delete later

    def build_image_dict(self):
        image_name_per_image_path = {}
        for image_name in self.image_names:
            image_path = self.resource_path(image_name + ".png")
            image_name_per_image_path[image_name] = PhotoImage(file=image_path)
        return image_name_per_image_path

    def get_done_sound_path(self):
        return "resources/sound_effects/" + self.done_sound_name
