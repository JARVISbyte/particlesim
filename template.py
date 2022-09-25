from vectors import Vector2D as Vector

class PhysObject:
	def __init__(self, 
		pos: Vector = Vector(0,0),
		vel: Vector = Vector(0,0),
		acc: Vector = Vector(0,0),
		netForce: Vector = Vector(0,0)
	): self.pos, self.vel, self.acc, self.netForce = pos, vel, acc, netForce 
	# todo: implement force for one moment (to reduce amount of operations)

