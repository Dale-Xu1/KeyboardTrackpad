class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def sub(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)

    def mult(self, value):
        return Vector(self.x * value, self.y * value)
