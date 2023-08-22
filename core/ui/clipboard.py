import pyperclip

class Clipboard:
    def copy(self, text):
        pyperclip.copy(text)