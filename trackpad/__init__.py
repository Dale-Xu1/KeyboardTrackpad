from trackpad.Keyboard import Keyboard


class Trackpad:

    def __init__(self, window):

        self.window = window
        self.keyboard = Keyboard()

        window.after(0, self.update)

    def update(self):

        self.window.after(20, self.update)
