from vector import Vector
from matrix import Matrix

class InvalidValueError(ValueError):
    def __init__(self, msg="Lerp : Invalid Value"):
        super().__init__(msg)

class InvalidTypeError(ValueError):
    def __init__(self, msg="Lerp : Invalid Type"):
        super().__init__(msg)

def lerp(u , v, t) -> Vector:
    """
    Computes a linear combination of vectors.
    
    Args:
        vectors: list of Vector [v1, v2, ..., vk]
        coefs: list of scalars [a1, a2, ..., ak]
    
    Returns:
        a1*v1 + a2*v2 + ... + ak*vk
    """
    if not isinstance(t, (float, int)):
        raise InvalidTypeError
    if  t > 1 or t < 0:
        raise InvalidTypeError
    if not isinstance(u, (int, float, complex, Matrix, Vector)):
        raise InvalidTypeError
    if type(u) != type(v):
        raise InvalidTypeError

    return u + t * (v - u)

