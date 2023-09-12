
from core.config import Config
from features.conversation.audio.audio_processor import AudioProcessor
from features.conversation.audio.audio_source import AudioSource
from features.conversation.conversation import ConversationService
from features.conversation.hotword_detection.core.hotword_detection_service import HotwordDetectionService
from features.conversation.hotword_detection.interactors.hotword_detection_interactor import HotwordDetectionInteractor
from features.conversation.interactors.conversation_interactor import ConversationInteractor
from features.conversation.task_execution.core.model_management_service import ModelManagementService
from features.conversation.task_execution.core.task_execution_service import TaskExecutionService
from features.conversation.task_execution.data.task_manager import TaskManager
from features.conversation.task_execution.interactors.task_execution_interactor import TaskExecutionInteractor
from features.conversation.transcription.core.transcription_service import TranscriptionService
from features.conversation.transcription.data.transcription_model import TranscriptionModel
from features.conversation.transcription.interactors.transcription_interactor import TranscriptionInteractor
from infrastructure.env_api_key_provider import EnvApiKeyProvider
from infrastructure.startup import setup


def main():
    key_provider = EnvApiKeyProvider()
    setup()
    config = Config()  # You need to define this config
    audio_source = AudioSource()
    audio_processor = AudioProcessor
    transcription_model = TranscriptionModel()
    task_manager = TaskManager()
    model_management_service = ModelManagementService(transcription_model)
    task_execution_service = TaskExecutionService(
        task_manager, model_management_service)
    transcription_service = TranscriptionService(transcription_model)
    hotword_detection_service = HotwordDetectionService(transcription_model)
    hotword_detection_interactor = HotwordDetectionInteractor(
        hotword_detection_service)
    conversation_service = ConversationService(
        transcription_service, hotword_detection_interactor, task_execution_service)
    conversation_interactor = ConversationInteractor(conversation_service)
    transcription_interactor = TranscriptionInteractor(transcription_service)
    task_execution_interactor = TaskExecutionInteractor(task_execution_service)

    # Set initial state to 'idle' and load the 'tiny' model
    task_execution_service.switch_state('setup')

    # Start conversation
    conversation_interactor.start_conversation(audio_source, audio_processor)


if __name__ == "__main__":
    main()
