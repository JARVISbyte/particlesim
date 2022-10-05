# Vector class

class Vec2:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """ dot product (скалярное произведение) """
        return self.x*other.x + self.y*other.y

