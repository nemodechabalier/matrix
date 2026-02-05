import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from matrix import Matrix

print("=" * 50)
print("EXERCICE 09 - Transpose (Complexes)")
print("=" * 50)

# Tests avec réels
print("\n--- Tests avec réels ---\n")

u = Matrix([
    [1., 2.],
    [3., 4.],
])
print("M =")
print(u)
print("\nM^T =")
print(u.transpose())
# Attendu: [[1, 3], [2, 4]]

u = Matrix([
    [1., 2., 3.],
    [4., 5., 6.],
])
print("\nM (2x3) =")
print(u)
print("\nM^T (3x2) =")
print(u.transpose())

# Tests avec complexes
print("\n--- Tests avec complexes ---\n")

u = Matrix([
    [1 + 1j, 2 - 1j],
    [3j, 4],
])
print("M =")
print(u)
print("\nM^H (transposée conjuguée) =")
print(u.transpose())
# Attendu: [[1-1j, -3j], [2+1j, 4]]

u = Matrix([
    [1j, 2j],
    [3j, 4j],
])
print("\nM =")
print(u)
print("\nM^H =")
print(u.transpose())
# Attendu: [[-1j, -3j], [-2j, -4j]]

# Propriété importante : (A^H)^H = A
u = Matrix([
    [1 + 2j, 3 - 1j],
    [2 - 3j, 4 + 1j],
])
print("\nM =")
print(u)
print("\n(M^H)^H = M ?")
print(u.transpose().transpose())

print("\n" + "=" * 50)
print("Tests terminés !")
print("=" * 50)