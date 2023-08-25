from core.task_management.state import State


class Listener:
    def __init__(self, audio_source, audio_processor, hotword_detector, task_manager):
        self.audio_source = audio_source
        self.audio_processor = audio_processor
        self.hotword_detector = hotword_detector
        self.task_manager = task_manager

    def start(self):
        while True:
            audio = self.audio_source.listen()
            processed_audio = self.audio_processor.process(audio)
            result = self.hotword_detector.listen_for_hotwords(processed_audio)
            if self.task_manager.current_state == State.LISTENING:
                # optional, print an indicator
                print("Hotword detected, now listening in mode: ", self.task_manager.current_state)