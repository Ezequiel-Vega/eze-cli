from abc import ABC
from abc import abstractmethod

class CreateTemplate(ABC):
    @abstractmethod
    def create(self):
        pass
