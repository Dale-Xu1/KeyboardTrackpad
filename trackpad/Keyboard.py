import tkinter as tk
from PIL import Image, ImageTk


class Keyboard(tk.Canvas):

    def __init__(self):
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
