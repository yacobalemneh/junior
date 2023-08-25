from core.task_management.state import State

class TaskManager:
    def __init__(self, transcription_model):
        self.current_state = State.IDLE
        self.transcription_model = transcription_model

    def switch_state(self, state):
        self.current_state = state
        print(f'Switching to state: {state}')
        if state == State.LISTENING:
            self.transcription_model.load('medium.en')
        elif state == State.IDLE:
            self.transcription_model.load('tiny.en')