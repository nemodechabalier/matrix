import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from vector import Vector

print("=" * 50)
print("EXERCICE 04 - Norms (Complexes)")
print("=" * 50)

# Tests avec réels (exemples du sujet)
print("\n--- Tests avec réels ---\n")

u = Vector([0., 0., 0.])
print(f"[0., 0., 0.] : norm_1={u.norm_1()}, norm={u.norm()}, norm_inf={u.norm_inf()}")
# Attendu: 0.0, 0.0, 0.0

u = Vector([1., 2., 3.])
print(f"[1., 2., 3.] : norm_1={u.norm_1()}, norm={u.norm():.6f}, norm_inf={u.norm_inf()}")
# Attendu: 6.0, 3.741657, 3.0

u = Vector([-1., -2.])
print(f"[-1., -2.] : norm_1={u.norm_1()}, norm={u.norm():.6f}, norm_inf={u.norm_inf()}")
# Attendu: 3.0, 2.236068, 2.0

# Tests avec complexes
print("\n--- Tests avec complexes ---\n")

# |3+4j| = 5
u = Vector([3 + 4j])
print(f"[3+4j] : norm_1={u.norm_1()}, norm={u.norm()}, norm_inf={u.norm_inf()}")
# Attendu: 5.0, 5.0, 5.0

# |1+1j| = sqrt(2), |2+2j| = sqrt(8)
u = Vector([1 + 1j, 2 + 2j])
print(f"[1+1j, 2+2j] : norm_1={u.norm_1():.6f}, norm={u.norm():.6f}, norm_inf={u.norm_inf():.6f}")
# norm_1 = sqrt(2) + sqrt(8) ≈ 4.242641
# norm = sqrt(2 + 8) = sqrt(10) ≈ 3.162278
# norm_inf = sqrt(8) ≈ 2.828427

# Vecteur purement imaginaire
u = Vector([3j, 4j])
print(f"[3j, 4j] : norm_1={u.norm_1()}, norm={u.norm()}, norm_inf={u.norm_inf()}")
# Attendu: 7.0, 5.0, 4.0

print("\n" + "=" * 50)
print("Tests terminés !")
print("=" * 50)