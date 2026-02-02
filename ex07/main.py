import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from matrix import Matrix
from vector import Vector

# Tests pour l'exercice 07 - Matrix multiplication

print("=== Matrix × Vector ===\n")

u = Matrix([
    [1., 0.],
    [0., 1.],
])
v = Vector([4., 2.])
print("Identity × [4, 2]:")
print(u.mul_vec(v))
# [4.]
# [2.]

print()

u = Matrix([
    [2., 0.],
    [0., 2.],
])
v = Vector([4., 2.])
print("Scale(2) × [4, 2]:")
print(u.mul_vec(v))
# [8.]
# [4.]

print()

u = Matrix([
    [2., -2.],
    [-2., 2.],
])
v = Vector([4., 2.])
print("[[2, -2], [-2, 2]] × [4, 2]:")
print(u.mul_vec(v))
# [4.]
# [-4.]

print("\n=== Matrix × Matrix ===\n")

u = Matrix([
    [1., 0.],
    [0., 1.],
])
v = Matrix([
    [1., 0.],
    [0., 1.],
])
print("Identity × Identity:")
print(u.mul_mat(v))
# [1., 0.]
# [0., 1.]

print()

u = Matrix([
    [1., 0.],
    [0., 1.],
])
v = Matrix([
    [2., 1.],
    [4., 2.],
])
print("Identity × [[2, 1], [4, 2]]:")
print(u.mul_mat(v))
# [2., 1.]
# [4., 2.]

print()

u = Matrix([
    [3., -5.],
    [6., 8.],
])
v = Matrix([
    [2., 1.],
    [4., 2.],
])
print("[[3, -5], [6, 8]] × [[2, 1], [4, 2]]:")
print(u.mul_mat(v))
# [-14., -7.]
# [44., 22.]