import csv
import keyboard

from trackpad.Keyboard import Keyboard
from trackpad.Key import Key
from trackpad.Vector import Vector


class Trackpad:

    def __init__(self, window):

        self.keys = []

        # Read key data
        with open('keys.csv', newline='') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:

                # Convert data to an object
                name = row[0]
                pos = Vector(float(row[1]), float(row[2]))

                a = Vector(float(row[3]), float(row[4]))
                b = Vector(float(row[5]), float(row[6]))

                # Create object
                key = Key(name, pos, a, b)
                self.keys.append(key)

        self.window = window
        self.keyboard = Keyboard(self.keys)

        # Bind events
        keyboard.on_press(self.on_key_down, True)
        keyboard.on_release(self.on_key_up, True)

        # Start loop
        window.after(0, self.update)

    def update(self):

        self.window.after(20, self.update)

    def on_key_down(self, e):

        self.keyboard.on_key_down(e.name)

    def on_key_up(self, e):

        self.keyboard.on_key_up(e.name)
