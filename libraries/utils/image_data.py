import tkinter as tk
from PIL import Image
import math

class ImageData:
     
    __path: str
    __name: str
    __size: str
    __dimensions: tuple
    __hash: str

    def __init__(self, image_path: str, image_name: str, image_size: int, image_dimensions: tuple, hash: str) -> None:
        self.__path = image_path
        self.__name = image_name
        self.__size = convert_size(image_size)
        self.__dimensions = image_dimensions
        self.__hash = hash
    
    def get_image(self) -> tk.PhotoImage:
        # the image is not loaded into memory until this method is called
        return Image.open(self.__path)
    
    def get_path(self) -> str:
        return self.__path

    def get_name(self) -> str:
        return self.__name
    
    def get_size(self) -> str:
        return self.__size
    
    def get_dimensions(self) -> tuple:
        return self.__dimensions
    
    def get_hash(self) -> str:
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
