from typing import Union
from PIL import Image
import math

import imagehash

class ImageData:
     
    __image: Image.Image
    __path: str
    __name: str
    __size: str
    __dimensions: tuple
    __hash: imagehash.ImageHash

    def __init__(self, image_path: str, image_name: str, image_size: Union[int, str], image_dimensions: tuple, hash: imagehash.ImageHash) -> None:
        self.__path = image_path
        self.__name = image_name
        self.__size = image_size if isinstance(image_size, str) else convert_size(image_size)
        self.__dimensions = image_dimensions
        self.__hash = hash

    def get_image(self, size: list[int]=[0, 0]) -> Image: # type: ignore
        """ Returns the image as a PIL Image object. If size is specified, the image will be resized to that size. """
        # the image is not loaded into memory until this method is called

        if not hasattr(self, "_"+self.__class__.__name__+"__image"):
            self.__image = Image.open(self.__path)

        if size == [0, 0]:
            return self.__image
        else:
            return self.__image.resize((size[0], size[1]), Image.ANTIALIAS) # Image.NEAREST is faster, but it looks bad
    
    def get_path(self) -> str:
        return self.__path

    def get_name(self) -> str:
        return self.__name
    
    def get_size(self) -> str:
        return self.__size
    
    def get_dimensions(self) -> tuple:
        return self.__dimensions
    
    def get_image_proportion(self) -> float:
        return self.__dimensions[0] / self.__dimensions[1]
    
    def get_hash(self) -> imagehash.ImageHash:
        return self.__hash
    
    def __str__(self) -> str:
        return self.__name + " " + self.__size

def convert_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])
