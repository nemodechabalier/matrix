from vector import Vector
from matrix import Matrix
from linear_interpolation import lerp


result_1 = lerp(0., 1., 0.)
print(f"lerp(0, 1, 0) = {result_1}")

result_2 = lerp(0., 1., 1.)
print(f"lerp(0, 1, 1) = {result_2}")

result_3 = lerp(0., 1., 0.5)
print(f"lerp(0, 1, 0.5) = {result_3}")

result_4 = lerp(21., 42., 0.3)
print(f"lerp(21, 42, 0.3) = {result_4}")

vec_u = Vector([2., 1.])
vec_v = Vector([4., 2.])
result_vec = lerp(vec_u, vec_v, 0.3)
print(f"\nlerp(Vector, Vector, 0.3):")
print(result_vec)

mat_u = Matrix([[2., 1.], [3., 4.]])
mat_v = Matrix([[20., 10.], [30., 40.]])
result_mat = lerp(mat_u, mat_v, 0.5)
print(f"\nlerp(Matrix, Matrix, 0.5):")
print(result_mat)