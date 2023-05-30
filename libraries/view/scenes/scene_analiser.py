from libraries.view.scenes.abstract_scene import AbstractScene
import tkinter as tk

class SceneAnaliser(AbstractScene):

    __window: tk.Tk

    __displayed_text: str = ""
    __widgets: list = []

    def __init__(self) -> None:
        pass

    def set_text(self, text: str) -> None:
        self.__displayed_text = text

    def setup(self, window: tk.Tk) -> None:
        self.__window = window
        self.__create_widgets()

    def __create_widgets(self) -> None:
        self.__widgets.append(tk.Label(self.__window, text=self.__displayed_text))
        self.__widgets[-1].pack()

    def destroy(self) -> None:
        for i in self.__widgets:
            i.destroy()
