# filepath: /home/nemo/Documents/Artificial-Inteligence/matrix/ex06/main.py
"""Exercice 06 - Cross Product.

Ce module teste le produit vectoriel de deux vecteurs 3D :
u × v = [u₂v₃ - u₃v₂, u₃v₁ - u₁v₃, u₁v₂ - u₂v₁]

Le résultat est un vecteur orthogonal aux deux vecteurs d'entrée.
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from vector import Vector


def main():
    """Fonction principale pour tester le produit vectoriel.
    
    Teste cross_product avec des vecteurs 3D réels et complexes.
    """

    print("=" * 50)
    print("EXERCICE 06 - Cross Product (Complexes)")
    print("=" * 50)
    
    # Tests avec réels (exemples du sujet)
    print("\n--- Tests avec réels ---\n")
    
    u = Vector([0., 0., 1.])
    v = Vector([1., 0., 0.])
    print(f"[0., 0., 1.] × [1., 0., 0.] =")
    print(u.cross_product(v))
    # Attendu: [0.] [1.] [0.]
    
    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(f"\n[1., 2., 3.] × [4., 5., 6.] =")
    print(u.cross_product(v))
    # Attendu: [-3.] [6.] [-3.]
    
    u = Vector([4., 2., -3.])
    v = Vector([-2., -5., 16.])
    print(f"\n[4., 2., -3.] × [-2., -5., 16.] =")
    print(u.cross_product(v))
    # Attendu: [17.] [-58.] [-16.]
    
    # Tests avec complexes
    print("\n--- Tests avec complexes ---\n")
    
    u = Vector([1 + 1j, 0, 0])
    v = Vector([0, 1 - 1j, 0])
    print(f"u = {u.data}")
    print(f"v = {v.data}")
    print(f"u × v =")
    print(u.cross_product(v))
    # Attendu: [0] [0] [(1+1j)*(1-1j)] = [0] [0] [2]
    
    u = Vector([1j, 2j, 3j])
    v = Vector([1, 2, 3])
    print(f"\nu = {u.data}")
    print(f"v = {v.data}")
    print(f"u × v =")
    print(u.cross_product(v))
    # Attendu: [0] [0] [0] (colinéaires)
    
    u = Vector([1 + 1j, 2 - 1j, 3])
    v = Vector([2, 1 + 2j, 1 - 1j])
    print(f"\nu = {u.data}")
    print(f"v = {v.data}")
    print(f"u × v =")
    print(u.cross_product(v))
    
    print("\n" + "=" * 50)
    print("Tests terminés !")
    print("=" * 50)

if __name__ == "__main__":
	main()