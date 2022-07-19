#Karol Pichurski Lista 4 Zadanie 6

from scipy.optimize import fsolve
from math import tan, cos, sin


def f(xy):
    x, y = xy
    return [tan(x) - y - 1, cos(x) - 3 * sin(y)]


root = fsolve(f, [0.0, 0.0])
print(root)