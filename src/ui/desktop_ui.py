from tkinter import *
from src.ui.controllers.controller import Controller
from src.engine.fetchers.text_fetcher import TextFetcher
from src.engine.audio_makers.audio_maker import AudioMaker


class DesktopUI:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
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
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_as_audio)
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
        self.text.set(TextFetcher().fetch_from_path(self.text_file_path))
        self.update_text(self.text.get())

    def save_as_audio(self):
        self.audio_file_path = self.controller.get_path_for_audio_file()
        if not self.audio_file_path.endswith('.mp3'):
            self.audio_file_path += '.mp3'
        AudioMaker().create_audio_file_from_text(self.text_area.get("1.0", END), self.audio_file_path)


if __name__ == '__main__':
    controller = Controller()
    ui = DesktopUI(controller)
    ui.run()
