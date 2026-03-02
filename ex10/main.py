"""Exercice 10 - Row Echelon Form.

Ce module teste la réduction en forme échelonnée réduite (RREF)
d'une matrice en utilisant l'élimination de Gauss-Jordan.
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from matrix import Matrix


def main():
    """Fonction principale pour tester la forme échelonnée.
    
    Teste row_echelon avec des matrices réelles et complexes.
    """

    print("=" * 50)
    print("EXERCICE 10 - Row Echelon Form (Complexes)")
    print("=" * 50)
    
    # Tests avec réels (exemples du sujet)
    print("\n--- Tests avec réels ---\n")
    
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.],
    ])
    print("I =")
    print(u.row_echelon())
    
    u = Matrix([
        [0., 2., 1.],
        [3., 6., 1.],
        [0., 4., 2.],
    ])
    print(f"I =\n{u}\nforme =\n")
    print(u.row_echelon())
    
    u = Matrix([
        [1., 2.],
        [3., 4.],
    ])
    print("\n[[1, 2], [3, 4]] →")
    print(u.row_echelon())
    # Attendu: [[1, 0], [0, 1]]
    
    u = Matrix([
        [1., 2.],
        [2., 4.],
    ])
    print("\n[[1, 2], [2, 4]] →")
    print(u.row_echelon())
    # Attendu: [[1, 2], [0, 0]]
    
    u = Matrix([
        [8., 5., -2., 4., 28.],
        [4., 2.5, 20., 4., -4.],
        [8., 5., 1., 4., 17.],
    ])
    print("\nMatrice augmentée →")
    print(u.row_echelon())
    
    # Tests avec complexes
    print("\n--- Tests avec complexes ---\n")
    
    u = Matrix([
        [1 + 1j, 2],
        [1 - 1j, 2],
    ])
    print("[[1+1j, 2], [1-1j, 2]] →")
    print(u.row_echelon())
    
    u = Matrix([
        [1j, 1],
        [1, 1j],
    ])
    print("\n[[1j, 1], [1, 1j]] →")
    print(u.row_echelon())
    # det = j*j - 1 = -1 - 1 = -2 ≠ 0, donc inversible
    
    u = Matrix([
        [1 + 1j, 0, 0],
        [0, 2 - 1j, 0],
        [0, 0, 3j],
    ])
    print("\nMatrice diagonale complexe →")
    print(u.row_echelon())
    # Attendu: I (identité)
    
    u = Matrix([
        [1, 1j, 2],
        [1j, -1, 2j],
        [2, 2j, 4],
    ])
    print("\nMatrice singulière complexe →")
    print(u.row_echelon())
    
    print("\n" + "=" * 50)
    print("Tests terminés !")
    print("=" * 50)

if __name__ == "__main__":
	main()