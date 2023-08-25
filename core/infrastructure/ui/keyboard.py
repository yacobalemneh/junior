import keyboard

class Keyboard:
    @staticmethod
    def add_hotkey(hotkey, callback):
        keyboard.add_hotkey(hotkey, callback)

    @staticmethod
    def wait():
        keyboard.wait()