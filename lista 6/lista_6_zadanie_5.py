#Karol Pichurski Lista 6 Zadanie 5

import numpy as np
from scipy import integrate

def h(O0, O):
    return 1 / np.sqrt(1 - (np.sin(O0 / 2) ** 2) * np.sin(O))


theta = [np.deg2rad(15), np.deg2rad(30), np.deg2rad(45)]
h0 = np.pi / 2

for i in theta:
    result = integrate.quad(h, 0, h0, args=i)[0]
    print(f'Theta = {int(np.round(np.rad2deg(i)))} wynik = {result} różnica={h0 - result}')