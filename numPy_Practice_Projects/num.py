import numpy as np
n= np.array([[2,4],[5,6]])
b=np.array([[4,5], [6,7]])
ar=np.concatenate((n,b),axis=1)
print(ar)