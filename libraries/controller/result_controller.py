from libraries.controller.abstract_controller import AbstractController
from libraries.view.scenes.scene_result import SceneResult

class ResultController(AbstractController):
    
        def __init__(self) -> None:
            self.set_scene(SceneResult())
            self.set_model(None)
