from time import sleep
from vectors import Vector2D as Vector
from template import PhysObject
from interaction import Spring
from constants import *

# we need coordinate system converting: 	x-O-y -> row-O'-column
# O'[c_x, c_y] - position of the upper-left corner of a screen (position is defined in constants.py)
# c_x, c_y = screenCorner
# column, row = x-c_x, -y+c_y

print("Hello World!")


objectsList = []
interactionsList = []

def loopThroughPairs(s: list):
	length = len(s)
	if length < 2:
		return (s[0], None)
	for l in range(length-1):
		for r in range(l+1, length):
			yield (s[l], s[r])

def setup():
	#global objectsList, interactionsList
	print("Setup! It runs once on start")

	global ObjectA, ObjectB
	ObjectA = PhysObject(pos=Vector(0,5))
	ObjectB = PhysObject(pos=Vector(0,-5))

	objectsList.append(ObjectA)
	objectsList.append(ObjectB)

	for pair in loopThroughPairs(objectsList):
		interactionsList.append(Spring(*pair, k, l_0))





def loop():
	for inter in interactionsList:
		inter.calculate()
	for obj in objectsList:
		obj.update(timeStep, True)
	print("\n--- ---")
	return 1
	




def main():
	setup()
	try:
		while True:
			if not loop(): 
				break
			sleep(realTimeDelay)
	except KeyboardInterrupt:
		print("KeyboardInterrupt")
	print("Sim is stopped. Exiting")


if __name__ == "__main__":
	main()