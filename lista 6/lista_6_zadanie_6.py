#Karol Pichurski Lista 6 Zadanie 6

import numpy as np
from scipy.special import roots_legendre

def f(x):
    return (np.log(x) / (x**2 - 2*x + 2))

n = [2, 4]
a = 1
b = np.pi

for i in n:
    x, a_ = roots_legendre(i)
    result = 0

    for j in range(len(a_)):
        x_ = (b + a) / 2 + (b - a) / 2 * x[j]
        result += (b - a) / 2 * a_[j] * f(x_)
    
    print(f'Wynik całki: {result} dla węzła: {i}')