from scipy import linalg
import numpy as np

A = np.array([
    [1,2],
    [3,4]
])

x = linalg.det(A)
print(x)

l, v = linalg.eig(A)

print(l)
print(v)

a = np.random.randn(3, 2) + 1.j*np.random.randn(3, 2)
U, s, Vh = linalg.svd(a)
print(U, Vh, s)