# transcription_service.py
from core.services.state import State

class TranscriptionService:
    def __init__(self, task_manager, transcription_model):
        self.task_manager = task_manager
        self.transcription_model = transcription_model

    def transcribe(self, audio):
        if self.task_manager.current_state == State.LISTENING:
            self.transcription_model.load('medium.en')  # Load the 'medium.en' model
            result = self.transcription_model.transcribe(audio)
            # TODO: Unload the model when transcription is complete
            return result
        return 'Not in transcription mode.'