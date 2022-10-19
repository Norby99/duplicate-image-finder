from libraries.view.GUI import GUI
from libraries.utils.iterator import Iterator
from libraries.scenes.scene_paths_selector import ScenePathsSelector
import multiprocessing

class Launcher:

    __app: GUI = None
    __application_point: Iterator = Iterator(["file_chooser"])

    def __init__(self) -> None:
        core_count = multiprocessing.cpu_count()
        self.__app = GUI(set_max_threads=core_count)

        next(self.__application_point)
        self.update()

        while self.__app.running:
            self.__app.update()

        self.__app.window.destroy()

    def update(self):
        if self.__application_point.current == "file_chooser":     # choosing path
            self.__app.set_scene(ScenePathsSelector())

if __name__ == "__main__":
    launcher = Launcher()
