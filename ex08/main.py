import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from matrix import Matrix

def main():
    # Test 1: Matrice identité 2x2
    u = Matrix([
        [1., 0.],
        [0., 1.],
    ])
    print(f"Trace test 1: {u.trace()}")
    # Expected: 2.0

    # Test 2: Matrice 3x3
    u = Matrix([
        [2., -5., 0.],
        [4., 3., 7.],
        [-2., 3., 4.],
    ])
    print(f"Trace test 2: {u.trace()}")
    # Expected: 9.0

    # Test 3: Matrice 3x3 avec valeurs négatives
    u = Matrix([
        [-2., -8., 4.],
        [1., -23., 4.],
        [0., 6., 4.],
    ])
    print(f"Trace test 3: {u.trace()}")
    # Expected: -21.0

if __name__ == "__main__":
    main()