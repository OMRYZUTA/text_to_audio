from tkinter import *
from src.ui.controllers.controller import Controller
from src.engine.engine import Engine
import threading
class DesktopUI:
    def __init__(self):
        self.engine = Engine()
        self.root = Tk()
        self.controller = Controller()
        self.build_toolbar()
        self.text = StringVar()
        self.text_file_path = StringVar()
        self.build_main_frame()
        self.build_menu()
        self.build_text_area()

    def build_text_area(self):
        self.text_area = Text(self.root)
        self.text_area.pack(fill="both", expand=True)

    def build_menu(self):
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open text file", command=self.open_file)
        self.file_menu.add_command(label="Save as audio file", command=self.save_as_audio)
        self.file_menu.add_command(label="Quit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

    def build_main_frame(self):
        self.root.title("Text To Speech")
        self.root.geometry("400x300")
        self.root.resizable(0, 0)

    def update_text(self, text):
        self.text_area.delete("1.0", END)
        self.text_area.insert("1.0", text)

    def run(self):
        self.root.mainloop()

    def open_file(self):
        self.text_file_path = self.controller.open_file()
        self.text.set(self.engine.fetch_text_from_path(self.text_file_path))
        self.update_text(self.text.get())

    def save_as_audio(self):
        self.audio_file_path = self.controller.get_path_for_audio_file()
        if not self.audio_file_path.endswith('.mp3'):
            self.audio_file_path += '.mp3'
        threading.Thread(target=self.engine.create_audio_file_from_text, args=(self.text_area.get("1.0", END), self.audio_file_path)).start()

    def build_toolbar(self):
        self.toolbar = Frame(self.root)
        self.toolbar.pack(side=TOP, fill=X)
        self.open_button = Button(
            self.toolbar,
            relief=FLAT,
            compound=LEFT,
            command=self.open_file,
            image=self.controller.get_image("open"))
        self.open_button.pack(side=LEFT, padx=0, pady=0)

        self.save_button = Button(
            self.toolbar,
            relief=FLAT,
            compound=LEFT,
            command=self.save_as_audio,
            image=self.controller.get_image("save"))
        self.save_button.pack(side=LEFT, padx=0, pady=0)


def main():
    ui = DesktopUI()
    ui.run()
    print('done')
