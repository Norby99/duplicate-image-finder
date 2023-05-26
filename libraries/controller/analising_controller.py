from libraries.controller.abstract_controller import AbstractController
from libraries.view.scenes.scene_analiser import SceneAnaliser
from libraries.model.analiser import Analiser

class AnalisingController(AbstractController):

    __image_folder: str = ""

    def __init__(self, max_threads, image_folder) -> None:
        self.__image_folder = image_folder

        self.set_scene(SceneAnaliser())
        self.set_model(Analiser(max_threads, self.__image_folder))

        print(self.__image_folder)

        self.get_scene().set_text("Loading images...")
        self.get_model().analise()
        self.get_scene().set_text("Done")
