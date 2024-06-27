import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Translation Popup")
        self.geometry("300x100")
        self.resizable(False, False)
        self.geometry("+100+100")

        self.label = tk.Label(self, text="Hello World!")
        self.label.pack(pady=10)

        self.button = tk.Button(self, text="Close", command=self.destroy)
        self.button.pack(pady=10)
    def translate_window(self, text):
        self.label.config(text=text)
        self.mainloop()

if __name__ == "__main__":
    window = Window()
    window.mainloop()