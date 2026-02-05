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
                if not isinstance(l, (int, float, complex)):
                    raise InvalidValueError
        self.data = data

    def shape(self):
        return  len(self.data), len(self.data[0])
    
    def is_square(self):
        return self.shape()[0] == self.shape()[1]
    
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
        if not isinstance(scalar, (int, float, complex)):
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
	
    def mul_vec(self, other):
        from vector import Vector
        if not isinstance(other, Vector):
            raise InvalidTypeError
        _, cols = self.shape()
        if cols != other.size():
            raise InvalidShapeError
        
        result = []
        for row in self.data:
            total = 0
            for j in range(len(row)):
                total += row[j] * other.data[j]
            result.append(total)
    
        return Vector(result)
    
    def trace(self):
        if self.is_square() == False:
            raise InvalidShapeError
        result = 0
        for n in range(self.shape()[0]):
            result = result + self.data[n][n]
        return result
    
    def transpose(self):
        result = []
        for y in range(self.shape()[1]):
            line = []
            for x in range(self.shape()[0]):
                line.append(self.data[x][y].conjugate())
            result.append(line)
        return Matrix(result)
        

    def row_echelon(self):
        # Copie des données pour ne pas modifier l'original
        result = [row[:] for row in self.data]
        rows, cols = self.shape()
        
        pivot_row = 0  # Ligne actuelle du pivot
        
        # Parcourir chaque colonne
        for col in range(cols):
            # Si on a traité toutes les lignes, on arrête
            if pivot_row >= rows:
                break
            
            # ========== ÉTAPE 1 : Trouver un pivot non-nul ==========
            # Chercher une ligne avec un élément non-nul dans cette colonne
            max_row = pivot_row
            for row in range(pivot_row, rows):
                # Prendre la valeur absolue la plus grande (plus stable)
                if abs(result[row][col]) > abs(result[max_row][col]):
                    max_row = row
            
            # Si le pivot est ~0, passer à la colonne suivante
            if abs(result[max_row][col]) < 1e-10:
                continue
            
            # ========== ÉTAPE 2 : Échanger les lignes ==========
            # Mettre la ligne avec le meilleur pivot en position
            result[pivot_row], result[max_row] = result[max_row], result[pivot_row]
            
            # ========== ÉTAPE 3 : Normaliser le pivot à 1 ==========
            # Diviser toute la ligne par le pivot
            pivot_val = result[pivot_row][col]
            for j in range(cols):
                result[pivot_row][j] /= pivot_val
            
            # ========== ÉTAPE 4 : Éliminer les autres éléments ==========
            # Mettre des 0 dans toute la colonne (sauf le pivot)
            for row in range(rows):
                if row != pivot_row:
                    factor = result[row][col]
                    for j in range(cols):
                        result[row][j] -= factor * result[pivot_row][j]
            
            # Passer à la ligne suivante pour le prochain pivot
            pivot_row += 1
        
        return Matrix(result)


    def determinant(self):
        if self.is_square() == False:
            raise InvalidShapeError
        if self.shape()[0] > 4:
            raise InvalidShapeError
        n = self.shape()[0]
        if n == 1:
            return self.data[0][0]
        if n == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        
        if n == 3:
            a = self.data
            return (a[0][0] * a[1][1] * a[2][2] +
                    a[0][1] * a[1][2] * a[2][0] +
                    a[0][2] * a[1][0] * a[2][1] -
                    a[0][2] * a[1][1] * a[2][0] -
                    a[0][1] * a[1][0] * a[2][2] -
                    a[0][0] * a[1][2] * a[2][1])
        
        if n == 4:
            det = 0
            for j in range(4):
                minor = []
                for row in range(1, 4):
                    minor_row = []
                    for col in range(4):
                        if col != j:
                            minor_row.append(self.data[row][col])
                    minor.append(minor_row)
                
                sign = 1 if j % 2 == 0 else -1
                det += sign * self.data[0][j] * Matrix(minor).determinant()
            
            return det


    def inverse(self):
        if not self.is_square():
            raise InvalidShapeError

        n = self.shape()[0]

        augmented = []
        for i in range(n):
            row = self.data[i][:] + [1.0 if i == j else 0.0 for j in range(n)]
            augmented.append(row)
        
        # Élimination de Gauss-Jordan
        for col in range(n):
            # Trouver le pivot (plus grande valeur absolue)
            max_row = col
            for row in range(col + 1, n):
                if abs(augmented[row][col]) > abs(augmented[max_row][col]):
                    max_row = row
            
            # Vérifier si la matrice est singulière
            if abs(augmented[max_row][col]) < 1e-10:
                raise InvalidValueError("Matrix is singular, cannot compute inverse")
            
            # Échanger les lignes
            augmented[col], augmented[max_row] = augmented[max_row], augmented[col]
            
            # Normaliser la ligne du pivot
            pivot = augmented[col][col]
            for j in range(2 * n):
                augmented[col][j] /= pivot
            
            # Éliminer les autres éléments de la colonne
            for row in range(n):
                if row != col:
                    factor = augmented[row][col]
                    for j in range(2 * n):
                        augmented[row][j] -= factor * augmented[col][j]
        
        # Extraire la partie droite (l'inverse)
        result = []
        for i in range(n):
            result.append(augmented[i][n:])
        
        return Matrix(result)
        
    def rank(self):
        echelon = self.row_echelon()
        
        rank = 0
        for raw in echelon.data:
            if any(abs(x) > 1e-10 for x in raw):
                rank += 1
                
        return rank