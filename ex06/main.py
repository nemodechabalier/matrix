import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from vector import Vector

# Tests pour l'exercice 06 - Cross Product

u = Vector([0., 0., 1.])
v = Vector([1., 0., 0.])
print(f"[0, 0, 1] × [1, 0, 0] =")
print(u.cross_product(v))
# [0.]
# [1.]
# [0.]

print()

u = Vector([1., 2., 3.])
v = Vector([4., 5., 6.])
print(f"[1, 2, 3] × [4, 5, 6] =")
print(u.cross_product(v))
# [-3.]
# [6.]
# [-3.]

print()

u = Vector([4., 2., -3.])
v = Vector([-2., -5., 16.])
print(f"[4, 2, -3] × [-2, -5, 16] =")
print(u.cross_product(v))
# [17.]
# [-58.]
# [-16.]