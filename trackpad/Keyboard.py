import tkinter as tk
from PIL import Image, ImageTk


class Keyboard(tk.Canvas):

    def __init__(self, keys):
        super().__init__()

        # Get image
        image = Image.open('keyboard.jpg')
        self.image = ImageTk.PhotoImage(image)

        # Set canvas dimensions
        width = self.image.width()
        height = self.image.height()

        self.config(width=width, height=height)
        self.pack()

        # Create image
        self.create_image(width / 2, height / 2, image=self.image)

        # Create keys
        self.keys = keys
        self.rectangles = {}

        self.create_keys()

    def create_keys(self):

        for key in self.keys:

            a = key.a
            b = key.b

            # Create rectangle
            rectangle = self.create_rectangle(a.x, a.y, b.x, b.y, outline='green')
            self.rectangles[key.name] = rectangle
