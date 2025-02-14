import numpy as np
import matplotlib.pyplot as plt
#from suiteSn import suiteSn


a = np.full((6,1), 1)
b = np.arange(1,7)
c = np.reshape(a, (1,6))
d = c * 53
I = np.identity(6)
J = np.full((6,6), 1)
K = np.diag(b)
L = 55*I - J + 2*a*c
M = 1*K ; M[:,0] = np.reshape(a, (1,6))
dd = np.linalg.det(M)


print(f'a =\n{a}\n\n')          # a
print(f'b =\n{b}\n\n')          # b
print(f'c =\n{c}\n\n')          # c
print(f'd =\n{d}\n\n')          # d
print(f'I =\n{I}\n\n')          # I
print(f'J =\n{J}\n\n')          # J
print(f'K =\n{K}\n\n')          # K
print(f'L =\n{L}\n\n')          # L
print(f'M =\n{M}\n\n')          # M
print(f'dd =\n{dd}\n\n')        # dd

