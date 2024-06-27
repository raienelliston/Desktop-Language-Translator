import pyautogui

def capture_screen(size=(100, 100)):
    sizeX = size[0] if size[0] % 2 == 0 else size[0] + 1
    sizeY = size[1] if size[1] % 2 == 0 else size[1] + 1
    x, y = pyautogui.position()
    screenshot = pyautogui.screenshot(region=(x - sizeX // 2, y - sizeY // 2, sizeX, sizeY))
    screenshot.save("screenshot.png")
    return "screenshot.png"

if __name__ == "__main__":
    from PIL import Image
    from keybind_detector import keybind_listen

    def test():
        img = Image.open(capture_screen((500, 500)))
        img.save("screenshot.png")

    keybind_listen(test)