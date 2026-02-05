# filepath: 
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from vector import Vector

print("=" * 50)
print("EXERCICE 05 - Cosine (Complexes)")
print("=" * 50)

# Tests avec réels (exemples du sujet)
print("\n--- Tests avec réels ---\n")

u = Vector([1., 0.])
v = Vector([1., 0.])
print(f"[1., 0.] · [1., 0.] → cos = {u.angle_cos(v)}")
# Attendu: 1.0

u = Vector([1., 0.])
v = Vector([0., 1.])
print(f"[1., 0.] · [0., 1.] → cos = {u.angle_cos(v)}")
# Attendu: 0.0

u = Vector([-1., 1.])
v = Vector([1., -1.])
print(f"[-1., 1.] · [1., -1.] → cos = {u.angle_cos(v)}")
# Attendu: -1.0

u = Vector([2., 1.])
v = Vector([4., 2.])
print(f"[2., 1.] · [4., 2.] → cos = {u.angle_cos(v)}")
# Attendu: 1.0

u = Vector([1., 2., 3.])
v = Vector([4., 5., 6.])
print(f"[1., 2., 3.] · [4., 5., 6.] → cos = {u.angle_cos(v):.9f}")
# Attendu: 0.974631846

# Tests avec complexes
print("\n--- Tests avec complexes ---\n")

# Même vecteur → cos = 1
u = Vector([1 + 1j, 2 - 1j])
print(f"u = {u.data}")
print(f"cos(u, u) = {u.angle_cos(u)}")
# Attendu: 1.0 (réel)

# Vecteurs orthogonaux
u = Vector([1, 1j])
v = Vector([1j, 1])
print(f"\nu = {u.data}")
print(f"v = {v.data}")
print(f"cos(u, v) = {u.angle_cos(v)}")

# Résultat complexe possible
u = Vector([1 + 1j, 0])
v = Vector([1, 1j])
print(f"\nu = {u.data}")
print(f"v = {v.data}")
print(f"cos(u, v) = {u.angle_cos(v)}")

print("\n" + "=" * 50)
print("Tests terminés !")
print("=" * 50)