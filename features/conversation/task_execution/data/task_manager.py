class TaskManager:
    def __init__(self):
        self.state = 'idle'

    def switch_state(self, state):
        self.state = state