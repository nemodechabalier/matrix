"""Exercice 01 - Linear Combination.

Ce module teste la fonction de combinaison linéaire de vecteurs :
a₁·v₁ + a₂·v₂ + ... + aₖ·vₖ
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from vector import Vector
from linear_combination import linear_combination


def main():
    """Fonction principale pour tester la combinaison linéaire.
    
    Teste la combinaison linéaire avec des vecteurs réels et complexes.
    """
    
    print("=" * 50)
    print("EXERCICE 01 - Linear Combination (Complexes)")
    print("=" * 50)
    
    # Test avec réels (exemples du sujet)
    print("\n--- Tests avec réels ---\n")
    
    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])
    
    print("linear_combination([e1, e2, e3], [10., -2., 0.5]) =")
    print(linear_combination([e1, e2, e3], [10., -2., 0.5]))
    # Attendu: [10.] [-2.] [0.5]
    
    v1 = Vector([1., 2., 3.])
    v2 = Vector([0., 10., -100.])
    
    print("\nlinear_combination([v1, v2], [10., -2.]) =")
    print(linear_combination([v1, v2], [10., -2.]))
    # Attendu: [10.] [0.] [230.]
    
    # Test avec complexes
    print("\n--- Tests avec complexes ---\n")
    
    c1 = Vector([1 + 1j, 0., 0.])
    c2 = Vector([0., 1 - 1j, 0.])
    c3 = Vector([0., 0., 2j])
    
    print("c1 =", c1.data)
    print("c2 =", c2.data)
    print("c3 =", c3.data)
    
    print("\nlinear_combination([c1, c2, c3], [2., 3., 1.]) =")
    print(linear_combination([c1, c2, c3], [2., 3., 1.]))
    # Attendu: [2+2j] [3-3j] [2j]
    
    # Coefficients complexes
    print("\nlinear_combination([c1, c2], [1+1j, 2-1j]) =")
    print(linear_combination([c1, c2], [1 + 1j, 2 - 1j]))
    # Attendu: [2j] [(1-3j)] [0j]
    
    print("\n" + "=" * 50)
    print("Tests terminés !")
    print("=" * 50)

if __name__ == "__main__":
	main()