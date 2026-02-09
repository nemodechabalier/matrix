import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from matrix import Matrix

print("=" * 50)
print("EXERCICE 13 - Rank (Complexes)")
print("=" * 50)

# Tests avec réels (exemples du sujet)
print("\n--- Tests avec réels ---\n")

u = Matrix([
    [1., 0., 0.],
    [0., 1., 0.],
    [0., 0., 1.],
])
print(f"rank(I) = {u.rank()}")
# Attendu: 3

u = Matrix([
    [1., 2., 0., 0.],
    [2., 4., 0., 0.],
    [-1., 2., 1., 1.],
])
print(f"rank([[1,2,0,0],[2,4,0,0],[-1,2,1,1]]) = {u.rank()}")
# Attendu: 2

u = Matrix([
    [8., 5., -2.],
    [4., 7., 20.],
    [7., 6., 1.],
    [21., 18., 7.],
])
print(f"rank(4x3) = {u.rank()}")
# Attendu: 3

# Tests avec complexes
print("\n--- Tests avec complexes ---\n")

# Identité complexe
u = Matrix([
    [1 + 0j, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
])
print(f"rank(I) = {u.rank()}")
# Attendu: 3

# Matrice de rang 1 (lignes multiples)
u = Matrix([
    [1 + 1j, 2 - 1j],
    [2 + 2j, 4 - 2j],
])
print(f"rank([[1+1j, 2-1j], [2+2j, 4-2j]]) = {u.rank()}")
# Attendu: 1 (ligne 2 = 2 * ligne 1)

# Matrice de rang plein
u = Matrix([
    [1j, 1],
    [1, 1j],
])
print(f"rank([[1j, 1], [1, 1j]]) = {u.rank()}")
# Attendu: 2 (det = -2 ≠ 0)

# Matrice rectangulaire complexe
u = Matrix([
    [1, 1j, 2],
    [1j, -1, 2j],
    [2, 2j, 4],
])
print(f"rank(singulière 3x3) = {u.rank()}")
# Attendu: 1 (toutes les lignes sont multiples)

# Matrice 4x3 complexe
u = Matrix([
    [1 + 1j, 0, 0],
    [0, 2 - 1j, 0],
    [0, 0, 3j],
    [1 + 1j, 2 - 1j, 3j],
])
print(f"rank(4x3 complexe) = {u.rank()}")
# Attendu: 3

print("\n" + "=" * 50)
print("Tests terminés !")
print("=" * 50)