from vectors import Vector2D as Vector
from constants import screenCorner, simpleSeriesAppr, verletIntegration

class PhysObject:
	def __init__(self, 
		pos: Vector = Vector(0,0),
		vel: Vector = Vector(0,0),
		acc: Vector = Vector(0,0),
		netForce: Vector = Vector(0,0),
		mass: float = 1,
		charge: float = 0,
		fixate: bool = False
	): 
		self.pos, self.vel, self.acc, self.netForce, self.mass, self.charge, self.fixate = pos, vel, acc, netForce, mass, charge, fixate
		self.flag = True
	# todo (maybe): implement force for one moment (to reduce amount of operations)

	def update(self, timeStep: float, visualize: bool):
		
		self.acc = self.netForce / self.mass 
		#print("Acc:", self.acc)
		

		# for next step 	(different technique may be used)
		#---
		if simpleSeriesAppr:
			self.pos += self.vel * timeStep + self.acc * timeStep**2 / 2
			self.vel += self.acc * timeStep
		elif verletIntegration:
			if self.flag:
				self.flag = False 
				self.pos += self.vel*timeStep + self.acc*timeStep**2 / 2	
			else:
				self.pos = 2*self.pos - self.pos_prev + self.acc * timeStep**2
			self.pos_prev = self.pos
		#---
		self.clearForce()

		if visualize: 
			#c_x, c_y = screenCorner
			#column, row = self.pos.x-c_x, -self.pos.y+c_y
			print(self.pos, end="   ")


	def interactionForce(self, force: Vector):
		self.netForce += force
	
	def clearAcc(self):
		self.acc = Vector(0,0)

	def clearForce(self):
		self.netForce = Vector(0,0)
		self.clearAcc()

