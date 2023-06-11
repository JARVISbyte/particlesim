from time import sleep
from vectors import Vector2D as Vector
from template import PhysObject
from interaction import Spring, ConstantField, Gravity, UnusualGravity
from constants import *
 

# we need coordinate system converting: 	x-O-y -> row-O'-column
# O'[c_x, c_y] - position of the upper-left corner of a screen (position is defined in constants.py)
# c_x, c_y = screenCorner
# column, row = x-c_x, -y+c_y


def visualizeFuncBasic(row: int, column: int, color: tuple = BLACK):
	# function to draw a circle where the object is 
	# pass to it the whole object?
	pygame.draw.circle(screen, color, (column, row), 3)



def loopThroughPairs(s: list):
	length = len(s)
	if length < 2:
		return (s[0], None)
	for l in range(length-1):
		for r in range(l+1, length):
			yield (s[l], s[r])

def objectsDefinition_Unusual_gravity(alpha: float = 0):
	Earth = PhysObject(
		pos=Vector(0,0), 
		vel=Vector(0,0),
		mass=mass_earth,
		fixate=True, 
		visualizeFunc = visualizeFuncBasic, 
		color=BLUE
	)
	Satellite = PhysObject(
		pos=Vector(geostationaryOrbit_radius, 0), 
		vel=Vector(0, geostationaryOrbit_velocity),
		mass=1,
		fixate=False,
		visualizeFunc = visualizeFuncBasic, 
		color=BLACK
	)
	objectsList.append(Earth)
	objectsList.append(Satellite)
	for pair in loopThroughPairs(objectsList):
		interactionsList.append(UnusualGravity(*pair, GravitationalConstant, alpha))

def objectsDefinition_Gravity():
	global ObjectA, ObjectB
	ObjectA = PhysObject(
		pos=Vector(0,0), 
		vel=Vector(0,0),
		mass=10**12,
		fixate=True, 
		visualizeFunc = visualizeFuncBasic, 
		color=BLACK
	)
	ObjectB = PhysObject(
		pos=Vector(10,0), 
		vel=Vector(0,2),
		mass=100,
		fixate=False,
		visualizeFunc = visualizeFuncBasic, 
		color=BLUE
	)
	ObjectC = PhysObject(
		pos=Vector(-10,0), 
		vel=Vector(0,3),
		mass=100,
		fixate=False,
		visualizeFunc = visualizeFuncBasic, 
		color=GREEN
	)
	objectsList.append(ObjectA)
	objectsList.append(ObjectB)
	objectsList.append(ObjectC)

	for pair in loopThroughPairs(objectsList):
		interactionsList.append(Gravity(*pair, GravitationalConstant))

def objectsDefinition_Massive_spring(N=1):
	length_natural = 100 
	k_natural = 100
	mass_natural = 1
	delta_l = length_natural / N
	delta_k = k_natural * N 
	delta_m = mass_natural / N
	for i in range(N+1):
		objectsList.append(PhysObject(pos=Vector(0, -delta_l*(i+1)), mass=delta_m, visualizeFunc=visualizeFuncBasic, dump_oscilations=True))
		if i==0: 
			objectsList[-1].fixate = True
		else:
			interactionsList.append(ConstantField(g0, objectsList[-1], objectsList[-1].mass))
			interactionsList.append(Spring(objectsList[-1], objectsList[-2], delta_k, delta_l))

			
def setup():
	print("Setup! It runs once on start")

	if getGraphics:
		global pygame
		import pygame
		pygame.init()
		global screen 
		screen = pygame.display.set_mode(window_size)
		screen.fill(WHITE)
		pygame.display.flip()

	global objectsList, interactionsList
	objectsList, interactionsList = [], []

	global frameCounter
	frameCounter = 0

	#objectsDefinition_Massive_spring(N=100)
	objectsDefinition_Gravity()
	#objectsDefinition_Unusual_gravity(alpha)



def loop():
	for inter in interactionsList:
		inter.calculate()
	for obj in objectsList:
		obj.update(timeStep, True)
	if getGraphics: 
		pygame.display.flip()
		if not tracePaths: 
			screen.fill(WHITE)
	if getText: print("\n--- ---")
	return 1
	


def main():
	setup()
	try:
		while True:
			if not loop(): 
				break
			sleep(realTimeDelay)
			#frameCounter += 1
	except KeyboardInterrupt:
		print("KeyboardInterrupt")
	print("Sim is stopped. Exiting")



if __name__ == "__main__":
	main()