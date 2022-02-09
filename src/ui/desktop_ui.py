from tkinter import *
from src.ui.controllers.controller import Controller


class DesktopUI:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.file_path = StringVar()
        self.build_main_frame()
        self.build_menu()
        self.build_open_button()
        self.build_path_label()
        self.build_text_area()

    def build_text_area(self):
        self.text_area = Text(self.root)
        self.text_area.pack(fill="both", expand=True)

    def build_menu(self):
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
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

    def build_open_button(self):
        B = Button(text="Open", command=self.open_file)
        B.pack()

    def open_file(self):
        self.file_path = controller.open_file()
        self.file_path_label.config(text=self.file_path)

    def build_path_label(self):
        self.file_path = 'No file selected'
        self.file_path_label = Label(self.root, text=self.file_path)
        self.file_path_label.pack()


if __name__ == '__main__':
    controller = Controller()
    ui = DesktopUI(controller)
    ui.run()
