# Object class
from api.math.vector import Vec2


class Object:
    def __init__(self):
        self.position = Vec2()
        self.position_old = Vec2()
        self.acceleration = Vec2()

    def updatePosition(self, dt: float) -> None:
        velocity = self.position - self.position_old
        # Dave the current position
        self.position_old = self.position
        # Perform Verlet integration
        self.position = self.position + velocity + self.acceleration * dt * dt
        self.acceleration = Vec2()

    def accelerate(self, acc: Vec2):
        self.acceleration += acc
