from matrix import Matrix

class Vector:
	def __init__(self, data):
		if not isinstance(data, list):
			raise TypeError("Vector must be a list")
		for d in data:
			if not isinstance(d, (int, float)):
				raise ValueError("Vector must be a list of int or float")
		self.data = data
		
	def size(self):
		return len(self.data)
	
	def __str__(self):
		return "\n".join(str(row) for row in self.data)
	
	def __str__(self):
		return "\n".join(f"[{x}]" for x in self.data)
		
	
		