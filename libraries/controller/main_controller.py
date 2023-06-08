""" Main controller of the application. It is responsible for managing the application's flow. """

import multiprocessing
import tkinter as tk

from libraries.view.main_view import MainView
from libraries.utils.iterator import Iterator

from libraries.controller.abstract_controller import AbstractController
from libraries.controller.setup_controller import SetuperController
from libraries.controller.analising_controller import AnalisingController
from libraries.controller.result_controller import ResultController

from libraries.controller.providers.folder_provider import FolderProvider
from libraries.model.setupper import Setupper
from libraries.model.analiser import Analiser
from libraries.model.result_model import ResultModel

from libraries.view.scenes.scene_setupper import SceneSetupper
from libraries.view.scenes.scene_analiser import SceneAnaliser
from libraries.view.scenes.scene_result import SceneResult

from libraries.controller.providers.duplicate_images_provider import DuplicateImagesProvider

class MainController:
    """ Main controller of the application.
    It is responsible for managing the application's flow. """

    __root: tk.Tk

    __current_controller: AbstractController
    __data_collection: FolderProvider
    __duplicate_images: DuplicateImagesProvider
    __app: MainView
    __application_point: Iterator = Iterator(
        ["file_chooser", "analizing", "results"])
    __core_count = 1

    def __init__(self) -> None:
        self.__core_count = multiprocessing.cpu_count()
        self.__root = tk.Tk()
        self.__app = MainView(self.__root)

        self.update()
        self.main_loop()

        self.__root.mainloop()

    def main_loop(self) -> None:
        """ Main loop of the application. """
        if self.__current_controller.tick():
            self.__current_controller.get_scene().destroy()
            self.update()
        self.__root.after(100, self.main_loop)
        
    def update(self) -> None:
        """ Updates the application's state. """
        self.__application_point.next()
        if self.__application_point.current == "file_chooser":     # choosing path
            self.__current_controller = SetuperController(Setupper(), SceneSetupper())
            self.__data_collection = self.__current_controller.get_model()

        elif self.__application_point.current == "analizing":
            self.__current_controller = AnalisingController(
                Analiser(self.__core_count, self.__data_collection.get_image_folder()), SceneAnaliser())
            self.__duplicate_images = self.__current_controller

        elif self.__application_point.current == "results":
            self.__current_controller = ResultController(ResultModel(self.__duplicate_images.get_duplicate_images()), SceneResult())

        self.__app.set_scene(self.__current_controller.get_scene())
