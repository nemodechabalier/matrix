import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from vector import Vector

# Tests pour l'exercice 05 - Cosine

u = Vector([1., 0.])
v = Vector([1., 0.])
print(f"[1, 0] · [1, 0] cos = {u.angle_cos(v)}")
# 1.0

u = Vector([1., 0.])
v = Vector([0., 1.])
print(f"[1, 0] · [0, 1] cos = {u.angle_cos(v)}")
# 0.0

u = Vector([-1., 1.])
v = Vector([1., -1.])
print(f"[-1, 1] · [1, -1] cos = {u.angle_cos(v)}")
# -1.0

u = Vector([2., 1.])
v = Vector([4., 2.])
print(f"[2, 1] · [4, 2] cos = {u.angle_cos(v)}")
# 1.0

u = Vector([1., 2., 3.])
v = Vector([4., 5., 6.])
print(f"[1, 2, 3] · [4, 5, 6] cos = {u.angle_cos(v)}")
# 0.974631846