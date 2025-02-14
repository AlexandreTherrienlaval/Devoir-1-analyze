import numpy as np
import matplotlib.pyplot as plt
from suiteSn import suiteSn
from math import e


a = np.full((6,1), 1)
b = np.arange(1,7)
c = np.reshape(a, (1,6))
d = c * 53
I = np.identity(6, 'i')
J = np.full((6,6), 1)
K = np.diag(b)
L = 55*I - J + 2 * a * c
M = 1 * K ; M[:,0] = np.reshape(a,(1,6))
dd = np.linalg.det(M)
x = np.linalg.solve(M, a)
M_transpose = np.transpose(M) ; N = np.linalg.solve(M, M_transpose)

'''print(a)
print(b)
print(c)
print(d)
print(I)
print(J)
print(K)
print(L)
print(M)
print(dd)
print(x)
print(M_transpose)'''

'''figure_1 = plt.matshow(N)
plt.title('Matrice N')
plt.show()'''

def f(x):
    return -1 * (x**2)/2 + np.exp(x) + np.sin(x)

x = np.linspace(0, 1, 101)
'''figure_2 = plt.plot(x, f(x))
plt.title('f(x) = -x^2/2 + exp(x) + sin(x)')
plt.show()'''

def S(n):
    return suiteSn(19)[n]

x = [i for i in range(1,20)]
'''figure_3 = plt.plot(x, S(x), 'o')
plt.xlabel('S')
plt.ylabel('n')
plt.ylabel('S en fonction de n')
plt.show()'''

def fprime(x):
    return -1 * x + e**x + np.cos(x)

def D(x, h):
    return (f((x+h)) - f(x))/h

h = np.array([])
for i in range(-6,-0):
    h= np.append(h, 10**i)


Figure = plt.loglog(h, abs(fprime(0) - D(0,h) ))
plt.xlabel('Erreur absolue')
plt.ylabel('h')
plt.title('''Erreur absolue de l'approximation de f(x) selon h''')
plt.show()

