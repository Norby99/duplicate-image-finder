from libraries.controller.abstract_controller import AbstractController

from libraries.view.scenes.abstract_scene import AbstractScene
from libraries.view.scenes.scene_analiser import SceneAnaliser

from libraries.model.abstract_model import AbstractModel
from libraries.model.analiser import Analiser

from threading import Thread

class AnalisingController(AbstractController, Thread):

    __scene: SceneAnaliser = None
    __model: Analiser = None
    __image_folder: str = ""

    def __init__(self, max_threads, image_folder) -> None:

        Thread.__init__(self)

        self.__image_folder = image_folder

        self.__scene = SceneAnaliser()
        self.__model = Analiser(max_threads, self.__image_folder)

    def run(self):
        self.__model.analise()

    def get_model(self) -> AbstractModel:
        return self.__model

    def get_scene(self) -> AbstractScene:
        return self.__scene
