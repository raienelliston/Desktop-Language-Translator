import tkinter as tk

class TranslationPopup:
    def __init__(self, text, x, y, duration=5000):
        print(f"Initializing popup at ({x}, {y}) with text: {text}")
        self.root = tk.Tk()
        self.text = text
        self.x = x
        self.y = y
        self.duration = duration
        self.setup_ui()

    def setup_ui(self):
        self.root.overrideredirect(True)  # Remove window decorations
        self.root.geometry(f"+{self.x}+{self.y}")  # Position the window at the given coordinates
        self.root.attributes("-topmost", True)  # Keep the window on top

        label = tk.Label(self.root, text=self.text, bg='yellow', fg='black')
        label.pack()

    def show(self):
        print("Showing popup...")
        self.root.after(self.duration, self.hide)  # Close the window after the specified duration
        self.root.grab_set()  # Make the window modal
        self.root.mainloop()

    def hide(self):
        print("Hiding popup...")
        self.root.destroy()

# Example usage
if __name__ == "__main__":
    from pynput.mouse import Controller

    mouse = Controller()

    popup = TranslationPopup("Translated text example", mouse.position[0] + 10, mouse.position[1] + 30)
    popup.show()
