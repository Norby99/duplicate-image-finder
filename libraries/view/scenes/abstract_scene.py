from abc import ABC, abstractmethod
import tkinter as tk

class AbstractScene(ABC):

    @abstractmethod
    def setup(self, window: tk.Tk) -> None:
        pass

    @abstractmethod
    def destroy(self) -> None:
        pass
