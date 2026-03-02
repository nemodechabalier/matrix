"""Exercice 00 - Add, Subtract and Scale.

Ce module teste les opérations de base sur les vecteurs et matrices :
- Addition de vecteurs/matrices (+)
- Soustraction de vecteurs/matrices (-)
- Multiplication par un scalaire (scaling)
- Conversion vecteur ↔ matrice
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from vector import Vector
from matrix import Matrix


def main():
    """Fonction principale pour tester les opérations de base.
    
    Teste l'addition, la soustraction et le scaling sur des vecteurs
    et matrices avec des nombres réels et complexes.
    """
    # Test Vector
    print("=== Vector Tests ===")
    u = Vector([2., 3.])
    v = Vector([5., 7.])
    print("u + v:")
    print(u + v)
    # [7.0]
    # [10.0]
    
    u = Vector([2., 3.])
    v = Vector([5., 7.])
    print("u - v:")
    print(u - v)
    # [-3.0]
    # [-4.0]
    
    u = Vector([2., 3.])
    print("u * 2:")
    print(u * 2)
    # [4.0]
    # [6.0]
    print(f"u = {u}  u reshape = {u.vector_to_matrix(2,1)}")
    
    # Test Matrix
    print("\n=== Matrix Tests ===")
    u = Matrix([[1., 2.], [3., 4.]])
    v = Matrix([[7., 4.], [-2., 2.]])
    print("u + v:")
    print(u + v)
    # [8.0, 6.0]
    # [1.0, 6.0]
    
    u = Matrix([[1., 2.], [3., 4.]])
    v = Matrix([[7., 4.], [-2., 2.]])
    print("u - v:")
    print(u - v)
    # [-6.0, -2.0]
    # [5.0, 2.0]
    
    u = Matrix([[1., 2.], [3., 4.]])
    print("u * 2:")
    print(u * 2)
    # [2.0, 4.0]
    # [6.0, 8.0]
    print(f"u = \n{u}\nu reshape =\n{u.matrix_to_vector()}")
    
    
    
    print("=" * 50)
    print("\n--- Tests avec complexes ---\n")
    print("=" * 50)
    
    # ========== VECTEURS ==========
    print("\n--- VECTEURS ---\n")
    
    u = Vector([2 + 1j, 3 - 2j])
    v = Vector([5 - 1j, 7 + 3j])
    
    print("u =")
    print(u)
    print("\nv =")
    print(v)
    
    # Addition
    print("\nu + v =")
    print(u + v)
    # Attendu: [7.0] [10.0+1j]
    
    # Soustraction
    print("\nu - v =")
    print(u - v)
    # Attendu: [-3.0+2j] [-4.0-5j]
    
    # Scaling
    print("\nu * 2 =")
    print(u * 2)
    # Attendu: [4.0+2j] [6.0-4j]
    
    # Scaling avec scalaire complexe
    print("\nu * (1 + 1j) =")
    print(u * (1 + 1j))
    # Attendu: [(2+1j)*(1+1j)] [(3-2j)*(1+1j)] = [1+3j] [5+1j]
    
    # ========== MATRICES ==========
    print("\n--- MATRICES ---\n")
    
    m1 = Matrix([
        [1 + 1j, 2 - 1j],
        [3j, 4]
    ])
    m2 = Matrix([
        [7, 4 + 2j],
        [-2 - 1j, 2j]
    ])
    
    print("m1 =")
    print(m1)
    print("\nm2 =")
    print(m2)
    
    # Addition
    print("\nm1 + m2 =")
    print(m1 + m2)
    
    # Soustraction
    print("\nm1 - m2 =")
    print(m1 - m2)
    
    # Scaling
    print("\nm1 * 2 =")
    print(m1 * 2)
    
    # Scaling avec scalaire complexe
    print("\nm1 * (1 - 1j) =")
    print(m1 * (1 - 1j))
    
    print("\n" + "=" * 50)
    print("Tests terminés !")
    print("=" * 50)

if __name__ == "__main__":
	main()