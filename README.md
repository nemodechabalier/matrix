# Matrix — 42 Linear Algebra Project

Implementation of a linear algebra library in Python, supporting both real numbers and **complex numbers** (bonus exercise 15).

## Structure

```
matrix/
├── matrix.py               # Matrix class
├── vector.py               # Vector class
├── linear_combination.py   # Ex01
├── linear_interpolation.py # Ex02
├── projection.py           # Ex14
├── ex00/ - ex14/           # Main test files
```

## Classes

### `Vector`
- Supports `int`, `float`, `complex`
- Stored as a flat list

### `Matrix`
- Supports `int`, `float`, `complex`
- Stored in **row-major order**

---

## Exercises

### Ex00 — Add, Subtract, Scale
Operations on vectors and matrices.

| Operation | Formula |
|-----------|---------|
| Addition | $C_{ij} = A_{ij} + B_{ij}$ |
| Subtraction | $C_{ij} = A_{ij} - B_{ij}$ |
| Scaling | $(\alpha A)_{ij} = \alpha A_{ij}$ |

**Complexity:** O(n) time, O(n) space

---

### Ex01 — Linear Combination
$$\sum_{i=1}^{k} \lambda_i \cdot u_i = \lambda_1 u_1 + \cdots + \lambda_k u_k$$

**Complexity:** O(nk) time, O(n) space

---

### Ex02 — Linear Interpolation (lerp)
$$\text{lerp}(u, v, t) = u + t\,(v - u), \quad t \in [0, 1] \subset \mathbb{R}$$

**Complexity:** O(n) time, O(n) space

---

### Ex03 — Dot Product
**Reals:** $u \cdot v = \sum_{i} u_i v_i$

**Complexes (hermitian):** $\langle u | v \rangle = \sum_{i} u_i \overline{v_i}$

> The conjugate of `v` ensures the result is real and positive when `u == v`.

**Complexity:** O(n) time, O(1) space

---

### Ex04 — Norms
| Norm | Formula |
|------|---------|
| 1-norm (Manhattan) | $\|v\|_1 = \sum_i \|v_i\|$ |
| 2-norm (Euclidean) | $\|v\|_2 = \sqrt{\sum_i \|v_i\|^2}$ |
| ∞-norm (Supremum) | $\|v\|_\infty = \max_i \|v_i\|$ |

> For complex numbers, `abs(z)` returns the modulus $\sqrt{a^2+b^2}$, keeping norms real and positive.

**Complexity:** O(n) time, O(1) space

---

### Ex05 — Cosine
$$\cos(\theta) = \frac{\langle u | v \rangle}{\|u\|\,\|v\|}$$

> For complex vectors, the result may be complex.

**Complexity:** O(n) time, O(1) space

---

### Ex06 — Cross Product (3D only)
$$u \times v = \begin{pmatrix} u_2 v_3 - u_3 v_2 \\ u_3 v_1 - u_1 v_3 \\ u_1 v_2 - u_2 v_1 \end{pmatrix}$$

**Complexity:** O(1) time, O(1) space

---

### Ex07 — Matrix Multiplication
**Matrix × Vector:** $(Au)_i = \sum_{j} A_{ij} u_j$

**Matrix × Matrix:** $(AB)_{ij} = \sum_{k} A_{ik} B_{kj}$

**Complexity:** O(nm) / O(nmp) time

---

### Ex08 — Trace
$$\text{Tr}(A) = \sum_{i=1}^{n} A_{ii}$$

**Complexity:** O(n) time, O(1) space

---

### Ex09 — Transpose
**Reals:** $(A^T)_{ij} = A_{ji}$

**Complexes (conjugate transpose):** $(A^H)_{ij} = \overline{A_{ji}}$

**Complexity:** O(nm) time, O(nm) space

---

### Ex10 — Row Echelon Form (RREF)
Gauss-Jordan elimination:
1. Find the largest pivot in the column
2. Swap rows
3. Normalize (divide by pivot → 1)
4. Eliminate above and below

**Complexity:** O(n³) time, O(n²) space

---

### Ex11 — Determinant
| Size | Method |
|------|--------|
| 1×1 | $a_{00}$ |
| 2×2 | $ad - bc$ |
| 3×3 | Sarrus rule |
| 4×4 | Cofactor expansion (recursive) |

> $\det(A) = 0 \Rightarrow$ singular matrix (no inverse)

**Complexity:** O(n³) time, O(n²) space

---

### Ex12 — Inverse
Gauss-Jordan on augmented matrix $[A\,|\,I]$:
$$[A | I] \xrightarrow{\text{Gauss-Jordan}} [I | A^{-1}]$$

Raises an error if the matrix is singular ($\det(A) = 0$).

**Complexity:** O(n³) time, O(n²) space

---

### Ex13 — Rank
$$\text{rank}(A) = \text{number of non-zero rows in RREF}$$

**Complexity:** O(n³) time (dominated by row echelon)

---

### Ex14 — Projection Matrix (Bonus)
Perspective projection matrix for 3D rendering (OpenGL).

$$P = \begin{pmatrix} \frac{1}{\tan(fov/2) \cdot ratio} & 0 & 0 & 0 \\ 0 & \frac{1}{\tan(fov/2)} & 0 & 0 \\ 0 & 0 & \frac{far}{far-near} & -\frac{far \cdot near}{far-near} \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

> Output written in column-major order for the display software.

---

### Ex15 — Complex Numbers (Bonus)
All exercises redone with $K = \mathbb{C}$ instead of $K = \mathbb{R}$.

**Modifications made:**
| Exercise | Change |
|----------|--------|
| All | Accept `complex` in type validation |
| Ex03 | `.conjugate()` on second vector |
| Ex04 | `abs(x) ** 2` instead of `x ** 2` |
| Ex09 | Conjugate transpose $A^H$ |

---

## Usage

```python
from vector import Vector
from matrix import Matrix

# Reals
v = Vector([1.0, 2.0, 3.0])
m = Matrix([[1, 0], [0, 1]])

# Complexes
v = Vector([1+1j, 2-1j])
m = Matrix([[1+1j, 0], [0, 1-1j]])
```

## Run tests

```bash
cd ex00 && python main.py
cd ex01 && python main.py
# ...
```
