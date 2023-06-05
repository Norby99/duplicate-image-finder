from libraries.view.scenes.abstract_scene import AbstractScene
from libraries.utils.image_data import ImageData
import tkinter as tk

class SceneResult(AbstractScene):
    
        __window: tk.Tk

        __image1: ImageData
        __image2: ImageData
    
        __widgets: dict[str, tk.Widget] = {}

        __extend_window_size: list[int] = [1200, 1000]
    
        def __init__(self) -> None:
            self.__create_widgets()
    
        def setup(self, window: tk.Tk) -> None:
            print("aaaaa")
            self.__window = window
            self.__window.geometry(str(self.__extend_window_size[0]) + "x"  + str(self.__extend_window_size[1]))
            self.__packWidgets()

        def set_image1(self, image: ImageData) -> None:
            print(self.__widgets)
            self.__image1 = image
            self.__widgets["left_img"].configure(image=self.__image1.get_image())   # type: ignore

        def set_image2(self, image: ImageData) -> None:
            self.__image2 = image
    
        def __create_widgets(self) -> None:
            self.__widgets.update({"left_img": tk.Label(self.__window, background="white")})
            self.__widgets.update({"right_img": tk.Label(self.__window, background="white")})
            
        def __packWidgets(self) -> None:
            for i in self.__widgets.values():
                i.pack()
    
        def destroy(self) -> None:
            for i in self.__widgets.values():
                i.destroy()
