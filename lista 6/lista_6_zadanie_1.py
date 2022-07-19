#Karol Pichurski Lista 6 Zadanie 1

import numpy as np


def f(x):
    return np.log(np.tanh(x / (x**2 + 1)))

def diff_1(f, x, h=0.01):
    return (f(x + h) - f(x - h))/(2*h)

def diff_2(f, x, h=0.01):
    return (f(x + h) - 2*f(x) + f(x - h))/(h**2)
    
def diff_3(f, x, h=0.01):
    return ( (f(x + 2*h) - 2*f(x + h) + 2*f(x - h) - f(x - 2*h))/(2*h**3))
    

print(f'Pierwsza pochodna od x=0.2: {diff_1(f, 0.2, 1e-6)}')
print(f'Druga pochodna od x=0.2: {diff_2(f, 0.2, 1e-6)}')
print(f'Trzecia pochodna od x=0.2: {diff_3(f, 0.2, 1e-6)}')

# dla h=1e-6 pochodne mają najlepszą dokładność