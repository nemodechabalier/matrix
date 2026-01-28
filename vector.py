class InvalidShapeError(ValueError):
	def __init__(self, msg="Vector: Invalid shape"):
		super().__init__(msg)

class InvalidValueError(ValueError):
	def __init__(self, msg="Vector: Invalid Value"):
		super().__init__(msg)

class InvalidTypeError(TypeError):
	def __init__(self, msg="Vector: Invalid Type"):
		super().__init__(msg)

class Vector:
	def __init__(self, data):
		if not isinstance(data, list):
			raise InvalidTypeError
		for d in data:
			if not isinstance(d, (int, float)):
				raise InvalidValueError
		self.data = data
		
	def size(self):
		return len(self.data)
	
	def __str__(self):
		return "\n".join(f"[{x}]" for x in self.data)
	
	def vector_to_matrix(self, rows, cols):
		from matrix import Matrix
		if rows * cols != len(self.data):
			raise InvalidShapeError
		matrix_data = []
		for i in range(rows):
			row = []
			for j in range(cols):
				row.append(self.data[i * cols + j])
			matrix_data.append(row)

		return Matrix(matrix_data)
	
	def __add__(self, other):
		if not isinstance(other, Vector):
			raise InvalidTypeError
		if self.size() != other.size():
			raise InvalidShapeError()
		data = []
		for i in range(len(self.data)):
			data.append(self.data[i] + other.data[i])
		return Vector(data)
	
	def __sub__(self, other):
		if not isinstance(other, Vector):
			raise InvalidTypeError
		if self.size() != other.size():
			raise InvalidShapeError()
		data = []
		for i in range(len(self.data)):
			data.append(self.data[i] - other.data[i])
		return Vector(data)
	
	def __mul__(self, scalar):
		"""Scaling: multiplies each element of the vector by a scalar"""
		if not isinstance(scalar, (int, float)):
			raise InvalidTypeError()
		data = []
		for x in self.data:
			data.append(x * scalar)
		return Vector(data)
    
	def __rmul__(self, scalar):
		"""Allows scalar * vector as well as vector * scalar"""
		return self.__mul__(scalar)
		