from libraries.view.scenes.abstract_scene import AbstractScene
from libraries.utils.image_data import ImageData
from libraries.utils.image_container_group import ImageContainerGroup
import tkinter as tk

from libraries.controller.observable import Observable
    
        __window: tk.Tk

        __image_remover: Observable
        __img1: ImageContainerGroup
        __img2: ImageContainerGroup
    

        __extend_window_size: list[int] = [1200, 1000]
        __last_size: list[int] = [0, 0]
    
        def __init__(self) -> None:
            pass

        def setup(self, window: tk.Tk) -> None:
            self.__window = window
            self.__window.geometry(str(self.__extend_window_size[0]) + "x" + str(self.__extend_window_size[1]))
            #self.__packWidgets()

        def set_image_remover(self, image_remover: Observable) -> None:
            self.__image_remover = image_remover

        def set_images(self, image1: ImageData, image2: ImageData) -> None:
            self.__img1.setup_widgets([0, 0], "w")

            self.__img2.setup_widgets([0, 1], "e")

            self.__set_image2(images[1])
            self.resize_window_elements()

        def resize_window_elements(self) -> None:
            self.__img1.resize()
            self.__img2.resize()

    
        def __create_widgets(self) -> None:
            self.__btn_skip = tk.Button(self.__window, text="Skip", command=lambda: self.__send_form())
            self.__btn_skip.grid()

        def __send_form(self) -> None:

        def detects_resize(self) -> bool:
            if self.__last_size != [self.__window.winfo_width(), self.__window.winfo_height()]:
                self.__last_size = [self.__window.winfo_width(), self.__window.winfo_height()]
                return True 
            return False

        def destroy(self) -> None:
            self.__btn_skip.destroy()
