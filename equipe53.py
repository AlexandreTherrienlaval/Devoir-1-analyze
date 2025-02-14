import numpy as np
import matplotlib.pyplot as plt
from suiteSn import suiteSn
from math import e



''' QUESTION 1 '''

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

figure_1 = plt.matshow(N)
plt.title('Matrice N')
plt.show()

def f(x):
    return -1 * (x**2)/2 + np.exp(x) + np.sin(x)

x = np.linspace(0, 1, 101)

figure_2 = plt.plot(x, f(x))
plt.title('f(x) = -x²/2 + e^x + sin(x)')
plt.show()



''' QUESTION 2 '''

def S(n):
    return suiteSn(19)[n]

x = [i for i in range(1,20)]

figure_3 = plt.plot(x, S(x), 'o')
plt.xlabel('n')
plt.ylabel('S')
plt.title('Sn en fonction de n')
plt.show()



''' QUESTION 3 '''

def fprime(x):
    return -1 * x + e**x + np.cos(x)

def D(x, h):
    return (f((x+h)) - f(x))/h

h = np.array([])
for i in range(-1, -7, -1):
    h = np.append(h, 10**i)

figure_4 = plt.loglog(h, abs(fprime(0) - D(0, h)))
plt.xlabel('h')
plt.ylabel('Erreur absolue')
plt.title("Erreur absolue de l'approximation de f'(x) en fonction de h")
plt.show()



''' QUESTION 4 '''

