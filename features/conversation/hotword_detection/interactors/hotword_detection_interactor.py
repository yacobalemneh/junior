import logging


class HotwordDetectionInteractor:
    def __init__(self, hotword_detection_service):
        self.hotword_detection_service = hotword_detection_service

    def listen_for_hotwords(self, audio):
        transcribed_text = self.hotword_detection_service.transcribe_audio(
            audio)
        return self.hotword_detection_service.is_hotword_or_stopword(transcribed_text)

    def is_hotword(self, audio):
        transcribed_text = self.hotword_detection_service.transcribe_audio(
            audio)
        return self.hotword_detection_service.is_hotword(transcribed_text)

    def is_stopword(self, audio):
        transcribed_text = self.hotword_detection_service.transcribe_audio(
            audio)
        return self.hotword_detection_service.is_stopword(transcribed_text)
