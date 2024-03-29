from libraries.view.scenes.abstract_scene import AbstractScene
import tkinter as tk

class SceneAnaliser(AbstractScene):

    __window: tk.Tk
    __label: tk.Label

    def __init__(self) -> None:
        pass

    def set_text(self, text: str) -> None:
        self.__label.configure(text=text)

    def setup(self, window: tk.Tk) -> None:
        self.__window = window
        self.__create_widgets()

    def __create_widgets(self) -> None:
        self.__label = tk.Label(self.__window)
        self.__label.place(relx=.5, rely=.5, anchor="center")

    def destroy(self) -> None:
        self.__label.destroy()
