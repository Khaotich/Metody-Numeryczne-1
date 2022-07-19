#Karol Pichurski Lista 7 Zadanie 2

import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt

def f1(t, y):
    Q = 2
    w = 2.0 / 3.0
    A = 0.5
    return  [y[1], -y[1]/Q - np.sin(y[0]) + A * np.cos(t*w)]

def f2(t, y):
    Q = 2
    w = 2.0 / 3.0
    A = 1.35
    return [y[1], -y[1]/Q - np.sin(y[0]) + A * np.cos(t*w)]

t = [0, 30]
t_ = np.linspace(0, 50)
sol1 = solve_ivp(f1, t, [0.01, 0], max_step=0.01)
sol2 = solve_ivp(f1, t, [0.3, 0], max_step=0.01)
sol3 = solve_ivp(f2, t, [0.3, 0], max_step=0.01)

plt.subplot(2,1,1)
plt.plot(sol1.y[0], sol1.y[1])
plt.plot(sol2.y[0], sol2.y[1])
plt.plot(sol3.y[0], sol3.y[1])
plt.legend(['t1', 't2', 't3'])

plt.subplot(2,1,2)
plt.plot(sol1.t, sol1.y[0])
plt.plot(sol2.t, sol2.y[0])
plt.plot(sol3.t, sol3.y[0])
plt.legend(['t1', 't2', 't3'])

plt.show()