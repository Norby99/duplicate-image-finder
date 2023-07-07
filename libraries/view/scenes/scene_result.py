from libraries.view.scenes.abstract_scene import AbstractScene
from libraries.utils.image_data import ImageData
from libraries.view.image_container_group import ImageContainerGroup
import tkinter as tk

from libraries.controller.observable import Observable

class SceneResult(AbstractScene, Observable):
    
        __window: tk.Tk

        __img1: ImageContainerGroup
        __img2: ImageContainerGroup

        __resize_ready: bool = False
    
        __btn_skip: tk.Button

        __extend_window_size: list[int] = [1200, 1000]
    
        def __init__(self) -> None:
            pass

        def setup(self, window: tk.Tk) -> None:
            self.__window = window
            self.__create_widgets()
            self.__window.geometry(str(self.__extend_window_size[0]) + "x" + str(self.__extend_window_size[1]))

            self.__window.bind("<Configure>", lambda e: self.resize_window_elements())

        def set_images(self, image1: ImageData, image2: ImageData) -> None:
            self.__img1 = ImageContainerGroup(image1, self.__window, self)
            self.__img1.setup_widgets([0, 0], "w")

            self.__img2 = ImageContainerGroup(image2, self.__window, self)
            self.__img2.setup_widgets([0, 1], "e")

            self.__resize_ready = True
            self.resize_window_elements()

        def resize_window_elements(self) -> None:
            if self.__resize_ready:
                self.__img1.resize()
                self.__img2.resize()
                self.__btn_skip.place(x=self.__window.winfo_width()/2, y=self.__window.winfo_height() - 20, anchor='center')
    
        def __create_widgets(self) -> None:
            self.__btn_skip = tk.Button(self.__window, text="Skip", command=lambda: self.__send_skip_form())
            self.__btn_skip.grid()
        
        def __send_skip_form(self) -> None:
            self.fire(image=None)
            self.destroy(only_images=True)

        def destroy(self, only_images: bool=False) -> None:
            if not only_images:
                self.__window.unbind("<Configure>")
                self.__btn_skip.destroy()
            self.__img1.destroy()
            self.__img2.destroy()
