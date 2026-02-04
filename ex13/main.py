import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from matrix import Matrix

def main():
    # Test 1: Matrice identité 3x3 → rang 3
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.],
    ])
    print(f"Rang test 1: {u.rank()}")
    # Expected: 3

    # Test 2: Matrice avec lignes dépendantes → rang 2
    u = Matrix([
        [1., 2., 0., 0.],
        [2., 4., 0., 0.],   # = 2 × ligne 1
        [-1., 2., 1., 1.],
    ])
    print(f"Rang test 2: {u.rank()}")
    # Expected: 2

    # Test 3: Matrice 4x3 → rang 3
    u = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
        [21., 18., 7.],
    ])
    print(f"Rang test 3: {u.rank()}")
    # Expected: 3

if __name__ == "__main__":
    main()