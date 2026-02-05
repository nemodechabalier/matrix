import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from vector import Vector
from matrix import Matrix

print("=" * 50)
print("EXERCICE 07 - Matrix Multiplication (Complexes)")
print("=" * 50)

# Tests avec réels (exemples du sujet)
print("\n--- Tests mul_vec avec réels ---\n")

u = Matrix([
    [1., 0.],
    [0., 1.],
])
v = Vector([4., 2.])
print("I * [4., 2.] =")
print(u.mul_vec(v))
# Attendu: [4.] [2.]

u = Matrix([
    [2., 0.],
    [0., 2.],
])
v = Vector([4., 2.])
print("\n2I * [4., 2.] =")
print(u.mul_vec(v))
# Attendu: [8.] [4.]

u = Matrix([
    [2., -2.],
    [-2., 2.],
])
v = Vector([4., 2.])
print("\n[[2, -2], [-2, 2]] * [4., 2.] =")
print(u.mul_vec(v))
# Attendu: [4.] [-4.]

print("\n--- Tests mul_mat avec réels ---\n")

u = Matrix([
    [1., 0.],
    [0., 1.],
])
v = Matrix([
    [1., 0.],
    [0., 1.],
])
print("I * I =")
print(u.mul_mat(v))
# Attendu: [[1., 0.], [0., 1.]]

u = Matrix([
    [3., -5.],
    [6., 8.],
])
v = Matrix([
    [2., 1.],
    [4., 2.],
])
print("\n[[3, -5], [6, 8]] * [[2, 1], [4, 2]] =")
print(u.mul_mat(v))
# Attendu: [[-14., -7.], [44., 22.]]

# Tests avec complexes
print("\n--- Tests mul_vec avec complexes ---\n")

u = Matrix([
    [1 + 1j, 0],
    [0, 1 - 1j],
])
v = Vector([2, 3j])
print(f"M = [[1+1j, 0], [0, 1-1j]]")
print(f"v = [2, 3j]")
print("M * v =")
print(u.mul_vec(v))
# (1+1j)*2 = 2+2j, (1-1j)*3j = 3j-3j² = 3+3j

print("\n--- Tests mul_mat avec complexes ---\n")

u = Matrix([
    [1j, 0],
    [0, 1j],
])
v = Matrix([
    [1j, 0],
    [0, 1j],
])
print("[[j, 0], [0, j]] * [[j, 0], [0, j]] =")
print(u.mul_mat(v))
# j*j = -1 → [[-1, 0], [0, -1]]

u = Matrix([
    [1 + 1j, 2 - 1j],
    [3j, 4],
])
v = Matrix([
    [2, 1j],
    [1 - 1j, 3],
])
print(f"\nM1 =")
print(u)
print(f"\nM2 =")
print(v)
print("\nM1 * M2 =")
print(u.mul_mat(v))

print("\n" + "=" * 50)
print("Tests terminés !")
print("=" * 50)