import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from matrix import Matrix

def main():
    # Test 1: Matrice identité (déjà en RREF)
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.],
    ])
    print("Test 1 - Identité:")
    print(u.row_echelon())
    # Expected:
    # [1.0, 0.0, 0.0]
    # [0.0, 1.0, 0.0]
    # [0.0, 0.0, 1.0]

    print("\n" + "="*40 + "\n")

    # Test 2: Matrice 2x2 simple
    u = Matrix([
        [1., 2.],
        [3., 4.],
    ])
    print("Test 2 - Matrice 2x2:")
    print(u.row_echelon())
    # Expected:
    # [1.0, 0.0]
    # [0.0, 1.0]

    print("\n" + "="*40 + "\n")

    # Test 3: Matrice avec lignes dépendantes (rang déficient)
    u = Matrix([
        [1., 2.],
        [2., 4.],
    ])
    print("Test 3 - Lignes dépendantes:")
    print(u.row_echelon())
    # Expected:
    # [1.0, 2.0]
    # [0.0, 0.0]

    print("\n" + "="*40 + "\n")

    # Test 4: Matrice rectangulaire (système augmenté)
    u = Matrix([
        [8., 5., -2., 4., 28.],
        [4., 2.5, 20., 4., -4.],
        [8., 5., 1., 4., 17.],
    ])
    print("Test 4 - Matrice 3x5:")
    print(u.row_echelon())
    # Expected:
    # [1.0, 0.625, 0.0, 0.0, -12.1666667]
    # [0.0, 0.0, 1.0, 0.0, -3.6666667]
    # [0.0, 0.0, 0.0, 1.0, 29.5]

    print("\n" + "="*40 + "\n")

    # Test 5: Matrice avec pivot nul (nécessite échange de lignes)
    u = Matrix([
        [0., 1.],
        [1., 0.],
    ])
    print("Test 5 - Pivot nul:")
    print(u.row_echelon())
    # Expected:
    # [1.0, 0.0]
    # [0.0, 1.0]

    print("\n" + "="*40 + "\n")

    # Test 6: Matrice 3x3
    u = Matrix([
        [1., 2., 3.],
        [4., 5., 6.],
        [7., 8., 9.],
    ])
    print("Test 6 - Matrice 3x3 (rang 2):")
    print(u.row_echelon())
    # Expected: rang 2, dernière ligne nulle

if __name__ == "__main__":
    main()