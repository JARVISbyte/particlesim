# File to store constants

from vectors import Vector2D as Vector

# position of the upper-left corner of a screen
screenCorner = Vector(-100, 100)

# time step for simulations, s
timeStep = 0.1

# time step for better visual representation, real seconds
realTimeDelay = 0.1

# acceleration near Earth's surface, m*s^(-2)
g0_abs = 10
g0 = Vector(0, -g0_abs)

# for springs
k = 1
l_0 = 2

simpleSeriesAppr = True
verletIntegration = False