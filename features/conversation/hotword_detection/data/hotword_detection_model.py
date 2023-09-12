from features.conversation.transcription.data.model_type import ModelType
from features.conversation.transcription.data.transcription_model import TranscriptionModel


class HotwordDetectionModel(TranscriptionModel):
    def transcribe(self, audio):
        self.switch_current_model(ModelType.BASE.value)
        return super().transcribe(audio)
