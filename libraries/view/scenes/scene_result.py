from libraries.view.scenes.abstract_scene import AbstractScene
from libraries.utils.image_data import ImageData
import tkinter as tk
from PIL import ImageTk

class SceneResult(AbstractScene):
    
        __window: tk.Tk

        __image1: ImageData
        __image2: ImageData
    
        __widgets: dict[str, tk.Widget]

        __extend_window_size: list[int] = [1200, 1000]
    
        def __init__(self) -> None:
            pass
    
        def setup(self, window: tk.Tk) -> None:
            self.__window = window
            self.__create_widgets()
            self.__window.geometry(str(self.__extend_window_size[0]) + "x" + str(self.__extend_window_size[1]))
            self.__packWidgets()

        def __set_image1(self, image: ImageData) -> None:
            self.__image1 = image
            photo = ImageTk.PhotoImage(self.__image1.get_image())
            self.__widgets["left_img"].configure(image=photo)   # type: ignore
            self.__widgets["left_img"].image = photo    # type: ignore  # it is necessary to keep a reference to the image

        def __set_image2(self, image: ImageData) -> None:
            self.__image2 = image
            photo = ImageTk.PhotoImage(self.__image2.get_image())
            self.__widgets["right_img"].configure(image=photo)   # type: ignore
            self.__widgets["right_img"].image = photo    # type: ignore  # it is necessary to keep a reference to the image

        def set_images(self, images: list[ImageData]) -> None:
            if len(images) != 2:
                raise ValueError("SceneResult.set_images: images list must have 2 elements.")
            self.__set_image1(images[0])
            self.__set_image2(images[1])
    
        def __create_widgets(self) -> None:
            self.__widgets = {"left_img": tk.Label(self.__window, background="white"),
                              "right_img": tk.Label(self.__window, background="white")}
            
        def __packWidgets(self) -> None:
            for i in self.__widgets.values():
                i.pack()
    
        def destroy(self) -> None:
            for i in self.__widgets.values():
                i.destroy()
