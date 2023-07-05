from typing import Union
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

        self.get_scene().subscribe(self.remove_image)

    def tick(self) -> bool:
        if self.__current_images == []:
            if not self.__set_next_images():
                return True
        if self.__scene.detects_resize():
            self.__scene.resize_window_elements()
        return False
    
    def __set_next_images(self) -> bool:
        self.__current_images = self.__model.get_next_two_images()
        if len(self.__current_images) == 0:
            return False
        self.__scene.set_images(self.__current_images[0], self.__current_images[1])
        return True

    def remove_image(self, image: Union[None, ImageData]) -> None:
        self.get_scene().destroy(destroy_btn_skip=False)
        if image is not None:
            self.get_model().remove_image(image)
            self.get_model().delete_image(image)
            self.__current_images.remove(image)
        else:
            self.get_model().remove_current_image_group()
        
        self.__current_images.clear()

    def _set_model(self, model: ResultModel) -> None:
        self.__model = model

    def _set_scene(self, scene: SceneResult) -> None:
        self.__scene = scene

    def get_model(self) -> ResultModel:
        return self.__model

    def get_scene(self) -> SceneResult:
        return self.__scene
