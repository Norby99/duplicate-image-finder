from libraries.view.scenes.abstract_scene import AbstractScene
from libraries.utils.image_data import ImageData
from libraries.utils.imageTk_data import ImageTk_data
import tkinter as tk
from PIL import ImageTk

class SceneResult(AbstractScene):
    
        __window: tk.Tk

        __img1: ImageTk_data
        __img2: ImageTk_data
    
        __widgets: dict[str, tk.Widget]

        __extend_window_size: list[int] = [1200, 1000]
        __last_size: list[int] = [0, 0]
    
        def __init__(self) -> None:
            pass

        def setup(self, window: tk.Tk) -> None:
            self.__window = window
            #self.__create_widgets()
            self.__window.geometry(str(self.__extend_window_size[0]) + "x" + str(self.__extend_window_size[1]))
            #self.__packWidgets()

        def __set_image1(self, image: ImageData) -> None:
            self.__img1 = ImageTk_data(image, self.__window)
            self.__img1.setup_widgets([0, 0], "w")

        def __set_image2(self, image: ImageData) -> None:
            self.__img2 = ImageTk_data(image, self.__window)
            self.__img2.setup_widgets([0, 1], "e")

        def set_images(self, images: list[ImageData]) -> None:
            if len(images) != 2:
                raise ValueError("SceneResult.set_images: images list must have 2 elements.")
            self.__set_image1(images[0])
            self.__set_image2(images[1])
            self.resize_window_elements()
        
        def __calc_label_dimension(self, img_proportion: float) -> list:
            lower_border_size = 100
            x = int(self.__window.winfo_width() // 2)
            y = int(x // img_proportion)

            if (y > self.__window.winfo_height() - lower_border_size):
                y = self.__window.winfo_height() - lower_border_size
                x = int(y * img_proportion)

            dimension = [x, y]
            return dimension

        def resize_window_elements(self) -> None:
            self.__img1.resize(self.__calc_label_dimension(self.__img1.get_image_proportion()))
            self.__img2.resize(self.__calc_label_dimension(self.__img2.get_image_proportion()))

    
        def __create_widgets(self) -> None:
            self.__widgets = {"left_img": tk.Label(self.__window, background="white"),
                              "right_img": tk.Label(self.__window, background="white")}
            
        def __packWidgets(self) -> None:
            for i in self.__widgets.values():
                i.pack()

        def detects_resize(self) -> bool:
            if self.__last_size != [self.__window.winfo_width(), self.__window.winfo_height()]:
                self.__last_size = [self.__window.winfo_width(), self.__window.winfo_height()]
                return True 
            return False
    
        def destroy(self) -> None:
            for i in self.__widgets.values():
                i.destroy()
