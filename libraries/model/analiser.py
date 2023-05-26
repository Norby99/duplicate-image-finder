from libraries.model.abstract_model import AbstractModel

import imagehash
from PIL import Image

from threading import Thread

from os import listdir, path
import warnings

class Analiser(AbstractModel):

    __image_folder: str = ""
    __image_extension: tuple = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')
    __ready: bool = False
    __max_threads: int = 1
    __images: list = []

    def __init__(self, core_count, image_folder) -> None:
        self.__image_folder = image_folder
        self.__max_threads = core_count

    def set_variables(self, image_folder, destination_path) -> None:
        pass

    def analise(self) -> None:
        images_path = self.__get_images_path()
        thread_list = []
        chunk_size = int(len(images_path) / self.__max_threads)

        for i in range(0, len(images_path), chunk_size):
            thread_list.append(Thread(target=self.__load_images, args=(images_path[i:i + chunk_size],)))
            thread_list[-1].start()
        
        for thread in thread_list:
            thread.join()
        print("Done")

    def __load_images(self, images_path: list) -> None:
        for img in images_path:
            try:
                self.__images.append([imagehash.average_hash(Image.open(img[0])), img[1]])
            except Exception as e:
                print(e.args)
                warnings.warn(("Probably the file is damaged: ", img[1]))

    def __get_images_path(self) -> None:
        images_path = []
        for x in listdir(self.__image_folder):
            if x.endswith(self.__image_extension):
                images_path.append([path.join(self.__image_folder, x), x])
        return images_path

    def ready(self) -> bool:
        return self.__ready
