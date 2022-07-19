#Karol Pichurski Lista 6 Zadanie 2

from numpy import array, poly1d, polyfit

x = array([0.0, 0.1, 0.2, 0.3, 0.4])
y = array([0.0, 0.078348, 0.13891, 0.192916, 0.244981])

f = poly1d(polyfit(x, y, 4))

print(f'f\'(0.2) = {f(0.2)}')

#dopasowanie niemal bezbłędne