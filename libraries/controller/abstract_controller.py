from abc import ABC, abstractmethod

class AbstractController(ABC):

    @abstractmethod
    def set_model(self, model) -> None:
        pass

    @abstractmethod
    def set_scene(self, scene) -> None:
        pass
