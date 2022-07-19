#Karol Pichurski
#Lista 2 / Zadanie 3

import math
import numpy as np


def f1(x):
    return np.sqrt(np.float32(math.pow(x, 2) + 1)) - 1


def f2(x):
    return math.pow(x, 2) / (np.sqrt(np.float32(math.pow(x, 2) + 1)) + 1)


for n in range(2, 25, 2):
    x = 2 ** -n
    print(f'n = {n}   x = {x}   f1 = {f1(x)}  f2 = {f2(x)}')

#jak widać po wynikach metoda 2 jest dokładniejsza