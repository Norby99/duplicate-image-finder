import tkinter as tk

from libraries.view.scenes.abstract_scene import AbstractScene

#TODO: this class needs a lot of refactoring
class MainView():

    __window: tk.Tk

    __analizing_methods: dict = { "Duplicate" : True, "Similar" : False }
    mini_window_size = [300, 200]
    __current_scene: AbstractScene
    
    def __init__(self, window: tk.Tk) -> None:

        self.__window = window
        self.__window.title("Image Detector")
        self.__window.geometry(str(self.mini_window_size[0]) + "x" + str(self.mini_window_size[1]))
        self.__window.configure(background="white")

    def set_scene(self, scene: AbstractScene) -> None:
        """ Sets the current scene of the application."""
        if hasattr(self, "__current_scene"):
            self.__current_scene.destroy()
            self.__window.geometry(str(self.mini_window_size[0]) + "x" + str(self.mini_window_size[1]))
        self.__current_scene = scene
        self.__current_scene.setup(self.__window)

    def get_scene(self) -> AbstractScene:
        return self.__current_scene
    
    def destroy(self) -> None:
        self.__current_scene.destroy()
        self.__window.destroy()
