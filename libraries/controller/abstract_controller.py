from abc import ABC, abstractmethod
from libraries.view.scenes.abstract_scene import AbstractScene
from libraries.model.abstract_model import AbstractModel

class AbstractController(ABC):

    __scene: AbstractScene = None
    __model: AbstractModel = None

    def set_model(self, model: AbstractModel) -> AbstractModel:
        self.__model = model

    def set_scene(self, scene: AbstractScene) -> AbstractScene:
        self.__scene = scene

    def get_model(self) -> AbstractModel:
        return self.__model

    def get_scene(self) -> AbstractScene:
        return self.__scene
