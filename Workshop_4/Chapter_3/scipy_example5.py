import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.interpolate import UnivariateSpline

x = np.linspace(0,4,12)
y = np.cos(x**2/3+4)
plt.plot(x,y,'o')
plt.show()

f1 = interpolate.interp1d(x,y,kind='linear')
f2 = interpolate.interp1d(x,y,kind='cubic')


xnew = np.linspace(0,4,30)
plt.plot(x,y,'o', xnew, f1(xnew),'-', xnew, f2(xnew), "--")
plt.legend(['data', 'linear', 'cubic','nearest'], loc = 'best')

plt.show()

x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * np.random.randn(50)
plt.plot(x, y, 'ro', ms = 5)

sp1 = UnivariateSpline(x,y)
xs = np.linspace(-3,3,1000)
plt.plot(xs,sp1(xs), 'g', lw=3)

sp1.set_smoothing_factor(0.5)
plt.plot(xs, sp1(xs), 'b', lw = 3)
plt.show()