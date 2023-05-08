import numpy as np

A = np.array([[5/6,1/6,0,0,0,0,0],
              [0,5/6,1/6,0,0,0,0],
              [0,0,5/6,1/6,0,0,0],
              [0,0,0,5/6,1/6,0,0],
              [0,0,0,0,5/6,1/6,0],
              [0,0,0,0,0,5/6,1/6],
              [0,0,0,0,0,0,5/6]])
B = np.linalg.matrix_power(A, 6)
np.set_printoptions(formatter={'float': lambda x: "{0:0.4f}".format(x)})
print(B)