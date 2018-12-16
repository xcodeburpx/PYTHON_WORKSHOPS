import numpy as np
import matplotlib.pyplot as plt


# Load the data
X = []
Y = []
for line in open('data_poly.csv'):
    x, y = line.split(',')
    x = float(x)
    X.append([1, x, x*x, 3*x**3])
    Y.append(float(y))


# To np.array
X = np.array(X)
Y = np.array(Y)

# plot the data
plt.scatter(X[:,1],Y)
plt.grid()
plt.show()

# Calculate weights
w = np.linalg.solve(np.dot(X.T, X), np.dot(X.T,Y))
Yhat = np.dot(X,w)

# plot line + points
plt.scatter(X[:,1], Y)
plt.plot(sorted(X[:,1]),sorted(Yhat), 'r')
plt.grid()
plt.show()

# r-squared
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1)/d2.dot(d2)
print("R2 score =", r2)