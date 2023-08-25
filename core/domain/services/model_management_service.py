import logging
from core.data_source.model_type import ModelType
from core.data_source.transcription_model import TranscriptionModel


class ModelManagementService:
    def __init__(self, transcription_model: TranscriptionModel):
        self.transcription_model = transcription_model
        self.logger = logging.getLogger(__name__)

    def handle_state_change(self, state):
        if state == 'listening':
            self.logger.info(f"Readying model: {ModelType.MEDIUM.value}")
            self.transcription_model.ready_model(ModelType.MEDIUM.value)
        elif state == 'idle':
            self.logger.info(f"Unloading model: {ModelType.MEDIUM.value}")
            self.transcription_model.unload_model(ModelType.MEDIUM.value)
        elif state == 'setup':
            self.logger.info(f"Setup Loading model: {ModelType.TINY.value}")
            self.transcription_model.load_model(ModelType.TINY.value)
