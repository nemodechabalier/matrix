"""Module Matrix - Implémentation d'une matrice mathématique.

Ce module fournit une classe Matrix pour représenter et manipuler
des matrices mathématiques avec support des nombres réels et complexes.
"""


class InvalidShapeError(ValueError):
    """Exception levée lorsque les dimensions des matrices sont incompatibles.
    
    Attributes:
        msg (str): Message d'erreur décrivant le problème de forme.
    """
    
    def __init__(self, msg="Matrix: Invalid shape"):
        super().__init__(msg)


class InvalidValueError(ValueError):
    """Exception levée lorsqu'une valeur invalide est fournie.
    
    Attributes:
        msg (str): Message d'erreur décrivant le problème de valeur.
    """
    
    def __init__(self, msg="Matrix: Invalid Value"):
        super().__init__(msg)


class InvalidTypeError(TypeError):
    """Exception levée lorsqu'un type invalide est fourni.
    
    Attributes:
        msg (str): Message d'erreur décrivant le problème de type.
    """
    
    def __init__(self, msg="Matrix: Invalid Type"):
        super().__init__(msg)


class Matrix:
    """Représente une matrice mathématique.
    
    Cette classe implémente les opérations matricielles incluant l'addition,
    la soustraction, le scaling, la multiplication, la transposée, la trace,
    le déterminant, l'inverse et le rang.
    
    Attributes:
        data (list[list]): Matrice sous forme de liste de listes.
    
    Examples:
        >>> m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        >>> print(m)
        [1.0, 2.0]
        [3.0, 4.0]
    """
    
    def __init__(self, data):
        """Initialise une matrice avec les données fournies.
        
        Args:
            data (list[list]): Liste de listes de nombres (int, float ou complex).
        
        Raises:
            InvalidTypeError: Si data n'est pas une liste.
            InvalidValueError: Si la structure ou les valeurs sont invalides.
        """
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
        """Retourne les dimensions de la matrice.
        
        Returns:
            tuple[int, int]: (nombre de lignes, nombre de colonnes).
        
        Examples:
            >>> m = Matrix([[1, 2, 3], [4, 5, 6]])
            >>> m.shape()
            (2, 3)
        """
        return len(self.data), len(self.data[0])

    def is_square(self):
        """Vérifie si la matrice est carrée.
        
        Returns:
            bool: True si nombre de lignes == nombre de colonnes.
        
        Examples:
            >>> m = Matrix([[1, 2], [3, 4]])
            >>> m.is_square()
            True
        """
        return self.shape()[0] == self.shape()[1]

    def matrix_to_vector(self):
        """Convertit la matrice en vecteur (aplatissement).
        
        Les éléments sont concaténés ligne par ligne.
        
        Returns:
            Vector: Vecteur contenant tous les éléments de la matrice.
        
        Examples:
            >>> m = Matrix([[1, 2], [3, 4]])
            >>> v = m.matrix_to_vector()
            >>> v.data
            [1, 2, 3, 4]
        """
        from vector import Vector
        data = []
        for row in self.data:
            for x in row:
                data.append(x)
        return Vector(data)

    def __str__(self):
        """Retourne une représentation en chaîne de la matrice.
        
        Returns:
            str: Représentation de la matrice avec une ligne par rangée.
        """
        return "\n".join(str(row) for row in self.data)
        
    def __add__(self, other):
        """Additionne deux matrices élément par élément.
        
        Args:
            other (Matrix): Matrice à additionner.
        
        Returns:
            Matrix: Nouvelle matrice résultant de l'addition.
        
        Raises:
            TypeError: Si other n'est pas une Matrix.
            ValueError: Si les matrices n'ont pas les mêmes dimensions.
        
        Examples:
            >>> m1 = Matrix([[1, 2], [3, 4]])
            >>> m2 = Matrix([[5, 6], [7, 8]])
            >>> print(m1 + m2)
            [6, 8]
            [10, 12]
        """
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
        """Soustrait deux matrices élément par élément.
        
        Args:
            other (Matrix): Matrice à soustraire.
        
        Returns:
            Matrix: Nouvelle matrice résultant de la soustraction.
        
        Raises:
            TypeError: Si other n'est pas une Matrix.
            ValueError: Si les matrices n'ont pas les mêmes dimensions.
        
        Examples:
            >>> m1 = Matrix([[5, 6], [7, 8]])
            >>> m2 = Matrix([[1, 2], [3, 4]])
            >>> print(m1 - m2)
            [4, 4]
            [4, 4]
        """
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
        """Multiplie chaque élément de la matrice par un scalaire.
        
        Args:
            scalar (int | float | complex): Scalaire multiplicateur.
        
        Returns:
            Matrix: Nouvelle matrice avec chaque élément multiplié.
        
        Raises:
            TypeError: Si scalar n'est pas un nombre.
        
        Examples:
            >>> m = Matrix([[1, 2], [3, 4]])
            >>> print(m * 2)
            [2, 4]
            [6, 8]
        """
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
        """Permet la multiplication scalaire * matrice.
        
        Args:
            scalar (int | float | complex): Scalaire multiplicateur.
        
        Returns:
            Matrix: Nouvelle matrice avec chaque élément multiplié.
        """
        return self.__mul__(scalar)
    
    def mul_mat(self, other):
        """Multiplie cette matrice par une autre matrice.
        
        Effectue la multiplication matricielle A × B.
        Le nombre de colonnes de self doit égaler le nombre de lignes de other.
        
        Args:
            other (Matrix): Matrice à multiplier.
        
        Returns:
            Matrix: Matrice résultante de dimensions (self.rows, other.cols).
        
        Raises:
            InvalidTypeError: Si other n'est pas une Matrix.
            InvalidShapeError: Si les dimensions sont incompatibles.
        
        Examples:
            >>> m1 = Matrix([[1, 2], [3, 4]])
            >>> m2 = Matrix([[5, 6], [7, 8]])
            >>> print(m1.mul_mat(m2))
            [19, 22]
            [43, 50]
        """
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
        """Multiplie cette matrice par un vecteur.
        
        Effectue la multiplication matrice × vecteur (A × v).
        Le nombre de colonnes de la matrice doit égaler la taille du vecteur.
        
        Args:
            other (Vector): Vecteur à multiplier.
        
        Returns:
            Vector: Vecteur résultant de dimensions (self.rows,).
        
        Raises:
            InvalidTypeError: Si other n'est pas un Vector.
            InvalidShapeError: Si les dimensions sont incompatibles.
        
        Examples:
            >>> m = Matrix([[1, 2], [3, 4]])
            >>> v = Vector([1, 2])
            >>> print(m.mul_vec(v))
            [5]
            [11]
        """
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
        """Calcule la trace de la matrice.
        
        La trace est la somme des éléments diagonaux.
        Uniquement définie pour les matrices carrées.
        
        Returns:
            int | float | complex: Somme des éléments diagonaux.
        
        Raises:
            InvalidShapeError: Si la matrice n'est pas carrée.
        
        Examples:
            >>> m = Matrix([[1, 2], [3, 4]])
            >>> m.trace()
            5
        """
        if self.is_square() == False:
            raise InvalidShapeError
        result = 0
        for n in range(self.shape()[0]):
            result = result + self.data[n][n]
        return result

    def transpose(self):
        """Calcule la transposée conjuguée (hermitienne) de la matrice.
        
        Pour une matrice réelle, c'est la transposée classique.
        Pour une matrice complexe, c'est la transposée conjuguée (A^H).
        
        Returns:
            Matrix: Matrice transposée conjuguée.
        
        Examples:
            >>> m = Matrix([[1, 2], [3, 4]])
            >>> print(m.transpose())
            [1, 3]
            [2, 4]
        """
        result = []
        for y in range(self.shape()[1]):
            line = []
            for x in range(self.shape()[0]):
                line.append(self.data[x][y].conjugate())
            result.append(line)
        return Matrix(result)
        

    def row_echelon(self):
        """Calcule la forme échelonnée réduite (RREF) de la matrice.
        
        Utilise l'élimination de Gauss-Jordan avec pivot partiel
        pour transformer la matrice en forme échelonnée réduite.
        
        Returns:
            Matrix: Matrice en forme échelonnée réduite.
        
        Examples:
            >>> m = Matrix([[1, 2], [3, 4]])
            >>> print(m.row_echelon())
            [1.0, 0.0]
            [0.0, 1.0]
        """
        result = [row[:] for row in self.data]
        rows, cols = self.shape()
        
        pivot_row = 0
        
        for col in range(cols):
            if pivot_row >= rows:
                break

            max_row = pivot_row
            for row in range(pivot_row, rows):
                if abs(result[row][col]) > abs(result[max_row][col]):
                    max_row = row
            
            if abs(result[max_row][col]) < 1e-10:
                continue

            result[pivot_row], result[max_row] = result[max_row], result[pivot_row]

            pivot_val = result[pivot_row][col]
            for j in range(cols):
                result[pivot_row][j] /= pivot_val

            for row in range(rows):
                if row != pivot_row:
                    factor = result[row][col]
                    for j in range(cols):
                        result[row][j] -= factor * result[pivot_row][j]

            pivot_row += 1

        return Matrix(result)


    def determinant(self):
        """Calcule le déterminant de la matrice.
        
        Utilise le développement par cofacteurs pour les matrices
        jusqu'à 4x4. La matrice doit être carrée.
        
        Returns:
            int | float | complex: Déterminant de la matrice.
        
        Raises:
            InvalidShapeError: Si la matrice n'est pas carrée ou > 4x4.
        
        Examples:
            >>> m = Matrix([[1, 2], [3, 4]])
            >>> m.determinant()
            -2
        """
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
        """Calcule l'inverse de la matrice.
        
        Utilise l'élimination de Gauss-Jordan avec matrice augmentée.
        La matrice doit être carrée et non singulière (déterminant ≠ 0).
        
        Returns:
            Matrix: Matrice inverse A⁻¹ telle que A × A⁻¹ = I.
        
        Raises:
            InvalidShapeError: Si la matrice n'est pas carrée.
            InvalidValueError: Si la matrice est singulière.
        
        Examples:
            >>> m = Matrix([[1, 2], [3, 4]])
            >>> inv = m.inverse()
            >>> print(m.mul_mat(inv))  # Doit être proche de I
        """
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
        """Calcule le rang de la matrice.
        
        Le rang est le nombre de lignes non nulles dans la forme
        échelonnée réduite de la matrice.
        
        Returns:
            int: Le rang de la matrice.
        
        Examples:
            >>> m = Matrix([[1, 2], [2, 4]])
            >>> m.rank()
            1
        """
        echelon = self.row_echelon()
        
        rank = 0
        for raw in echelon.data:
            if any(abs(x) > 1e-10 for x in raw):
                rank += 1
                
        return rank