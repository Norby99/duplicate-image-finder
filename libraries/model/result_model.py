from libraries.model.abstract_model import AbstractModel

from libraries.utils.image_data import ImageData

class ResultModel(AbstractModel):

    __data_collector: list[list[ImageData]]
    
    def __init__(self, data_collector: list[list[ImageData]]) -> None:
        self.__data_collector = data_collector

    def get_duplicate_images(self) -> list[list[ImageData]]:
        return self.__data_collector
