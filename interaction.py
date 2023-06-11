from vectors import Vector2D as Vector
from template import PhysObject as Object


class Interaction:
	"""Describes interactions between objects in general"""
	def __init__(self, A: Object, B: Object, rule):
		self.A, self.B, self.rule = A, B, rule 
	
	def calculate(self):
		r = self.B.pos - self.A.pos
		F = self.rule(r)
		self.A.interactionForce(F)
		self.B.interactionForce((-1)*F)

	
class ConstantField:
	"""To describe external fields like gravitational and electrostatic"""
	def __init__(self, forceCharacteristic: Vector, A: Object, charge: float):
		# todo: forceCharacteristic as a function of coordinates
		self.E, self.A, self.charge = forceCharacteristic, A, charge
	
	def calculate(self):
		self.A.interactionForce(self.E * self.charge)


class Spring:
	"""Describes interaction between two objects as if they were connected by an ideal spring"""
	def __init__(self, A: Object, B: Object, springConstant: float, length_undeformed: float):
		#self.pair = [A, B]
		self.A, self.B = A, B
		self.k = springConstant
		self.l = length_undeformed

	def calculate(self):
		r = self.B.pos - self.A.pos
		F = - self.k * (self.l*r.normalized() - r)
		self.A.interactionForce(F)
		self.B.interactionForce((-1)*F)


class Gravity:
	"""Describes gravity interaction between actual bodies"""
	def __init__(self, A: Object, B: Object, GravitationalConstant: float):
		self.A = A
		self.B = B
		self.G = GravitationalConstant
	
	def calculate(self):
		r = self.B.pos - self.A.pos
		F = (r) * self.G * self.A.mass * self.B.mass * abs(r)**(-3)
		self.A.interactionForce(F)
		self.B.interactionForce((-1)*F)


class UnusualGravity:
	"""Describes hypothetical gravity interaction with different exponent (-2-alpha) between bodies"""
	def __init__(self, A: Object, B: Object, GravitationalConstant: float, alpha: float):
		self.A = A
		self.B = B
		self.G = GravitationalConstant
		self.alpha = alpha
	
	def calculate(self):
		r = self.B.pos - self.A.pos
		F = (r) * self.G * self.A.mass * self.B.mass * abs(r)**(-3-self.alpha)
		self.A.interactionForce(F)
		self.B.interactionForce((-1)*F)

