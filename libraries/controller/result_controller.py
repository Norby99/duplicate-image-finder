from libraries.controller.abstract_controller import AbstractController
from libraries.utils.image_data import ImageData
from libraries.view.scenes.scene_result import SceneResult
from libraries.model.result_model import ResultModel

from libraries.controller.observable import Observable

class ResultController(AbstractController):
    
    __model: ResultModel
    __scene: SceneResult

    __current_images: list[ImageData] = []

    def __init__(self, model: ResultModel, scene: SceneResult) -> None:
        self._set_scene(scene)
        self._set_model(model)

        self.get_scene().subscribe(self.remove_image)

    def tick(self) -> bool:
        if self.__current_images == []:
            self.__set_next_images()
        if self.__scene.detects_resize():
            self.__scene.resize_window_elements()
        return False
    
    def __set_next_images(self) -> None:
        self.__current_images = self.__model.get_next_two_images()
        self.__scene.set_images(self.__current_images[0], self.__current_images[1])

    def remove_image(self, image_index: int) -> None:
        """ Remove the image with the given index,
            if image_index is -1, remove both images but only from scene """
        if image_index == -1:
            pass
        print("remove image")

    def _set_model(self, model: ResultModel) -> None:
        self.__model = model

    def _set_scene(self, scene: SceneResult) -> None:
        self.__scene = scene

    def get_model(self) -> ResultModel:
        return self.__model

    def get_scene(self) -> SceneResult:
        return self.__scene
