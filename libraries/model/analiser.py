from libraries.model.abstract_model import AbstractModel
from libraries.utils.image_data import ImageData

import imagehash
from PIL import Image
from collections import defaultdict
from threading import Thread

from os import listdir, path, stat
import warnings

class Analiser(AbstractModel):

    __image_folder: str = ""
    __image_extension: tuple = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')
    __ready: bool = False
    __max_threads: int = 1
    __images: list[ImageData] = []

    def __init__(self, core_count: int, image_folder: str) -> None:
        self.__image_folder = image_folder
        self.__max_threads = core_count

    def load_images(self) -> None:
        images_path = self.__get_images_path()
        thread_list = []
        chunk_size = int(len(images_path) / self.__max_threads)

        for i in range(0, len(images_path), chunk_size):
            thread_list.append(Thread(target=self.__threadable_load_images, args=(images_path[i:i + chunk_size],)))
            thread_list[-1].start()
        
        for thread in thread_list:
            thread.join()

    def compare_images(self) -> list[list[ImageData]]:
        #old_var = [images_name[i] for i, x in enumerate(images_hash) if images_hash.count(x) > 1] # O(n^2)
        #TODO: investigate for better performance
        old_var = defaultdict(list) # O(n)
        for i in self.__images:
            old_var[i.get_hash()].append(i)
        old_var_2 = {k:v for k,v in old_var.items() if len(v)>1}

        self.__ready = True

        return [[i for i in x] for x in old_var_2.values()]   # changing the index to the name outside of the loop above is a bit faster

    def __threadable_load_images(self, images_path: list[str]) -> None:
        for img in images_path:
            try:
                image = Image.open(img[0])
                self.__images.append(ImageData(img[0], img[1], stat(img[0]).st_size, image.size, imagehash.average_hash(image)))
            except Exception as e:
                print(e.args)
                warnings.warn("Probably the file is damaged: " + img[1])

    def __get_images_path(self) -> list[list[str]]:
        images_path = []
        for x in listdir(self.__image_folder):
            if x.endswith(self.__image_extension):
                images_path.append([path.join(self.__image_folder, x), x])

        return images_path

    def ready(self) -> bool:
        return self.__ready
