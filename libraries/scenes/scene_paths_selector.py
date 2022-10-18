from libraries.scenes.abstract_scene import AbstractScene
import tkinter as tk
import tkinter.filedialog

class ScenePathsSelector(AbstractScene):

    __window: tk.Tk = None

    def __init__(self) -> None:
        pass

    def setup(self, window: tk.Tk) -> None:
        self.__window = window
        self.create_path_widgets()

    def destroy(self) -> None:
        pass

    def create_path_widgets(self) -> None:
        self.btns_path = []
        for i in ["Source", "Destination"]:
            self.btns_path.append(tk.Button(self.__window, text=i, command=lambda i=i: self.btns_path_click(tkinter.filedialog.askdirectory())))
            self.btns_path[-1].pack(pady=5)

            self.label_path = tk.Label(self.__window, text="", font=("Helvetica", 12), background="white")
            self.label_path.pack(pady=5)
