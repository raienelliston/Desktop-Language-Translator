from pynput import keyboard

def keybind_listen(func, keybind='<ctrl>+<alt>+h'):
    def for_canonical(f):
        return lambda k: f(l.canonical(k))

    hotkey = keyboard.HotKey(
        keyboard.HotKey.parse(keybind),
        func)
    with keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release)) as l:
        l.join()

def on_release(key):
    def for_canonical(f):
        return lambda k: f(l.canonical(k))

    with keyboard.Listener(on_release=for_canonical(key)) as l:
        l.join()

if __name__ == "__main__":

    def my_function():
        print("Hello World!")

    keybind_listen(my_function)
    on_release(my_function)