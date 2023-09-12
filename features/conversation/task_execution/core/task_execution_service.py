import logging


class TaskExecutionService:
    def __init__(self, task_manager, model_management_service):
        self.task_manager = task_manager
        self.model_management_service = model_management_service
        self.logger = logging.getLogger(__name__)

    def switch_state(self, state):
        self.logger.info(f"Switching state to {state}")
        self.task_manager.switch_state(state)
        self.model_management_service.handle_state_change(state)

    def stop_listening(self):
        self.switch_state('idle')

    @property
    def current_state(self):
        return self.task_manager.state
