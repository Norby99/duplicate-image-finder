import tkinter as tk
from PIL import Image

class ImageData:
     
    __image_path: tk.PhotoImage = None
    __image_name: str = None
    __image_size: str = None
    __image_dimensions: tuple = None

    def __init__(self, image_path: str, image_name: str, image_size: str, image_dimensions: tuple) -> None:
        self.__image_path = image_path
        self.__image_name = image_name
        self.__image_size = image_size
        self.__image_dimensions = image_dimensions
    
    def get_image(self) -> tk.PhotoImage:
        # the image is not loaded into memory until this method is called
        return Image.open(self.__image_path)
    
    def get_image_path(self) -> str:
        return self.__image_path

    def get_image_name(self) -> str:
        return self.__image_name
    
    def get_image_size(self) -> str:
        return self.__image_size
    
    def get_image_dimensions(self) -> tuple:
        return self.__image_dimensions
    
    def __str__(self) -> str:
        return self.__image_name + " " + self.__image_size
