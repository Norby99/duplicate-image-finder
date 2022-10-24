from libraries.model.abstract_model import AbstractModel

class Analiser(AbstractModel):

    __image_folder: str = ""
    __destination_path: str = ""

    def set_variables(self, image_folder, destination_path) -> None:
        self.__image_folder = image_folder
        self.__destination_path = destination_path

    def analise(self) -> None:
        pass

    def ready(self) -> bool:
        pass
