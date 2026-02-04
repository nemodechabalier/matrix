import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from vector import Vector


u = Vector([0., 0.])
v = Vector([1., 1.])
print(f"[0, 0] · [1, 1] = {u.dot(v)}")
# 0.0

u = Vector([1., 1.])
v = Vector([1., 1.])
print(f"[1, 1] · [1, 1] = {u.dot(v)}")
# 2.0

u = Vector([-1., 6.])
v = Vector([3., 2.])
print(f"[-1, 6] · [3, 2] = {u.dot(v)}")
# 9.0