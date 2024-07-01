# Detects keybinds and executes a function or kills the listener when a keybind is detected 
from pynput import keyboard
from plyer import notification
from time import sleep

def keybind_listen(func, main_keybind='<ctrl>+<alt>+h', kill_keybind='<ctrl>+<alt>+k'):
    def for_canonical(f):
        return lambda k: f(l.canonical(k))

    def runFunc():
        for i in main_keybind.split('+'):
            main_hotkey.release(i)
        for i in kill_keybind.split('+'):
            kill_hotkey.release(i)
        func()

    def stop():
        notification.notify(
            title='Keybind Listener',
            message='Exiting listener...',
            app_name='Keybind Listener',
            timeout=5
        )
        sleep(5)
        exit()

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