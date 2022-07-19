#Karol Pichurski Lista 4 Zadanie 1

from numpy import sqrt
from scipy.optimize import ridder

f = lambda x: 2*x**4+24*x**3+61*x**2-16*x+1

print(ridder(f, -10, -6))
print(ridder(f, -6, -2))
print(ridder(f, -2, (0.5*(3*sqrt(2)-4)+(sqrt(17)-4))/2))
print(ridder(f, (0.5*(3*sqrt(2)-4)+(sqrt(17)-4))/2, 3))