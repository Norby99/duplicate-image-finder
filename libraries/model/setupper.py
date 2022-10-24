from libraries.model.abstract_model import AbstractModel

class Setupper(AbstractModel):

    __image_folder: str = ""
    __destination_path: str = ""

    def __init__(self) -> None:
        pass

    def set_variables(self, image_folder: str, destination_path: str) -> None:
        self.__image_folder = image_folder
        self.__destination_path = destination_path

    def ready(self) -> bool:
        return self.__image_folder != "" and self.__destination_path != ""
