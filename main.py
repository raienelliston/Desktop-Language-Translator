from modules.keybind_detector import keybind_listen
from modules.screen_capture import capture_screen_region
from modules.translator import translate
from modules.OCR import find_text_in_image
from modules.popup import TranslationPopup
from modules.selection_tool import select_screen_region
from modules.main_window import MainWindow
from PIL import Image
from pynput.mouse import Controller
import tkinter as tk

def main():
    settings = {}
    mouse = Controller()

    try:
        with open("settings.txt", "r") as settings_file:
            for line in settings_file:
                key, value = line.strip().split("=")
                settings[key] = value
    except FileNotFoundError:
        print("No settings file found, using default settings")
        settings = {
            "main_language": "english",
            "main_keybind": "crtl+alt+h",
            "kill_keybind": "crtl+alt+k",
            "dictionary": False,
            "dictionary_language": "english"
        }

    # Load settings
    main_keybind = settings['main_keybind']
    kill_keybind = settings['kill_keybind']
    language = settings['main_language']
    dictionary = settings['dictionary']
    dictionary_language = settings['dictionary_language']
    
    if dictionary:
        print("Dictionary mode is enabled")

    def translate_from_region():
        region = select_screen_region()
        if region:
            text = find_text_in_image(capture_screen_region(region), isFile=True)
            print("text: " + str(text))
            translated_text = translate(str(text), language)
            print(translated_text)
            popup = TranslationPopup(root, translated_text, mouse.position[0], mouse.position[1])
            popup.show()

    def monitor_to_translate():
        print("Monitoring for keybind...")
        keybind_listen(translate_from_region, main_keybind, kill_keybind)

    monitor_to_translate()


root = tk.Tk()
app = MainWindow(root, main)
app.mainloop()