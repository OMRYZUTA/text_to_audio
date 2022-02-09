from tkinter.filedialog import askopenfilename


class Controller:
    def __init__(self):
        self.text_file_path = None

    def open_file(self):
        file_path = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        self.text_file_path = file_path
        return file_path
