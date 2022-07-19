#Karol Pichurski Lista 8 Zadanie 4.1

import numpy as np 
from scipy.integrate import solve_ivp
from scipy import optimize
import matplotlib.pyplot as plt


def f1(t, y):
    return [y[1], -np.sin(y[0])-1]


def f2(a):
    y = [0, a]
    woh = solve_ivp(f1, [0, np.pi], y, atol=1e-10, rtol=1e-8)
    return woh.y[0, -1] - 0


a = optimize.ridder(f2, 2.69, 2.90, rtol=1e-10, maxiter=200)
result = solve_ivp(f1, [0, np.pi], [0, a], atol=1e-10, rtol=1e-8)

plt.plot(result.t, result.y[0])
plt.scatter(np.pi, 0, color='red')
plt.xlabel('t')
plt.ylabel('dy')
plt.show()

print(f'{a} {f2(a)}')