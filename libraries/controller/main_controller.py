from libraries.view.GUI import GUI
from libraries.utils.iterator import Iterator
from libraries.view.scenes.scene_paths_selector import ScenePathsSelector
import multiprocessing

class MainController:

    __app: GUI = None
    __application_point: Iterator = Iterator(["file_chooser", "mode_chooser"])

    def __init__(self) -> None:
        core_count = multiprocessing.cpu_count()
        self.__app = GUI(set_max_threads=core_count)

        next(self.__application_point)
        self.update()

        self.main_loop()

        self.__app.window.destroy()
        

    def main_loop(self):
        while self.__app.running:
            self.__app.update()

    def update(self):
        if self.__application_point.current == "file_chooser":     # choosing path
            self.__app.set_scene(ScenePathsSelector())
