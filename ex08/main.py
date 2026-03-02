"""Exercice 08 - Trace.

Ce module teste le calcul de la trace d'une matrice carrée :
Tr(A) = Σ A[i][i] (somme des éléments diagonaux)
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from matrix import Matrix


def main():
    """Fonction principale pour tester la trace matricielle.
    
    Teste la trace avec des matrices réelles et complexes.
    """
	
    print("=" * 50)
    print("EXERCICE 08 - Trace (Complexes)")
    print("=" * 50)
    
    # Tests avec réels (exemples du sujet)
    print("\n--- Tests avec réels ---\n")
    
    u = Matrix([
        [1., 0.],
        [0., 1.],
    ])
    print(f"Tr(I) = {u.trace()}")
    # Attendu: 2.0
    
    u = Matrix([
        [2., -5., 0.],
        [4., 3., 7.],
        [-2., 3., 4.],
    ])
    print(f"Tr([[2, -5, 0], [4, 3, 7], [-2, 3, 4]]) = {u.trace()}")
    # Attendu: 9.0
    
    u = Matrix([
        [-2., -8., 4.],
        [1., -23., 4.],
        [0., 6., 4.],
    ])
    print(f"Tr([[-2, -8, 4], [1, -23, 4], [0, 6, 4]]) = {u.trace()}")
    # Attendu: -21.0
    
    # Tests avec complexes
    print("\n--- Tests avec complexes ---\n")
    
    u = Matrix([
        [1 + 1j, 0],
        [0, 1 - 1j],
    ])
    print(f"Tr([[1+1j, 0], [0, 1-1j]]) = {u.trace()}")
    # Attendu: 2+0j = 2
    
    u = Matrix([
        [1j, 2],
        [3, 4j],
    ])
    print(f"Tr([[1j, 2], [3, 4j]]) = {u.trace()}")
    # Attendu: 5j
    
    u = Matrix([
        [1 + 2j, 0, 0],
        [0, 3 - 1j, 0],
        [0, 0, 2 + 3j],
    ])
    print(f"Tr(diag(1+2j, 3-1j, 2+3j)) = {u.trace()}")
    # Attendu: 6+4j
    
    print("\n" + "=" * 50)
    print("Tests terminés !")
    print("=" * 50)
    
if __name__ == "__main__":
	main()