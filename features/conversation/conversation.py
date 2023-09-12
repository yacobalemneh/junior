import logging
from features.conversation.hotword_detection.domain.hotword import DetectionResult


class ConversationService:
    def __init__(self, transcription_service, hotword_detection_interactor, task_execution_service):
        self.transcription_service = transcription_service
        self.hotword_detection_interactor = hotword_detection_interactor
        self.task_execution_service = task_execution_service
        self.stopword_detected = False

    def start_conversation(self, audio_source, audio_processor):
        audio_source.start_stream()
        while True:
            audio_chunk = audio_source.audio_queue.get()
            processed_audio = audio_processor.process(audio_chunk)
            if self.hotword_detection_interactor.listen_for_hotwords(processed_audio) == DetectionResult.HOTWORD:
                self.task_execution_service.switch_state('listening')
                while self.task_execution_service.current_state == 'listening':
                    audio_chunk = audio_source.audio_queue.get()
                    processed_audio = audio_processor.process(audio_chunk)
                    if self.hotword_detection_interactor.listen_for_hotwords(processed_audio) == DetectionResult.STOPWORD:
                        self.stopword_detected = True
                        break
                if self.stopword_detected:
                    complete_audio = audio_processor.process(
                        audio_source.buffer)
                    result = self.transcription_service.transcribe(
                        complete_audio)
                    logging.warning(
                        f'Transcription result in listening: {result.text}')
                    self.task_execution_service.switch_state('idle')
                    audio_source.stop_stream()
                    break
            else:
                self.task_execution_service.switch_state('idle')
