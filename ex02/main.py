import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from vector import Vector
from matrix import Matrix
from linear_interpolation import lerp

print("=" * 50)
print("EXERCICE 02 - Linear Interpolation (Complexes)")
print("=" * 50)

# Tests avec réels (exemples du sujet)
print("\n--- Tests avec réels ---\n")

print(f"lerp(0., 1., 0.) = {lerp(0., 1., 0.)}")
# Attendu: 0.0

print(f"lerp(0., 1., 1.) = {lerp(0., 1., 1.)}")
# Attendu: 1.0

print(f"lerp(0., 1., 0.5) = {lerp(0., 1., 0.5)}")
# Attendu: 0.5

print(f"lerp(21., 42., 0.3) = {lerp(21., 42., 0.3)}")
# Attendu: 27.3

# Vecteurs réels
print("\nlerp(Vector([2., 1.]), Vector([4., 2.]), 0.3) =")
print(lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3))
# Attendu: [2.6] [1.3]

# Matrices réelles
print("\nlerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5) =")
print(lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5))
# Attendu: [[11., 5.5], [16.5, 22.]]

# Tests avec complexes
print("\n--- Tests avec complexes ---\n")

# Scalaires complexes
print(f"lerp(0+0j, 2+2j, 0.5) = {lerp(0+0j, 2+2j, 0.5)}")
# Attendu: 1+1j

print(f"lerp(1+1j, 3-1j, 0.5) = {lerp(1+1j, 3-1j, 0.5)}")
# Attendu: 2+0j

# Vecteurs complexes
u = Vector([1 + 1j, 2 - 2j])
v = Vector([3 + 3j, 4 - 4j])

print(f"\nu = {u.data}")
print(f"v = {v.data}")
print("\nlerp(u, v, 0.) =")
print(lerp(u, v, 0.))
# Attendu: [1+1j] [2-2j]

print("\nlerp(u, v, 1.) =")
print(lerp(u, v, 1.))
# Attendu: [3+3j] [4-4j]

print("\nlerp(u, v, 0.5) =")
print(lerp(u, v, 0.5))
# Attendu: [2+2j] [3-3j]

# Matrices complexes
m1 = Matrix([[1 + 1j, 2], [3j, 4 - 1j]])
m2 = Matrix([[5 + 5j, 6], [7j, 8 - 5j]])

print("\nm1 =")
print(m1)
print("\nm2 =")
print(m2)
print("\nlerp(m1, m2, 0.5) =")
print(lerp(m1, m2, 0.5))
# Attendu: milieu entre m1 et m2

print("\n" + "=" * 50)
print("Tests terminés !")
print("=" * 50)