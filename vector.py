"""Module Vector - Implémentation d'un vecteur mathématique.

Ce module fournit une classe Vector pour représenter et manipuler
des vecteurs mathématiques avec support des nombres réels et complexes.
"""


class InvalidShapeError(ValueError):
    """Exception levée lorsque les dimensions des vecteurs sont incompatibles.
    
    Attributes:
        msg (str): Message d'erreur décrivant le problème de forme.
    """
    
    def __init__(self, msg="Vector: Invalid shape"):
        super().__init__(msg)


class InvalidValueError(ValueError):
    """Exception levée lorsqu'une valeur invalide est fournie.
    
    Attributes:
        msg (str): Message d'erreur décrivant le problème de valeur.
    """
    
    def __init__(self, msg="Vector: Invalid Value"):
        super().__init__(msg)


class InvalidTypeError(TypeError):
    """Exception levée lorsqu'un type invalide est fourni.
    
    Attributes:
        msg (str): Message d'erreur décrivant le problème de type.
    """
    
    def __init__(self, msg="Vector: Invalid Type"):
        super().__init__(msg)


class Vector:
    """Représente un vecteur mathématique.
    
    Cette classe implémente les opérations vectorielles de base incluant
    l'addition, la soustraction, le scaling, le produit scalaire, les normes,
    le cosinus d'angle et le produit vectoriel.
    
    Attributes:
        data (list): Liste des composantes du vecteur (int, float ou complex).
    
    Examples:
        >>> v = Vector([1.0, 2.0, 3.0])
        >>> u = Vector([4.0, 5.0, 6.0])
        >>> print(v + u)  # Addition
        [5.0]
        [7.0]
        [9.0]
    """
    
    def __init__(self, data):
        """Initialise un vecteur avec les données fournies.
        
        Args:
            data (list): Liste de nombres (int, float ou complex).
        
        Raises:
            InvalidTypeError: Si data n'est pas une liste.
            InvalidValueError: Si un élément n'est pas un nombre valide.
        """
        if not isinstance(data, list):
            raise InvalidTypeError
        for d in data:
            if not isinstance(d, (int, float, complex)):
                raise InvalidValueError
        self.data = data

    def size(self):
        """Retourne la taille (dimension) du vecteur.
        
        Returns:
            int: Le nombre de composantes du vecteur.
        
        Examples:
            >>> v = Vector([1.0, 2.0, 3.0])
            >>> v.size()
            3
        """
        return len(self.data)

    def __str__(self):
        """Retourne une représentation en chaîne du vecteur.
        
        Returns:
            str: Représentation du vecteur avec une composante par ligne.
        """
        return "\n".join(f"[{x}]" for x in self.data)

    def vector_to_matrix(self, rows, cols):
        """Convertit le vecteur en matrice de dimensions spécifiées.
        
        Reshape le vecteur en une matrice rows x cols.
        
        Args:
            rows (int): Nombre de lignes de la matrice résultante.
            cols (int): Nombre de colonnes de la matrice résultante.
        
        Returns:
            Matrix: Matrice de dimensions (rows, cols).
        
        Raises:
            InvalidShapeError: Si rows * cols != taille du vecteur.
        
        Examples:
            >>> v = Vector([1.0, 2.0, 3.0, 4.0])
            >>> m = v.vector_to_matrix(2, 2)
            >>> print(m)
            [1.0, 2.0]
            [3.0, 4.0]
        """
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
        """Additionne deux vecteurs composante par composante.
        
        Args:
            other (Vector): Vecteur à additionner.
        
        Returns:
            Vector: Nouveau vecteur résultant de l'addition.
        
        Raises:
            InvalidTypeError: Si other n'est pas un Vector.
            InvalidShapeError: Si les vecteurs n'ont pas la même taille.
        
        Examples:
            >>> u = Vector([1.0, 2.0])
            >>> v = Vector([3.0, 4.0])
            >>> print(u + v)
            [4.0]
            [6.0]
        """
        if not isinstance(other, Vector):
            raise InvalidTypeError
        if self.size() != other.size():
            raise InvalidShapeError()
        data = []
        for i in range(len(self.data)):
            data.append(self.data[i] + other.data[i])
        return Vector(data)

    def __sub__(self, other):
        """Soustrait deux vecteurs composante par composante.
        
        Args:
            other (Vector): Vecteur à soustraire.
        
        Returns:
            Vector: Nouveau vecteur résultant de la soustraction.
        
        Raises:
            InvalidTypeError: Si other n'est pas un Vector.
            InvalidShapeError: Si les vecteurs n'ont pas la même taille.
        
        Examples:
            >>> u = Vector([5.0, 7.0])
            >>> v = Vector([2.0, 3.0])
            >>> print(u - v)
            [3.0]
            [4.0]
        """
        if not isinstance(other, Vector):
            raise InvalidTypeError
        if self.size() != other.size():
            raise InvalidShapeError()
        data = []
        for i in range(len(self.data)):
            data.append(self.data[i] - other.data[i])
        return Vector(data)

    def __mul__(self, scalar):
        """Multiplie chaque composante du vecteur par un scalaire (scaling).
        
        Args:
            scalar (int | float | complex): Scalaire multiplicateur.
        
        Returns:
            Vector: Nouveau vecteur avec chaque composante multipliée.
        
        Raises:
            InvalidTypeError: Si scalar n'est pas un nombre.
        
        Examples:
            >>> v = Vector([1.0, 2.0, 3.0])
            >>> print(v * 2)
            [2.0]
            [4.0]
            [6.0]
        """
        if not isinstance(scalar, (int, float, complex)):
            raise InvalidTypeError()
        data = []
        for x in self.data:
            data.append(x * scalar)
        return Vector(data)

    def __rmul__(self, scalar):
        """Permet la multiplication scalaire * vecteur.
        
        Args:
            scalar (int | float | complex): Scalaire multiplicateur.
        
        Returns:
            Vector: Nouveau vecteur avec chaque composante multipliée.
        """
        return self.__mul__(scalar)
    
    def dot(self, other):
        """Calcule le produit scalaire (dot product) de deux vecteurs.
        
        Pour les vecteurs complexes, utilise le produit hermitien :
        <u, v> = Σ u[i] * conj(v[i])
        
        Args:
            other (Vector): Vecteur avec lequel calculer le produit scalaire.
        
        Returns:
            int | float | complex: Résultat du produit scalaire.
        
        Raises:
            InvalidTypeError: Si other n'est pas un Vector.
            InvalidShapeError: Si les vecteurs n'ont pas la même taille.
        
        Examples:
            >>> u = Vector([1.0, 2.0])
            >>> v = Vector([3.0, 4.0])
            >>> u.dot(v)
            11.0
        """
        if not isinstance(other, Vector):
            raise InvalidTypeError
        if self.size() != other.size():
            raise InvalidShapeError
        result = 0
        for i in range(self.size()):
            result = result + self.data[i] * other.data[i].conjugate()
        return result

    def __matmul__(self, other):
        """Calcule le produit scalaire avec l'opérateur @.
        
        Args:
            other (Vector): Vecteur avec lequel calculer le produit.
        
        Returns:
            int | float | complex: Résultat du produit scalaire.
        """
        return self.dot(other)

    def norm_1(self):
        """Calcule la norme L1 (Manhattan) du vecteur.
        
        La norme L1 est la somme des valeurs absolues des composantes.
        ||v||₁ = Σ |v[i]|
        
        Returns:
            float: La norme L1 du vecteur.
        
        Examples:
            >>> v = Vector([1.0, -2.0, 3.0])
            >>> v.norm_1()
            6.0
        """
        return sum(abs(x) for x in self.data)

    def norm(self):
        """Calcule la norme L2 (euclidienne) du vecteur.
        
        La norme L2 est la racine carrée de la somme des carrés.
        ||v||₂ = √(Σ |v[i]|²)
        
        Returns:
            float: La norme L2 du vecteur.
        
        Examples:
            >>> v = Vector([3.0, 4.0])
            >>> v.norm()
            5.0
        """
        result = 0
        for i in range(self.size()):
            result = result + abs(self.data[i]) ** 2
        return pow(result, 0.5)

    def norm_inf(self):
        """Calcule la norme infinie (supremum) du vecteur.
        
        La norme infinie est la valeur absolue maximale des composantes.
        ||v||∞ = max(|v[i]|)
        
        Returns:
            float: La norme infinie du vecteur.
        
        Examples:
            >>> v = Vector([1.0, -5.0, 3.0])
            >>> v.norm_inf()
            5.0
        """
        return max(abs(x) for x in self.data)
    
    def angle_cos(self, other):
        """Calcule le cosinus de l'angle entre deux vecteurs.
        
        Utilise la formule : cos(θ) = (u · v) / (||u|| * ||v||)
        
        Args:
            other (Vector): Second vecteur.
        
        Returns:
            float | complex: Cosinus de l'angle entre les vecteurs.
        
        Raises:
            InvalidValueError: Si other n'est pas un Vector, si les tailles
                diffèrent, ou si l'un des vecteurs est nul.
        
        Examples:
            >>> u = Vector([1.0, 0.0])
            >>> v = Vector([0.0, 1.0])
            >>> u.angle_cos(v)
            0.0
        """
        if not isinstance(other, Vector):
            raise InvalidValueError
        if self.size() != other.size():
            raise InvalidValueError
        if self.norm() == 0 or other.norm() == 0:
            raise InvalidValueError

        return self.dot(other) / (self.norm() * other.norm())

    def cross_product(self, other):
        """Calcule le produit vectoriel de deux vecteurs 3D.
        
        Le produit vectoriel est défini uniquement pour les vecteurs
        de dimension 3 et produit un vecteur orthogonal aux deux vecteurs.
        
        Args:
            other (Vector): Second vecteur 3D.
        
        Returns:
            Vector: Vecteur résultant du produit vectoriel.
        
        Raises:
            TypeError: Si other n'est pas un Vector.
            ValueError: Si les vecteurs ne sont pas de dimension 3.
        
        Examples:
            >>> u = Vector([1.0, 0.0, 0.0])
            >>> v = Vector([0.0, 1.0, 0.0])
            >>> print(u.cross_product(v))
            [0.0]
            [0.0]
            [1.0]
        """
        if not isinstance(other, Vector):
            raise TypeError
        if self.size() != 3 or other.size() != 3:
            raise ValueError
        return Vector([
            self.data[1] * other.data[2] - self.data[2] * other.data[1],
            self.data[2] * other.data[0] - self.data[0] * other.data[2],
            self.data[0] * other.data[1] - self.data[1] * other.data[0]
        ])

