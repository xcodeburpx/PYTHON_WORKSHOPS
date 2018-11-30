import numpy as np
import matplotlib.pyplot as plt

# Dane wejściowe
N = 50
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))

# print(x.shape, y.shape)
# print(x)
# print(y)

# Funkcja wyjściowa
Z = (np.cos(x*0.2) + np.sin(y*0.3))

# Zamaskuj pewne wartości
Zpos = np.ma.masked_less(Z,0)
Zneg = np.ma.masked_greater(Z,0)

# Stwórz plot mapę
fig, (ax1, ax2) = plt.subplots(figsize=(8,3), ncols=2)

# Narysuj posytywne wartości
pos = ax1.imshow(Zpos, cmap='Blues', interpolation='none')
fig.colorbar(pos, ax=ax1)

# Narysuj negatywne wartości
neg = ax2.imshow(Zneg, cmap='Reds_r', interpolation='none')
fig.colorbar(neg, ax=ax2)

plt.show()


