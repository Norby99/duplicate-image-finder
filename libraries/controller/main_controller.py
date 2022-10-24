from libraries.view.main_view import MainView
from libraries.utils.iterator import Iterator

from libraries.controller.abstract_controller import AbstractController
from libraries.controller.setup_controller import SetuperController
from libraries.controller.analising_controller import AnalisingController

import multiprocessing

class MainController:

    __current_controller: AbstractController = None
    __app: MainView = None
    __application_point: Iterator = Iterator(["file_chooser", "analizing"])

    def __init__(self) -> None:
        core_count = multiprocessing.cpu_count()
        self.__app = MainView(set_max_threads=core_count)

        self.update()

        self.main_loop()

        self.__app.window.destroy()

    def main_loop(self):
        while self.__app.running:
            self.__app.update()
            if self.__current_controller.get_model().ready():
                self.__current_controller.get_scene().destroy()
                self.update()

    def update(self):
        next(self.__application_point)
        if self.__application_point.current == "file_chooser":     # choosing path
            self.__current_controller = SetuperController()
            self.__app.set_scene(self.__current_controller.get_scene())

        elif self.__application_point.current == "analizing":
            self.__current_controller = AnalisingController()
            self.__app.set_scene(self.__current_controller.get_scene())
