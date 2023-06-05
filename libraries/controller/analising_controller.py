""" Analising Controller """

import threading

from libraries.controller.abstract_controller import AbstractController
from libraries.view.scenes.scene_analiser import SceneAnaliser
from libraries.model.analiser import Analiser
from libraries.utils.image_data import ImageData

from libraries.utils.iterator import Iterator

class AnalisingController(AbstractController):
    """ Analising Controller """

    __duplicate_images: list[list[ImageData]] = []
    __stages: Iterator = Iterator(["loading", "comparing", "done"])
    __working_thread: threading.Thread

    def __init__(self, model: Analiser, scene: SceneAnaliser) -> None:

        self._set_scene(scene)
        self._set_model(model)

    def tick(self) -> bool:
        """ Tick of the controller.
            Returns True if the controller is ready. """
        if not hasattr(self, "__working_thread") or not self.__working_thread.is_alive():
            self.__stages.next()
            self.__main()
            return False
        return self.__stages.current == "done"
    
    def __main(self) -> None:
        if self.__stages.current == "loading":
            self.get_scene().set_text("Loading images...")
            self.__working_thread = threading.Thread(target=self.__model.load_images)
            self.__working_thread.start()
        elif self.__stages.current == "comparing":
            self.get_scene().set_text("Comparing images...")
            self.__working_thread = threading.Thread(target=self.__model.compare_images)
            self.__working_thread.start()
        elif self.__stages.current == "done":
            self.get_scene().set_text("Done!")

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
