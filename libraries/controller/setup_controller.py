from libraries.controller.abstract_controller import AbstractController
from libraries.view.scenes.scene_setupper import SceneSetupper
from libraries.model.setupper import Setupper

class SetuperController(AbstractController):

    __scene: SceneSetupper = None
    __model: Setupper = None

    def __init__(self) -> None:
        self.__scene = SceneSetupper()
        self.__model = Setupper()

    def set_model(self, model) -> None:
        self.__model = model

    def set_scene(self, scene) -> None:
        self.__scene = scene
