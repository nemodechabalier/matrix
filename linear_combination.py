"""Module Linear Combination - Combinaison linéaire de vecteurs.

Ce module fournit une fonction pour calculer la combinaison linéaire
d'une liste de vecteurs avec des coefficients scalaires.
"""

from vector import Vector


class InvalidValueError(ValueError):
    """Exception levée lorsqu'une valeur invalide est fournie.
    
    Attributes:
        msg (str): Message d'erreur décrivant le problème.
    """
    
    def __init__(self, msg="Linear combination: Invalid Value"):
        super().__init__(msg)


class InvalidTypeError(ValueError):
    """Exception levée lorsqu'un type invalide est fourni.
    
    Attributes:
        msg (str): Message d'erreur décrivant le problème.
    """
    
    def __init__(self, msg="Linear combination: Invalid Type"):
        super().__init__(msg)


def linear_combination(vectors: list[Vector], coefs: list[float, int, complex]) -> Vector:
    """Calcule une combinaison linéaire de vecteurs.
    
    Étant donné une liste de vecteurs [v₁, v₂, ..., vₖ] et une liste
    de coefficients [a₁, a₂, ..., aₖ], calcule :
    a₁·v₁ + a₂·v₂ + ... + aₖ·vₖ
    
    Args:
        vectors (list[Vector]): Liste de vecteurs de même dimension.
        coefs (list): Liste de scalaires (int, float ou complex).
    
    Returns:
        Vector: Le vecteur résultant de la combinaison linéaire.
    
    Raises:
        InvalidValueError: Si les listes sont vides ou de tailles différentes,
            ou si les vecteurs ont des dimensions différentes.
        InvalidTypeError: Si les types des éléments sont invalides.
    
    Examples:
        >>> e1 = Vector([1., 0., 0.])
        >>> e2 = Vector([0., 1., 0.])
        >>> e3 = Vector([0., 0., 1.])
        >>> result = linear_combination([e1, e2, e3], [10., -2., 0.5])
        >>> result.data
        [10.0, -2.0, 0.5]
    """
    if len(vectors) != len(coefs) or len(vectors) == 0:
        raise InvalidValueError
    size = vectors[0].size()
    for i in range(len(vectors)):
        if not isinstance(vectors[i], Vector) or not isinstance(coefs[i], (int, float, complex)):
            raise InvalidTypeError
        if vectors[i].size() != size:
            raise InvalidValueError

    result = Vector([0.0] * size)
    
    for i in range(len(vectors)):
        result = result + vectors[i] * coefs[i]
    
    return result
