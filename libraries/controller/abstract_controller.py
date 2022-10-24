from abc import ABC, abstractmethod
from libraries.view.scenes.abstract_scene import AbstractScene
from libraries.model.abstract_model import AbstractModel

class AbstractController(ABC):

    @abstractmethod
    def get_model(self) -> AbstractModel:
        pass

    @abstractmethod
    def get_scene(self) -> AbstractScene:
        pass
