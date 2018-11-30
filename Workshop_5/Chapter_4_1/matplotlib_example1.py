import matplotlib.pyplot as plt
import numpy as np

# Example 1
# Plot line
plt.plot([1,2,3,4])
plt.ylabel("some number")
plt.show()

# Example 2
# Plot points
x_data = np.array([1,2,3,4,5])
y_data = x_data**2

plt.plot(x_data,y_data,'ro')
plt.axis([0, 6, 0, 30])
plt.show()

# Example 3
# Multiple lines
t = np.arange(0., 5., 0.2)

plt.plot(t,t, "r--", t,t**2,"bs",t,t**3,'g^')
plt.show()

# Example 4
# Multiple graphs

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0,5,0.2)
t2 = np.arange(0,5,0.01)

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t1, f(t1),'bo',t2, f(t2),'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()


# Example 5
# Histogram
np.random.seed(2331)

mu, sigma = 100, 15
x = mu + sigma*np.random.randn(1000)

n, bins, patches = plt.hist(x, 50, normed=1,facecolor='g',alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

# Multiple bar plots on one figure
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
label="BMW",width=.5)
plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
label="Audi", color='r',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()

# Stocking plots - Area plots

# Simple data
days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

# Create aggregates for data
plt.plot([], [], color='m', label='Sleeping', linewidth=5)
plt.plot([], [], color='c', label='Eating', linewidth=5)
plt.plot([], [], color='r', label='Working', linewidth=5)
plt.plot([], [], color='k', label='Playing', linewidth=5)

# Invoke stackplot
plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot')
plt.legend()
plt.show()

# Pie chart
# Data
days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]
slices = [7, 2, 2, 13]
# Labels and colors
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,       # <- The data
  labels=activities,  # <- labels
  colors=cols,        # <- colors
  startangle=90,      # <- Starting angle
  shadow= True,       # <- shadow effect
  explode=(0,0.1,0,0),# <- offset from circle center
  autopct='%1.1f%%')  # <- data formatting

plt.title('Pie Plot')
plt.show()

# Polar plots
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()