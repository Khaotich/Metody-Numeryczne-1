#Karol Pichurski Lista 6 Zadanie 4

import numpy as np
from scipy import integrate

def f(x):
    return np.cos(2*np.cos(x)**-1)

n = [3, 5, 7, 100]

for i in n:
    x = np.linspace(-1, 1, i)
    print(f'Całka dla węzła {i} = {integrate.simps(f(x), x)}')

'''
Wynik wychodzi na minusie ponieważ wykres od -1 do 1 znajduję się po osią OX
dla węzła 100 dostajemy bardzo dokładny wynik, zgadza się z wolframalpha
zwiększając liczbę węzłów zwiększamy dokładność wyniku.
'''