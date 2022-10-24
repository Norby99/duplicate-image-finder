from abc import ABC, abstractmethod

class AbstractModel(ABC):

    @abstractmethod
    def set_variables(self) -> None:
        pass
