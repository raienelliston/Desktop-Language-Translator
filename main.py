from modules.keybind_detector import keybind_listen
from modules.screen_capture import capture_screen
from modules.translator import translate
from modules.OCR import find_text_in_image
from modules.gui import TranslationPopup
from PIL import Image
from pynput.mouse import Controller

keybind = '<ctrl>+<alt>+h'
mouse = Controller()

def translate_from_screen():
    img = Image.open(capture_screen((500, 500)))
    img.save("screenshot.png")
    print("text: " + find_text_in_image(capture_screen((500, 500)), isFile=True))

def show_translation(text):
    popup = TranslationPopup(text, mouse.position[0], mouse.position[1])
    popup.show()

def main():
    keybind_listen(show_translation(translate_from_screen), keybind)

main()