from abc import ABC, abstractmethod
from libraries.view.scenes.abstract_scene import AbstractScene
from libraries.model.abstract_model import AbstractModel

class AbstractController(ABC):

    __scene: AbstractScene
    __model: AbstractModel

    def __set_model(self, model: AbstractModel) -> None:
        self.__model = model

    def __set_scene(self, scene: AbstractScene) -> None:
        self.__scene = scene

    def get_model(self) -> AbstractModel:
        return self.__model

    def get_scene(self) -> AbstractScene:
        return self.__scene
