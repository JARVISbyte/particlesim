class Vector2D:
	def __init__(self, x: float = 0, y: float = 0):
		self.x, self.y = x, y

	def __add__(self, other):
		if not isinstance(other, Vector2D): raise ValueError("Tried to add vector with non-vector instance")
		return Vector2D(self.x+other.x, self.y+other.y)
	
	def __sub__(self, other):
		if not isinstance(other, Vector2D): raise ValueError("Tried to subtract non-vector instance from vector")
		return Vector2D(self.x-other.x, self.y-other.y) 

	def __mul__(self, other: float): return Vector2D(self.x*other, self.y*other)
	def __rmul__(self, other: float): return Vector2D(self.x*other, self.y*other)
	def __truediv__(self, other: float): return Vector2D(self.x / other, self.y / other)

	def __abs__(self): return (self.x**2 + self.y**2)**(.5)

	def __str__(self):
		return f"({self.x}, {self.y})"
	
	def normalized(self): return self/abs(self)