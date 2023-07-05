from libraries.view.scenes.abstract_scene import AbstractScene

import tkinter as tk

class SceneEnd(AbstractScene):

    __window: tk.Tk

    __lb_no_more_images: tk.Label

    def __init__(self) -> None:
        pass

    def setup(self, window: tk.Tk) -> None:
        self.__window = window
        self.__create_widgets()

    def __create_widgets(self) -> None:
        self.__lb_no_more_images = tk.Label(self.__window, text="No more images to analize", font=("Arial", 11))
        self.__lb_no_more_images.place(relx=.5, rely=.5, anchor="center")

    def destroy(self) -> None:
        self.__lb_no_more_images.destroy()
