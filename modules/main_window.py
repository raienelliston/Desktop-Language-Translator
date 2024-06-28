import tkinter as tk
from tkinter import ttk

class MainWindow:
    def __init__(self, root, save_callback, start_callback):
        self.root = root
        self.root.title("Screen Translator Configuration")
        self.save_callback = save_callback
        self.start_callback = start_callback
        self.create_widgets()
        self.load_settings()

    def create_widgets(self):
        # OCR Languages Selection
        self.language_label = tk.Label(self.root, text="OCR Languages (e.g., eng+fra):")
        self.language_label.grid(row=0, column=0, padx=10, pady=10)
        self.language_entry = tk.Entry(self.root, width=30)
        self.language_entry.grid(row=0, column=1, padx=10, pady=10)

        # Keybind Configuration
        self.keybind_label = tk.Label(self.root, text="Keybind (e.g., <ctrl>+<alt>+h):")
        self.keybind_label.grid(row=1, column=0, padx=10, pady=10)
        self.keybind_entry = tk.Entry(self.root, width=30)
        self.keybind_entry.grid(row=1, column=1, padx=10, pady=10)

        # Save Button
        self.save_button = tk.Button(self.root, text="Save Settings", command=self.save_settings)
        self.save_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Start Button
        self.start_button = tk.Button(self.root, text="Start", command=self.start_application)
        self.start_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Alert Label
        self.alert_label = tk.Label(self.root, text="", fg='red')
        self.alert_label.grid(row=2, column=1, pady=10, padx=10)

    def start_application(self):
        self.start_callback()

    def _read_settings_file(self):
        settings = {}
        try:
            with open("settings.txt", "r") as settings_file:
                for line in settings_file:
                    key, value = line.strip().split("=")
                    settings[key] = value
        except FileNotFoundError:
            print("No settings file found, using default settings")

        return settings
    
    def load_settings(self):
        settings = self._read_settings_file()

        languages = settings.get("languages", "")
        keybind = settings.get("keybind", "")

        self.language_entry.insert(0, languages)
        self.keybind_entry.insert(0, keybind)

    def save_settings(self):
        languages = self.language_entry.get()
        keybind = self.keybind_entry.get()

        if not languages or not keybind:
            self.alert_label.config(text="Please fill in all fields")
            return

        settings = {
            "languages": languages,
            "keybind": keybind
        }

        with open("settings.txt", "w") as settings_file:
            for key, value in settings.items():
                settings_file.write(f"{key}={value}\n")

        self.alert_label.config(text="Settings saved successfully")
        self.root.after(2000, lambda: self.alert_label.config(text=""))
    
    


def load_settings():
    settings = {}
    try:
        with open("settings.txt", "r") as settings_file:
            for line in settings_file:
                key, value = line.strip().split("=")
                settings[key] = value
    except FileNotFoundError:
        print("No settings file found, using default settings")

    return settings

if __name__ == "__main__":

    def save_settings():
        print("Settings saved")

    def start_application():
        print("Application started")

    root = tk.Tk()
    app = MainWindow(root, save_settings, start_application)
    root.mainloop()
