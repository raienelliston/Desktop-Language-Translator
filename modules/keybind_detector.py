from pynput import keyboard

def keybind_listen(func, main_keybind='<ctrl>+<alt>+h', kill_keybind='<ctrl>+<alt>+k'):
    def for_canonical(f):
        return lambda k: f(l.canonical(k))

    main_hotkey = keyboard.HotKey(
        keyboard.HotKey.parse(main_keybind),
        func)
    
    kill_hotkey = keyboard.HotKey(
        keyboard.HotKey.parse(kill_keybind),
        lambda: exit())

    l = keyboard.Listener(
            on_press=for_canonical(main_hotkey.press),
            on_release=for_canonical(main_hotkey.release))
    
    main_hotkey.start()
    kill_hotkey.start()
    l.start()
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