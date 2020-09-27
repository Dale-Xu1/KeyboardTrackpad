import csv
import keyboard
import mouse

from trackpad.Keyboard import Keyboard
from trackpad.TouchRegister import TouchRegister
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
        self.touch_register = TouchRegister(self.keyboard)

        # Bind events
        keyboard.on_press(self.on_key_down, True)
        keyboard.on_release(self.on_key_up, True)

        # Start loop
        window.after(0, self.update)

    def update(self):

        self.touch_register.update()
        touches = self.touch_register.touches

        if len(touches) > 1:

            # Average y velocity of touches
            vel = 0

            for touch in touches:
                vel += touch.vel.y

            mouse.wheel(vel / len(touches) * 0.1)

        elif len(touches) > 0:

            # Move mouse
            touch = touches[0]
            mouse.move(touch.vel.x * 5, touch.vel.y * 5, absolute=False)

        self.window.after(20, self.update)

    def on_key_down(self, e):

        if e.name == 'space':
            mouse.click()

        elif e.name == 'right alt':
            mouse.right_click()

        else:
            for key in self.keys:
                if key.name == e.name:

                    # Register touch
                    self.touch_register.on_touch(key)
                    break

            self.keyboard.on_key_down(e.name)

    def on_key_up(self, e):

        for key in self.keys:
            if key.name == e.name:

                # Register release
                self.touch_register.on_release(key)
                break

        self.keyboard.on_key_up(e.name)
