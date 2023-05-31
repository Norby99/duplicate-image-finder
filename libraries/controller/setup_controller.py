from libraries.controller.abstract_controller import AbstractController
from libraries.view.scenes.scene_setupper import SceneSetupper
from libraries.model.setupper import Setupper

class SetuperController(AbstractController):

    __scene: SceneSetupper
    __model: Setupper

    def __init__(self, model: Setupper, scene: SceneSetupper) -> None:
        self._set_scene(scene)
        self._set_model(model)
        print(type(self.get_model().set_variables))
        self.get_scene().subscribe(self.get_model().set_variables)

    def _set_model(self, model: Setupper) -> None:
        self.__model = model

    def _set_scene(self, scene: SceneSetupper) -> None:
        self.__scene = scene

    def get_model(self) -> Setupper:
        return self.__model

    def get_scene(self) -> SceneSetupper:
        return self.__scene
