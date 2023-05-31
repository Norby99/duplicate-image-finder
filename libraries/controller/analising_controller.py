""" Analising Controller """

from libraries.controller.abstract_controller import AbstractController
from libraries.view.scenes.scene_analiser import SceneAnaliser
from libraries.model.analiser import Analiser
from libraries.utils.image_data import ImageData

class AnalisingController(AbstractController):
    """ Analising Controller """

    __duplicate_images: list[list[ImageData]] = []

    def __init__(self, model: Analiser, scene: SceneAnaliser) -> None:

        self._set_scene(scene)
        self._set_model(model)

        self.get_scene().set_text("Loading images...")
        self.get_model().load_images()
        self.get_scene().set_text("Images loaded. Comparing Images...")
        self.__duplicate_images = self.get_model().compare_images()
        print(type(self.__duplicate_images))
        self.get_scene().set_text("Images compared.")

        for i in self.__duplicate_images:
            print(str(i[0].get_size()) + " " + str(i[1].get_size()))

    def get_duplicate_images(self) -> list[list[ImageData]]:
        """ Returns the duplicate images. """
        return self.__duplicate_images
    
    def _set_model(self, model: Analiser) -> None:
        self.__model = model

    def _set_scene(self, scene: SceneAnaliser) -> None:
        self.__scene = scene

    def get_model(self) -> Analiser:
        return self.__model

    def get_scene(self) -> SceneAnaliser:
        return self.__scene
