from abc import ABC, abstractmethod

class AbstractModel(ABC):

    @abstractmethod
    def set_variables(self) -> None:
        pass

    @abstractmethod
    def ready(self) -> bool:
        pass
