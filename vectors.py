class Vector2D:
	def __init__(self, x: float = 0, y: float = 0):
		self.x, self.y = x, y

	def __add__(self, other):
		if not isinstance(other, Vector2D): raise ValueError("Tried to add vector with non-vector instance")
		return Vector2D(self.x+other.x, self.y+other.y)

	def __mul__(self, other: float): return Vector2D(self.x*other, self.y*other)
	def __rmul__(self, other: float): return Vector2D(self.x*other, self.y*other)
	def __truediv__(self, other: float): return Vector2D(self.x / other, self.y / other)

	def __str__(self):
		return f"({self.x}, {self.y})"