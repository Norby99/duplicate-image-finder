from libraries.view.main_view import MainView
from libraries.utils.iterator import Iterator

from libraries.controller.setup_controller import SetuperController
from libraries.controller.abstract_controller import AbstractController

import multiprocessing

class MainController:

    __current_controller: AbstractController = None
    __application_point: Iterator = Iterator(["file_chooser", "mode_chooser"])

    def __init__(self) -> None:
        core_count = multiprocessing.cpu_count()
        self.__app = MainView(set_max_threads=core_count)

        next(self.__application_point)
        self.update()

        self.main_loop()

        self.__app.window.destroy()
        

    def main_loop(self):
        while self.__app.running:
            self.__app.update()

    def update(self):
        if self.__application_point.current == "file_chooser":     # choosing path
            self.__current_controller = SetuperController()
            self.__app.set_scene(self.__current_controller.get_scene())
