from libraries.controller.abstract_controller import AbstractController
from libraries.view.scenes.scene_setupper import SceneSetupper
from libraries.model.setupper import Setupper

class SetuperController(AbstractController):

    __scene: SceneSetupper = None
    __model: Setupper = None

    def __init__(self) -> None:
        self.__scene = SceneSetupper()
        self.__model = Setupper()
        self.__scene.subscribe(self.__model.set_variables)

    def get_model(self) -> None:
        return self.__model

    def get_scene(self) -> None:
        return self.__scene
