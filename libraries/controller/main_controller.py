""" Main controller of the application. It is responsible for managing the application's flow. """

import multiprocessing

from libraries.view.main_view import MainView
from libraries.utils.iterator import Iterator

from libraries.controller.abstract_controller import AbstractController
from libraries.controller.setup_controller import SetuperController
from libraries.controller.analising_controller import AnalisingController
from libraries.controller.result_controller import ResultController

from libraries.model.abstract_data_collector import AbstractDataCollector
from libraries.model.setupper import Setupper
from libraries.model.analiser import Analiser
from libraries.model.result_model import ResultModel

from libraries.view.scenes.scene_setupper import SceneSetupper
from libraries.view.scenes.scene_analiser import SceneAnaliser
from libraries.view.scenes.scene_result import SceneResult

class MainController:
    """ Main controller of the application.
    It is responsible for managing the application's flow. """

    __current_controller: AbstractController
    __data_collection: AbstractDataCollector
    __app: MainView
    __application_point: Iterator = Iterator(
        ["file_chooser", "analizing", "results"])
    __core_count = 1

    def __init__(self) -> None:
        self.__core_count = multiprocessing.cpu_count()
        self.__app = MainView()

        self.update()
        self.main_loop()

        self.__app.destroy()

    def main_loop(self) -> None:
        """ Main loop of the application. """
        while self.__app.running:
            self.__app.update()
            if self.__current_controller.get_model().ready():
                self.__current_controller.get_scene().destroy()
                self.update()

    def update(self) -> None:
        """ Updates the application's state. """
        next(self.__application_point)
        if self.__application_point.current == "file_chooser":     # choosing path
            self.__current_controller = SetuperController(Setupper(), SceneSetupper())
            self.__data_collection = self.__current_controller.get_model()

        elif self.__application_point.current == "analizing":
            self.__current_controller = AnalisingController(
                Analiser(self.__core_count, self.__data_collection.get_image_folder()), SceneAnaliser())

        elif self.__application_point.current == "results":
            self.__current_controller = ResultController(ResultModel(), SceneResult())
        
        self.__app.set_scene(self.__current_controller.get_scene())
