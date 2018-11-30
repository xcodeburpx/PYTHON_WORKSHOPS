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