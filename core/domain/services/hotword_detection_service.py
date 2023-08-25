import logging
from core.data_source.hotword_detection_model import HotwordDetectionModel
from enum import Enum

class DetectionResult(Enum):
    NONE = 0
    HOTWORD = 1
    STOPWORD = 2


class HotwordDetectionService:
    def __init__(self, transcription_model: HotwordDetectionModel):
        self.transcription_model = transcription_model

    def transcribe_audio(self, audio):  
        result = self.transcription_model.transcribe(audio)
        logging.error(f'Transcription result in hotword detection (NEGATIVE): {result.text}')
        return result.text  

    def is_hotword_or_stopword(self, transcribed_text):
        if self.is_hotword(transcribed_text):
            logging.warning(f'Transcription result HOTWORD DETECTED: {transcribed_text}')
            return DetectionResult.HOTWORD
        elif self.is_stopword(transcribed_text):
            logging.warning(f'Transcription result STOPWORD DETECTED: {transcribed_text}')
            return DetectionResult.STOPWORD
        return DetectionResult.NONE

    def is_stopword(self, transcribed_text):
        return 'done' in transcribed_text.lower()

    def is_hotword(self, transcribed_text):
        return 'junior' in transcribed_text.lower()
