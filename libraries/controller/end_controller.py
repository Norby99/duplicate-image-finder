from libraries.controller.abstract_controller import AbstractController

from libraries.view.scenes.scene_end import SceneEnd

class EndController(AbstractController):
    
    __scene: SceneEnd

    def __init__(self, scene: SceneEnd) -> None:
        self._set_scene(scene)

    def tick(self) -> bool:
        return False
    
    def _set_scene(self, scene: SceneEnd) -> None:
        self.__scene = scene

    def get_scene(self) -> SceneEnd:
        return self.__scene
    
    def _set_model(self, model: None) -> None:
        return None

    def get_model(self) -> None:
        return None
