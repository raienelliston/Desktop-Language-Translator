from modules.keybind_detector import keybind_listen
from modules.screen_capture import capture_screen
from modules.translator import translate_text
from modules.OCR import find_text_in_image

keybind = '<ctrl>+<alt>+h'

def translate_from_screen():
    text = find_text_in_image(capture_screen())
    return translate_text(text, 'es')

def main():
    keybind_listen(translate_from_screen, keybind)

main()