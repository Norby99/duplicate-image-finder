from abc import ABC, abstractmethod

class DuplicateImagesProvider(ABC):
    @abstractmethod
    def get_duplicate_images(self) -> list:
        pass
