# FFTpack
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import scipy.fftpack as fftpack

x = np.array([1.,2.,1.,-1.,1.5])
y = fft(x)                # Fast Fourier Transform
print(y)

yinv = ifft(y)
print(yinv)

N = 600  # <- liczba próbek
T = 1./800. # <- Czas

x = np.linspace(0.0,N*T,N) # <- linia czasu
y = np.sin(50.0*2.0*np.pi*x) + 0.5*np.sin(80.0*2.0*np.pi*x) # <- sygnał

yf = fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2) # <- Linia częstotliwości
plt.semilogy(xf, 2./N * np.abs(yf[0:int(N/2)]))
plt.grid()
plt.show()

