from vectors import Vector2D as Vector
from template import PhysObject as Object


class Interaction:
	"""Describes interactions between objects in general"""
	def __init__(self, A: Object, B: Object):
		self.A, self.B = A, B
	
class ConstantField:
	"""To describe external fields like gravitational and electrostatic"""
	def __init__(self, forceCharacteristic: float, A: Object, charge: float):
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


