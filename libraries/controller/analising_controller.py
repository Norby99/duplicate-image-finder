from libraries.controller.abstract_controller import AbstractController

from libraries.view.scenes.abstract_scene import AbstractScene
from libraries.view.scenes.scene_analiser import SceneAnaliser

from libraries.model.abstract_model import AbstractModel
from libraries.model.analiser import Analiser

class AnalisingController(AbstractController):

    __scene: SceneAnaliser = None
    __model: Analiser = None

    def __init__(self) -> None:
        self.__scene = SceneAnaliser()
        self.__model = Analiser()

    def get_model(self) -> AbstractModel:
        return self.__model

    def get_scene(self) -> AbstractScene:
        return self.__scene
