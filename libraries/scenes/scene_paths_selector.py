from libraries.scenes.abstract_scene import AbstractScene
import tkinter as tk
from tkinter import filedialog

class ScenePathsSelector(AbstractScene):

    __window: tk.Tk = None

    __image_folder: str = ""
    __destination_path: str = ""
    
    __widgets = []

    def __init__(self) -> None:
        pass

    def setup(self, window: tk.Tk) -> None:
        self.__window = window
        self.create_path_widgets()

    def destroy(self) -> None:
        for i in self.__widgets:
            i.destroy()

    def create_path_widgets(self) -> None:
        lbl_image_path = tk.Label(self.__window, text=self.__image_folder)
        btn_image_path = tk.Button(self.__window, text="Image folder", command=lambda: self.bind_button_to_label(filedialog.askdirectory(), self.__image_folder, lbl_image_path))

        lbl_dest_path = tk.Label(self.__window, text=self.__destination_path)
        btn_dest_path = tk.Button(self.__window, text="Destination folder", command=lambda: self.bind_button_to_label(filedialog.askdirectory(), self.__destination_path, lbl_dest_path))

        self.__widgets.extend([lbl_image_path, btn_image_path, lbl_dest_path, btn_dest_path])

        btn_image_path.grid(row=0, column=0, sticky=tk.EW, padx=5, pady=5)
        lbl_image_path.grid(row=0, column=1, padx=5, pady=5)
        btn_dest_path.grid(row=1, column=0, sticky=tk.EW, padx=5, pady=5)
        lbl_dest_path.grid(row=1, column=1, padx=5, pady=5)
        
    def bind_button_to_label(self, path, attribute, lable) -> None:
        attribute = path
        lable.configure(text=attribute)

    def get_image_folder(self) -> str:
        return self.__image_folder
    
    def get_destination_path(self) -> str:
        return self.__destination_path
