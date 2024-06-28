from modules.keybind_detector import keybind_listen
from modules.screen_capture import capture_screen, capture_screen_region
from modules.translator import translate
from modules.OCR import find_text_in_image
from modules.gui import TranslationPopup
from modules.selection_tool import select_screen_region
from modules.main_window import MainWindow
from PIL import Image
from pynput.mouse import Controller

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
        "languages": "en",
        "keybind": "crtl+alt+h"
    }

keybind = settings['keybind']
language = settings['languages']

def show_translation(text):
    print(text)
    popup = TranslationPopup(text, mouse.position[0], mouse.position[1])
    popup.show()

def translate_from_screen():
    img = Image.open(capture_screen((500, 500)))
    img.save("screenshot.png")
    text = find_text_in_image(capture_screen((500, 50)), isFile=True)
    print("text: " + str(text))
    translated_text = translate(str(text), language)
    print(translated_text)
    popup = TranslationPopup(translated_text, mouse.position[0], mouse.position[1])
    popup.show()

def translate_from_region():
    region = select_screen_region()
    if region:
        img = Image.open(capture_screen_region(region))
        img.save("screenshot.png")
        text = find_text_in_image(capture_screen_region(region), isFile=True)
        print("text: " + str(text))
        translated_text = translate(str(text), language)
        print(translated_text)
        popup = TranslationPopup(translated_text, mouse.position[0], mouse.position[1])
        popup.show()

main_window = MainWindow(keybind_listen(translate_from_region))

def main():
    # keybind_listen(translate_from_screen)
    pass

main()