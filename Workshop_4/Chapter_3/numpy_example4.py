import numpy as np

# Example 1
# flat
a = np.arange(10).reshape(2,-1)
print(a, "\n")

print(a.flat[5], "\n")

# Example 2
# flatten
a = np.arange(8).reshape(2,-1)
print(a.flatten(), "\n")
print(a.flatten(order='F'), "\n")

# Example 3
# ravel
print(a.ravel(),"\n")
print(a.ravel(order="F"), "\n")

# Example 4
# transpose
a = np.arange(12).reshape(3,4)
print(a,"\n")
print(np.transpose(a), "\n")
print(a.T,"\n")

# Example 5
# swapaxes
a = np.arange(8).reshape(2,2,2)
print(a,"\n")
print(np.swapaxes(a, 2, 0), "\n")

# Example 6
# expand_dims
x = np.array(([1,2],[3,4]))
print(x, "\n")
print(x.shape,"\n")

y = np.expand_dims(x, axis=0)
print(y,"\n")
print(y.shape,"\n")

# Example 7
# squeeze
x = np.arange(9).reshape(1,3,3)
print(x.shape,"\n")
y = np.squeeze(x)
print(y.shape,"\n")

# Example 8
# concatenate
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(a,"\n")
print(b,"\n")

c = np.concatenate([a,b])
print(c,"\n")

# Example 9
# hstack

c = np.hstack([a,b])
print(c,"\n")

# Example 10
# vstack
c = np.vstack([a,b])
print(c,"\n")

# Example 11
# unique
a = np.array([5,2,6,2,7,5,6,8,2,9])

print(a, "\n")

u = np.unique(a)
print(u, "\n")

u, indices = np.unique(a,return_index=True)
print(indices,"\n")