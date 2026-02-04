import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from matrix import Matrix

def main():
    # Test 1: Matrice 2x3
    u = Matrix([
        [1., 2., 3.],
        [4., 5., 6.],
    ])
    print("Original (2x3):")
    print(u)
    print(f"Shape: {u.shape()}")
    print("\nTransposée (3x2):")
    t = u.transpose()
    print(t)
    print(f"Shape: {t.shape()}")
    # Expected:
    # [1.0, 4.0]
    # [2.0, 5.0]
    # [3.0, 6.0]

    print("\n" + "="*30 + "\n")

    # Test 2: Matrice carrée 3x3
    u = Matrix([
        [1., 2., 3.],
        [4., 5., 6.],
        [7., 8., 9.],
    ])
    print("Original (3x3):")
    print(u)
    print("\nTransposée (3x3):")
    print(u.transpose())
    # Expected:
    # [1.0, 4.0, 7.0]
    # [2.0, 5.0, 8.0]
    # [3.0, 6.0, 9.0]

    print("\n" + "="*30 + "\n")

    # Test 3: Vecteur ligne 1x4
    u = Matrix([
        [1., 2., 3., 4.],
    ])
    print("Original (1x4):")
    print(u)
    print(f"Shape: {u.shape()}")
    print("\nTransposée (4x1):")
    t = u.transpose()
    print(t)
    print(f"Shape: {t.shape()}")

    print("\n" + "="*30 + "\n")

    # Test 4: Double transposée = originale
    u = Matrix([
        [1., 2.],
        [3., 4.],
        [5., 6.],
    ])
    print("Test (Aᵀ)ᵀ = A:")
    print(f"Original: {u.shape()}")
    print(f"Double transposée: {u.transpose().transpose().shape()}")
    print(f"Égalité des données: {u.data == u.transpose().transpose().data}")

if __name__ == "__main__":
    main()