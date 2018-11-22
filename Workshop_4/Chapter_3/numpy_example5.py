import numpy as np

# Example 1
# math functions

a = np.array([0,30,45,60,90])
sin = np.sin(a*np.pi/180)
print(sin, "\n")
print(np.cos(a*np.pi/180), "\n")

inv = np.arcsin(sin)
print(inv, "\n")

print(np.degrees(inv), "\n")


# Example 2
# Floor and ceil
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print(np.floor(a), "\n")
print(np.ceil(a), "\n")

# Example 3
# arithmetic operations

a = np.arange(9,dtype=np.float_).reshape(3,3)
b = np.array([10,10,10])

print(a - b, "\n")
print(a + b, "\n")
print(a * b, "\n")
print(a / b, "\n")

# Example 4
# reciprocal
# UWAGA NA TYPY
a = np.array([0.25, 1.33, 1, 0, 100])
print(a,"\n")
print(np.reciprocal(a), "\n")

# Example 5
# Liczby zespolone
a = np.array([-5.6j, 0.2j, 11. , 1+1j])
print(a,"\n")
print(np.imag(a), "\n")
print(np.real(a), "\n")
print(np.conj(a), "\n")
print(np.angle(a), "\n")

# Example 6
# Mean, std, median
a = np.array([1,6,3,8,3,2,6,2,5,8,2,4,6,3,2,1,7,4])

print(np.mean(a),"\n")
print(np.median(a),"\n")
print(np.std(a),"\n")

# Example 7
# argmax, argmin, where
print(np.argmax(a), "\n")
print(np.argmin(a), "\n")
print(np.where(a > 4), "\n")