import tkinter as tk
from sqliteDictionary.sqlite_dictionary import sqliteDictionary 

db = sqliteDictionary("english")

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

        # Display definitions
        frame_definitions = tk.Frame(self.root)
        frame_definitions.pack()

        for definition in self.definitions:
            word, meaning, wordtype, example, synonyms, antonyms = definition
            label = tk.Label(frame_definitions, text=f"{word} ({wordtype}): {meaning}")
            label.pack()

            if example:
                label = tk.Label(frame_definitions, text=f"Example: {example}")
                label.pack()

            if synonyms:
                label = tk.Label(frame_definitions, text=f"Synonyms: {synonyms}")
                label.pack()

            if antonyms:
                label = tk.Label(frame_definitions, text=f"Antonyms: {antonyms}")
                label.pack()



    def select_word(self, event):
        pass

    def show(self):
        print("Showing popup...")
        self.root.grab_set()
        self.root.mainloop()

    def hide(self):
        print("Hiding popup...")
        self.root.destroy()
