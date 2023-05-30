from libraries.view.scenes.abstract_scene import AbstractScene
from libraries.utils.image_data import ImageData
import tkinter as tk

class SceneResult(AbstractScene):
    
        __window: tk.Tk

        __image1: ImageData
        __image2: ImageData
    
        __widgets: list = []
    
        def __init__(self) -> None:
            pass
    
        def setup(self, window: tk.Tk) -> None:
            self.__window = window
            self.__create_widgets()

        def set_image1(self, image: ImageData) -> None:
            self.__image1 = image

        def set_image2(self, image: ImageData) -> None:
            self.__image2 = image
    
        def __create_widgets(self) -> None:
            self.__widgets.append(tk.Label(self.__window, text=self.__displayed_text))
            self.__widgets[-1].pack()
    
        def destroy(self) -> None:
            for i in self.__widgets:
                i.destroy()
