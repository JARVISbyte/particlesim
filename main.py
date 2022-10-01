from time import sleep
from vectors import Vector2D as Vector
from template import PhysObject
from constants import *

print("Hello World!")





def setup():
	print("Setup! It runs once on start")
	global ObjectA
	ObjectA = PhysObject(pos=Vector(0,5))
	ObjectA.netForce += ObjectA.mass * g0





def loop():
	print(f"Loop! It runs every {timeStep} seconds")
	if ObjectA.pos.y <= 0:
		print(f"Pos: {ObjectA.pos}\nObject has fallen!\nStopping simulation")
		return 1
	print(f"Pos: {ObjectA.pos}")
	ObjectA.update()
	




def main():
	setup()
	# main loop
	while True:
		if loop(): 
			break
		sleep(timeStep)
	print("Sim is stopped. Exiting")


if __name__ == "__main__":
	main()