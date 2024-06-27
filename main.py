from pynput import keyboard

keys_down = set()

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        keys_down.add(key.char)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        keys_down.add(key)

def on_release(key):
    print('{0} released'.format(
        key))
    keys_down.remove(key)
    

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)

def main():
    listener.start()
    while True:
        print(str(keys_down))

if __name__ == "__main__":
    main()