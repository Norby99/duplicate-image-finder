import tkinter as tk

class ImageData:
     
    __image: tk.PhotoImage = None
    __image_name: str = None
    __image_size: str = None
    __image_dimensions: tuple = None

    def __init__(self, image: tk.PhotoImage, image_name: str, image_size: str, image_dimensions: tuple) -> None:
        self.__image = image
        self.__image_name = image_name
        self.__image_size = image_size
        self.__image_dimensions = image_dimensions
    
    def get_image(self) -> tk.PhotoImage:
        return self.__image

    def get_image_name(self) -> str:
        return self.__image_name
    
    def get_image_size(self) -> str:
        return self.__image_size
    
    def get_image_dimensions(self) -> tuple:
        return self.__image_dimensions
    
    def __str__(self) -> str:
        return self.__image_name + " " + self.__image_size
