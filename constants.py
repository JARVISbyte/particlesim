# File to store constants

from vectors import Vector2D as Vector

# use graphics?
getGraphics = True
tracePaths = False
getText = False

# size of window
window_size = (500, 500)

# zoom = num of c-C-r units (pixels) in one x-O-y unit
#zoom = 3 * 10**(-6)
zoom = 10

# parameters for camera
screenCenter = Vector(0,0)
screenSize = Vector(window_size[0]//2, window_size[1]//2)
screenCorner = screenCenter + Vector(- screenSize.x, 0) + Vector(0, screenSize.y)



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)

# time step for simulations, s
timeStep = 0.01

# time step for better visual representation, real seconds
realTimeDelay = 0

#
GravitationalConstant = 6.67*10**(-11)
alpha = -0.015

# Parameters of objects in Solar system
# --- Earth parameters
mass_earth = 5.972*10**24
geostationaryOrbit_radius = 4.2164000 * 10**7
geostationaryOrbit_velocity = 3.0746 * 10**3

# acceleration near Earth's surface, m*s^(-2)
g0_abs = 9
g0 = Vector(0, -g0_abs)

# for springs
k = 10
l_0 = 8



simpleSeriesAppr = False
verletIntegration = True