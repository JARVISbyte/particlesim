from vectors import Vector2D as Vector
from constants import getGraphics, getText, screenCorner, zoom, simpleSeriesAppr, verletIntegration

class PhysObject:
	def __init__(self, 
		pos: Vector = Vector(0,0),
		vel: Vector = Vector(0,0),
		acc: Vector = Vector(0,0),
		netForce: Vector = Vector(0,0),
		mass: float = 1,
		charge: float = 0,
		fixate: bool = False,
		visualizeFunc = lambda x,y: None,
		color = (0, 0, 0),
		dump_oscilations: bool = False
	): 
		self.pos, self.vel, self.acc, self.netForce, self.mass, self.charge, self.fixate = pos, vel, acc, netForce, mass, charge, fixate
		self.visualizeFunc = visualizeFunc
		self.color = color
		self.dump = dump_oscilations
		self.flag = True
	# todo (maybe): implement force for one moment (to reduce amount of operations)

	def update(self, timeStep: float, visualize: bool = True):
		self.acc = self.netForce / self.mass 

		# for next step 	(different technique may be used)
		if self.fixate:
			pass
		elif simpleSeriesAppr:
			self.pos += self.vel * timeStep + self.acc * timeStep**2 / 2
			self.vel += self.acc * timeStep
		elif verletIntegration:
			if self.flag:
				self.flag = False 
				self.pos_prev = self.pos
				self.pos += self.vel*timeStep + self.acc*timeStep**2 / 2	
			else:
				self.vel = (self.pos - self.pos_prev) / timeStep
				if self.dump: self.vel *= 0.999
				#self.pos, self.pos_prev = 2*self.pos - self.pos_prev + self.acc * timeStep**2, self.pos
				self.pos, self.pos_prev = self.pos + self.vel*timeStep + self.acc * timeStep**2, self.pos
		self.clearForce()

		if getGraphics and visualize: 
			if False:
				vect = self.pos - screenCorner
				column = vect.x * zoom
				row = - vect.y * zoom
			if True:
				vect = self.pos * zoom - screenCorner
				column = vect.x 
				row = - vect.y 
			#c_x, c_y = screenCorner.x, screenCorner.y
			#row, column = -self.pos.y+c_y, (self.pos.x)-c_x,
			#row, column = -round(self.pos.y)+c_y, round(self.pos.x)-c_x,
			self.visualizeFunc(row, column, color=self.color)
		if getText: print(self.pos, end="   ")
		return


	def interactionForce(self, force: Vector):
		self.netForce += force
	
	def clearAcc(self):
		self.acc = Vector(0,0)

	def clearForce(self):
		self.netForce = Vector(0,0)
		self.clearAcc()

