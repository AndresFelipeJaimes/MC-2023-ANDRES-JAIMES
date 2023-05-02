import numpy as np

def InterpolacionLagrange(x, y):
    n = len(x)
    L = np.zeros((n, n))

    for i in range(n):
        p = np.poly([x[j] for j in range(n) if j != i])
        L[i, :] = p / np.prod(np.array([x[i] - x[j] for j in range(n) if j != i]))

    return np.sum(np.array([y[i] * L[i, :] for i in range(n)]), axis=0)

x = [0, 1, 2, 3, 4]
y = [1, 0.9, -1, -2.3, 1.8]

Polinomio = InterpolacionLagrange(x, y)

print("El polinomio de interpolación de Lagrange es: ")
print(np.poly1d(Polinomio))