import tkinter as tk
from sqliteDictonary import sqlite_database as db

class DictionaryWindow:
    def __init__(self, root, text, x, y):
        self.root = tk.Tk()
        self.text = text
        self.definitions = db.search_sentance(text)
        self.x = x
        self.y = y
        self.setup_ui()

    def setup_ui(self):
        self.root.overrideredirect(True)
        self.root.geometry(f"+{self.x}+{self.y}")
        self.root.attributes("-topmost", True)

        label = tk.Label(self.root, text=self.text, bg='yellow', fg='black')
        label.pack()

    def show(self):
        print("Showing popup...")
        self.root.grab_set()
        self.root.mainloop()

    def hide(self):
        print("Hiding popup...")
        self.root.destroy()
