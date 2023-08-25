class TaskExecutionInteractor:
    def __init__(self, task_execution_service):
        self.task_execution_service = task_execution_service

    def switch_state(self, state):
        self.task_execution_service.switch_state(state)