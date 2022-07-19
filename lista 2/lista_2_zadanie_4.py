#Karol Pichurski
#Lista 2 / Zadanie 4

import math
import numpy as np


def f1(x):
    return np.sqrt(np.float32(math.pow(x, 4) + 4)) - 2


def f2(x):
    return math.pow(x, 4) / (np.sqrt(np.float32(math.pow(x, 4) + 4)) + 2)


for n in range(2, 25):
    x = 2 ** -n
    print(f'n = {n}   x = {x}   f1 = {f1(x)}  f2 = {f2(x)}')

#wzór został analogicznie zmieniony jak w poprzednim zadaniu