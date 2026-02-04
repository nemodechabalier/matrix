import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from matrix import Matrix
# Matrice identité
m1 = Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
print(m1.inverse(),"\n")  # Identité

# Matrice 2*I
m2 = Matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]])
print(m2.inverse(),"\n")  # 0.5 * I

# Matrice quelconque
m3 = Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]])
print(m3.inverse())