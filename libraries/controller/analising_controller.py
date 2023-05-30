""" Analising Controller """

from libraries.controller.abstract_controller import AbstractController
from libraries.view.scenes.scene_analiser import SceneAnaliser
from libraries.model.analiser import Analiser
from libraries.utils.image_data import ImageData

class AnalisingController(AbstractController):
    """ Analising Controller """

    __image_folder: str = ""
    __duplicate_images: list[ImageData] = []

    def __init__(self, max_threads, image_folder) -> None:
        self.__image_folder = image_folder

        self.set_scene(SceneAnaliser())
        self.set_model(Analiser(max_threads, self.__image_folder))

        print(self.__image_folder)

        self.get_scene().set_text("Loading images...")
        self.get_model().load_images()
        self.get_scene().set_text("Images loaded. Comparing Images...")
        self.__duplicate_images = self.get_model().compare_images()
        self.get_scene().set_text("Images compared.")

        for i in self.__duplicate_images:
            print(str(i[0].get_size()) + " " + str(i[1].get_size()))

    def get_duplicate_images(self) -> list[ImageData]:
        """ Returns the duplicate images. """
        return self.__duplicate_images
