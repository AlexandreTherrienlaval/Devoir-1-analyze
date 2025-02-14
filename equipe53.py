import numpy as np
import matplotlib.pyplot as plt
#from suiteSn import suiteSn


a = np.full((6,1), 1)
b = np.arange(1,7)
c = np.reshape(a, (1,6))
d = c * 53
I = np.identity(6, 'i')
J = np.full((6,6), 1)
K = np.diag(b)
L = 55*I - J + 2*a*c
M = 1*K ; M[:,0] = np.reshape(a, (1,6))
dd = int(np.linalg.det(M))
x = np.array(np.linalg.solve(M, a), 'i')
N = np.linalg.solve(M, np.transpose(M))


print(f'a =\n{a}\n')
print(f'b =\n{b}\n')
print(f'c =\n{c}\n')
print(f'd =\n{d}\n')
print(f'I =\n{I}\n')
print(f'J =\n{J}\n')
print(f'K =\n{K}\n')
print(f'L =\n{L}\n')
print(f'M =\n{M}\n')
print(f'dd =\n{dd}\n')
print(f'x =\n{x}\n')
print(f'N =\n{N}\n')


plt.matshow(N)
plt.title("Matrice N")
plt.show()

