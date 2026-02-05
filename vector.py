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
            if not isinstance(d, (int, float, complex)):
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
        if not isinstance(scalar, (int, float, complex)):
            raise InvalidTypeError()
        data = []
        for x in self.data:
            data.append(x * scalar)
        return Vector(data)
    
    def __rmul__(self, scalar):
        """Allows scalar * vector as well as vector * scalar"""
        return self.__mul__(scalar)
    
    def dot(self, other):
        if not isinstance(other, Vector):
            raise InvalidTypeError
        if self.size() != other.size():
            raise InvalidShapeError
        result = 0
        for i in range(self.size()):
            result = result + self.data[i] * other.data[i].conjugate()
        return result
    
    def __matmul__(self, other):
        """Dot product using @ operator"""
        return self.dot(other)
    
        
    def norm_1(self):
        return sum(abs(x) for x in self.data)
        
    def norm(self):
        result = 0
        for i in range(self.size()):
            result = result + abs(self.data[i]) ** 2
        return pow(result, 0.5)
    
    def norm_inf(self):
        return max(abs(x) for x in self.data)
    
    def angle_cos(self, other):
        if not isinstance(other, Vector):
            raise InvalidValueError
        if self.size() != other.size():
            raise InvalidValueError
        if self.norm() == 0 or other.norm() == 0:
            raise InvalidValueError
        
        return self.dot(other) / (self.norm() * other.norm())
        
    def cross_product(self, other):
        if not isinstance(other, Vector):
            raise TypeError
        if self.size() != 3 or other.size() != 3:
            raise ValueError
        return Vector([
            self.data[1] * other.data[2] - self.data[2] * other.data[1],
            self.data[2] * other.data[0] - self.data[0] * other.data[2],
            self.data[0] * other.data[1] - self.data[1] * other.data[0]
        ])

