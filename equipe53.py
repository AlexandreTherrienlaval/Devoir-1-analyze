import numpy as np
import matplotlib.pyplot as plt
#from suiteSn import suiteSn


a = np.full((6,1),1)
b = np.arange(1,7)
c = np.reshape(a, (1,6))
d = c * 53
I = np.identity(6)
J = np.full((6,6), 1)
K = np.diag(b)
L = 55*I - J + 2 * a * c
M = 1 * K ; M[:,0] = np.reshape(a,(1,6))
dd = np.linalg.det(M)


print(a)
print(f'b= {b}')
print(c)
print(d)
print(I)
print(J)
print(f'K= {K}')
print(L)
print(M)