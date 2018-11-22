import numpy as np

# Simple numpy array
a = np.array([1, 2, 3])
print(a)

a = np.array([[1, 2], [3, 4]])
print(a)

# Assign the type -> e.g. complex
a = np.array([1,2,3], dtype=np.complex64)
print(a)

# Data type
# Mamy wartości od int8 aż do complex128

# Example 1
dt = np.dtype(np.int32)
print(dt)

# Example 2
# >i4 -> int8 big endian
# <i4 -> int8 little endian
dt = np.dtype('>i4')
print(dt)

# Example 3
# Zastosowanie typu własnego
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a)
print(a['age'])

# Example 4
# Bardziej rozbudowany typ
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a)

# Example 5
# Atrubyty tablicy NumPy
a = np.array([[1,2,3], [4,5,6]])
print(a.shape)

# Example 6
# Możliwość zmiany kształtu
# atrybut shape
a = np.array([[1,2,3], [4,5,6]])
a.shape = (3,2)
print(a)

# Example 7
# Preferowana metoda do zmiany kształtu
# np.reshape

a = np.array([[1,2,3], [4,5,6]])
a = a.reshape(3,2)
print(a)


# Example 8
# Atrybut ndim
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.ndim)
b = np.array([
    [[1,2,3], [4,5,6]],
    [[7,8,9], [10,11,12]]
])
print(b.ndim)

# Example 9
# Zmiana kształtu tablicy -> trzeci wymiar
# UWAGA -> iloczyn liczb stanowiących nowe wymiary = liczbie elementów
a = np.array(np.arange(24))
print(a)
b = a.reshape(2,3,4)
print(b)

# Sztuczka, wartość -1 -> gdy nie mamy pewności co wstawić
c = a.reshape(6,-1)
print(c.shape)

# Example 10
# itemsize -> długość każdego elementu tablicy (w bajtach)
x = np.array([1,2,3,4,5], dtype = np.int8)
print(x.itemsize)
x = np.array([1,2,3,4,5], dtype = np.float128)
print(x.itemsize)

# Example 10
# numpy.empty -> tworzenie "pustej tablicy"
a = np.empty([3,2], dtype=np.int8)
print(a)

# Example 11
# numpy.zeros -> tablica z elementami = 0
a = np.zeros(5, dtype=np.complex64)
print(a)

# Example 12
# numpy.ones -> tablica z elementami = 1
x = np.ones([2,2], dtype = int)
print(x)

# Example 13
# numpy.asarray -> zmiana typu pythonowego -> typ numpy
data = [(1,2,3), (6,7)]
a = np.asarray(data)
print(a)


# Example 14
# numpy.arange
# Działa tak jak pythonowy range
x = np.arange(10,30,2)
print(x)

# Example 15
# numpy linspace
x = np.linspace(1,30,150, endpoint=True)
print(x.shape)
print(x)

print("\n\n")
x = np.linspace(1,30,11, retstep=True, endpoint=True)
#print(x.shape)
print(x)


# Example 16
# numpy.logspace -> funkcja range ale dla wartości potęgowe
# e.g logspace(1.0,2.0, num=10) -> range od 10^1.0 do 10^2.0 dla 10 punktów
a = np.logspace(1.0,2.0, num=10)
print(a)

# Kolejny przykład -> baza 2
a = np.logspace(1,10,num=10, base=2)
print(a)