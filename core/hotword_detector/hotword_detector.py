# hotword_detector.py
from core.services.state import State

class HotwordDetector:
    def __init__(self, task_manager, transcription_model):
        self.task_manager = task_manager
        self.transcription_model = transcription_model
        self.transcription_model.load('tiny.en')  # Load the 'tiny.en' model

    def detect(self, audio):
        result = self.transcription_model.transcribe(audio)
        print('Transcription:', result)
        if 'hotword' in result:
            self.task_manager.switch_state(State.LISTENING)
            return 'Hotword detected!'
        return 'No hotword detected.'