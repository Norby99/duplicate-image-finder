from libraries.model.abstract_model import AbstractModel

from libraries.model.providers.duplicate_images_provider import DuplicateImagesProvider
from libraries.model.providers.folder_provider import FolderProvider
from libraries.utils.image_data import ImageData

import shutil, os

class ResultModel(AbstractModel, DuplicateImagesProvider):

    __data_collector: list[list[ImageData]]
    __folder_provider: FolderProvider
    
    def __init__(self, data_collector: list[list[ImageData]], folder_provider: FolderProvider) -> None:
        self.__data_collector = data_collector
        self.__folder_provider = folder_provider

    def get_next_two_images(self) -> list[ImageData]:
        if len(self.__data_collector) > 0:
            if len(self.__data_collector[0]) > 1:
                return [self.__data_collector[0][0], self.__data_collector[0][1]]
            return self.__data_collector[0]
        return []

    def get_duplicate_images(self) -> list[list[ImageData]]:
        return self.__data_collector
    
    def remove_current_image_group(self) -> None:
        if len(self.__data_collector) > 0:
            self.__data_collector.pop(0)

    def remove_image(self, image_data: ImageData) -> None:
        for i in self.__data_collector:
            if image_data in i:
                i.remove(image_data)
                if len(i) == 1:
                    self.__data_collector.remove(i)
                break
    
    def delete_image(self, image_data: ImageData) -> None:
        if not self.__check_image_path(image_data):
            shutil.move(image_data.get_path(), self.__folder_provider.get_destination_path())
        else:
            print("Image already in destination folder")

    def __check_image_path(self, image_data: ImageData) -> bool:
        return image_data.get_path() == os.path.join(self.__folder_provider.get_destination_path(), image_data.get_name())
