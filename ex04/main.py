import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from vector import Vector

# Tests pour l'exercice 04 - Norms

u = Vector([0., 0., 0.])
print(f"[0, 0, 0] -> norm_1: {u.norm_1()}, norm: {u.norm()}, norm_inf: {u.norm_inf()}")
# 0.0, 0.0, 0.0

u = Vector([1., 2., 3.])
print(f"[1, 2, 3] -> norm_1: {u.norm_1()}, norm: {u.norm()}, norm_inf: {u.norm_inf()}")
# 6.0, 3.74165738, 3.0

u = Vector([-1., -2.])
print(f"[-1, -2] -> norm_1: {u.norm_1()}, norm: {u.norm()}, norm_inf: {u.norm_inf()}")
# 3.0, 2.236067977, 2.0