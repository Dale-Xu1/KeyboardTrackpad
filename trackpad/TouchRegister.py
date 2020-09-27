from trackpad.Touch import Touch


class TouchRegister:

    def __init__(self, keyboard):

        self.keyboard = keyboard
        self.touches = []

    def update(self):

        # Update touches
        for touch in self.touches:
            if touch.is_dead:

                touch.delete()
                self.touches.remove(touch)

            else:
                touch.update()

    def on_touch(self, key):

        # Create touch
        touch = Touch(key, self.keyboard)
        self.touches.append(touch)

    def on_release(self, key):

        # Stop touches
        for touch in self.touches:
            if touch.key.name == key.name:
                touch.stop()
