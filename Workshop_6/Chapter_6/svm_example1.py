import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

# Load the data
iris = datasets.load_iris()
X = iris.data
Y = iris.target

# Grab only two classes
X = X[Y != 0, :2]
Y = Y[Y != 0]

n_samples = len(X)

# Randomization
np.random.seed(0)
order = np.random.permutation(n_samples)
X = X[order]
Y = Y[order].astype(np.float)

# Split for training and testing set
X_train = X[:int(0.9* n_samples)]
y_train = Y[:int(0.9*n_samples)]
X_test = X[int(0.9*n_samples):]
y_test = Y[int(0.9*n_samples):]

# Fit, predict and plot
for fig_num, kernel in enumerate(['linear', 'rbf', 'poly']):
    clf = svm.SVC(kernel=kernel, gamma=10)
    clf.fit(X_train, y_train)

    # Plot the points
    plt.figure(fig_num)
    plt.clf()
    plt.scatter(X[:, 0], X[:, 1], c=Y, zorder=10, cmap=plt.cm.Paired,
                edgecolor='k', s=20)

    # Circle out the test data
    plt.scatter(X_test[:, 0], X_test[:, 1], s=80, facecolors='none',
                zorder=10, edgecolor='k')

    plt.axis('tight')

    # Big predict matrix
    x_min = X[:, 0].min()
    x_max = X[:, 0].max()
    y_min = X[:, 1].min()
    y_max = X[:, 1].max()

    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    # Calculate the distance from the boundary
    Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
    # Put the results into a color plot
    Z = Z.reshape(XX.shape)
    plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
    plt.contour(XX, YY, Z, colors=['k', 'k', 'k'],
                linestyles=['--', '-', '--'], levels=[-.5, 0, .5])

    plt.title(kernel)
plt.show()
