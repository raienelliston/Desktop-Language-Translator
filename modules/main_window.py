import tkinter as tk

class MainWindow:
    def __init__(self, root, start_callback):
        self.root = root
        self.root.title("Screen Translator Configuration")
        self.start_callback = start_callback
        self.languages_list = ["english", "french", "spanish", "dutch", "italian", "chinese (simplified)"]  # Add more languages as needed
        self.create_widgets()
        self.load_settings()

    def create_widgets(self):
        # OCR Languages Selection
        self.language_label = tk.Label(self.root, text="OCR Languages:")
        self.language_label.grid(row=0, column=0, padx=10, pady=10)
        
        #Listbox
        self.language_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, exportselection=0)
        for language in self.languages_list:
            self.language_listbox.insert(tk.END, language)
        self.language_listbox.grid(row=0, column=1, padx=10, pady=10)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.language_listbox.yview)
        self.language_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=2, sticky='ns')

        # Keybind Configuration
        self.keybind_label = tk.Label(self.root, text="Keybind (e.g., <ctrl>+<alt>+h):")
        self.keybind_label.grid(row=1, column=0, padx=10, pady=10)
        self.keybind_entry = tk.Entry(self.root, width=30)
        self.keybind_entry.grid(row=1, column=1, padx=10, pady=10)

        # Save Button
        self.save_button = tk.Button(self.root, text="Save Settings", command=self.save_settings)
        self.save_button.grid(row=2, column=0, columnspan=3, pady=10)

        # Start Button
        self.start_button = tk.Button(self.root, text="Start", command=self.start_application)
        self.start_button.grid(row=3, column=0, columnspan=3, pady=10)

        # Alert Label
        self.alert_label = tk.Label(self.root, text="", fg='red')
        self.alert_label.grid(row=2, column=1, pady=10, padx=10)

    def start_application(self):
        self.save_settings()
        self.root.destroy()
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

        if languages in self.languages_list:
            idx = self.languages_list.index(languages)
            self.language_listbox.select_set(idx)

        self.keybind_entry.insert(0, keybind)

    def save_settings(self):
        selected_languages = [self.languages_list[idx] for idx in self.language_listbox.curselection()]
        if selected_languages:
            languages = selected_languages[0]
        else:
            languages = ""

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

    def mainloop(self):
        self.root.mainloop()

    def destroy(self):
        self.root.destroy()


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
    app = MainWindow(root, start_application)
    root.mainloop()