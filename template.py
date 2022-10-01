from vectors import Vector2D as Vector
from constants import timeStep

class PhysObject:
	def __init__(self, 
		pos: Vector = Vector(0,0),
		vel: Vector = Vector(0,0),
		acc: Vector = Vector(0,0),
		netForce: Vector = Vector(0,0),
		mass = 1
	): self.pos, self.vel, self.acc, self.netForce, self.mass = pos, vel, acc, netForce, mass
	# todo (maybe): implement force for one moment (to reduce amount of operations)

	def update(self):
		self.acc = self.netForce / self.mass 

		# for next step
		self.pos += self.vel * timeStep + self.acc * timeStep**2 / 2	#--- different technique may be used
		self.vel += self.acc * timeStep

	def clearAcc(self):
		self.acc = Vector(0,0)

	def clearForce(self):
		self.netForce = Vector(0,0)
		self.clearAcc()

