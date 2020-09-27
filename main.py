import tkinter as tk

from trackpad import Trackpad


if __name__ == '__main__':

    # Create window
    window = tk.Tk()
    window.title("Keyboard Trackpad")

    trackpad = Trackpad(window)

    window.mainloop()
