from libraries.model.abstract_model import AbstractModel

class Analiser(AbstractModel):

    __image_folder: str = ""

    def __init__(self, image_folder) -> None:
        self.__image_folder = image_folder

    def set_variables(self, image_folder, destination_path) -> None:
        pass

    def analise(self) -> None:
        pass

    def ready(self) -> bool:
        pass
