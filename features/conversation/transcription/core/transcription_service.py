from features.conversation.transcription.data.model_type import ModelType
from features.conversation.transcription.data.transcription_model import TranscriptionModel


class TranscriptionService:
    def __init__(self, transcription_model: TranscriptionModel):
        self.transcription_model = transcription_model

    def transcribe(self, audio):
        self.transcription_model.switch_current_model(ModelType.SMALL.value)
        return self.transcription_model.transcribe(audio)
