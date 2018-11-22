# Example 1
# Matrices
import numpy as np
mat = np.matrix('1 2; 3 4')
print(mat)

print(mat.H)
print(mat.T)

# Example 2
# Clusters
from scipy.cluster.vq import kmeans, vq, whiten

data = np.vstack((np.random.rand(100,3) + np.array([.5,.5,.5]),np.random.rand(100,3)))

print(data)

data = whiten(data) # <- Normalize a group of observations on a per feature basis.

centroids,_ = kmeans(data,3) # <- Compute K-means cluster centers

print(centroids)

clx,_ = vq(data,centroids) # <- assign data to each center

print(clx)