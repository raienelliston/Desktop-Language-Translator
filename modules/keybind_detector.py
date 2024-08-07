# Detects keybinds and executes a function or kills the listener when a keybind is detected 
from pynput import keyboard
from plyer import notification
from time import sleep

def keybind_listen(func, main_keybind='<ctrl>+<alt>+h', kill_keybind='<ctrl>+<alt>+k'):
    loop = True
    while loop:
        loop = main_loop(func, main_keybind, kill_keybind)

def main_loop(func, main_keybind='<ctrl>+<alt>+h', kill_keybind='<ctrl>+<alt>+k'):
    def for_canonical(f):
        return lambda k: f(l.canonical(k))

    def runFunc():
        l.stop()
        func()
        return True

    def stop():
        notification.notify(
            title='Desktop Translator',
            message='Exiting listener...',
            app_name='Desktop Translator',
            timeout=5
        )
        sleep(5)
        l.stop()
        return False

    main_hotkey = keyboard.HotKey(
        keyboard.HotKey.parse(main_keybind),
        runFunc)
    

    kill_hotkey = keyboard.HotKey(
        keyboard.HotKey.parse(kill_keybind),
        lambda: stop())
    
    def press(k):
        main_hotkey.press(k)
        kill_hotkey.press(k)

    def release(k):
        main_hotkey.release(k)
        kill_hotkey.release(k)

    l = keyboard.Listener(
        on_press=for_canonical(press),
        on_release=for_canonical(release))
    
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