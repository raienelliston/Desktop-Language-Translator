# Extracts the text out of a .png image file
import pytesseract
from PIL import Image
from plyer import notification

# Set the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def find_text_in_image(image, isFile=True, lang='eng+chi_sim+jap'):
    try:
        text = pytesseract.image_to_string(image, lang=lang)
        return text
    except:
        notification.notify(
            title='Desktop Translator',
            message='Either you clicked or there\'s an issue',
            app_name='Desktop Translator',
            timeout=5
        )
        return ""


if __name__ == "__main__":
    from PIL import Image
    from keybind_detector import keybind_listen
    from screen_capture import capture_screen

    def test():
        img = Image.open(capture_screen((500, 500)))
        img.save("screenshot.png")
        print("text: " + find_text_in_image(capture_screen((500, 500)), isFile=True))
    keybind_listen(test)