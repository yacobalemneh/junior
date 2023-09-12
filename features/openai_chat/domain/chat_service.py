from abc import ABC, abstractmethod

class ChatService(ABC):
    @abstractmethod
    def create_chat(self, model, messages, response_type, completion_parameters):
        pass