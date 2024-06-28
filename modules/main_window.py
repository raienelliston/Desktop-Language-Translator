# Main window with options and settings, along with a start button to start the rest of the application
import tkinter as tk

languages = ["english", "chinese (simplified)", "afrikaans", "albanian", "amharic", "arabic", "armenian", "assamese", "ayamara", "azerbaijani", "bambara", "basque", "belarusian", "bengali", "bhojpuri", "bosnian", "bulgarian", "catalan", "cebuano", "chichewa", "chinese (simplified)", "chinese (traditional)", "corsican", "croatian", "czech", "danish", "dhivehi", "dogri", "dutch", "english", "esperanto", "estonian", "filipino", "finnish", "french", "frisian", "galician", "georgian", "german", "greek", "guarani", "gujarati", "haitian creole", "hausa", "hawaiian", "hebrew", "hindi", "hmong", "hungarian", "icelandic", "igbo", "ilocano", "indonesian", "irish", "italian", "japanese", "javanese", "kannada", "kazakh", "khmer", "kinyarwanda", "konkani", "korean", "krio", "kurdish (kurmanji)", "kurdish (sorani)", "kyrgyz", "lao", "latin", "latvian", "lingala", "lithuanian", "luganda", "luxembourgish", "macedonian", "maithili", "malagasy", "malay", "malayalam", "maltese", "maori", "marathi", "meiteilon (manipuri)", "mni-Mtei", "mizo", "mongolian", "myanmar", "nepali", "norwegian", "odia (oriya)", "oromo", "pashto", "persian", "polish", "portuguese", "punjabi", "quechua", "romanian", "russian", "samoan", "sanskrit", "scots gaelic", "sepedi", "serbian", "sesotho", "shona", "sindhi", "sinhala", "slovak", "slovenian", "somali", "spanish", "sundanese", "swahili", "swedish", "tajik", "tamil", "tatar", "telugu", "thai", "tigrinya", "tsonga", "turkish", "turkmen", "twi", "ukrainian", "urdu", "uyghur", "uzbek", "vietnamese", "welsh", "xhosa", "yiddish", "yoruba", "zulu"]

class MainWindow:
    def __init__(self, root, start_callback):
        self.root = root
        self.root.title("Screen Translator Configuration")
        self.start_callback = start_callback
        self.languages_list = languages # Add more languages as needed
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

        # Main Keybind Configuration
        self.main_keybind_label = tk.Label(self.root, text="Keybind (e.g., <ctrl>+<alt>+h):")
        self.main_keybind_label.grid(row=1, column=0, padx=10, pady=10)
        self.main_keybind_entry = tk.Entry(self.root, width=30)
        self.main_keybind_entry.grid(row=1, column=1, padx=10, pady=10)

        # Kill Keybind Configuration
        self.kill_keybind_label = tk.Label(self.root, text="Kill Keybind (e.g., <ctrl>+<alt>+k):")
        self.kill_keybind_label.grid(row=2, column=0, padx=10, pady=10)
        self.kill_keybind_entry = tk.Entry(self.root, width=30)
        self.kill_keybind_entry.grid(row=2, column=1, padx=10, pady=10)

        # Save Button
        self.save_button = tk.Button(self.root, text="Save Settings", command=self.save_settings)
        self.save_button.grid(row=3, column=0, columnspan=3, pady=10)

        # Start Button
        self.start_button = tk.Button(self.root, text="Start", command=self.start_application)
        self.start_button.grid(row=4, column=0, columnspan=3, pady=10)

        # Alert Label
        self.alert_label = tk.Label(self.root, text="", fg='red')
        self.alert_label.grid(row=3, column=1, pady=10, padx=10)

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
            settings = {
                "languages": "english",
                "main_keybind": "<ctrl>+<alt>+h",
                "kill_keybind": "<ctrl>+<alt>+k"
            }

        return settings
    
    def load_settings(self):
        settings = self._read_settings_file()

        languages = settings.get("languages", "")
        main_keybind = settings.get("main_keybind", "")
        kill_keybind = settings.get("kill_keybind", "")

        if languages in self.languages_list:
            idx = self.languages_list.index(languages)
            self.language_listbox.select_set(idx)

        self.main_keybind_entry.insert(0, main_keybind)
        self.kill_keybind_entry.insert(0, kill_keybind)

    def save_settings(self):
        selected_languages = [self.languages_list[idx] for idx in self.language_listbox.curselection()]
        if selected_languages:
            languages = selected_languages[0]
        else:
            languages = ""

        main_keybind = self.main_keybind_entry.get()
        kill_keybind = self.kill_keybind_entry.get()

        if not languages or not main_keybind or not kill_keybind:
            self.alert_label.config(text="Please fill in all fields")
            return

        settings = {
            "languages": languages,
            "main_keybind": main_keybind,
            "kill_keybind": kill_keybind
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