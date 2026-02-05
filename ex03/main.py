import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from vector import Vector

print("=" * 50)
print("EXERCICE 03 - Dot Product (Complexes)")
print("=" * 50)

# Tests avec réels (exemples du sujet)
print("\n--- Tests avec réels ---\n")

u = Vector([0., 0.])
v = Vector([1., 1.])
print(f"[0., 0.] · [1., 1.] = {u.dot(v)}")
# Attendu: 0.0

u = Vector([1., 1.])
v = Vector([1., 1.])
print(f"[1., 1.] · [1., 1.] = {u.dot(v)}")
# Attendu: 2.0

u = Vector([-1., 6.])
v = Vector([3., 2.])
print(f"[-1., 6.] · [3., 2.] = {u.dot(v)}")
# Attendu: 9.0

# Tests avec complexes
print("\n--- Tests avec complexes ---\n")

# Test basique
u = Vector([1 + 1j, 2 - 1j])
v = Vector([1 - 1j, 2 + 1j])
print(f"u = {u.data}")
print(f"v = {v.data}")
print(f"u · v = {u.dot(v)}")
# (1+1j)*(1+1j) + (2-1j)*(2-1j) = 2j + (4-4j+1) = 5 - 2j

# Produit avec soi-même (doit être réel et positif)
u = Vector([1 + 1j, 2 - 1j])
print(f"\nu = {u.data}")
print(f"u · u = {u.dot(u)}")
# |1+1j|² + |2-1j|² = 2 + 5 = 7 (réel positif)

# Vecteurs purement imaginaires
u = Vector([1j, 2j, 3j])
v = Vector([1j, 1j, 1j])
print(f"\nu = {u.data}")
print(f"v = {v.data}")
print(f"u · v = {u.dot(v)}")
# 1j*(-1j) + 2j*(-1j) + 3j*(-1j) = 1 + 2 + 3 = 6

print("\n" + "=" * 50)
print("Tests terminés !")
print("=" * 50)

"""
>>> (3 + 4j).conjugate()
(3-4j)

>>> (2 - 5j).conjugate()
(2+5j)

>>> (7 + 0j).conjugate()  # réel pur
(7-0j)

>>> (0 + 3j).conjugate()  # imaginaire pur
-3j

"""