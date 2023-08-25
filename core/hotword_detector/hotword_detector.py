# hotword_detector.py
from core.task_management.state import State

class HotwordDetector:
    def __init__(self, task_manager, transcription_model, audio_source):
        self.task_manager = task_manager
        self.transcription_model = transcription_model
        self.audio_source = audio_source


    def listen_for_hotwords(self, audio):
        if self.task_manager.current_state == State.IDLE:
            result = self.transcription_model.transcribe(audio)
            print(result)
            if 'junior' in result.text.lower():
                self.task_manager.switch_state(State.LISTENING)
                return 'Hotword detected!'
        return 'No hotword detected.'