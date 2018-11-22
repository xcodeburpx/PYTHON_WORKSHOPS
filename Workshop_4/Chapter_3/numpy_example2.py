import numpy as np

# Example 1
# Array slicing

a = np.arange(10)
b = a[2:7:2]
print(b, "\n")

# Example 2
b = a[2:]
print(b, "\n")

# Example 3
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a, "\n")

b = a[..., 1]
print(b, "\n")

b = a[1, ...]
print(b, "\n")

# Example 4
# Advance
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x, "\n")

z = x[1:4, 1:3]
print(z, "\n")

y = x[1:4, [1, 2]]
print(y, "\n")

# Example 5
# boolean array
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x, "\n")

print(x[x>5], "\n")