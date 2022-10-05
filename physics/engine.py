# Physics Engine
# Varlet method
from api.math.vector import Vec2


GRAVITY = Vec2(0, 1000)


class Engine:
    def __init__(self):
        self.object_list = list()

    def update(self, dt):
        self.applyGravity()
        self.updatePositions(dt)

    def updatePositions(self, dt):
        for obj in self.object_list:
            obj.updatePosition(dt)

    def applyGravity(self):
        for obj in self.object_list:
            obj.accelerate(GRAVITY)

