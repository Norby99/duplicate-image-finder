from abc import ABC, abstractmethod

class AbstractFolderCollector(ABC):

    @abstractmethod
    def get_image_folder(self) -> str:
        pass

    @abstractmethod
    def get_destination_path(self) -> str:
        pass
