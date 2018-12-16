import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

n_neighbors = 15 # <- ilość sąsiadów brana pod uwagę przy ocenie klasy

# Import data
iris = datasets.load_iris()


# Split the data
X = iris.data[:,:2]
y = iris.target

h = 0.02    # Step size in the meshgrid

cmap_light = ListedColormap(['#FFAAAA', "#AAFFAA", "#AAAAFF"])
cmap_bold = ListedColormap(['#FF0000',"#00FF00", "#0000FF"])

# List of types of weight interpetations
for weights in ['uniform', 'distance']:
    # Create Neighbours Classifier
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X,y) # <- Pass all the data to create boundaries

    # Plot the decision boundary.
    #
    x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Into color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx,yy,Z, cmap=cmap_light)

    # Plot points
    plt.scatter(X[:,0], X[:,1],c=y, cmap=cmap_bold, edgecolor='k',s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
              % (n_neighbors, weights))

plt.show()
