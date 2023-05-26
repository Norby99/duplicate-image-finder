from libraries.controller.abstract_controller import AbstractController
from libraries.view.scenes.scene_setupper import SceneSetupper
from libraries.model.setupper import Setupper

class SetuperController(AbstractController):

    def __init__(self) -> None:
        self.set_scene(SceneSetupper())
        self.set_model(Setupper())
        self.get_scene().subscribe(self.get_model().set_variables)
