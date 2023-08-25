from dataclasses import dataclass


@dataclass
class Hotword:
    word: str
    detected: bool