from libraries.model.abstract_model import AbstractModel

from libraries.model.providers.duplicate_images_provider import DuplicateImagesProvider
from libraries.utils.image_data import ImageData

class ResultModel(AbstractModel, DuplicateImagesProvider):

    __data_collector: list[list[ImageData]]
    
    def __init__(self, data_collector: list[list[ImageData]]) -> None:
        self.__data_collector = data_collector

    def get_next_two_images(self) -> list[ImageData]:
        if len(self.__data_collector) > 0:
            if len(self.__data_collector[0]) > 1:
                return [self.__data_collector[0][0], self.__data_collector[0][1]]
            return self.__data_collector[0]
        return []

    def get_duplicate_images(self) -> list[list[ImageData]]:
        return self.__data_collector
