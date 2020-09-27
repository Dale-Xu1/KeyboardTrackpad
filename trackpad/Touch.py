from trackpad.Vector import Vector


class Touch:

    def __init__(self, key, keyboard):

        self.key = key

        self.pos = key.pos
        self.vel = Vector(0, 0)

        self.keyboard = keyboard
        self.oval = keyboard.create_oval(0, 0, 0, 0, fill='blue', outline='')

        self.r = 3

        self.is_dying = False
        self.lifespan = 10

        self.is_dead = False

    def update(self):

        # Calculate acceleration force
        a = self.pos
        b = self.key.pos

        force = b.sub(a)

        # Integrate force
        self.vel = self.vel.add(force.mult(0.3)).mult(0.5)  # Poor man's inverse mass and drag
        self.pos = self.pos.add(self.vel)

        # Update circle
        self.keyboard.coords(
            self.oval,
            self.pos.x - self.r, self.pos.y - self.r,
            self.pos.x + self.r, self.pos.y + self.r
        )

        # Decrement lifespan if dying
        if self.is_dying:
            self.lifespan -= 1

            if self.lifespan <= 0:
                self.is_dead = True
                self.is_dying = False

    def set_target(self, key):
        self.key = key

    def stop(self):
        self.is_dying = True

    def delete(self):
        self.keyboard.delete(self.oval)
