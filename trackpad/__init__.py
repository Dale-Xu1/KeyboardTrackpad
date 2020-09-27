class Trackpad:

    def __init__(self, window):

        self.window = window
        window.after(0, self.update)

    def update(self):

        self.window.after(20, self.update)
