#Karol Pichurski Lista 7 Zadanie 4

from scipy.integrate import solve_ivp
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np


y_0 = 0
t = np.pi
y_k= 0


def f1(t, y):
    return [y[1], -np.sin(y[0]) - 1]

def f2(a):
    y0 = [y_0, a]
    woh = solve_ivp(f1, [0, t], y0, atol=1e-10, rtol=1e-8)
    return woh.y[0, -1] - y_k


a = optimize.newton(f2, 1, tol=1e-12, maxiter=150)
y0 = [y_0, a]
woh = solve_ivp(f1, [0, t], y0, atol=1e-10, rtol=1e-8)

print(a, ' ', f2(a))
plt.plot(woh.t, woh.y[0])
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Strzał')
plt.show()