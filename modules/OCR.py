import pytesseract
from PIL import Image

def find_text_in_image(image_path, isFile=True):
    if isFile:
        image = Image.open(image_path)
    else:
        image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    from PIL import Image
    from keybind_detector import keybind_listen
    from screen_capture import capture_screen

    def test():
        img = Image.open(capture_screen((500, 500)))
        img.save("screenshot.png")
    print("text" + find_text_in_image(keybind_listen(test)))