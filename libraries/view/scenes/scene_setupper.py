from libraries.view.scenes.abstract_scene import AbstractScene
from libraries.controller.observable import Observable
import tkinter as tk
from tkinter import filedialog

class SceneSetupper(AbstractScene, Observable):

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
        self.__window.columnconfigure(1, weight=1)
        self.__window.rowconfigure(1, weight=1)

        lbl_image_path = tk.Label(self.__window, text=self.__image_folder)
        btn_image_path = tk.Button(self.__window, text="Image folder", command=lambda: self.set_image_folder(filedialog.askdirectory(), lbl_image_path))
        
        lbl_dest_path = tk.Label(self.__window, text=self.__destination_path)
        btn_dest_path = tk.Button(self.__window, text="Destination folder", command=lambda: self.set_destination_path(filedialog.askdirectory(), lbl_dest_path))

        btn_radio1 = tk.Radiobutton(self.__window, text="test", variable="test", value="test")
        btn_radio2 = tk.Radiobutton(self.__window, text="test1", variable="test", value="test1")

        btn_next = tk.Button(self.__window, text="Next", command=lambda: self.fire(image_folder=self.__image_folder, destination_path=self.__destination_path))

        lbl_image_path.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        btn_image_path.grid(row=0, column=0, padx=5, pady=5, sticky=tk.EW)
        lbl_dest_path.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        btn_dest_path.grid(row=1, column=0, padx=5, pady=5, sticky=tk.EW)
        btn_radio1.grid(row=2, column=0)
        btn_radio2.grid(row=2, column=1)
        btn_next.grid(row=3, column=1, sticky=tk.E, padx=5, pady=5)

        self.__widgets.extend([lbl_image_path, btn_image_path, lbl_dest_path, btn_dest_path, btn_radio1, btn_radio2, btn_next])
        
    def set_image_folder(self, path, lable) -> None:
        self.__image_folder = path
        lable.configure(text=self.__image_folder)

    def set_destination_path(self, path, lable) -> None:
        self.__destination_path = path
        lable.configure(text=self.__destination_path)

    def get_image_folder(self) -> str:
        return self.__image_folder
    
    def get_destination_path(self) -> str:
        return self.__destination_path
