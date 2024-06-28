# Captures the screen from a specified size/region and outputs a .png
import pyautogui

def capture_screen(size=(100, 100)):
    sizeX = size[0] if size[0] % 2 == 0 else size[0] + 1
    sizeY = size[1] if size[1] % 2 == 0 else size[1] + 1
    x, y = pyautogui.position()
    left = max(0, x - sizeX // 2)
    top = max(0, y - sizeY // 2)
    screenshot = pyautogui.screenshot(region=(left, top, sizeX, sizeY))
    screenshot.save("screenshot.png")
    return "screenshot.png"

def capture_screen_region(region):
    x1, y1, x2, y2 = region
    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return screenshot

if __name__ == "__main__":
    from PIL import Image
    from keybind_detector import keybind_listen

    def test():
        img = Image.open(capture_screen((500, 500)))
        img.save("screenshot.png")

    keybind_listen(test)
