class InvalidShapeError(ValueError):
    def __init__(self, msg="Matrix: Invalid shape"):
        super().__init__(msg)

class InvalidValueError(ValueError):
    def __init__(self, msg="Matrix: Invalid Value"):
        super().__init__(msg)

class InvalidTypeError(TypeError):
    def __init__(self, msg="Matrix: Invalid Type"):
        super().__init__(msg)

class Matrix:
    def __init__(self, data):
        if not isinstance(data, list):
            raise InvalidTypeError
        size = len(data[0])
        if size == 0:
            raise InvalidValueError
        for lst in data:
            if not isinstance(lst, list) or len(lst) != size:
                raise InvalidValueError
            for l in lst:
                if not isinstance(l, (int, float)):
                    raise InvalidValueError
        self.data = data

    def is_square(self):
        if len(self.data[0]) == len(self.data):
            return True
        return False

    def shape(self):
        return  len(self.data), len(self.data[0])
    
    def matrix_to_vector(self):
        from vector import Vector
        data = []
        for row in self.data:
            for x in row:
                data.append(x)
        return Vector(data)
        
    def __str__(self):
        return "\n".join(str(row) for row in self.data)
        
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Matrix: Invalid Type")
        if self.shape() != other.shape():
            raise ValueError("Matrix: Invalid Shape")
        data = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])
            data.append(row)
        return Matrix(data)
    
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Matrix: Invalid Type")
        if self.shape() != other.shape():
            raise ValueError("Matrix: Invalid Shape")
        data = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] - other.data[i][j])
            data.append(row)
        return Matrix(data)
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Matrix: Invalid Type")
        data = []
        for row in self.data:
            new_row = []
            for x in row:
                new_row.append(x * scalar)
            data.append(new_row)
        return Matrix(data)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def mul_mat(self, other):
        if not isinstance(other, Matrix):
            raise InvalidTypeError
        x1, y1 = self.shape()   # lignes, colonnes de self
        x2, y2 = other.shape()  # lignes, colonnes de other
        if y1 != x2:
            raise InvalidShapeError
    
        result = []
        for i in range(x1):  # pour chaque ligne de self
            row = []
            for j in range(y2):  # pour chaque colonne de other
            total = 0
                for k in range(y1):  # produit scalaire
                    total += self.data[i][k] * other.data[k][j]
            row.append(total)
        result.append(row)
    
    return Matrix(result)
        
        
    def mult_vec(self, other):
        from vector import Vector
        if not isinstance(other, Vector):
            raise InvalidTypeError
