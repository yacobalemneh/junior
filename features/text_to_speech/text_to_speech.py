from abc import ABC, abstractmethod

from features.text_to_speech.azure.data.speech_config import SpeechConfig


class TextToSpeechService(ABC):
    @abstractmethod
    def synthesize_speech(self, text, config=SpeechConfig()):
        pass

    @abstractmethod
    def synthesize_speech_from_ssml(self, ssml, config=SpeechConfig()):
        pass
