
from core.data_source.model_type import ModelType
from core.data_source.transcription_model import TranscriptionModel


class HotwordDetectionModel(TranscriptionModel):
    def transcribe(self, audio):
        self.switch_current_model(ModelType.TINY.value)
        return super().transcribe(audio)
