from libraries.controller.abstract_controller import AbstractController
from libraries.utils.image_data import ImageData
from libraries.view.scenes.scene_result import SceneResult
from libraries.model.result_model import ResultModel

class ResultController(AbstractController):
    
    __model: ResultModel
    __scene: SceneResult

    __current_images: list[ImageData] = []

    def __init__(self, model: ResultModel, scene: SceneResult) -> None:
        self._set_scene(scene)
        self._set_model(model)

    def tick(self) -> bool:
        if self.__current_images == []:
            self.__set_next_images()
        return False
    
    def __set_next_images(self) -> None:
        self.__current_images = self.__model.get_next_two_images()
        self.__scene.set_images(self.__current_images)

    def _set_model(self, model: ResultModel) -> None:
        self.__model = model

    def _set_scene(self, scene: SceneResult) -> None:
        self.__scene = scene

    def get_model(self) -> ResultModel:
        return self.__model

    def get_scene(self) -> SceneResult:
        return self.__scene
