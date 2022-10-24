from libraries.view.scenes.abstract_scene import AbstractScene
import tkinter as tk


class SceneAnaliser(AbstractScene):

    __window: tk.Tk = None

    __widgets: list = []

    def __init__(self) -> None:
        pass

    def setup(self, window: tk.Tk) -> None:
        self.__window = window
        self.__create_widgets()

    def __create_widgets(self) -> None:
        pass

    def destroy(self) -> None:
        for i in self.__widgets:
            i.destroy()
