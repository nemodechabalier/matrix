import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from vector import Vector
from linear_combination import linear_combination


e1 = Vector([1., 0., 0.])
e2 = Vector([0., 1., 0.])
e3 = Vector([0., 0., 1.])

result = linear_combination([e1, e2, e3], [10., -2., 0.5])
print(result,"\n")
# [10.0]
# [-2.0]
# [0.5]

v1 = Vector([1., 2., 3.])
v2 = Vector([0., 10., -100.])
print(linear_combination([v1, v2], [10., -2.]))
# [10.0]
# [0.0]
# [230.0]