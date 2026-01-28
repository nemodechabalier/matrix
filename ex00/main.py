from vector import Vector
from matrix import Matrix

# Test Vector
print("=== Vector Tests ===")
u = Vector([2., 3.])
v = Vector([5., 7.])
print("u + v:")
print(u + v)
# [7.0]
# [10.0]

u = Vector([2., 3.])
v = Vector([5., 7.])
print("u - v:")
print(u - v)
# [-3.0]
# [-4.0]

u = Vector([2., 3.])
print("u * 2:")
print(u * 2)
# [4.0]
# [6.0]

# Test Matrix
print("\n=== Matrix Tests ===")
u = Matrix([[1., 2.], [3., 4.]])
v = Matrix([[7., 4.], [-2., 2.]])
print("u + v:")
print(u + v)
# [8.0, 6.0]
# [1.0, 6.0]

u = Matrix([[1., 2.], [3., 4.]])
v = Matrix([[7., 4.], [-2., 2.]])
print("u - v:")
print(u - v)
# [-6.0, -2.0]
# [5.0, 2.0]

u = Matrix([[1., 2.], [3., 4.]])
print("u * 2:")
print(u * 2)
# [2.0, 4.0]
# [6.0, 8.0]