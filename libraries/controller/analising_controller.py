""" Analising Controller """

import threading

from libraries.controller.abstract_controller import AbstractController
from libraries.view.scenes.scene_analiser import SceneAnaliser
from libraries.model.analiser import Analiser
from libraries.utils.image_data import ImageData

from libraries.utils.iterator import Iterator

import time

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
        if not hasattr(self, "_"+self.__class__.__name__+"__working_thread") or not self.__working_thread.is_alive():
            self.__stages.next()
            self.__main()
        return self.__stages.current == "done"
    
    def __main(self) -> None:
        if self.__stages.current == "loading":
            self.load_time_start = time.time()
            self.get_scene().set_text("Loading images...")
            self.__working_thread = threading.Thread(target=self.__model.load_images)
            self.__working_thread.start()
        elif self.__stages.current == "comparing":
            print(f"Load time: {time.time()-self.load_time_start} s")
            self.compare_time_start = time.time()
            self.get_scene().set_text("Comparing images...")
            self.__working_thread = threading.Thread(target=self.__model.compare_images)
            self.__working_thread.start()
        elif self.__stages.current == "done":
            print(f"Compare time: {time.time()-self.compare_time_start} s")
            print(f"Total time: {time.time()-self.load_time_start} s")
            self.get_scene().set_text("Done!")
    
    def _set_model(self, model: Analiser) -> None:
        self.__model = model

    def _set_scene(self, scene: SceneAnaliser) -> None:
        self.__scene = scene

    def get_model(self) -> Analiser:
        return self.__model

    def get_scene(self) -> SceneAnaliser:
        return self.__scene
