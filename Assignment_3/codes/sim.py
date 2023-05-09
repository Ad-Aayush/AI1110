import numpy as np
from scipy.stats import binom
from scipy.stats import norm


simlen = 10000000
n = 6
k = 2
p = 1/6
sigma = np.sqrt(n*p*(1-p))

X = binom.rvs(n,p,size=simlen)
outcomes,fav_count = np.unique(X,return_counts=True)
fav_count = np.cumsum(fav_count)/simlen
print("Observed:",round(fav_count[2],4))
print("Actual:",round(binom.cdf(k,n,p),4))
print(norm(n*p,sigma).cdf(2.5))