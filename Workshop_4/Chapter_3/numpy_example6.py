import numpy as np

# Example 1
# Dot operation

a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])

print(a.dot(b), "\n")

# Example 2
# vdot
print(np.vdot(a,b),"\n")

# Example 3
# Matmul

a = [[1,0],[0,1]]
b = [[4,1],[2,2]]
print(np.matmul(a,b),"\n")
print(np.matmul(b,a),"\n")


# Example 4
# solve

a = np.array([[1,2,3], [3,2,1], [1,4,1]])
b = np.array([10,5,2])
x = np.linalg.solve(a,b)
print(x,"\n")

print(np.allclose(np.dot(a,x),b),"\n")