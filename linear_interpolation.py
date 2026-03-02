"""Module Linear Interpolation - Interpolation linéaire (lerp).

Ce module fournit une fonction pour calculer l'interpolation linéaire
entre deux valeurs scalaires, vecteurs ou matrices.
"""

from vector import Vector
from matrix import Matrix


class InvalidValueError(ValueError):
    """Exception levée lorsqu'une valeur invalide est fournie.
    
    Attributes:
        msg (str): Message d'erreur décrivant le problème.
    """
    
    def __init__(self, msg="Lerp : Invalid Value"):
        super().__init__(msg)


class InvalidTypeError(ValueError):
    """Exception levée lorsqu'un type invalide est fourni.
    
    Attributes:
        msg (str): Message d'erreur décrivant le problème.
    """
    
    def __init__(self, msg="Lerp : Invalid Type"):
        super().__init__(msg)


def lerp(u, v, t):
    """Calcule l'interpolation linéaire entre deux valeurs.
    
    L'interpolation linéaire (lerp) retourne un point entre u et v
    en fonction du paramètre t : lerp(u, v, t) = u + t × (v - u)
    
    - t = 0 retourne u
    - t = 1 retourne v
    - t = 0.5 retourne le milieu entre u et v
    
    Args:
        u: Valeur de départ (int, float, complex, Vector ou Matrix).
        v: Valeur d'arrivée (même type que u).
        t (float): Paramètre d'interpolation dans [0, 1].
    
    Returns:
        Le résultat de l'interpolation (même type que u et v).
    
    Raises:
        InvalidTypeError: Si t n'est pas un nombre, si t ∉ [0, 1],
            ou si u et v ne sont pas du même type.
    
    Examples:
        >>> lerp(0., 10., 0.5)
        5.0
        >>> lerp(Vector([0., 0.]), Vector([10., 20.]), 0.5)
        Vector([5., 10.])
    """
    if not isinstance(t, (float, int)):
        raise InvalidTypeError
    if t > 1 or t < 0:
        raise InvalidTypeError
    if not isinstance(u, (int, float, complex, Matrix, Vector)):
        raise InvalidTypeError
    if type(u) != type(v):
        raise InvalidTypeError

    return u + t * (v - u)

