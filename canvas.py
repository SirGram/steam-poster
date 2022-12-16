import tkinter as tk
from PIL import Image,ImageTk


class CreateLabel:
    def __init__(self,resize, item, type, row, column, window,columnspan, rowspan,grid_size,pad):
        self.grid_size=grid_size
        self.image = Image.open(item)
        self.resize=resize
        if self.resize:
            self.image = self.image.resize(self.resize_image(type))
        self.img = ImageTk.PhotoImage(image=self.image)
        self.label = tk.Label(window, image=self.img, background=window["bg"],anchor="nw")
        self.label.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, padx=pad,pady=pad)

    def resize_image(self,type):
        if type=="big":
            return (self.grid_size*2, self.grid_size*2)
        elif type=="medium":
            return (self.grid_size*2, self.grid_size)
        elif type == "medium2":
            return (self.grid_size, self.grid_size*2)
        elif type == "small":
            return (self.grid_size, self.grid_size)




