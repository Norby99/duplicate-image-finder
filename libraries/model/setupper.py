from libraries.model.abstract_model import AbstractModel
from libraries.model.providers.folder_provider import FolderProvider

class Setupper(AbstractModel, FolderProvider):

    __image_folder: str = ""
    __destination_path: str = ""

    def __init__(self) -> None:
        pass

    def set_variables(self, image_folder: str, destination_path: str) -> None:
        self.__image_folder = image_folder
        self.__destination_path = destination_path

    def get_image_folder(self) -> str:
        return self.__image_folder

    def get_destination_path(self) -> str:
        return self.__destination_path

    def ready(self) -> bool:
        return self.__image_folder != "" and self.__destination_path != ""
