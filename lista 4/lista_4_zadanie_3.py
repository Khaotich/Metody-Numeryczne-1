#Karol Pichurski Lista 4 Zadanie 3

from numpy import log, round

u = 2510
M0 = 2.8 * 10**6
m = 13.3 * 10**3
g = 9.81

v = lambda u, M0, m, g, t: u * log(M0/(M0 - m*t)) - g*t

t = 0.001
result = 0
while round(result, 3) != 335:
    result = v(u, M0, m, g, t)
    t += 0.001

print(f'Czas potrzebny aby rakieta osiągnęła 335 m/s wynosi {round(t, 2)} sekundy.')