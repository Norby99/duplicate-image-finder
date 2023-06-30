from typing import Literal
from libraries.utils.image_data import ImageData
import tkinter as tk
from PIL import Image, ImageTk

#? imgage widget group?
class ImageTk_data(ImageData):

    __window: tk.Tk

    __img: ImageTk.PhotoImage

    __lb_img: tk.Label
    __lb_name: tk.Label
    __lb_details: tk.Label

    def __init__(self, image: ImageData, window: tk.Tk) -> None:
        super().__init__(image.get_path(), image.get_name(), image.get_size(), image.get_dimensions(), image.get_hash())
        self.__img = ImageTk.PhotoImage(image.get_image())
        self.__window = window

    def setup_widgets(self, grid_pos: list[int], sticky: Literal['nw', 'n', 'ne', 'w', 'center', 'e', 'sw', 's', 'se']) -> None:
        self.__lb_img = tk.Label(self.__window, image=self.__img, background="white")
        self.__lb_img.grid(row=grid_pos[0], column=grid_pos[1], sticky=sticky)

        self.__lb_name = tk.Label(self.__window, text=self.get_name(), font=("Helvetica", 12), background="white")
        self.__lb_name.grid(row=grid_pos[0] + 1, column=grid_pos[1], sticky=sticky)

        self.__lb_details = tk.Label(self.__window, text=self.get_size(), font=("Helvetica", 12), background="white")
        self.__lb_details.grid(row=grid_pos[0] + 2, column=grid_pos[1], sticky=sticky)

    def resize(self, size: list[int]) -> None:
        self.__img = ImageTk.PhotoImage(self.get_image(size))
        self.__lb_img.configure(image=self.__img)

    def get_image_Tk(self, size: list[int]=[0, 0]) -> ImageTk.PhotoImage:
        if size == [0, 0]:
            self.__img = ImageTk.PhotoImage(self.get_image())
        else:
            self.__img = ImageTk.PhotoImage(self.get_image(size))
        return self.__img
