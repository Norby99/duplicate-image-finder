from libraries.view.main_view import MainView
from libraries.utils.iterator import Iterator
from libraries.view.scenes.scene_setupper import SceneSetupper

from libraries.model.setupper import Setupper
import multiprocessing

class MainController:

    __app: MainView = None
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
            setupper = Setupper()
            scene = SceneSetupper()
            scene.subscribe(setupper.set_variables)
            self.__app.set_scene(scene)
