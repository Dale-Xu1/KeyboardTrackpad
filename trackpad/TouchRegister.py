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

        # Get nearest touch
        nearest_touch = None
        nearest_distance = 100 ** 2  # Squared so sqrt() doesn't have to be used

        for touch in self.touches:

            distance = key.pos.sub(touch.pos).mag_sq()

            if distance < nearest_distance:
                nearest_touch = touch
                nearest_distance = distance

        if nearest_touch is None:

            # Create touch
            touch = Touch(key, self.keyboard)
            self.touches.append(touch)

        else:
            nearest_touch.set_target(key.pos)

    def on_release(self, key):

        # Stop touches
        for touch in self.touches:
            if touch.key.name == key.name:
                touch.stop()
