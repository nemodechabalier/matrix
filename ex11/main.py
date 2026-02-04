import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from matrix import Matrix
m1 = Matrix([[1., -1.], [-1., 1.]])
print(m1.determinant())  # 0.0

m2 = Matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]])
print(m2.determinant())  # 8.0

m3 = Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]])
print(m3.determinant())  # -174.0

m4 = Matrix([[8., 5., -2., 4.], [4., 2.5, 20., 4.], [8., 5., 1., 4.], [28., -4., 17., 1.]])
print(m4.determinant())  # 1032.0