from libraries.controller.abstract_controller import AbstractController

from libraries.view.scenes.abstract_scene import AbstractScene
from libraries.view.scenes.scene_analiser import SceneAnaliser

from libraries.model.abstract_model import AbstractModel
from libraries.model.analiser import Analiser

class AnalisingController(AbstractController):

    __scene: SceneAnaliser = None
    __model: Analiser = None
    __image_folder: str = ""

    def __init__(self) -> None:
        self.__scene = SceneAnaliser()
        self.__model = Analiser(self.__image_folder)

        print(self.__image_folder)

        self.__scene.set_text("Loading images...")
        self.__model.analise()

    def get_model(self) -> AbstractModel:
        return self.__model

    def get_scene(self) -> AbstractScene:
        return self.__scene
