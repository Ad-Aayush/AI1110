import numpy as np

p = 1/12

X = np.random.choice([1,6],10000000)
Y = np.random.choice([1,2,3,4,5,6],10000000)
Z = X + Y
fav_ind = np.nonzero(Z == 3)
fav_size = np.size(fav_ind)
print("The experimental value for probability of occurrence of 3:",round(fav_size/10000000,4))
print("Actual Value:",round(p,3))
fav_ind = np.nonzero(Z == 12)
fav_size = np.size(fav_ind)
print("The experimental value for probability of occurrence of 12:",round(fav_size/10000000,4))
print("Actual Value:",round(p,3))