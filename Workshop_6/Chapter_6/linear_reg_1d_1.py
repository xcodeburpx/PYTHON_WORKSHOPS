import numpy as np
import matplotlib.pyplot as plt

# load the data
X = []
Y = []
for line in open("data_1d.csv"):
    x, y = line.split(",")
    X.append(float(x))
    Y.append(float(y))


# Into numpy arrays
X = np.array(X)
Y = np.array(Y)

# Plot the data
plt.scatter(X,Y)
plt.grid()
plt.show()

# Calculate A and B

demoninator = X.dot(X) - X.mean()*X.sum()
a = (X.dot(Y) - Y.mean()*X.sum())/demoninator
b = (Y.mean()*X.dot(X) - X.mean()*X.dot(Y))/demoninator


Yhat = a*X + b

# Plot points + line
plt.scatter(X,Y)
plt.plot(X, Yhat, 'r')
plt.grid()
plt.show()


# Calculate the R^2
d1 = Y - Yhat
d2 = Y - Y.mean()

r2 = 1 - d1.dot(d1)/d2.dot(d2)
print("R2 score =", r2)
