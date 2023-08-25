import pyperclip

class Clipboard:
    @staticmethod
    def copy(text: str):
        pyperclip.copy(text)

    @staticmethod
    def paste() -> str:
        return pyperclip.paste()