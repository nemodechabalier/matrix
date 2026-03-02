"""Exercice 11 - Determinant.

Ce module teste le calcul du déterminant d'une matrice carrée
jusqu'à 4x4 en utilisant le développement par cofacteurs.
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from matrix import Matrix


def main():
    """Fonction principale pour tester le déterminant.
    
    Teste determinant avec des matrices réelles et complexes (1x1 à 4x4).
    """
    
    print("=" * 50)
    print("EXERCICE 11 - Determinant (Complexes)")
    print("=" * 50)
    
    # Tests avec réels (exemples du sujet)
    print("\n--- Tests avec réels ---\n")
    
    u = Matrix([
        [1., -1.],
        [-1., 1.],
    ])
    print(f"det([[1, -1], [-1, 1]]) = {u.determinant()}")
    # Attendu: 0.0
    
    u = Matrix([
        [2., 0., 0.],
        [0., 2., 0.],
        [0., 0., 2.],
    ])
    print(f"det(2I) = {u.determinant()}")
    # Attendu: 8.0
    
    u = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
    ])
    print(f"det([[8,5,-2],[4,7,20],[7,6,1]]) = {u.determinant()}")
    # Attendu: -174.0
    
    u = Matrix([
        [8., 5., -2., 4.],
        [4., 2.5, 20., 4.],
        [8., 5., 1., 4.],
        [28., -4., 17., 1.],
    ])
    print(f"det(4x4) = {u.determinant()}")
    # Attendu: 1032
    
    # Tests avec complexes
    print("\n--- Tests avec complexes ---\n")
    
    # Matrice 2x2
    u = Matrix([
        [1 + 1j, 2],
        [3, 4 - 1j],
    ])
    print(f"det([[1+1j, 2], [3, 4-1j]]) = {u.determinant()}")
    # (1+1j)(4-1j) - 2*3 = 4-1j+4j-1j² - 6 = 4+3j+1-6 = -1+3j
    
    # det = 0 pour matrice singulière
    u = Matrix([
        [1 + 1j, 2 + 2j],
        [1, 2],
    ])
    print(f"det([[1+1j, 2+2j], [1, 2]]) = {u.determinant()}")
    # (1+1j)*2 - (2+2j)*1 = 2+2j - 2-2j = 0
    
    # Matrice diagonale complexe
    u = Matrix([
        [1j, 0, 0],
        [0, 2j, 0],
        [0, 0, 3j],
    ])
    print(f"det(diag(1j, 2j, 3j)) = {u.determinant()}")
    # 1j * 2j * 3j = 6j³ = 6 * (-j) = -6j
    
    # Matrice 3x3 complexe
    u = Matrix([
        [1, 1j, 0],
        [1j, 1, 1j],
        [0, 1j, 1],
    ])
    print(f"det([[1,1j,0],[1j,1,1j],[0,1j,1]]) = {u.determinant()}")
    
    # Matrice 4x4 complexe
    u = Matrix([
        [1+1j, 0, 0, 0],
        [0, 1-1j, 0, 0],
        [0, 0, 2j, 0],
        [0, 0, 0, 1],
    ])
    print(f"det(diag 4x4) = {u.determinant()}")
    # (1+1j)(1-1j)(2j)(1) = 2 * 2j = 4j
    
    print("\n" + "=" * 50)
    print("Tests terminés !")
    print("=" * 50)
    
if __name__ == "__main__":
	main()