import numpy as np

# Example 1
# Broadcasting
a = np.array([10,20,30,40])
b = np.array([1,2,3,4])
c = a * b

print(c, "\n")


# Example 2
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
b = np.array([1.0,2.0,3.0])

c = a + b
print(c, "\n")