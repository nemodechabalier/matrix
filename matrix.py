#from vector import Vector


class Matrix:
	def __init__(self, data):
		if not isinstance(data, list):
			raise TypeError("Matrix must be a list")
		size = len(data[0])
		if size == 0:
			raise ValueError("Error")
		for lst in data:
			if not isinstance(lst, list) or len(lst) != size:
				raise ValueError("Matrix must be a list of list and have the same size")
			for l in lst:
			    if not isinstance(l, (int, float)):
			    	raise ValueError("Matrix must be a list of int or float")
		self.data = data

	def is_square(self):
		if len(self.data[0]) == len(self.data):
			return True
		return False

	def shape(self):
		return len(self.data[0]) , len(self.data)
	
    def matrix_to_vector(mat):
        data = []
        for row in mat.data:
            for x in row:
                data.append(x)
        from vector import Vector
        return Vector(data)


	
test = [
	[1,2],
	[3,2]
]

M = Matrix(test)
print(test)

test = [
	[1,2],
	[3,2,1]
]

M = Matrix(test)
print(test)

test = [
	[],
	[]
]

M = Matrix(test)
print(test)

test = [
	["n",2],
	[3,2,1]
]

M = Matrix(test)
print(test)