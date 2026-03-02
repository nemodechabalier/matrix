"""Module Projection - Matrice de projection perspective.

Ce module fournit une fonction pour générer une matrice de projection
perspective utilisée en graphisme 3D.
"""

from math import tan, radians
from matrix import Matrix


class InvalidValueError(ValueError):
    """Exception levée lorsqu'une valeur invalide est fournie.
    
    Attributes:
        msg (str): Message d'erreur décrivant le problème.
    """
    
    def __init__(self, msg="Projection: Invalid Value"):
        super().__init__(msg)


def projection(fov: float = 60.0, ratio: float = 16 / 9, near: float = 0.1, far: float = 100.0) -> Matrix:
    """Génère une matrice de projection perspective 4x4.
    
    Cette fonction crée une matrice de projection utilisée pour
    transformer des coordonnées 3D en coordonnées 2D avec effet
    de perspective (objets plus lointains apparaissent plus petits).
    
    Args:
        fov (float): Champ de vision vertical en degrés (0 < fov < 180).
            Par défaut: 60.0
        ratio (float): Rapport largeur/hauteur de l'écran (> 0).
            Par défaut: 16/9
        near (float): Distance du plan de clipping proche (> 0).
            Par défaut: 0.1
        far (float): Distance du plan de clipping éloigné (> near).
            Par défaut: 100.0
    
    Returns:
        Matrix: Matrice de projection 4x4.
    
    Raises:
        InvalidValueError: Si les paramètres sont hors limites valides.
    
    Examples:
        >>> proj = projection(60.0, 16/9, 0.1, 100.0)
        >>> proj.shape()
        (4, 4)
    """
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