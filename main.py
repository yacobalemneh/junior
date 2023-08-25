from core.interaction.listener import Listener
from core.task_management.state import State
from core.transcription.transcription_model import TranscriptionModel
from core.task_management.task_manager import TaskManager
from core.hotword_detector.hotword_detector import HotwordDetector
from core.services.transcription_service.transcription_service import TranscriptionService
from core.config import Config
from core.audio.audio_processor import AudioProcessor
from core.audio.audio_source import AudioSource
from infrastructure.startup import Startup
from infrastructure.logging import Logging

def main():
    # Initialize components
    config = Config()
    transcription_model = TranscriptionModel(config)
    task_manager = TaskManager(transcription_model)
    audio_source = AudioSource()
    hotword_detector = HotwordDetector(task_manager, transcription_model, audio_source)
    transcription_service = TranscriptionService(task_manager, transcription_model)
    hotwords = config.get('hotwords')
    audio_processor = AudioProcessor
    startup = Startup()
    logging = Logging()
    
    # Load the daemon into the system startup
    startup.load()
    task_manager.switch_state(State.IDLE)
    logging.log("Daemon loaded into system startup")

    # Initialize and start Listener
    listener = Listener(audio_source, audio_processor, hotword_detector, task_manager)
    listener.start()

if __name__ == "__main__":
    main()