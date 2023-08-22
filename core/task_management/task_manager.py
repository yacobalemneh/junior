# task_manager.py
from core.services.state import State

class TaskManager:
    def __init__(self):
        self.current_state = State.IDLE

    def switch_state(self, state):
        self.current_state = state