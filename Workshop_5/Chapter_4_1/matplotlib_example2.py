import numpy as np
import matplotlib.pyplot as plt

# Generate the data
x = np.linspace(0.0, 100, 50)
y = np.random.uniform(low=0,high=10,size=50)

# Invoke 4 plot areas(2 rows and 2 columns)
fig, axes = plt.subplots(2,2)

# Plot some things
axes[0][0].scatter(x,y,c='red',marker="+")
axes[0][1].bar(x,y)
axes[1][0].scatter(y,x,marker="x")
axes[1][1].barh(x,y)

# Show the plots
plt.show()