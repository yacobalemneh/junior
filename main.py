from core.config import Config
from core.data_source.transcription_model import TranscriptionModel
from core.domain.models.task_manager import TaskManager
from core.domain.models.transcription import Transcription
from core.domain.models.hotword import Hotword
from core.domain.models.task import Task
from core.domain.models.conversation import Conversation
from core.domain.services.model_management_service import ModelManagementService
from core.domain.services.transcription_service import TranscriptionService
from core.domain.services.hotword_detection_service import HotwordDetectionService
from core.domain.services.task_execution_service import TaskExecutionService
from core.domain.services.conversation_service import ConversationService
from core.application.interactors.transcription_interactor import TranscriptionInteractor
from core.application.interactors.hotword_detection_interactor import HotwordDetectionInteractor
from core.application.interactors.task_execution_interactor import TaskExecutionInteractor
from core.application.interactors.conversation_interactor import ConversationInteractor
from core.infrastructure.audio.audio_source import AudioSource
from core.infrastructure.audio.audio_processor import AudioProcessor
from core.infrastructure.startup import setup

def main():
    setup()
    config = Config()  # You need to define this config
    audio_source = AudioSource()
    audio_processor = AudioProcessor
    transcription_model = TranscriptionModel()
    task_manager = TaskManager()
    model_management_service = ModelManagementService(transcription_model)
    task_execution_service = TaskExecutionService(task_manager, model_management_service)
    transcription_service = TranscriptionService(transcription_model)
    hotword_detection_service = HotwordDetectionService(transcription_model)
    hotword_detection_interactor = HotwordDetectionInteractor(hotword_detection_service)
    conversation_service = ConversationService(transcription_service, hotword_detection_interactor, task_execution_service)
    conversation_interactor = ConversationInteractor(conversation_service)
    transcription_interactor = TranscriptionInteractor(transcription_service)
    task_execution_interactor = TaskExecutionInteractor(task_execution_service)

    # Set initial state to 'idle' and load the 'tiny' model
    task_execution_service.switch_state('setup')

    # Start conversation
    conversation_interactor.start_conversation(audio_source, audio_processor)

if __name__ == "__main__":
    main()