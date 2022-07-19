#Karol Pichurski Lista 7 Zadanie 1

import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt


def dydt(t, y):
    return np.sin(t*y)


y = [2, 2.5, 3, 3.5]
t = np.linspace(0, 6)

x = odeint(dydt, y, t)

plt.plot(t, x)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.title('dy/dt = sin(t*y)')
plt.legend(['y(0) = 2', 'y(0) = 2,5', 'y(0) = 3', 'y(0) = 3,5'])
plt.show()