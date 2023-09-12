from abc import ABC, abstractmethod

class ApiKeyProvider(ABC):
    @abstractmethod
    def get_key(self, key_name):
        pass