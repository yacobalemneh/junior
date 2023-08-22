# main.py
from core.transcription.model import TranscriptionModel
from core.task_management.task_manager import TaskManager
from core.hotword_detector.hotword_detector import HotwordDetector
from core.services.transcription_service.transcription_service import TranscriptionService
from core.config import Config
from core.audio_processor import AudioProcessor
from infrastructure.startup import Startup
from infrastructure.logging import Logging

def main():
    # Initialize components
    config = Config()
    transcription_model = TranscriptionModel(config)
    task_manager = TaskManager()
    hotword_detector = HotwordDetector(task_manager, transcription_model)
    transcription_service = TranscriptionService(task_manager, transcription_model)
    hotwords = config.get('hotwords')
    audio_processor = AudioProcessor(hotwords, config, hotword_detector, transcription_service)
    startup = Startup()
    logging = Logging()
    
    # Load the daemon into the system startup
    startup.load()
    logging.log("Daemon loaded into system startup")

    # Start listening in the background
    audio_processor.listen(mode="wav")

if __name__ == "__main__":
    main()