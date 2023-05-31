import tkinter as tk
from PIL import Image, ImageTk

from libraries.view.scenes.abstract_scene import AbstractScene

import math
import shutil
import os

#TODO: this class needs a lot of refactoring
class MainView():

    __window: tk.Tk

    __analizing_methods: dict = { "Duplicate" : True, "Similar" : False }
    mini_window_size = [300, 200]
    running: str = True
    __current_scene: AbstractScene = None
    
    def __init__(self) -> None:

        self.__window = tk.Tk()
        self.__window.title("Image Detector")
        self.__window.geometry(str(self.mini_window_size[0]) + "x" + str(self.mini_window_size[1]))
        self.__window.configure(background="white")

        self.__window.protocol("WM_DELETE_WINDOW", self.set_stop_running)

    def set_scene(self, scene: AbstractScene) -> None:
        if self.__current_scene is not None:
            self.__current_scene.destroy()
        self.__current_scene = scene
        self.__current_scene.setup(self.__window)

    def get_scene(self) -> AbstractScene:
        return self.__current_scene

    def create_result_widgets(self) -> None:
        if len(self.duplicate_images) > 0:
            self.__window.geometry(str(self.extend_window_size[0]) + "x" + str(self.extend_window_size[1]))
            images = self.duplicate_images[0]

            img_path1 = os.path.join(self.__image_folder, images[0])
            self.image1 = Image.open(img_path1)
            self.tk_image1 = self.get_imageTk(self.image1)
            self.left_image = tk.Label(self.__window, image=self.tk_image1, background="white")
            self.left_image.bind("<Button-1>", lambda event: self.image_clicked(0))
            self.left_image_label = tk.Label(self.__window, text=images[0], font=("Helvetica", 12), background="white")

            text = "Size: " + str(self.image1.size[0]) + " x " + str(self.image1.size[1]) + "\nDimension= " + convert_size(os.stat(img_path1).st_size)
            self.left_image_details = tk.Label(self.__window, text=text, font=("Helvetica", 12), background="white")

            img_path2 = os.path.join(self.__image_folder, images[1])
            self.image2 = Image.open(img_path2)
            self.tk_image2 = self.get_imageTk(self.image2)
            self.right_image = tk.Label(self.__window, image=self.tk_image1, background="white")
            self.right_image.bind("<Button-1>", lambda event: self.image_clicked(1))
            self.right_image_label = tk.Label(self.__window, text=images[1], font=("Helvetica", 12), background="white")

            text = "Size: " + str(self.image2.size[0]) + " x " + str(self.image2.size[1]) + "\nDimension= " + convert_size(os.stat(img_path2).st_size)
            self.right_image_details = tk.Label(self.__window, text=text, font=("Helvetica", 12), background="white")
            
            self.btn_skip = tk.Button(self.__window, text="Skip", command=lambda: self.image_clicked(None, skip=True))

            self.__set_image_selection_position_and_size()

        else :
            if hasattr(self, "left_image"):
                self.delete_all_image_related_widgets()

            self.__window.geometry(str(self.mini_window_size[0]) + "x" + str(self.mini_window_size[1]))
            self.label_loading.config(text="No duplicates found")
            self.label_loading.pack(pady=10, anchor="center")

    def image_clicked(self, image_element, skip=False) -> None:
        if not skip:
            shutil.move(os.path.join(self.__image_folder, self.duplicate_images[0][image_element]), os.path.join(self.__destination_path, self.duplicate_images[0][image_element]))
        self.duplicate_images.pop(0)
        self.delete_all_image_related_widgets()
        self.create_result_widgets()

    def update(self) -> None:
        self.__window.update()

    def get_imageTk(self, image) -> ImageTk.PhotoImage:
        dim = self.get_image_dimensions(image)
        return ImageTk.PhotoImage(image.resize((dim[0], dim[1]), Image.ANTIALIAS))

    def resize(self) -> None:
        if not hasattr(self, "left_image"):
            return 
        self.__set_image_selection_position_and_size()
        
    def __set_image_selection_position_and_size(self) -> None:
        self.tk_image1 = self.get_imageTk(self.image1)
        self.left_image.config(image=self.tk_image1)
        self.left_image.place(anchor="nw", x=10, y=20)
        self.left_image_label.place(anchor="nw", x=0, y=0)
        self.left_image_details.place(anchor="sw", x=0, y=self.__window.winfo_height() - 20)

        self.tk_image2 = self.get_imageTk(self.image2)
        self.right_image.config(image=self.tk_image2)
        self.right_image.place(anchor="ne", x=self.__window.winfo_width()-10, y=20)
        self.right_image_label.place(x=self.__window.winfo_width()-10, y=0, anchor='ne')
        self.right_image_details.place(x=self.__window.winfo_width()-10, y=self.__window.winfo_height() - 20, anchor='se')

        self.btn_skip.place(x=self.__window.winfo_width()/2, y=self.__window.winfo_height() - 20, anchor='center')

    def get_image_dimensions(self, img) -> list:
        img_proportion = img.size[0] / img.size[1]
        lower_border_size = 100
        x = int(self.__window.winfo_width() // 2)
        y = int(x // img_proportion)

        if (y > self.__window.winfo_height() - lower_border_size):
            y = self.__window.winfo_height() - lower_border_size
            x = int(y * img_proportion)

        dimension = [x, y]
        return dimension

    def detects_resize(self):
        if hasattr(self, "last_size"):
            if self.last_size != self.__window.winfo_width() + self.__window.winfo_height():
                self.last_size = self.__window.winfo_width() + self.__window.winfo_height()
                return True
            else:
                return False
        else:
            self.last_size = [self.__window.winfo_width(), self.__window.winfo_height()]

    def delete_all_image_related_widgets(self) -> None:
        self.left_image.destroy()
        self.left_image_label.destroy()
        self.left_image_details.destroy()
        
        self.right_image.destroy()
        self.right_image_label.destroy()
        self.right_image_details.destroy()

        self.btn_skip.destroy()

    def set_stop_running(self) -> None:
        self.running = False

    def destroy_buttons(self, btns) -> None:
        for i in btns:
            i.pack_forget()

    def destroy(self) -> None:
        self.__window.destroy()
