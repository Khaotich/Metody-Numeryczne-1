#Karol Pichurski Lista 6 Zadanie 7

import numpy as np
from scipy import integrate

def f(x):
    return (np.cos(x) - np.e**x) / np.sin(x)


x = np.linspace(-1, 1, 10000)
result = integrate.simps(f(x), x)

print(f'Wynik całki: {result}')