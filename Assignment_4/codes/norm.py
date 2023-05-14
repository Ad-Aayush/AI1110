from scipy.stats import norm
from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

p = 0.9
n = 10
k = 6
sig = np.sqrt(n*p*(1-p))

xpoints = np.linspace(0,10,11)
ypoints = np.array(binom.cdf(xpoints,n,p) )
plt.stem(xpoints, ypoints,linefmt='r-', markerfmt='ro', basefmt='k--')
xpoints = np.linspace(0,10,10000)
ypoints = np.array(norm.cdf((xpoints-n*p+0.5)/sig))
plt.plot(xpoints, ypoints,'b')
print(norm.cdf((k-n*p+0.5)/sig))
print((binom.cdf(k,n,p)-norm.cdf((k-n*p+0.5)/sig))/binom.cdf(k,n,p))
plt.show() 
