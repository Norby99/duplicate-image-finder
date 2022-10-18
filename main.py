from libraries.GUI import GUI
from libraries.utils.iterator import Iterator
import multiprocessing

class Launcher:

    __app: GUI = None
    __application_point: Iterator = Iterator(["file_chooser"])

    def __init__(self) -> None:
        core_count = multiprocessing.cpu_count()
        self.__app = GUI(set_max_threads=core_count)

        next(self.__application_point)
        self.update()

        self.__app.window.mainloop()

    def update(self):
        if self.__application_point.current == "file_chooser":     # choosing path
            self.__app.create_path_widgets()

if __name__ == "__main__":
    launcher = Launcher()
