from libraries.controller.abstract_controller import AbstractController

from libraries.view.scenes.scene_setupper import SceneSetupper
from libraries.view.scenes.abstract_scene import AbstractScene

from libraries.model.abstract_model import AbstractModel
from libraries.model.setupper import Setupper


class SetuperController(AbstractController):

    __scene: SceneSetupper = None
    __model: Setupper = None

    def __init__(self) -> None:
        self.__scene = SceneSetupper()
        self.__model = Setupper()
        self.__scene.subscribe(self.__model.set_variables)

    def get_model(self) -> AbstractModel:
        return self.__model

    def get_scene(self) -> AbstractScene:
        return self.__scene
