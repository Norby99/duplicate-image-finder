from abc import ABC, abstractmethod
from libraries.view.scenes.abstract_scene import AbstractScene

class AbstractController(ABC):

    @abstractmethod
    def get_model(self) -> None:
        pass

    @abstractmethod
    def get_scene(self) -> AbstractScene:
        pass
