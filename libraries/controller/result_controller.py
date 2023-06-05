from libraries.controller.abstract_controller import AbstractController
from libraries.view.scenes.scene_result import SceneResult
from libraries.model.result_model import ResultModel

class ResultController(AbstractController):
    
    __model: ResultModel
    __scene: SceneResult

    def __init__(self, model: ResultModel, scene: SceneResult) -> None:
        self._set_scene(scene)
        self._set_model(model)

        for i in self.__model.get_duplicate_images():
            while len(i) > 0:
                self.__scene.set_image1(i[0])
                self.__scene.set_image2(i[1])

    def tick(self) -> None:
        pass

    def _set_model(self, model: ResultModel) -> None:
        self.__model = model

    def _set_scene(self, scene: SceneResult) -> None:
        self.__scene = scene

    def get_model(self) -> ResultModel:
        return self.__model

    def get_scene(self) -> SceneResult:
        return self.__scene
