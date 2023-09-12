import whisper
import logging
from features.conversation.transcription.data.model_type import ModelType
from features.conversation.transcription.domain.transcription import Transcription


class TranscriptionModel:
    def __init__(self):
        self.models = {}
        self.current_model = None
        self.pad_audio = whisper.pad_or_trim
        self.logger = logging.getLogger(__name__)

    def load_model(self, model_type: ModelType):
        self.logger.info(f"load_model called with model_type: {model_type}")
        if model_type not in self.models:
            self.logger.info(
                f"Loading model (TranscriptionModel): {model_type}")
            model = whisper.load_model(model_type)
            self.models[model_type] = model
        self.current_model = self.models[model_type]
        self.logger.info(f"current_model set to in load model: {model_type}")

    def ready_model(self, model_type: ModelType):
        self.logger.info(f"ready_model called with model_type: {model_type}")
        if model_type not in self.models:
            self.logger.info(
                f"Loading model (TranscriptionModel): {model_type}")
            model = whisper.load_model(model_type)
            self.models[model_type] = model
        self.logger.info(f"Model readied: {model_type}")

    def unload_model(self, model_type: ModelType):
        if model_type in self.models:
            self.logger.info(
                f"Unloading model (TranscriptionModel): {model_type}")
            del self.models[model_type]

    def switch_current_model(self, model_type: ModelType):
        self.logger.info(
            f"switch_current_model called with model_type: {model_type}")
        self.current_model = self.models[model_type]
        self.logger.info(
            f"current_model set to : {model_type} by switch_current_model")

    def transcribe(self, audio):
        if self.current_model is None:
            raise ValueError("Model not loaded.")
        audio = self.pad_audio(audio)
        result_dict = self.current_model.transcribe(
            audio, fp16=False, language='English')
        result = Transcription.from_dict(result_dict)
        return result
