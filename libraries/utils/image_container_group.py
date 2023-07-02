from typing import Literal
from libraries.utils.image_data import ImageData
import tkinter as tk
from PIL import ImageTk

class ImageContainerGroup():

    __window: tk.Tk
    __img_data: ImageData

    __img: ImageTk.PhotoImage

    __lb_img: tk.Label
    __lb_details: tk.Label

    def __init__(self, image: ImageData, window: tk.Tk) -> None:
        self.__img_data = image
        self.__img = ImageTk.PhotoImage(image.get_image())
        self.__window = window

    def setup_widgets(self, grid_pos: list[int], sticky: Literal['nw', 'n', 'ne', 'w', 'center', 'e', 'sw', 's', 'se']) -> None:
        self.__lb_img = tk.Label(self.__window, image=self.__img, background="white")
        self.__lb_img.grid(row=grid_pos[0], column=grid_pos[1], sticky=sticky)

        self.__lb_details = tk.Label(self.__window, text=self.__img_data.get_name() + "\n" + self.__img_data.get_size(), font=("Helvetica", 12), background="white")
        self.__lb_details.grid(row=grid_pos[0] + 2, column=grid_pos[1], sticky=sticky)

    def resize(self) -> None:
        self.__img = ImageTk.PhotoImage(self.__img_data.get_image(self.__calc_label_dimension(self.__img_data.get_image_proportion())))
        self.__lb_img.configure(image=self.__img)

    def get_image_Tk(self, size: list[int]=[0, 0]) -> ImageTk.PhotoImage:
        if size == [0, 0]:
            self.__img = ImageTk.PhotoImage(self.__img_data.get_image())
        else:
            self.__img = ImageTk.PhotoImage(self.__img_data.get_image(size))
        return self.__img
    
    def __calc_label_dimension(self, img_proportion: float) -> list:
        lower_border_size = 100
        x = int(self.__window.winfo_width() // 2)
        y = int(x // img_proportion)

        if (y > self.__window.winfo_height() - lower_border_size):
            y = self.__window.winfo_height() - lower_border_size
            x = int(y * img_proportion)

        dimension = [x, y]
        return dimension
