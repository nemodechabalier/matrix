from math import tan, radians
from matrix import Matrix


class InvalidValueError(ValueError):
    def __init__(self, msg="Projection: Invalid Value"):
        super().__init__(msg)

def projection(fov: float = 60.0, ratio: float = 16 / 9, near: float = 0.1, far: float = 100.0):
    if not all(isinstance(x, (int, float)) for x in (fov, ratio, near, far)):
        raise InvalidValueError
    if fov >= 180 or fov <= 0:
        raise InvalidValueError
    if ratio <= 0 or near <= 0:
        raise InvalidValueError
    if near >= far:
        raise InvalidValueError
    fov_rad = radians(fov)  # Convertir degrés → radians
    scale = 1 / tan(fov_rad / 2)
    proj = Matrix([
            [scale / ratio, 0.0, 0.0, 0.0],
            [0.0, scale, 0.0, 0.0],
            [0.0, 0.0, -far / (far - near), -(far * near) / (far - near)],
            [0.0, 0.0, -1, 0.0]
    ])
    return proj