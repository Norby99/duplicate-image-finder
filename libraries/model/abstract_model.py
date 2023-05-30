from abc import ABC, abstractmethod

class AbstractModel(ABC):

    @abstractmethod
    def ready(self) -> bool:
        pass
