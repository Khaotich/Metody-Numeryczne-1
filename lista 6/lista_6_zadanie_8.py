#Karol Pichurski Lista 6 Zadanie 8

import numpy as np
from scipy import integrate

def f(y, x):
    return np.sin(np.pi * x) * np.sin(np.pi * (y - x))

result = integrate.dblquad(f, 0, 1, lambda x : 0, lambda x: x)[0]
print(f'Wynik podwójnej całki: {result}')