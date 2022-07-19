#Karol Pichurski Lista 4 Zadanie 5

from scipy import optimize
from numpy import pi, sin, cos


def f(v0d): 
    v0, d = v0d
    tk = 10 / (v0 * cos(d))
    return [v0 * sin(d) * tk - (g * tk**2 / 2) - 1, v0 * (sin(d) + cos(d)) - (g * tk)]


g = 9.81
v0, d = optimize.root(f, [10.4, pi * 45 / 180]).x   
v0 = round(v0, 2)
d = round(d * 180 / pi, 2)

print(f'v0 = {v0} m/s')
print(f'd = {d} stopni')