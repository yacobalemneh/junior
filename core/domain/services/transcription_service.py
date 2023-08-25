
from core.data_source.model_type import ModelType
from core.data_source.transcription_model import TranscriptionModel


class TranscriptionService:
    def __init__(self, transcription_model: TranscriptionModel):
        self.transcription_model = transcription_model

    def transcribe(self, audio):
        self.transcription_model.switch_current_model(ModelType.MEDIUM.value)
        return self.transcription_model.transcribe(audio)