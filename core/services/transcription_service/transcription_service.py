# transcription_service.py
from core.task_management.state import State

class TranscriptionService:
    def __init__(self, task_manager, transcription_model):
        self.task_manager = task_manager
        self.transcription_model = transcription_model

    def transcribe(self, audio):
        if self.task_manager.current_state == State.LISTENING:
            result = self.transcription_model.transcribe(audio)
            # Unloading handled in task manager 
            # while switching the state
            print('Transcription result in listening:', result.text)
            return result
        return 'Not in transcription mode.'