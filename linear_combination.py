from vector import Vector


class InvalidValueError(ValueError):
    def __init__(self, msg="Linear combination: Invalid Value"):
        super().__init__(msg)

class InvalidTypeError(ValueError):
    def __init__(self, msg="Linear combination: Invalid Type"):
        super().__init__(msg)

def linear_combination(vectors: list[Vector], coefs: list[float, int, complex]) -> Vector:
    """
    Computes a linear combination of vectors.
    
    Args:
        vectors: list of Vector [v1, v2, ..., vk]
        coefs: list of scalars [a1, a2, ..., ak]
    
    Returns:
        a1*v1 + a2*v2 + ... + ak*vk
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
