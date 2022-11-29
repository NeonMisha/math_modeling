import numpy as np 
k = np.array([1,7,6])
def u (a):
    s = 1
    for i in k:
        s = s * i
    print(s)

u(k)
  